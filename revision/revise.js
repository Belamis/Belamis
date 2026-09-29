/*
 * Belamis — espace de travail de la 1re épreuve (CRPE BAC+3) : français (partie A) et mathématiques (partie B).
 * Liste des sujets, entraînement par type d'exercice, et page sujet :
 * texte à gauche (français), questions, réponses sauvegardées, corrigés et auto-évaluation.
 */
(() => {
  "use strict";

  const MATIERES = {
    francais: {
      data: window.BELAMIS_FRANCAIS,
      eyebrow: "Français · 1re épreuve d'admissibilité",
      title: "Partie A : un texte, <em>trois phases</em>.",
      intro: "Chaque sujet suit le modèle du CRPE BAC+3 : un texte de 500 mots au plus, puis l'étude de la langue (6 points), le lexique (4 points) et une réflexion rédigée d'une trentaine de lignes (10 points). Durée conseillée : 2 heures. Au concours, la partie est notée sur 10, et une note de 2,5 ou moins est éliminatoire.",
    },
    epreuve2: {
      data: window.BELAMIS_EPREUVE2,
      eyebrow: "2e épreuve d'admissibilité · 3 domaines sur 4",
      title: "Histoire-géo-EMC, sciences, arts, <em>langue vivante</em>.",
      intro: "Le jour de l'épreuve (4 heures, coefficient 3), tu choisis trois domaines sur quatre. Chaque domaine repose sur un dossier documentaire et des questions ; le programme est celui du cycle 4, avec les notions des cycles 1 à 3. Commence par le guide « Ce qui peut tomber », puis filtre les sujets par domaine. Une note globale de 5 sur 20 ou moins est éliminatoire.",
    },
    maths: {
      data: window.BELAMIS_MATHS,
      eyebrow: "Mathématiques · 1re épreuve d'admissibilité",
      title: "Partie B : des exercices, <em>du raisonnement</em>.",
      intro: "Le programme du concours est celui du cycle 4 (5e, 4e, 3e). Tu trouveras le sujet 0 officiel, les deux sujets de la session 2026, puis des sujets originaux inspirés des annales du CRPE et du brevet. Les questions marquées « Lycée » (programme de 2de et 1re) sont des approfondissements. Durée conseillée : 2 heures, calculatrice autorisée. La rédaction et la justification comptent dans la note.",
    },
    mayotte: {
      data: window.BELAMIS_MAYOTTE,
      eyebrow: "2nd concours interne · spécifique Mayotte",
      title: "Deux écrits sur 40, <em>trois oraux</em>.",
      intro: "Sujets construits sur le modèle des annales 2019-2025 de l'académie de Mayotte : français (compréhension orale, synthèse, langue et productions d'élèves) et maths-sciences (problème complexe, exercices, didactique), 4 heures chacun, une note de 10 sur 40 ou moins étant éliminatoire. Les oraux d'admission (étude de cas et mise en situation professionnelle) se préparent en 1 heure. Commence par le guide tiré des rapports de jury.",
    },
    interne1: {
      data: window.BELAMIS_INTERNE1,
      eyebrow: "1er concours interne · instituteurs titulaires",
      title: "Un dossier à analyser, <em>une classe à construire</em>.",
      intro: "Sujets construits sur le modèle des annales 2019-2025 de l'académie de Mayotte. L'écrit (4 heures, noté sur 40) demande d'analyser un dossier, puis de proposer une programmation et une séquence. L'oral (noté sur 40) s'appuie sur ton dossier personnel de 10 pages ; une épreuve facultative porte sur l'éducation prioritaire. Commence par le guide.",
    },
    "rev-bac3": {
      data: (window.BELAMIS_REV || {}).bac3,
      eyebrow: "CRPE BAC+3 · séances de révision conseillées",
      title: "Choisis un thème, <em>révise l'essentiel</em>.",
      intro: "Chaque séance dure 20 à 40 minutes : un rappel de cours, un quiz corrigé tout de suite, puis un ou deux exercices d'application. Rien n'est obligatoire : fais celles qui te manquent avant de t'attaquer aux sujets.",
    },
    "rev-myt2": {
      data: (window.BELAMIS_REV || {}).myt2,
      eyebrow: "2nd concours interne · séances de révision conseillées",
      title: "Choisis un thème, <em>révise l'essentiel</em>.",
      intro: "Chaque séance dure 20 à 40 minutes : un rappel de cours, un quiz corrigé tout de suite, puis un ou deux exercices d'application. Rien n'est obligatoire : fais celles qui te manquent avant les sujets d'écrit et d'oral.",
    },
    "rev-p1": {
      data: (window.BELAMIS_REV || {}).p1,
      eyebrow: "1er concours interne · séances de révision conseillées",
      title: "Choisis un thème, <em>révise l'essentiel</em>.",
      intro: "Chaque séance dure 20 à 40 minutes : un rappel de cours, un quiz corrigé tout de suite, puis un ou deux exercices d'application. Rien n'est obligatoire : fais celles qui te manquent avant l'écrit et la préparation de ton dossier.",
    },
  };

  // ---------- Concours : on choisit d'abord son concours, puis ses épreuves ----------
  const CONCOURS = {
    bac3: {
      nom: "CRPE BAC+3", lead: "CRPE BAC+3 : choisis une épreuve.",
      blocs: [
        { m: "francais", name: "Français", sub: "Épreuve 1 · partie A" },
        { m: "maths", name: "Mathématiques", sub: "Épreuve 1 · partie B" },
        { m: "epreuve2", name: "Épreuve 2", sub: "HG-EMC · sciences · arts · anglais" },
      ],
      rev: "rev-bac3",
    },
    myt2: {
      nom: "2nd concours interne", lead: "2nd concours interne spécifique Mayotte : choisis une épreuve.",
      blocs: [
        { m: "mayotte", dom: "francais", name: "Écrit de français", sub: "4 h · noté sur 40" },
        { m: "mayotte", dom: "maths", name: "Écrit de maths-sciences", sub: "4 h · noté sur 40" },
        { m: "mayotte", dom: "oral", name: "Oraux d'admission", sub: "Étude de cas · mise en situation" },
      ],
      rev: "rev-myt2",
    },
    p1: {
      nom: "1er concours interne", lead: "1er concours interne : choisis une épreuve.",
      blocs: [
        { m: "interne1", dom: "p1-ecrit", name: "Écrit d'admissibilité", sub: "4 h · analyse, programmation, séquence" },
        { m: "interne1", dom: "p1-oral", name: "Oral sur dossier", sub: "Exposé et entretien · noté sur 40" },
        { m: "interne1", dom: "p1-facultatif", name: "Épreuve facultative", sub: "Éducation prioritaire · sur 10" },
      ],
      rev: "rev-p1",
    },
  };
  const CONCOURS_KEY = "belamis-concours";

  function countSujets(m, dom) {
    const d = MATIERES[m] && MATIERES[m].data;
    if (!d) return 0;
    return d.sujets.filter((x) => !dom || x.domaine === dom).length;
  }

  function showConcours(id) {
    const c = CONCOURS[id];
    const choice = $("concours-choice"), blocs = $("concours-blocs"), lead = $("space-lead");
    if (!c) {
      choice.hidden = false; blocs.hidden = true;
      lead.textContent = "Ton guide de révision est prêt. Choisis d'abord ton concours.";
      try { localStorage.removeItem(CONCOURS_KEY); } catch (_) {}
      return;
    }
    try { localStorage.setItem(CONCOURS_KEY, id); } catch (_) {}
    choice.hidden = true; blocs.hidden = false;
    lead.textContent = c.lead;
    $("concours-list").innerHTML = c.blocs.map((b) => {
      const n = countSujets(b.m, b.dom);
      return `<button class="matiere" type="button" data-matiere="${b.m}"${b.dom ? ` data-dom="${b.dom}"` : ""}>
        <span class="matiere-name">${esc(b.name)}</span>
        <span class="matiere-sub">${esc(b.sub)}${n ? ` · ${n} sujet${n > 1 ? "s" : ""}` : ""}</span>
      </button>`;
    }).join("");
    const nr = countSujets(c.rev);
    $("concours-rev").innerHTML = `<button class="matiere matiere-rev" type="button" data-matiere="${c.rev}"${nr ? "" : " disabled"}>
        <span class="matiere-name">Séances de révision <small>conseillé</small></span>
        <span class="matiere-sub">${nr ? `Rappels de cours et quiz par thème, à faire quand tu veux · ${nr} thèmes` : "En préparation"}</span>
      </button>`;
  }

  const $ = (id) => document.getElementById(id);
  const study = $("study");
  const listView = $("study-list");
  const sujetView = $("study-sujet");
  const EVAL = { ok: 1, half: 0.5, ko: 0 };
  const EVAL_LABEL = { ok: "Tout juste", half: "À moitié", ko: "À revoir" };

  let matiere = "francais"; // matière ouverte
  let DATA = null;
  let domaine = "tous";      // filtre de la 2e épreuve
  let progress = {};         // progression de l'élève dans la matière ouverte, par sujet
  let current = null;        // sujet ouvert
  let saveTimer = 0;
  let chrono = { running: false, start: 0, base: 0, timer: 0 };

  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const underline = (s) => esc(s).replace(/\[\[(.+?)\]\]/g, "<u>$1</u>");
  const fmtPts = (n) => String(Math.round(n * 100) / 100).replace(".", ",");
  const pts = (n) => `${fmtPts(n)} pt${n > 1 ? "s" : ""}`;
  const qkey = (p, q) => `${p.id}-${q.id}`;
  const allQuestions = (s) => s.parties.flatMap((p) => p.questions.map((q) => ({ p, q })));
  const partShort = (p) => p.short || p.id.replace("A", "A.");
  const partLabel = (p) => p.label || `Partie ${p.id.replace("A", "A.")}`;
  const sujetTotal = (s) => s.total || 20;
  const sujetName = (s) => s.titre || (s.officiel ? "Sujet 0 officiel" : "Sujet " + s.num);

  // ---------- Progression ----------
  const store = () => window.Belamis && window.Belamis.store;

  async function loadProgress() {
    try {
      const all = (await store().read()) || {};
      progress = all[matiere] || {};
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
    const id = current.id, key = matiere;
    const snapshot = JSON.parse(JSON.stringify(entry(id)));
    snapshot.updatedAt = new Date().toISOString();
    try {
      await store().update((all) => ({ ...all, [key]: { ...(all[key] || {}), [id]: snapshot } }));
      setSaveState(window.Belamis.user ? "Sauvegardé sur ton compte" : "Sauvegardé dans ce navigateur");
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
  function renderIntro() {
    const m = MATIERES[matiere];
    $("study-eyebrow").textContent = m.eyebrow;
    $("study-heading").innerHTML = m.title;
    $("study-desc").textContent = m.intro;
    study.setAttribute("aria-label", ({ maths: "Sujets de mathématiques", francais: "Sujets de français", epreuve2: "Sujets de la 2e épreuve", mayotte: "Sujets du 2nd concours interne", interne1: "Sujets du 1er concours interne" }[matiere] || "Séances de révision"));
  }

  function cardHTML(s) {
    const sc = score(s);
    const pct = Math.round((sc.answered / sc.total) * 100);
    const status = sc.evaluated
      ? `<span class="chip chip-score">${fmtPts(sc.got)} / ${fmtPts(sc.evaluated)} pts évalués</span>`
      : sc.answered ? `<span class="chip">${sc.answered} / ${sc.total} réponses</span>` : `<span class="chip chip-new">Nouveau</span>`;
    const kind = s.revision ? `Séance · ${Math.round((s.duree || 1800) / 60)} min` : s.officiel ? "Annale officielle" : s.lycee ? "Approfondissement" : s.entrainement ? "Entraînement rapide" : /oral/.test(s.domaine) ? "Oral d'admission" : "Sujet type";
    const top = s.texte
      ? `<span class="sujet-num">${sujetName(s)}</span><span class="sujet-genre">${esc(s.genre)}</span>`
      : `<span class="sujet-num">${kind}</span><span class="sujet-genre">${DATA.domaines ? esc(DATA.domaines[s.domaine] || "") : `noté sur ${sujetTotal(s)}`}</span>`;
    const body = s.texte
      ? `<span class="sujet-title">${esc(s.oeuvre)}</span><span class="sujet-author">${esc(s.auteur)}, ${esc(s.date)}</span><span class="sujet-theme">Réflexion : ${esc(s.theme)}</span>`
      : `<span class="sujet-title">${esc(s.titre)}</span><span class="sujet-theme">${esc(s.theme)}</span>`;
    return `<button class="sujet-card${s.lycee ? " is-lycee" : ""}" type="button" data-open="${s.id}">
      <span class="sujet-top">${top}</span>${body}
      <span class="sujet-foot">${status}<span class="bar" aria-hidden="true"><i style="width:${pct}%"></i></span></span>
    </button>`;
  }

  const visibleSujets = () => DATA.sujets.filter((s) => !DATA.domaines || domaine === "tous" || s.domaine === domaine);

  function renderDomains() {
    const box = $("study-domains"), guide = $("study-guide");
    if (!DATA.domaines) { box.hidden = true; guide.hidden = true; return; }
    box.hidden = false;
    const n = (d) => DATA.sujets.filter((s) => d === "tous" || s.domaine === d).length;
    box.innerHTML = [["tous", "Tous les domaines"], ...Object.entries(DATA.domaines)].map(([k, label]) =>
      `<button type="button" class="type-chip dom-chip" data-domaine="${k}" aria-pressed="${k === domaine}">${esc(label)} <small>${n(k)}</small></button>`).join("");
    guide.hidden = !DATA.guide;
    if (DATA.guide && guide.dataset.filled !== matiere) {
      guide.innerHTML = `<summary>${esc(DATA.guideTitre || "Ce qui peut tomber en histoire-géo-EMC : le programme passé au crible")}</summary><div class="guide-body">${DATA.guide}</div>`;
      guide.dataset.filled = matiere;
      guide.open = false;
    }
  }

  function renderList() {
    renderIntro();
    renderDomains();
    $("study-sujets").innerHTML = visibleSujets().map(cardHTML).join("");

    const counts = {};
    for (const s of visibleSujets()) for (const { q } of allQuestions(s)) counts[q.type] = (counts[q.type] || 0) + 1;
    $("study-types").innerHTML = Object.entries(DATA.types).filter(([k]) => counts[k]).map(([k, label]) =>
      `<button type="button" class="type-chip" data-type="${k}" aria-pressed="false">${esc(label)} <small>${counts[k] || 0}</small></button>`).join("");
    renderTypeList(null);
  }

  function renderTypeList(type) {
    document.querySelectorAll(".type-chip[data-type]").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.type === type)));
    const box = $("study-type-list");
    if (!type) {
      box.innerHTML = `<p class="muted">Choisis un type d'exercice pour voir toutes les questions de ce type, tous sujets confondus.</p>`;
      return;
    }
    const items = [];
    for (const s of visibleSujets()) for (const { p, q } of allQuestions(s)) if (q.type === type) {
      const done = progress[s.id] && progress[s.id].evals[qkey(p, q)];
      const where = s.texte ? `${esc(s.auteur)} · <em>${esc(s.oeuvre)}</em>` : esc(sujetName(s));
      items.push(`<li><button type="button" class="type-item" data-open="${s.id}" data-q="${qkey(p, q)}">
        <span class="type-item-head">${where} · ${partShort(p)} question ${esc(q.id)} (${pts(q.points)})${q.niveau === "lycee" ? ` <span class="badge-lycee">Lycée</span>` : ""}</span>
        <span class="type-item-q">${q.enonce}</span>
        ${done ? `<span class="chip chip-${done}">${EVAL_LABEL[done]}</span>` : ""}
      </button></li>`);
    }
    box.innerHTML = `<ul class="type-items">${items.join("")}</ul>`;
  }

  // ---------- Vue sujet ----------
  function renderSujet(s) {
    const e = entry(s.id);
    const hasText = Boolean(s.texte);
    sujetView.classList.toggle("no-text", !hasText);
    $("study-sujet-title").textContent = hasText ? `${sujetName(s)} · ${s.auteur}` : sujetName(s);

    $("study-text").innerHTML = hasText ? `
      <header class="text-head">
        <span class="eyebrow-sm">${esc(s.genre)} · ${s.mots} mots</span>
        <h3><em>${esc(s.oeuvre)}</em></h3>
        <p class="text-author">${esc(s.auteur)} (${esc(s.date)})</p>
        <p class="text-context">${esc(s.contexte)}</p>
      </header>
      <div class="text-body">${s.texte.map((p, i) => `<p><span class="par-num" aria-hidden="true">§${i + 1}</span>${underline(p)}</p>`).join("")}</div>
      ${s.notes.map((n) => `<p class="text-note">${n}</p>`).join("")}` : "";

    const head = hasText ? "" : `<header class="sujet-head">
        ${s.source ? `<p class="sujet-source">${esc(s.source)}</p>` : ""}
        <p class="sujet-meta">${s.revision ? `Séance de révision conseillée · environ ${Math.round((s.duree || 1800) / 60)} minutes · lis le rappel, puis fais le quiz : il se corrige dès que tu ouvres la correction.` : matiere === "mayotte" || matiere === "interne1" ? metaMayotte(s) : matiere === "maths" ? `Calculatrice autorisée · noté sur ${sujetTotal(s)} · justifie tes réponses, sauf mention contraire.` : s.entrainement ? `${allQuestions(s).length} questions · réponds de tête, puis vérifie.` : `${esc((DATA.domaines || {})[s.domaine] || "")} · noté sur ${sujetTotal(s)} · appuie-toi sur les documents et sur tes connaissances.`}</p>
        ${s.remarque ? `<p class="sujet-remarque">${esc(s.remarque)}</p>` : ""}
      </header>`;

    $("study-questions").innerHTML = head + s.parties.map((p) => `
      <section class="partie" aria-labelledby="partie-${p.id}">
        <header class="partie-head">
          <h3 id="partie-${p.id}"><span>${esc(partLabel(p))}</span> ${esc(p.titre || "")}</h3>
          ${p.points ? `<span class="partie-pts" data-partie="${p.id}">${pts(p.points)}</span>` : ""}
        </header>
        ${p.intro ? `<div class="partie-intro math">${p.intro}</div>` : ""}
        ${p.audio ? audioHTML(p) : ""}
        ${p.questions.map((q) => questionHTML(p, q, e)).join("")}
      </section>`).join("");

    updateTotals();
  }

  function metaMayotte(s) {
    const h = (s.duree || 7200) / 3600;
    if (s.domaine === "p1-ecrit") return `1er concours interne · durée : 4 heures · noté sur ${sujetTotal(s)} · deux parties de quatre pages au plus chacune.`;
    if (s.domaine === "p1-oral") return `1er concours interne · noté sur ${sujetTotal(s)} · 15 minutes de préparation, exposé de 10 minutes, entretien de 10 minutes.`;
    if (s.domaine === "p1-facultatif") return `1er concours interne · épreuve facultative de 10 minutes · notée sur ${sujetTotal(s)} ; seuls les points au-dessus de la moyenne comptent.`;
    if (s.domaine === "oral") return `Préparation : ${h} h · noté sur ${sujetTotal(s)} · exposé de 10 minutes puis entretien de 20 minutes avec le jury.`;
    return `Durée : ${h} heures${s.domaine === "maths" ? " · calculatrice autorisée" : " · sans document ni calculatrice"} · noté sur ${sujetTotal(s)} · une note de ${s.eliminatoire} ou moins est éliminatoire.`;
  }

  // ---------- Compréhension orale : le texte est lu deux fois par la synthèse vocale ----------
  const speech = { on: false, key: null };

  function audioHTML(p) {
    const a = p.audio;
    const ok = "speechSynthesis" in window;
    return `<div class="audio-box" data-audio="${p.id}">
      <p class="audio-title">Texte entendu : « ${esc(a.titre)} »</p>
      <p class="audio-help">${ok
        ? "Comme au concours, le texte est lu deux fois de suite (titre compris). Prends des notes, puis réponds au questionnaire sans relire le texte : 30 minutes en tout à partir de la première lecture."
        : "Ton navigateur ne propose pas de lecture à voix haute : fais-toi lire le texte par quelqu'un, ou lis-le une seule fois avant de le masquer."}</p>
      <div class="audio-actions">
        ${ok ? `<button type="button" class="btn btn-primary btn-sm audio-play" data-audio="${p.id}">Écouter les deux lectures</button>` : ""}
        <button type="button" class="btn btn-ghost btn-sm audio-show" data-audio="${p.id}" aria-expanded="false">Afficher le texte</button>
        <span class="audio-state" data-audio-state="${p.id}" aria-live="polite"></span>
      </div>
      <div class="audio-text" data-audio-text="${p.id}" hidden>
        <p class="audio-text-title">${esc(a.titre)}</p>
        ${a.texte.map((t) => `<p>${esc(t)}</p>`).join("")}
        ${a.source ? `<p class="doc-src">${esc(a.source)}</p>` : ""}
      </div>
    </div>`;
  }

  function frenchVoice() {
    const vs = window.speechSynthesis.getVoices().filter((v) => /^fr(-|_|$)/i.test(v.lang));
    return vs.find((v) => /fr-FR/i.test(v.lang) && v.localService) || vs.find((v) => /fr-FR/i.test(v.lang)) || vs[0] || null;
  }

  function stopSpeech() {
    if (!("speechSynthesis" in window)) return;
    speech.on = false;
    window.speechSynthesis.cancel();
    document.querySelectorAll(".audio-play").forEach((b) => { b.textContent = "Écouter les deux lectures"; });
    document.querySelectorAll("[data-audio-state]").forEach((el) => { el.textContent = ""; });
  }

  function playAudio(id) {
    const p = current && current.parties.find((x) => x.id === id);
    if (!p || !p.audio) return;
    if (speech.on) { stopSpeech(); return; }
    const synth = window.speechSynthesis;
    synth.cancel();
    const voice = frenchVoice();
    const state = document.querySelector(`[data-audio-state="${id}"]`);
    const btn = document.querySelector(`.audio-play[data-audio="${id}"]`);
    const chunks = [p.audio.titre, ...p.audio.texte];
    const utter = (text, lecture, i) => {
      const u = new SpeechSynthesisUtterance(text);
      u.lang = "fr-FR";
      if (voice) u.voice = voice;
      u.rate = lecture === 1 ? 0.95 : 1;
      u.onstart = () => { if (state) state.textContent = `Lecture ${lecture} sur 2 · paragraphe ${i} sur ${chunks.length - 1 || 1}`; };
      return u;
    };
    speech.on = true;
    btn.textContent = "Arrêter la lecture";
    if (!voice && state) state.textContent = "Aucune voix française trouvée : la lecture utilise la voix par défaut.";
    for (const lecture of [1, 2]) chunks.forEach((t, i) => synth.speak(utter(t, lecture, i)));
    const last = new SpeechSynthesisUtterance(" ");
    last.onend = () => { if (!speech.on) return; stopSpeech(); if (state) state.textContent = "Fin des deux lectures : réponds maintenant au questionnaire."; };
    synth.speak(last);
  }

  // ---------- QCM (« la ou les réponses correctes ») ----------
  const qcmChoice = (v) => (v || "").split(",").filter(Boolean).map(Number).sort((a, b) => a - b);

  function qcmHTML(q, k, e, shown) {
    const chosen = qcmChoice(e.answers[k]);
    return `<fieldset class="qcm" data-key="${k}"><legend class="sr-only">Coche la ou les bonnes réponses</legend>
      ${q.options.map((o, i) => {
        const mark = shown ? (q.bonnes.includes(i) ? " is-good" : chosen.includes(i) ? " is-bad" : "") : "";
        return `<label class="qcm-opt${mark}"><input type="checkbox" class="qcm-input" data-key="${k}" value="${i}" ${chosen.includes(i) ? "checked" : ""}><span>${o}</span></label>`;
      }).join("")}
    </fieldset>`;
  }

  function markQcm(k, q, show) {
    const chosen = qcmChoice(entry(current.id).answers[k]);
    document.querySelectorAll(`.qcm[data-key="${k}"] .qcm-opt`).forEach((lab, i) => {
      lab.classList.toggle("is-good", show && q.bonnes.includes(i));
      lab.classList.toggle("is-bad", show && !q.bonnes.includes(i) && chosen.includes(i));
    });
  }

  function findQuestion(k) {
    for (const { p, q } of allQuestions(current)) if (qkey(p, q) === k) return q;
    return null;
  }

  function questionHTML(p, q, e) {
    const k = qkey(p, q);
    const ev = e.evals[k];
    const big = (q.type === "expression" && matiere === "francais") || ["synthese", "analyse", "programmation", "sequence"].includes(q.type);
    const isQcm = Array.isArray(q.options);
    return `<article class="question" id="q-${k}" data-key="${k}">
      <header class="question-head">
        <span class="question-num">${partShort(p)} · ${esc(q.id)}</span>
        <span class="question-type">${esc(DATA.types[q.type])}</span>
        ${q.niveau === "lycee" ? `<span class="badge-lycee" title="Hors programme du concours : niveau 2de ou 1re">Lycée</span>` : ""}
        <span class="question-pts">${pts(q.points)}</span>
      </header>
      <div class="question-enonce math">${q.enonce}</div>
      ${q.passage ? `<blockquote class="question-passage">${underline(q.passage)}</blockquote>` : ""}
      ${isQcm ? qcmHTML(q, k, e, Boolean(ev)) : `<label class="sr-only" for="a-${k}">Ta réponse</label>
      <textarea id="a-${k}" class="answer-input${big ? " big" : ""}" data-key="${k}" rows="${big ? 16 : 4}"
        placeholder="${placeholder(q, big)}">${esc(e.answers[k] || "")}</textarea>`}
      <div class="question-actions">
        <button type="button" class="btn btn-ghost btn-sm reveal-btn" data-key="${k}" aria-expanded="${ev ? "true" : "false"}" aria-controls="c-${k}">
          ${ev ? "Masquer le corrigé" : "Voir le corrigé"}
        </button>
        ${big ? `<span class="word-count" data-count="${k}">${words(e.answers[k])} mots</span>` : ""}
      </div>
      <div class="corrige math" id="c-${k}" ${ev ? "" : "hidden"}>
        <p class="corrige-title">Corrigé</p>
        ${q.corrige}
        <div class="self-eval" role="group" aria-label="Évalue ta réponse">
          <span>Ta réponse :</span>
          ${["ok", "half", "ko"].map((v) => `<button type="button" class="eval-btn eval-${v}" data-key="${k}" data-eval="${v}" aria-pressed="${ev === v}">${EVAL_LABEL[v]}</button>`).join("")}
        </div>
      </div>
    </article>`;
  }

  function placeholder(q, big) {
    if (["analyse", "programmation", "sequence"].includes(q.type)) return q.type === "analyse" ? "Problématique, plan, idées clés de chaque partie en croisant les documents…" : "Construis ta proposition (périodes, objectifs, séances, évaluation)…";
    if (big) return q.type === "synthese" ? "Rédige ta réponse : introduction avec la problématique, développement en deux ou trois parties qui croisent les textes, conclusion…" : "Rédige ton développement : introduction, deux ou trois parties, conclusion…";
    if (q.type === "dossier") return "Tes notes pour ton propre dossier…";
    if (q.type === "expose") return "Note ton plan d'exposé : problématique, deux ou trois parties, conclusion (pas de phrases entières, comme le jour de l'oral)…";
    if (q.type === "entretien" || q.type === "valeurs") return "Réponds comme devant le jury, en quelques phrases précises et argumentées…";
    if (q.type === "qualite") return "Relis ta copie avec la grille du corrigé et note ici ce que tu dois corriger…";
    if (matiere === "maths" || ["calcul", "probleme"].includes(q.type)) return "Écris ta démarche et ton résultat…";
    return q.type === "expression" ? "Write your answer here…" : "Écris ta réponse ici…";
  }

  const words = (t) => (t || "").trim().split(/\s+/).filter(Boolean).length;

  function updateTotals() {
    if (!current) return;
    const sc = score(current);
    const e = entry(current.id);
    const total = sujetTotal(current);
    for (const p of current.parties) {
      let got = 0, ev = 0;
      for (const q of p.questions) {
        const v = e.evals[qkey(p, q)];
        if (v) { ev += q.points; got += q.points * EVAL[v]; }
      }
      const el = document.querySelector(`[data-partie="${p.id}"]`);
      if (el) el.textContent = ev ? `${fmtPts(got)} / ${pts(p.points)}` : pts(p.points);
    }
    const sur10 = (sc.got / total) * 10;
    const conversion = total !== 10 && (matiere === "francais" || matiere === "maths") && !current.entrainement;
    $("study-score").innerHTML = sc.evaluated
      ? `<strong>${fmtPts(sc.got)}</strong> / ${total}${conversion ? ` <small>soit ${fmtPts(sur10)} / 10 au concours</small>` : ""}`
      : `<small>${sc.answered} / ${sc.total} réponses</small>`;
    const seuil = current.eliminatoire;
    const warn = Math.abs(sc.evaluated - total) < 1e-9 && !current.entrainement
      && (seuil != null ? sc.got <= seuil : conversion && sur10 <= 2.5);
    $("study-score").classList.toggle("danger", warn);
    $("study-score").title = warn ? (seuil != null ? `Une note égale ou inférieure à ${seuil} / ${total} est éliminatoire.` : "Une note égale ou inférieure à 2,5 / 10 est éliminatoire.") : "";
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
    const lim = (current && current.duree) || 7200;
    $("chrono").classList.toggle("over", sec > lim);
    const lab = lim >= 3600 ? `${lim / 3600} h` : `${Math.round(lim / 60)} min`;
    $("chrono-btn").textContent = chrono.running ? "Pause" : sec ? "Reprendre" : `Lancer le chrono (${lab})`;
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
  }

  async function openStudy(which, dom) {
    if (!MATIERES[which] || !MATIERES[which].data) return;
    matiere = which;
    DATA = MATIERES[which].data;
    domaine = dom || "tous";
    document.body.classList.add("studying");
    study.hidden = false;
    requestAnimationFrame(() => study.classList.add("open"));
    await loadProgress();
    renderList();
    show("list");
    $("study-close").focus();
  }

  function closeStudy() {
    stopSpeech();
    if (current) { stopChrono(); saveNow(); current = null; }
    study.classList.remove("open");
    study.hidden = true;
    document.body.classList.remove("studying");
  }

  function openSujet(id, focusKey) {
    const s = DATA.sujets.find((x) => x.id === id);
    if (!s) return;
    stopSpeech();
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
    stopSpeech();
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
  document.addEventListener("click", (ev) => {
    const c = ev.target.closest("[data-concours]");
    if (c) { showConcours(c.dataset.concours); return; }
    if (ev.target.closest("#concours-change")) { showConcours(null); return; }
    const b = ev.target.closest("[data-matiere]");
    if (b && !study.contains(b)) openStudy(b.dataset.matiere, b.dataset.dom);
  });
  try { showConcours(localStorage.getItem(CONCOURS_KEY)); } catch (_) { showConcours(null); }
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
    const dom = ev.target.closest(".dom-chip");
    if (dom) { domaine = dom.dataset.domaine; renderList(); return; }
    const type = ev.target.closest(".type-chip");
    if (type) { renderTypeList(type.getAttribute("aria-pressed") === "true" ? null : type.dataset.type); return; }
    const play = ev.target.closest(".audio-play");
    if (play) { playAudio(play.dataset.audio); return; }
    const showTxt = ev.target.closest(".audio-show");
    if (showTxt) {
      const box = document.querySelector(`[data-audio-text="${showTxt.dataset.audio}"]`);
      box.hidden = !box.hidden;
      showTxt.textContent = box.hidden ? "Afficher le texte" : "Masquer le texte";
      showTxt.setAttribute("aria-expanded", String(!box.hidden));
      return;
    }
    const reveal = ev.target.closest(".reveal-btn");
    if (reveal) {
      const box = $(`c-${reveal.dataset.key}`);
      box.hidden = !box.hidden;
      const q = current && findQuestion(reveal.dataset.key);
      if (q && Array.isArray(q.options)) {
        markQcm(reveal.dataset.key, q, !box.hidden);
        const e = entry(current.id), k = reveal.dataset.key;
        if (!box.hidden && !e.evals[k] && e.answers[k]) {
          const ok = qcmChoice(e.answers[k]).join() === [...q.bonnes].sort((a, b) => a - b).join();
          e.evals[k] = ok ? "ok" : "ko";
          document.querySelectorAll(`.eval-btn[data-key="${k}"]`).forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.eval === e.evals[k])));
          updateTotals();
          scheduleSave();
        }
      }
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

  study.addEventListener("change", (ev) => {
    const c = ev.target.closest(".qcm-input");
    if (!c || !current) return;
    const k = c.dataset.key;
    const vals = [...document.querySelectorAll(`.qcm-input[data-key="${k}"]`)].filter((x) => x.checked).map((x) => x.value);
    entry(current.id).answers[k] = vals.join(",");
    updateTotals();
    scheduleSave();
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
