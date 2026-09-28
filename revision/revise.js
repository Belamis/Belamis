/*
 * Belamis — espace de travail : sujets de français (CRPE BAC+3, 1re épreuve, partie A).
 * Liste des sujets, entraînement par type d'exercice, et page sujet :
 * texte à gauche, questions à droite, réponses sauvegardées, corrigés et auto-évaluation.
 */
(() => {
  "use strict";

  const DATA = window.BELAMIS_FRANCAIS;
  if (!DATA) return;

  const $ = (id) => document.getElementById(id);
  const study = $("study");
  const listView = $("study-list");
  const sujetView = $("study-sujet");
  const EVAL = { ok: 1, half: 0.5, ko: 0 };
  const EVAL_LABEL = { ok: "Tout juste", half: "À moitié", ko: "À revoir" };

  let progress = {};        // progression française de l'élève, par sujet
  let current = null;       // sujet ouvert
  let saveTimer = 0;
  let chrono = { running: false, start: 0, base: 0, timer: 0 };

  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const underline = (s) => esc(s).replace(/\[\[(.+?)\]\]/g, "<u>$1</u>");
  const fmtPts = (n) => String(Math.round(n * 100) / 100).replace(".", ",");
  const qkey = (p, q) => `${p.id}-${q.id}`;
  const allQuestions = (s) => s.parties.flatMap((p) => p.questions.map((q) => ({ p, q })));

  // ---------- Progression ----------
  const store = () => window.Belamis && window.Belamis.store;

  async function loadProgress() {
    try {
      const all = (await store().read()) || {};
      progress = all.francais || {};
    } catch (_) {
      progress = {};
    }
  }

  function entry(id) {
    if (!progress[id]) progress[id] = { answers: {}, evals: {}, seconds: 0 };
    return progress[id];
  }

  function setSaveState(text) {
    const el = $("study-save");
    if (el) el.textContent = text;
  }

  function scheduleSave() {
    setSaveState("Modifications en cours…");
    clearTimeout(saveTimer);
    saveTimer = setTimeout(saveNow, 1000);
  }

  async function saveNow() {
    clearTimeout(saveTimer);
    if (!current) return;
    const id = current.id;
    const snapshot = JSON.parse(JSON.stringify(entry(id)));
    snapshot.updatedAt = new Date().toISOString();
    try {
      await store().update((all) => ({ ...all, francais: { ...(all.francais || {}), [id]: snapshot } }));
      const u = window.Belamis.user;
      setSaveState(u ? "Sauvegardé sur ton compte" : "Sauvegardé dans ce navigateur");
    } catch (_) {
      setSaveState("Échec de la sauvegarde. Vérifie ta connexion internet.");
    }
  }

  function score(s) {
    const e = progress[s.id];
    let got = 0, evaluated = 0, answered = 0;
    for (const { p, q } of allQuestions(s)) {
      const k = qkey(p, q);
      if (e && e.answers[k] && e.answers[k].trim()) answered++;
      if (e && e.evals[k]) { evaluated += q.points; got += q.points * EVAL[e.evals[k]]; }
    }
    return { got, evaluated, answered, total: allQuestions(s).length };
  }

  // ---------- Vue liste ----------
  function renderList() {
    const cards = DATA.sujets.map((s) => {
      const sc = score(s);
      const pct = Math.round((sc.answered / sc.total) * 100);
      const status = sc.evaluated
        ? `<span class="chip chip-score">${fmtPts(sc.got)} / ${fmtPts(sc.evaluated)} pts évalués</span>`
        : sc.answered ? `<span class="chip">${sc.answered} / ${sc.total} réponses</span>` : `<span class="chip chip-new">Nouveau</span>`;
      return `<button class="sujet-card" type="button" data-open="${s.id}">
        <span class="sujet-top">
          <span class="sujet-num">${s.officiel ? "Sujet 0 officiel" : "Sujet " + s.num}</span>
          <span class="sujet-genre">${esc(s.genre)}</span>
        </span>
        <span class="sujet-title">${esc(s.oeuvre)}</span>
        <span class="sujet-author">${esc(s.auteur)}, ${esc(s.date)}</span>
        <span class="sujet-theme">Réflexion : ${esc(s.theme)}</span>
        <span class="sujet-foot">${status}<span class="bar" aria-hidden="true"><i style="width:${pct}%"></i></span></span>
      </button>`;
    }).join("");
    $("study-sujets").innerHTML = cards;

    const counts = {};
    for (const s of DATA.sujets) for (const { q } of allQuestions(s)) counts[q.type] = (counts[q.type] || 0) + 1;
    $("study-types").innerHTML = Object.entries(DATA.types).map(([k, label]) =>
      `<button type="button" class="type-chip" data-type="${k}" aria-pressed="false">${esc(label)} <small>${counts[k] || 0}</small></button>`).join("");
    renderTypeList(null);
  }

  function renderTypeList(type) {
    document.querySelectorAll(".type-chip").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.type === type)));
    const box = $("study-type-list");
    if (!type) {
      box.innerHTML = `<p class="muted">Choisis un type d'exercice pour voir toutes les questions de ce type, tous sujets confondus.</p>`;
      return;
    }
    const items = [];
    for (const s of DATA.sujets) for (const { p, q } of allQuestions(s)) if (q.type === type) {
      const done = progress[s.id] && progress[s.id].evals[qkey(p, q)];
      items.push(`<li><button type="button" class="type-item" data-open="${s.id}" data-q="${qkey(p, q)}">
        <span class="type-item-head">${esc(s.auteur)} · <em>${esc(s.oeuvre)}</em> · ${p.id} question ${esc(q.id)} (${fmtPts(q.points)} pt${q.points > 1 ? "s" : ""})</span>
        <span class="type-item-q">${q.enonce}</span>
        ${done ? `<span class="chip chip-${done}">${EVAL_LABEL[done]}</span>` : ""}
      </button></li>`);
    }
    box.innerHTML = `<ul class="type-items">${items.join("")}</ul>`;
  }

  // ---------- Vue sujet ----------
  function renderSujet(s) {
    const e = entry(s.id);
    $("study-sujet-title").textContent = `${s.officiel ? "Sujet 0 officiel" : "Sujet " + s.num} · ${s.auteur}`;

    const texte = s.texte.map((p, i) => `<p><span class="par-num" aria-hidden="true">§${i + 1}</span>${underline(p)}</p>`).join("");
    $("study-text").innerHTML = `
      <header class="text-head">
        <span class="eyebrow-sm">${esc(s.genre)} · ${s.mots} mots</span>
        <h3><em>${esc(s.oeuvre)}</em></h3>
        <p class="text-author">${esc(s.auteur)} (${esc(s.date)})</p>
        <p class="text-context">${esc(s.contexte)}</p>
      </header>
      <div class="text-body">${texte}</div>
      ${s.notes.map((n) => `<p class="text-note">${n}</p>`).join("")}`;

    $("study-questions").innerHTML = s.parties.map((p) => `
      <section class="partie" aria-labelledby="partie-${p.id}">
        <header class="partie-head">
          <h3 id="partie-${p.id}"><span>Partie ${p.id.replace("A", "A.")}</span> ${esc(p.titre)}</h3>
          <span class="partie-pts" data-partie="${p.id}">${fmtPts(p.points)} points</span>
        </header>
        ${p.questions.map((q) => questionHTML(p, q, e)).join("")}
      </section>`).join("");

    updateTotals();
  }

  function questionHTML(p, q, e) {
    const k = qkey(p, q);
    const ev = e.evals[k];
    const big = q.type === "expression";
    return `<article class="question" id="q-${k}" data-key="${k}">
      <header class="question-head">
        <span class="question-num">${p.id.replace("A", "A.")} · ${esc(q.id)}</span>
        <span class="question-type">${esc(DATA.types[q.type])}</span>
        <span class="question-pts">${fmtPts(q.points)} pt${q.points > 1 ? "s" : ""}</span>
      </header>
      <p class="question-enonce">${q.enonce}</p>
      ${q.passage ? `<blockquote class="question-passage">${underline(q.passage)}</blockquote>` : ""}
      <label class="sr-only" for="a-${k}">Ta réponse</label>
      <textarea id="a-${k}" class="answer-input${big ? " big" : ""}" data-key="${k}" rows="${big ? 16 : 4}"
        placeholder="${big ? "Rédige ton développement : introduction, deux ou trois parties, conclusion…" : "Écris ta réponse ici…"}">${esc(e.answers[k] || "")}</textarea>
      <div class="question-actions">
        <button type="button" class="btn btn-ghost btn-sm reveal-btn" data-key="${k}" aria-expanded="${ev ? "true" : "false"}" aria-controls="c-${k}">
          ${ev ? "Masquer le corrigé" : "Voir le corrigé"}
        </button>
        ${big ? `<span class="word-count" data-count="${k}">${words(e.answers[k])} mots</span>` : ""}
      </div>
      <div class="corrige" id="c-${k}" ${ev ? "" : "hidden"}>
        <p class="corrige-title">Corrigé</p>
        ${q.corrige}
        <div class="self-eval" role="group" aria-label="Évalue ta réponse">
          <span>Ta réponse :</span>
          ${["ok", "half", "ko"].map((v) => `<button type="button" class="eval-btn eval-${v}" data-key="${k}" data-eval="${v}" aria-pressed="${ev === v}">${EVAL_LABEL[v]}</button>`).join("")}
        </div>
      </div>
    </article>`;
  }

  const words = (t) => (t || "").trim().split(/\s+/).filter(Boolean).length;

  function updateTotals() {
    if (!current) return;
    const sc = score(current);
    const e = entry(current.id);
    for (const p of current.parties) {
      let got = 0, ev = 0;
      for (const q of p.questions) {
        const v = e.evals[qkey(p, q)];
        if (v) { ev += q.points; got += q.points * EVAL[v]; }
      }
      const el = document.querySelector(`[data-partie="${p.id}"]`);
      if (el) el.textContent = ev ? `${fmtPts(got)} / ${fmtPts(p.points)} points` : `${fmtPts(p.points)} points`;
    }
    $("study-score").innerHTML = sc.evaluated
      ? `<strong>${fmtPts(sc.got)}</strong> / 20 <small>soit ${fmtPts(sc.got / 2)} / 10 au concours</small>`
      : `<small>${sc.answered} / ${sc.total} réponses</small>`;
    const warn = sc.evaluated === 20 && sc.got / 2 <= 2.5;
    $("study-score").classList.toggle("danger", warn);
    $("study-score").title = warn ? "Une note égale ou inférieure à 2,5 / 10 est éliminatoire." : "";
  }

  // ---------- Chrono (2 h conseillées) ----------
  const fmtTime = (sec) => {
    const h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60), s = Math.floor(sec % 60);
    return `${h}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  };
  const chronoSeconds = () => chrono.base + (chrono.running ? (performance.now() - chrono.start) / 1000 : 0);

  function renderChrono() {
    const sec = chronoSeconds();
    $("chrono-time").textContent = fmtTime(sec);
    $("chrono").classList.toggle("over", sec > 7200);
    $("chrono-btn").textContent = chrono.running ? "Pause" : sec ? "Reprendre" : "Lancer le chrono (2 h)";
  }

  function toggleChrono() {
    if (chrono.running) {
      chrono.base = chronoSeconds();
      chrono.running = false;
      clearInterval(chrono.timer);
      entry(current.id).seconds = Math.round(chrono.base);
      scheduleSave();
    } else {
      chrono.running = true;
      chrono.start = performance.now();
      chrono.timer = setInterval(renderChrono, 1000);
    }
    renderChrono();
  }

  function stopChrono() {
    if (chrono.running && current) {
      chrono.base = chronoSeconds();
      entry(current.id).seconds = Math.round(chrono.base);
    }
    chrono.running = false;
    clearInterval(chrono.timer);
  }

  // ---------- Navigation ----------
  function show(view) {
    listView.hidden = view !== "list";
    sujetView.hidden = view !== "sujet";
    study.scrollTop = 0;
    const scroller = view === "sujet" ? $("study-questions-wrap") : null;
    if (scroller) scroller.scrollTop = 0;
  }

  async function openStudy() {
    document.body.classList.add("studying");
    study.hidden = false;
    requestAnimationFrame(() => study.classList.add("open"));
    await loadProgress();
    renderList();
    show("list");
    $("study-close").focus();
  }

  function closeStudy() {
    if (current) { stopChrono(); saveNow(); current = null; }
    study.classList.remove("open");
    study.hidden = true;
    document.body.classList.remove("studying");
  }

  function openSujet(id, focusKey) {
    const s = DATA.sujets.find((x) => x.id === id);
    if (!s) return;
    current = s;
    stopChrono();
    chrono.base = entry(s.id).seconds || 0;
    renderSujet(s);
    renderChrono();
    setSaveState(window.Belamis.user ? "Sauvegarde automatique sur ton compte" : "Mode invité : sauvegarde dans ce navigateur");
    show("sujet");
    setMobileTab("questions");
    if (focusKey) {
      const el = $(`q-${focusKey}`);
      if (el) { el.scrollIntoView({ block: "start" }); el.classList.add("flash"); setTimeout(() => el.classList.remove("flash"), 1600); }
    }
  }

  function backToList() {
    stopChrono();
    saveNow();
    current = null;
    renderList();
    show("list");
  }

  function setMobileTab(tab) {
    sujetView.dataset.tab = tab;
    document.querySelectorAll(".mtab").forEach((b) => b.setAttribute("aria-selected", String(b.dataset.tab === tab)));
  }

  // ---------- Événements ----------
  $("open-francais").addEventListener("click", openStudy);
  $("study-close").addEventListener("click", closeStudy);
  $("study-back").addEventListener("click", backToList);
  $("chrono-btn").addEventListener("click", toggleChrono);
  document.querySelectorAll(".mtab").forEach((b) => b.addEventListener("click", () => setMobileTab(b.dataset.tab)));
  document.querySelectorAll(".list-tab").forEach((b) => b.addEventListener("click", () => {
    document.querySelectorAll(".list-tab").forEach((x) => x.setAttribute("aria-selected", String(x === b)));
    $("panel-sujets").hidden = b.dataset.panel !== "sujets";
    $("panel-types").hidden = b.dataset.panel !== "types";
  }));

  study.addEventListener("click", (ev) => {
    const open = ev.target.closest("[data-open]");
    if (open) { openSujet(open.dataset.open, open.dataset.q); return; }
    const type = ev.target.closest(".type-chip");
    if (type) { renderTypeList(type.getAttribute("aria-pressed") === "true" ? null : type.dataset.type); return; }
    const reveal = ev.target.closest(".reveal-btn");
    if (reveal) {
      const box = $(`c-${reveal.dataset.key}`);
      box.hidden = !box.hidden;
      reveal.textContent = box.hidden ? "Voir le corrigé" : "Masquer le corrigé";
      reveal.setAttribute("aria-expanded", String(!box.hidden));
      return;
    }
    const evalBtn = ev.target.closest(".eval-btn");
    if (evalBtn && current) {
      const e = entry(current.id);
      const k = evalBtn.dataset.key;
      e.evals[k] = e.evals[k] === evalBtn.dataset.eval ? undefined : evalBtn.dataset.eval;
      if (!e.evals[k]) delete e.evals[k];
      document.querySelectorAll(`.eval-btn[data-key="${k}"]`).forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.eval === e.evals[k])));
      updateTotals();
      scheduleSave();
    }
  });

  study.addEventListener("input", (ev) => {
    const t = ev.target.closest(".answer-input");
    if (!t || !current) return;
    entry(current.id).answers[t.dataset.key] = t.value;
    const wc = document.querySelector(`[data-count="${t.dataset.key}"]`);
    if (wc) wc.textContent = `${words(t.value)} mots`;
    updateTotals();
    scheduleSave();
  });

  document.addEventListener("keydown", (ev) => {
    if (ev.key !== "Escape" || study.hidden || !document.getElementById("auth").hidden) return;
    ev.stopPropagation();
    if (current) backToList(); else closeStudy();
  });

  window.addEventListener("beforeunload", () => { if (current) { stopChrono(); saveNow(); } });

  // l'espace se referme avec le retour à l'accueil
  $("back").addEventListener("click", () => { if (!study.hidden) closeStudy(); });
})();
