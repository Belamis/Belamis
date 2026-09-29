/*
 * Belamis — panneaux « Ma progression » (pour le concours choisi) et « Paramètres ».
 */
(() => {
  "use strict";

  const $ = (id) => document.getElementById(id);
  const R = () => window.BelamisRevise;
  const P = window.BelamisPrefs;
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const fmt = (n) => String(Math.round(n * 10) / 10).replace(".", ",");
  const store = () => window.Belamis && window.Belamis.store;
  let lastFocus = null;

  // ---------- Ouverture / fermeture ----------
  function openPanel(name) {
    const el = $(`panel-${name}`);
    if (!el) return;
    lastFocus = document.activeElement;
    document.querySelectorAll(".sheet").forEach((x) => { x.hidden = x !== el; });
    el.hidden = false;
    (name === "progress" ? renderProgress : renderSettings)();
    const x = el.querySelector("[data-close-panel]");
    if (x) x.focus();
  }
  function closePanels() {
    document.querySelectorAll(".sheet").forEach((x) => { x.hidden = true; });
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  document.addEventListener("click", (e) => {
    const o = e.target.closest("[data-open-panel]");
    if (o) { e.preventDefault(); openPanel(o.dataset.openPanel); return; }
    if (e.target.closest("[data-close-panel]") || e.target.classList.contains("sheet")) closePanels();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    if ([...document.querySelectorAll(".sheet")].some((x) => !x.hidden)) { e.stopImmediatePropagation(); closePanels(); }
  }, true);

  // ---------- Calcul de la progression ----------
  function sujetStats(s, e) {
    const qs = s.parties.flatMap((p) => p.questions.map((q) => ({ k: `${p.id}-${q.id}`, pts: q.points })));
    let answered = 0, evaluated = 0, got = 0, evPts = 0;
    const W = { ok: 1, half: 0.5, ko: 0 };
    for (const { k, pts } of qs) {
      if (e && e.answers && e.answers[k] && String(e.answers[k]).trim()) answered++;
      const v = e && e.evals && e.evals[k];
      if (v) { evaluated++; evPts += pts; got += pts * W[v]; }
    }
    const n = qs.length;
    const status = !e || (!answered && !evaluated) ? "new" : (evaluated === n || answered === n) ? "done" : "doing";
    return { n, answered, evaluated, got, evPts, status, seconds: (e && e.seconds) || 0, updatedAt: (e && e.updatedAt) || "" };
  }

  function blocsOf(c) {
    const list = c.blocs.map((b) => ({ ...b }));
    list.push({ m: c.rev, name: "Séances de révision", rev: true });
    return list;
  }

  async function computeProgress(cid) {
    const c = R().CONCOURS[cid];
    let all = {};
    try { all = (await store().read()) || {}; } catch (_) { all = {}; }
    const rows = [], resume = [];
    const tot = { sujets: 0, done: 0, doing: 0, answered: 0, questions: 0, got: 0, evPts: 0, seconds: 0 };
    for (const b of blocsOf(c)) {
      const data = R().MATIERES[b.m] && R().MATIERES[b.m].data;
      if (!data) continue;
      const sujets = data.sujets.filter((s) => !b.dom || s.domaine === b.dom);
      const r = { ...b, sujets: sujets.length, done: 0, doing: 0, got: 0, evPts: 0, seconds: 0 };
      for (const s of sujets) {
        const st = sujetStats(s, (all[b.m] || {})[s.id]);
        r.done += st.status === "done"; r.doing += st.status === "doing";
        r.got += st.got; r.evPts += st.evPts; r.seconds += st.seconds;
        tot.answered += st.answered; tot.questions += st.n;
        if (st.status === "doing") resume.push({ m: b.m, dom: b.dom, id: s.id, titre: s.titre || s.id, bloc: b.name, st });
      }
      tot.sujets += r.sujets; tot.done += r.done; tot.doing += r.doing;
      tot.got += r.got; tot.evPts += r.evPts; tot.seconds += r.seconds;
      rows.push(r);
    }
    resume.sort((a, b) => String(b.st.updatedAt).localeCompare(String(a.st.updatedAt)));
    return { c, rows, resume: resume.slice(0, 6), tot };
  }

  const hm = (sec) => {
    const h = Math.floor(sec / 3600), m = Math.round((sec % 3600) / 60);
    return h ? `${h} h ${String(m).padStart(2, "0")}` : `${m} min`;
  };

  async function renderProgress() {
    const body = $("progress-body");
    const cid = R() && R().concours();
    if (!cid || !R().CONCOURS[cid]) {
      $("progress-sub").textContent = "";
      body.innerHTML = `<p class="empty-note">Choisis d'abord ton concours dans l'espace de Raphaël : ta progression s'affichera ici.</p>`;
      return;
    }
    body.innerHTML = `<p class="sheet-note">Calcul en cours…</p>`;
    const { c, rows, resume, tot } = await computeProgress(cid);
    $("progress-sub").textContent = `${c.nom} · ${window.Belamis && window.Belamis.user ? "sauvegardée sur ton compte" : "sauvegardée dans ce navigateur"}`;
    const rate = tot.evPts ? Math.round((tot.got / tot.evPts) * 100) : null;
    const pctDone = tot.sujets ? Math.round((tot.done / tot.sujets) * 100) : 0;
    body.innerHTML = `
      <section class="sheet-sec">
        <h3>En un coup d'œil</h3>
        <div class="kpis">
          <div class="kpi"><b>${pctDone} %</b><span>du programme terminé</span><small>${tot.done} sur ${tot.sujets} sujets et séances</small></div>
          <div class="kpi"><b>${tot.answered}</b><span>réponses écrites</span><small>sur ${tot.questions} questions</small></div>
          <div class="kpi"><b>${rate === null ? "–" : rate + " %"}</b><span>de réussite</span><small>${rate === null ? "corrige-toi pour la calculer" : `${fmt(tot.got)} pts sur ${fmt(tot.evPts)} évalués`}</small></div>
          <div class="kpi"><b>${hm(tot.seconds)}</b><span>de travail chronométré</span><small>${tot.doing} en cours</small></div>
        </div>
      </section>
      <section class="sheet-sec">
        <h3>Par épreuve</h3>
        <div class="prog-rows">
          ${rows.map((r) => {
            const p = r.sujets ? Math.round((r.done / r.sujets) * 100) : 0;
            const rr = r.evPts ? Math.round((r.got / r.evPts) * 100) + " % de réussite" : "pas encore corrigé";
            return `<div class="prog-row">
              <div><b>${esc(r.name)}</b><small>${r.done} terminé${r.done > 1 ? "s" : ""} · ${r.doing} en cours · ${r.sujets} au total</small></div>
              <div class="prog-bar" role="img" aria-label="${p} % terminé"><i style="width:${p}%"></i></div>
              <div class="prog-val">${p} %<small>${rr}</small></div>
            </div>`;
          }).join("")}
        </div>
      </section>
      <section class="sheet-sec">
        <h3>À reprendre</h3>
        ${resume.length ? `<ul class="resume-list">${resume.map((x) => `<li><button type="button" class="resume-item" data-resume="${esc(x.m)}|${esc(x.dom || "")}|${esc(x.id)}">
            <span><b>${esc(x.titre)}</b><br><small>${esc(x.bloc)} · ${x.st.answered} réponse${x.st.answered > 1 ? "s" : ""} sur ${x.st.n}</small></span>
            <span class="go">Reprendre ›</span></button></li>`).join("")}</ul>`
          : `<p class="empty-note">Rien en cours pour l'instant. Commence un sujet ou une séance de révision : il apparaîtra ici.</p>`}
      </section>
      <p class="sheet-note">Un sujet est « terminé » quand toutes ses questions ont une réponse ou une auto-évaluation. Le taux de réussite se calcule à partir de tes auto-évaluations dans les corrigés.</p>`;
  }

  $("progress-body").addEventListener("click", async (e) => {
    const b = e.target.closest("[data-resume]");
    if (!b) return;
    const [m, dom, id] = b.dataset.resume.split("|");
    closePanels();
    await R().open(m, dom || undefined, id);
  });

  // ---------- Paramètres ----------
  const THEMES = [
    { id: "nuit", name: "Nuit dorée", desc: "Le thème d'origine, sombre et doré.", bg: "#0b0c08", c: ["#ffc864", "#c9f25a", "#5ce1e6"] },
    { id: "clair", name: "Clair", desc: "Fond papier, texte foncé : idéal en plein jour.", bg: "#f6f3ec", c: ["#9a5a00", "#2f7d1c", "#1f1d18"] },
    { id: "lagon", name: "Lagon", desc: "Clair et turquoise, aux couleurs de Mayotte.", bg: "#e3f2f2", c: ["#0b7f8a", "#1e7d46", "#0f272c"] },
    { id: "ocean", name: "Océan", desc: "Sombre et bleuté, reposant le soir.", bg: "#06121f", c: ["#6cc7ff", "#7be0a8", "#e6f1fb"] },
    { id: "contraste", name: "Contraste élevé", desc: "Noir, blanc et jaune : lisibilité maximale.", bg: "#000000", c: ["#ffe14d", "#7dff7d", "#ffffff"] },
  ];
  const seg = (key, items) => `<div class="seg" role="group">${items.map(([v, label]) =>
    `<button type="button" data-pref="${key}" data-val="${v}" aria-pressed="${String(P.get(key)) === String(v)}">${label}</button>`).join("")}</div>`;

  function renderSettings() {
    const cid = R() && R().concours();
    const c = cid && R().CONCOURS[cid];
    const user = window.Belamis && window.Belamis.user;
    $("settings-body").innerHTML = `
      <section class="sheet-sec">
        <h3>Thème</h3>
        <div class="opts">${THEMES.map((t) => `<button type="button" class="opt" data-pref="theme" data-val="${t.id}" aria-pressed="${P.get("theme") === t.id}">
          <span class="sw" style="background:${t.bg}">${t.c.map((x) => `<i style="background:${x}"></i>`).join("")}</span>
          <b>${t.name}</b><small>${t.desc}</small></button>`).join("")}</div>
        <p class="sheet-note">Le thème s'applique aux sujets, aux séances, à la progression et aux paramètres. L'accueil et la transition gardent leur univers étoilé.</p>
      </section>
      <section class="sheet-sec">
        <h3>Confort</h3>
        <div class="set-row"><div><b>Taille du texte</b><small>Agrandit tout le texte de la plateforme.</small></div>
          ${seg("text", [["normal", "Normale"], ["grand", "Grande"], ["tres-grand", "Très grande"]])}</div>
        <div class="set-row"><div><b>Animations</b><small>« Réduites » saute la transition et calme les mouvements de l'accueil.</small></div>
          ${seg("motion", [["complet", "Complètes"], ["reduit", "Réduites"]])}</div>
        <div class="set-row"><div><b>Son de la transition</b><small>La musique qui accompagne la naissance de Raphaël.</small></div>
          ${seg("sound", [["true", "Activé"], ["false", "Coupé"]])}</div>
      </section>
      <section class="sheet-sec">
        <h3>Concours</h3>
        <div class="set-row"><div><b>${c ? esc(c.nom) : "Aucun concours choisi"}</b><small>Tu peux changer à tout moment : ta progression de chaque concours est gardée.</small></div>
          <button type="button" class="btn btn-ghost btn-sm" data-action="change-concours">Changer de concours</button></div>
      </section>
      <section class="sheet-sec">
        <h3>Mes données</h3>
        <div class="set-row"><div><b>Sauvegarde</b><small>${user ? `Sur ton compte (${esc(user.email)}) : tu retrouves tes révisions sur tous tes appareils.` : "Dans ce navigateur, sur cet appareil. Ne vide pas les données du site pour les garder."}</small></div></div>
        <div class="set-row"><div><b>Exporter ma progression</b><small>Un fichier à garder de côté, par précaution.</small></div>
          <button type="button" class="btn btn-ghost btn-sm" data-action="export">Télécharger</button></div>
        <div class="set-row"><div><b>Effacer ma progression${c ? ` du ${esc(c.nom)}` : ""}</b><small>Réponses, corrections et temps de ce concours. Irréversible.</small></div>
          <button type="button" class="btn btn-sm btn-danger" data-action="reset" ${c ? "" : "disabled"}>Effacer</button></div>
      </section>`;
  }

  $("settings-body").addEventListener("click", async (e) => {
    const b = e.target.closest("[data-pref]");
    if (b) {
      let v = b.dataset.val;
      if (b.dataset.pref === "sound") v = v === "true";
      P.set(b.dataset.pref, v);
      renderSettings();
      return;
    }
    const a = e.target.closest("[data-action]");
    if (!a) return;
    if (a.dataset.action === "change-concours") {
      closePanels();
      const study = $("study");
      if (study && !study.hidden) $("study-close").click();
      R().showConcours(null);
    } else if (a.dataset.action === "export") {
      let all = {};
      try { all = (await store().read()) || {}; } catch (_) { /* rien */ }
      const blob = new Blob([JSON.stringify({ app: "Belamis", date: new Date().toISOString(), progression: all }, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const link = Object.assign(document.createElement("a"), { href: url, download: `belamis-progression-${new Date().toISOString().slice(0, 10)}.json` });
      document.body.appendChild(link); link.click(); link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 2000);
    } else if (a.dataset.action === "reset") {
      const cid = R().concours();
      const c = cid && R().CONCOURS[cid];
      if (!c || !confirm(`Effacer toute ta progression du ${c.nom} ? Cette action est irréversible.`)) return;
      const keys = new Set([...c.blocs.map((x) => x.m), c.rev]);
      const doms = {};
      c.blocs.forEach((x) => { if (x.dom) (doms[x.m] = doms[x.m] || new Set()).add(x.dom); });
      await store().update((all) => {
        const next = { ...all };
        for (const m of keys) {
          if (!next[m]) continue;
          if (doms[m]) {
            // matière partagée entre épreuves : on n'efface que les sujets de ce concours
            const data = R().MATIERES[m].data;
            const ids = new Set(data.sujets.filter((s) => doms[m].has(s.domaine)).map((s) => s.id));
            next[m] = Object.fromEntries(Object.entries(next[m]).filter(([id]) => !ids.has(id)));
          } else delete next[m];
        }
        return next;
      });
      await R().refresh();
      a.textContent = "Effacé";
      a.disabled = true;
    }
  });
})();
