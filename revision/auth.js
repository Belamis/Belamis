/*
 * Belamis — comptes et sauvegarde des révisions.
 * Avec Supabase (config.js rempli) : comptes en ligne (mail + mot de passe), révisions retrouvées sur tous les appareils.
 * Sans Supabase : comptes enregistrés sur cet appareil (mot de passe haché), révisions rangées par compte.
 * Sans compte : mode invité, révisions dans ce navigateur.
 */
(() => {
  "use strict";

  const cfg = window.BELAMIS_CONFIG || {};
  const configured = Boolean(cfg.supabaseUrl && cfg.supabaseAnonKey && window.supabase);
  const sb = configured ? window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey) : null;

  const $ = (id) => document.getElementById(id);
  const modal = $("auth");
  const forms = { login: $("auth-login"), signup: $("auth-signup"), reset: $("auth-reset") };

  let user = null;          // { id, email, prenom }
  let lastFocus = null;

  // ---------- Adresses perso : fautes de frappe courantes ----------
  const DOMAINS = [
    "gmail.com", "googlemail.com", "hotmail.fr", "hotmail.com", "outlook.fr", "outlook.com", "live.fr", "live.com",
    "msn.com", "yahoo.fr", "yahoo.com", "ymail.com", "orange.fr", "wanadoo.fr", "free.fr", "sfr.fr", "neuf.fr",
    "laposte.net", "bbox.fr", "numericable.fr", "icloud.com", "me.com", "mac.com", "aol.com", "aol.fr", "gmx.fr",
    "gmx.com", "protonmail.com", "proton.me", "club-internet.fr", "aliceadsl.fr", "cegetel.net", "voila.fr",
  ];
  // noms qui n'existent pas mais qu'on tape souvent
  const ALIASES = { "gmail.fr": "gmail.com", "gmail.co": "gmail.com", "gmail.con": "gmail.com", "hotmail.con": "hotmail.com", "outlook.con": "outlook.com", "wanadoo.com": "wanadoo.fr", "orange.com": "orange.fr", "free.com": "free.fr", "laposte.fr": "laposte.net", "icloud.fr": "icloud.com" };

  function distance(a, b) {
    const d = Array.from({ length: a.length + 1 }, (_, i) => [i]);
    for (let j = 1; j <= b.length; j++) d[0][j] = j;
    for (let i = 1; i <= a.length; i++)
      for (let j = 1; j <= b.length; j++) {
        d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
      }
    return d[a.length][b.length];
  }

  function suggestEmail(email) {
    const at = email.lastIndexOf("@");
    if (at < 1) return null;
    const local = email.slice(0, at), domain = email.slice(at + 1).toLowerCase();
    if (!domain || DOMAINS.includes(domain)) return null;
    if (ALIASES[domain]) return `${local}@${ALIASES[domain]}`;
    let best = null, bestD = 3;
    for (const d of DOMAINS) {
      const dist = distance(domain, d);
      if (dist < bestD) { best = d; bestD = dist; }
    }
    // « gmial.com », « hotmial.fr », « wanado.fr », « orange.f »…
    return best && bestD <= (domain.length > 6 ? 2 : 1) ? `${local}@${best}` : null;
  }


  const suggestBox = $("auth-suggest");
  const suggestBtn = $("auth-suggest-btn");
  let suggestionShownFor = "";
  function showSuggestion(email) {
    const s = suggestEmail(email);
    suggestBox.hidden = !s;
    if (s) suggestBtn.textContent = s;
    return s;
  }
  suggestBtn.addEventListener("click", () => {
    $("signup-mail").value = suggestBtn.textContent;
    suggestBox.hidden = true;
    $("signup-mail").focus();
  });

  // ---------- Stockage local ----------
  const jsonStore = (key) => ({
    read() { try { return JSON.parse(localStorage.getItem(key)) || {}; } catch (_) { return {}; } },
    write(v) { try { localStorage.setItem(key, JSON.stringify(v)); } catch (_) { /* stockage bloqué */ } },
  });
  const guest = jsonStore("belamis-guest");        // révisions sans compte
  const accounts = jsonStore("belamis-accounts");  // comptes de cet appareil
  const session = jsonStore("belamis-session");    // compte connecté sur cet appareil

  async function hashPassword(password, salt) {
    const data = new TextEncoder().encode(`${salt}:${password}`);
    if (window.crypto && crypto.subtle) {
      const buf = await crypto.subtle.digest("SHA-256", data);
      return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
    }
    let h = 0; for (const b of data) h = (h * 31 + b) >>> 0; return `x${h.toString(16)}`;
  }
  const newSalt = () => [...(window.crypto ? crypto.getRandomValues(new Uint8Array(12)) : [Date.now() % 255])].map((b) => b.toString(16)).join("");

  // ---------- Sauvegarde des révisions ----------
  const store = {
    async load() {
      if (!user) return guest.read();
      if (sb) {
        const { data, error } = await sb.from("progress").select("data").eq("user_id", user.id).maybeSingle();
        if (error) throw error;
        return (data && data.data) || {};
      }
      const a = accounts.read()[user.email];
      return (a && a.progress) || {};
    },
    async save(progress) {
      if (!user) { guest.write(progress); return; }
      if (sb) {
        const { error } = await sb.from("progress").upsert({ user_id: user.id, data: progress, updated_at: new Date().toISOString() });
        if (error) throw error;
        return;
      }
      const all = accounts.read();
      if (all[user.email]) { all[user.email].progress = progress; accounts.write(all); }
    },
    async read() { return store.load(); },
    // modifications une par une, pour ne jamais écraser une sauvegarde plus récente
    update(fn) {
      queue = queue.then(async () => {
        const current = (await store.load()) || {};
        const next = fn(current) || current;
        await store.save(next);
        return next;
      });
      const result = queue;
      queue = queue.catch(() => {});
      return result;
    },
  };
  let queue = Promise.resolve();

  // ---------- État du compte ----------
  function renderAccount() {
    const name = user ? (user.prenom || user.email.split("@")[0]) : "";
    $("nav-guest").hidden = Boolean(user);
    $("nav-account").hidden = !user;
    $("nav-email").textContent = user ? name : "";
    $("nav-email").title = user ? user.email : "";
    $("nav-avatar").textContent = name ? name[0].toUpperCase() : "";
    const sp = $("space-account");
    if (sp) sp.textContent = user ? name : "Créer un compte";
  }

  function setUser(u) {
    const before = user && user.id;
    user = u ? { id: u.id, email: u.email, prenom: u.prenom || (u.user_metadata && u.user_metadata.prenom) || "" } : null;
    renderAccount();
    if (before !== (user && user.id)) window.dispatchEvent(new CustomEvent("belamis:account"));
  }

  // ---------- Fenêtre ----------
  function msg(form, text, kind) {
    const el = form.querySelector(".auth-msg");
    el.textContent = text || "";
    el.dataset.kind = kind || "";
  }

  function showTab(tab) {
    for (const [k, f] of Object.entries(forms)) f.hidden = k !== tab;
    $("tab-login").setAttribute("aria-selected", String(tab === "login"));
    $("tab-signup").setAttribute("aria-selected", String(tab === "signup"));
    modal.querySelector(".auth-tabs").hidden = tab === "reset";
    const first = forms[tab].querySelector("input");
    if (first) first.focus();
  }

  function openAuth(tab = "login") {
    lastFocus = document.activeElement;
    Object.values(forms).forEach((f) => msg(f, ""));
    suggestBox.hidden = true;
    suggestionShownFor = "";
    $("auth-local").hidden = configured;
    modal.hidden = false;
    requestAnimationFrame(() => modal.classList.add("open"));
    showTab(tab);
  }

  function closeAuth() {
    modal.classList.remove("open");
    modal.hidden = true;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function busy(form, on) {
    const b = form.querySelector("button[type=submit]");
    b.disabled = on;
    b.classList.toggle("loading", on);
  }

  function friendlyError(error) {
    const m = ((error && error.message) || "").toLowerCase();
    if ((error && error.status === 429) || m.includes("rate limit") || m.includes("security purposes")) return "Trop de tentatives d'affilée. Attends une minute, puis réessaie.";
    if (m.includes("invalid login") || m.includes("invalid credentials")) return "Adresse mail ou mot de passe incorrect.";
    if (m.includes("already registered") || m.includes("already been registered")) return "Un compte existe déjà avec cette adresse : connecte-toi.";
    if (m.includes("not confirmed")) return "Ton adresse n'est pas encore confirmée : clique sur le lien reçu par mail.";
    if (m.includes("password")) return "Choisis un mot de passe d'au moins 8 caractères.";
    if (m.includes("email")) return "Cette adresse mail ne semble pas valide. Vérifie-la.";
    if (m.includes("fetch") || m.includes("network")) return "Impossible de joindre le serveur. Vérifie ta connexion internet.";
    return "Ça n'a pas marché. Réessaie dans un instant.";
  }

  const validEmail = (e) => /^[^@\s]+@[^@\s.]+(\.[^@\s.]+)+$/.test(e);

  // ---------- Créer un compte ----------
  forms.signup.addEventListener("submit", async (e) => {
    e.preventDefault();
    const f = forms.signup;
    const prenom = $("signup-name").value.trim();
    const email = $("signup-mail").value.trim().toLowerCase();
    const password = $("signup-pass").value;
    $("signup-mail").value = email;
    if (!prenom) { msg(f, "Indique ton prénom.", "error"); return; }
    if (!validEmail(email)) { msg(f, "Entre une adresse mail complète, par exemple prenom.nom@gmail.com.", "error"); return; }
    if (suggestionShownFor !== email && showSuggestion(email)) {
      suggestionShownFor = email;
      msg(f, "Vérifie ton adresse. Clique sur la suggestion, ou valide tel quel si elle est juste.", "error");
      return;
    }
    if (password.length < 8) { msg(f, "Choisis un mot de passe d'au moins 8 caractères.", "error"); return; }
    const carry = $("signup-import").checked ? guest.read() : {};
    busy(f, true); msg(f, "");
    try {
      if (sb) {
        const { data, error } = await sb.auth.signUp({ email, password, options: { data: { prenom }, emailRedirectTo: location.origin + location.pathname } });
        if (error) throw error;
        if (data.session) {
          setUser(data.user);
          if (Object.keys(carry).length) await store.save(carry);
          closeAuth();
        } else {
          try { localStorage.setItem("belamis-carry", JSON.stringify(carry)); } catch (_) { /* rien */ }
          msg(f, "Presque fini : clique sur le lien reçu par mail pour activer ton compte, puis connecte-toi.", "ok");
        }
      } else {
        const all = accounts.read();
        if (all[email]) throw { message: "already registered" };
        const salt = newSalt();
        all[email] = { prenom, salt, hash: await hashPassword(password, salt), created: new Date().toISOString(), progress: carry };
        accounts.write(all);
        session.write({ email });
        setUser({ id: `local:${email}`, email, prenom });
        closeAuth();
      }
    } catch (err) {
      msg(f, friendlyError(err), "error");
    } finally {
      busy(f, false);
    }
  });

  // ---------- Se connecter ----------
  forms.login.addEventListener("submit", async (e) => {
    e.preventDefault();
    const f = forms.login;
    const email = $("login-mail").value.trim().toLowerCase();
    const password = $("login-pass").value;
    if (!validEmail(email) || !password) { msg(f, "Entre ton adresse mail et ton mot de passe.", "error"); return; }
    busy(f, true); msg(f, "");
    try {
      if (sb) {
        const { data, error } = await sb.auth.signInWithPassword({ email, password });
        if (error) throw error;
        setUser(data.user);
        let carry = null;
        try { carry = JSON.parse(localStorage.getItem("belamis-carry") || "null"); localStorage.removeItem("belamis-carry"); } catch (_) { /* rien */ }
        if (carry && Object.keys(carry).length) {
          const cur = await store.load();
          if (!Object.keys(cur).length) await store.save(carry);
        }
      } else {
        const a = accounts.read()[email];
        if (!a || a.hash !== (await hashPassword(password, a.salt))) throw { message: "invalid login" };
        session.write({ email });
        setUser({ id: `local:${email}`, email, prenom: a.prenom });
      }
      $("login-pass").value = "";
      closeAuth();
    } catch (err) {
      msg(f, friendlyError(err), "error");
    } finally {
      busy(f, false);
    }
  });

  // ---------- Mot de passe oublié ----------
  $("auth-forgot").addEventListener("click", async () => {
    const f = forms.login;
    const email = $("login-mail").value.trim().toLowerCase();
    if (!validEmail(email)) { msg(f, "Entre d'abord ton adresse mail ci-dessus.", "error"); $("login-mail").focus(); return; }
    if (!sb) {
      msg(f, "Ton compte est enregistré sur cet appareil : le mot de passe ne peut pas être envoyé par mail. Si tu l'as oublié, crée un nouveau compte.", "error");
      return;
    }
    try {
      const { error } = await sb.auth.resetPasswordForEmail(email, { redirectTo: location.origin + location.pathname });
      if (error) throw error;
      msg(f, "Si un compte existe avec cette adresse, un mail vient d'être envoyé pour choisir un nouveau mot de passe. Pense à regarder dans les spams.", "ok");
    } catch (err) {
      msg(f, friendlyError(err), "error");
    }
  });

  forms.reset.addEventListener("submit", async (e) => {
    e.preventDefault();
    const f = forms.reset;
    const password = $("reset-pass").value;
    if (password.length < 8) { msg(f, "Choisis un mot de passe d'au moins 8 caractères.", "error"); return; }
    busy(f, true);
    try {
      const { error } = await sb.auth.updateUser({ password });
      if (error) throw error;
      msg(f, "Mot de passe enregistré. Tu es connecté.", "ok");
      setTimeout(closeAuth, 1200);
    } catch (err) {
      msg(f, friendlyError(err), "error");
    } finally {
      busy(f, false);
    }
  });

  // ---------- Se déconnecter ----------
  async function logout() {
    if (sb) { try { await sb.auth.signOut(); } catch (_) { /* hors ligne */ } }
    session.write({});
    setUser(null);
  }

  // ---------- Événements ----------
  $("signup-mail").addEventListener("input", () => { suggestBox.hidden = true; });
  $("signup-mail").addEventListener("blur", () => { const v = $("signup-mail").value.trim().toLowerCase(); if (v.includes("@")) showSuggestion(v); });
  modal.querySelectorAll("[data-close]").forEach((el) => el.addEventListener("click", closeAuth));
  modal.addEventListener("click", (e) => { const t = e.target.closest("[data-tab]"); if (t) showTab(t.dataset.tab); });
  modal.addEventListener("keydown", (e) => {
    if (e.key === "Escape") { e.stopPropagation(); closeAuth(); }
    if (e.key !== "Tab") return;
    const f = [...modal.querySelectorAll("button, input")].filter((el) => !el.disabled && el.offsetParent !== null);
    if (!f.length) return;
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  });
  document.addEventListener("click", (e) => {
    const a = e.target.closest("[data-auth]");
    if (a) {
      e.preventDefault();
      // connecté : le bouton « compte » de l'espace ouvre les paramètres (section Mon compte)
      if (user && a.id === "space-account") { const s = document.querySelector('[data-open-panel="settings"]'); if (s) s.click(); return; }
      openAuth(a.dataset.auth);
      return;
    }
    if (e.target.closest("[data-logout]")) { e.preventDefault(); logout(); }
  });

  // ---------- Lancement des révisions ----------
  async function startRevision() {
    const note = $("space-note");
    note.textContent = "";
    window.BelamisLaunch();
    if (!user) return;
    try {
      const now = new Date().toISOString();
      const next = await store.update((p) => ({ ...p, sessions: (p.sessions || 0) + 1, firstVisit: p.firstVisit || now, lastVisit: now }));
      const name = user.prenom ? `${user.prenom}, ` : "";
      note.textContent = next.sessions === 1 ? `Bienvenue ${name}c'est ta première séance !` : `Bon retour ${name}séance n°${next.sessions}.`;
    } catch (_) {
      note.textContent = "Ta progression n'a pas pu être chargée. Vérifie ta connexion internet.";
    }
  }
  document.querySelectorAll("[data-launch]").forEach((el) =>
    el.addEventListener("click", (e) => { e.preventDefault(); startRevision(); })
  );

  // ---------- Démarrage : session existante ? ----------
  if (sb) {
    sb.auth.getSession().then(({ data }) => setUser(data.session && data.session.user));
    sb.auth.onAuthStateChange((event, s) => {
      setUser(s && s.user);
      if (event === "PASSWORD_RECOVERY") { openAuth("reset"); }
    });
  } else {
    const s = session.read();
    const a = s.email && accounts.read()[s.email];
    setUser(a ? { id: `local:${s.email}`, email: s.email, prenom: a.prenom } : null);
  }

  window.Belamis = {
    store, configured,
    get user() { return user; },
    openAuth, logout,
  };
})();
