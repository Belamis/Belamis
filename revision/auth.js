/*
 * Belamis — connexion par mail et sauvegarde des révisions.
 * Connexion sans mot de passe (Supabase) : l'élève reçoit un mail avec un lien
 * et un code à 6 chiffres. Sa progression est rangée dans la table `progress`,
 * une ligne par élève, que lui seul peut lire et modifier.
 */
(() => {
  "use strict";

  const cfg = window.BELAMIS_CONFIG || {};
  const configured = Boolean(cfg.supabaseUrl && cfg.supabaseAnonKey && window.supabase);
  const sb = configured ? window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey) : null;
  const DEMO_KEY = "belamis-demo";

  const $ = (id) => document.getElementById(id);
  const modal = $("auth");
  const emailForm = $("auth-email");
  const codeForm = $("auth-code");
  const mailInput = $("auth-mail");
  const otpInput = $("auth-otp");
  const guestBtn = $("auth-guest");
  const loginBtn = $("nav-login");
  const account = $("nav-account");

  let user = null;
  let pendingEmail = "";
  let launchAfterLogin = false;
  let lastFocus = null;

  // ---------- Stockage (Supabase, ou navigateur en mode démo) ----------
  const demo = {
    read() { try { return JSON.parse(localStorage.getItem(DEMO_KEY)) || {}; } catch (_) { return {}; } },
    write(v) { try { localStorage.setItem(DEMO_KEY, JSON.stringify(v)); } catch (_) { /* stockage bloqué */ } },
  };

  const store = {
    async load() {
      if (!user) return null;
      if (!sb) return demo.read().progress || {};
      const { data, error } = await sb.from("progress").select("data").eq("user_id", user.id).maybeSingle();
      if (error) throw error;
      return (data && data.data) || {};
    },
    async save(progress) {
      if (!user) return;
      if (!sb) { demo.write({ ...demo.read(), progress }); return; }
      const { error } = await sb.from("progress").upsert({ user_id: user.id, data: progress, updated_at: new Date().toISOString() });
      if (error) throw error;
    },
  };

  // ---------- Affichage de l'état connecté ----------
  function renderAccount() {
    const email = user ? user.email : "";
    loginBtn.hidden = Boolean(user);
    account.hidden = !user;
    $("nav-email").textContent = email;
    $("nav-avatar").textContent = email ? email[0].toUpperCase() : "";
  }

  function setUser(u) {
    user = u ? { id: u.id, email: u.email } : null;
    renderAccount();
  }

  // ---------- Fenêtre de connexion ----------
  function msg(form, text, kind) {
    const el = form.querySelector(".auth-msg");
    el.textContent = text || "";
    el.dataset.kind = kind || "";
  }

  function showStep(step) {
    emailForm.hidden = step !== "email";
    codeForm.hidden = step !== "code";
    (step === "email" ? mailInput : otpInput).focus();
  }

  function openAuth({ reason = "", fromLaunch = false } = {}) {
    lastFocus = document.activeElement;
    launchAfterLogin = fromLaunch;
    $("auth-why").textContent = reason || "Entre ton adresse mail : tu reçois un lien pour te connecter, sans mot de passe.";
    guestBtn.hidden = !fromLaunch;
    $("auth-demo").hidden = configured;
    msg(emailForm, "");
    msg(codeForm, "");
    modal.hidden = false;
    requestAnimationFrame(() => modal.classList.add("open"));
    showStep("email");
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
    if (error && error.status === 429 || m.includes("rate limit") || m.includes("security purposes")) return "Trop de demandes d'affilée. Attends une minute, puis redemande un lien.";
    if (m.includes("expired") || m.includes("invalid") || m.includes("token")) return "Ce code ne marche pas ou a expiré. Vérifie-le, ou redemande un lien.";
    if (m.includes("email")) return "Cette adresse mail ne semble pas valide. Vérifie-la.";
    if (m.includes("fetch") || m.includes("network")) return "Impossible de joindre le serveur. Vérifie ta connexion internet.";
    return "La connexion a échoué. Réessaie dans un instant.";
  }

  emailForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = mailInput.value.trim();
    if (!mailInput.checkValidity()) { msg(emailForm, "Entre une adresse mail complète, par exemple prenom.nom@exemple.fr.", "error"); return; }
    busy(emailForm, true);
    msg(emailForm, "");
    try {
      if (sb) {
        const { error } = await sb.auth.signInWithOtp({
          email,
          options: { emailRedirectTo: location.origin + location.pathname, shouldCreateUser: true },
        });
        if (error) throw error;
      }
      pendingEmail = email;
      $("auth-sent-to").textContent = email;
      otpInput.value = "";
      msg(codeForm, "");
      showStep("code");
    } catch (err) {
      msg(emailForm, friendlyError(err), "error");
    } finally {
      busy(emailForm, false);
    }
  });

  codeForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const token = otpInput.value.replace(/\D/g, "");
    if (token.length !== 6) { msg(codeForm, "Le code contient 6 chiffres.", "error"); return; }
    busy(codeForm, true);
    try {
      if (sb) {
        const { data, error } = await sb.auth.verifyOtp({ email: pendingEmail, token, type: "email" });
        if (error) throw error;
        setUser(data.user);
      } else {
        const u = { id: "demo", email: pendingEmail };
        demo.write({ ...demo.read(), user: u });
        setUser(u);
      }
      closeAuth();
      if (launchAfterLogin) startRevision();
    } catch (err) {
      msg(codeForm, friendlyError(err), "error");
    } finally {
      busy(codeForm, false);
    }
  });

  mailInput.addEventListener("input", () => msg(emailForm, ""));
  otpInput.addEventListener("input", () => msg(codeForm, ""));
  $("auth-back").addEventListener("click", () => showStep("email"));
  guestBtn.addEventListener("click", () => { closeAuth(); startRevision(); });
  modal.querySelectorAll("[data-close]").forEach((el) => el.addEventListener("click", closeAuth));
  modal.addEventListener("keydown", (e) => {
    if (e.key === "Escape") { e.stopPropagation(); closeAuth(); }
    if (e.key !== "Tab") return;
    // garder le focus dans la fenêtre
    const f = [...modal.querySelectorAll("button, input")].filter((el) => !el.disabled && el.offsetParent !== null);
    if (!f.length) return;
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  });

  loginBtn.addEventListener("click", () => openAuth());
  $("nav-logout").addEventListener("click", async () => {
    if (sb) await sb.auth.signOut();
    else { const d = demo.read(); delete d.user; demo.write(d); }
    setUser(null);
  });

  // ---------- Lancement des révisions ----------
  async function startRevision() {
    const note = $("space-note");
    note.textContent = user ? "Chargement de ta progression…" : "Mode invité : rien n'est sauvegardé. Connecte-toi depuis l'accueil pour garder ta progression.";
    window.BelamisLaunch();
    if (!user) return;
    try {
      const p = await store.load();
      const now = new Date().toISOString();
      const next = { ...p, sessions: (p.sessions || 0) + 1, firstVisit: p.firstVisit || now, lastVisit: now };
      await store.save(next);
      const where = sb ? "sur ton compte" : "dans ce navigateur (mode démo)";
      note.textContent = next.sessions === 1
        ? `Première séance, bienvenue ! Ta progression est sauvegardée ${where}.`
        : `Séance n°${next.sessions}. Ta progression est sauvegardée ${where}.`;
    } catch (_) {
      note.textContent = "Ta progression n'a pas pu être chargée. Vérifie ta connexion internet.";
    }
  }

  document.querySelectorAll("[data-launch]").forEach((el) =>
    el.addEventListener("click", (e) => {
      e.preventDefault();
      if (user) startRevision();
      else openAuth({ fromLaunch: true, reason: "Connecte-toi pour que tes révisions soient sauvegardées. Tu reçois un lien par mail, sans mot de passe." });
    })
  );

  // ---------- Démarrage : session existante ? ----------
  if (sb) {
    sb.auth.getSession().then(({ data }) => setUser(data.session && data.session.user));
    sb.auth.onAuthStateChange((_event, session) => setUser(session && session.user));
  } else {
    setUser(demo.read().user || null);
  }

  window.Belamis = { store, get user() { return user; }, configured };
})();
