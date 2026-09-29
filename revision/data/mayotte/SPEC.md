# Belamis — 2nd concours interne CRPE spécifique Mayotte : format des fichiers de sujets

Les sujets originaux officiels (texte extrait des PDF) sont dans :
/tmp/claude-0/-home-user-Belamis/871cbcdd-87c6-53f0-82ea-4f6d34f33643/scratchpad/mayotte/*.txt
- sujet-1-crpe-myt-session-20XX-*.txt = épreuve de français (2023, 2024, 2025) ; crpe-2019/cpre-2020/2021/2022 premi-re = français plus anciens
- sujet-2-crpe-myt-session-20XX-*.txt = épreuve maths-sciences-techno ; *deuxi-me* = anciennes
- texte-compr-hension-orale-session-20XX = texte lu aux candidats (compréhension orale)
- rj2023.txt, rj2025.txt = rapports de jury (format des épreuves, attentes, conseils)
LIS-LES (au moins 2023-2025) avant d'écrire : il faut reproduire exactement le type de questions et le niveau.

## Format des épreuves (arrêté du 19 juillet 2016, rapports 2023 et 2025)
Français, 4 h (dont 30 min pour la 1re partie), /40, note ≤ 10 éliminatoire :
 P1 compréhension orale d'un texte didactique (8 pts) : texte lu 2 fois, puis QCM (« la ou les réponses correctes ») ;
 P2 compréhension écrite et rédaction (12 pts) : réponse construite / synthèse sur un corpus de textes littéraires ou documentaires (sciences humaines) ;
 P3 connaissance de la langue et approche didactique à partir de productions d'élèves (14 pts) ;
 + 6 pts de correction syntaxique et qualité écrite.
Maths-sciences-techno, 4 h, calculatrice autorisée, /40, ≤ 10 éliminatoire :
 P1 problème complexe (10 pts) — souvent contextualisé à Mayotte (eau, population, énergie, nutrition) avec 4-6 documents ;
 P2 exercices (12 pts) : vrai/faux justifié, QCM, suites de motifs, géométrie, Scratch, probabilités, fonctions, ET sciences (corps humain, états de l'eau, astronomie…) ;
 P3 didactique : analyse de productions d'élèves de la maternelle au cycle 3 (14 pts) ;
 + 4 pts de qualité syntaxique et écrite.
Admission (oraux) : 1) mise en situation professionnelle /50 (1 h de préparation ; exposé 10 min /20, entretien 20 min /30 ; dossier de 5 pages max choisi parmi 3 disciplines) ;
 2) étude de cas « connaissance du système éducatif et dimension éthique » /50 (1 h ; exposé 10 min /15, entretien 20 min /25, valeurs de la République /10 ; dossier de 4 pages max sur une situation professionnelle ordinaire de l'école primaire, avec TROIS questions ; particularités de Mayotte attendues) ;
 3) épreuve au choix (LVE ou EPS).

## Fichier à produire : JSON UTF-8 {"sujets": [ ... ]}
Chaque sujet :
{
 "id": "myt-fr-1",                // unique, préfixe myt-fr- / myt-ms- / myt-oral-
 "num": 1,
 "domaine": "francais" | "maths" | "oral",
 "titre": "Sujet 1 · L'enfant et l'école",
 "theme": "une ligne résumant le contenu",
 "source": "Sujet original construit sur le modèle de la session 2024 (académie de Mayotte)",
 "remarque": "facultatif : précision (données simplifiées, etc.)",
 "total": 40 (écrits) ou 50 (oraux),
 "eliminatoire": 10 (écrits uniquement ; omettre pour les oraux),
 "duree": 14400 (écrits, en secondes) ou 3600 (oraux : temps de préparation),
 "parties": [
   {"id": "P1", "label": "Première partie", "short": "P1", "titre": "Compréhension orale d’un texte didactique", "points": 8,
    "intro": "HTML (consignes, documents)",
    "audio": {"titre": "titre lu", "texte": ["paragraphe 1", "paragraphe 2", ...], "source": "référence"},   // UNIQUEMENT pour la compréhension orale
    "questions": [
      {"id": "1", "type": "...", "points": 1, "enonce": "HTML", "corrige": "HTML",
       "options": ["choix A", "choix B", "choix C"], "bonnes": [0, 2] }   // options/bonnes UNIQUEMENT pour les QCM
    ]}
 ]
}
Contrainte : la somme des points des questions = points de la partie ; la somme des parties = total.
Types autorisés : "oral-qcm" (QCM de compréhension orale), "synthese" (réponse construite sur corpus), "langue" (grammaire, orthographe, conjugaison, lexique), "didactique-fr" (analyse de production d'élève, annotations, séance, remédiation en français), "probleme" (problème complexe), "calcul" (exercices de maths), "sciences" (sciences et technologie), "didactique-maths" (analyse d'erreurs d'élèves en maths), "qualite" (qualité de la langue écrite : dernière partie « Qualité de l’écrit » d'un écrit, 1 question auto-évaluée avec une grille dans le corrigé), "expose" (exposé oral), "entretien" (question du jury), "valeurs" (valeurs de la République / laïcité / éthique).
Pour les écrits, ajoute en DERNIÈRE partie : {"id":"Q","label":"Qualité de l’écrit","short":"Q","titre":"Correction syntaxique et qualité écrite","points":6 (français) ou 4 (maths),"questions":[{"id":"1","type":"qualite",...}]} — énoncé : relire sa copie ; corrigé : grille de relecture précise (accords, conjugaison, ponctuation, lexique, lisibilité, structuration) et comment se répartissent les points.

HTML utilisable (classes CSS existantes) :
- document : <div class="doc"><p class="doc-title">Document 1 – titre</p> ... <p class="doc-src">Source</p></div> ; citation : <blockquote>…</blockquote>
- production d'élève : <div class="copie-eleve"><p class="copie-titre">Production de Nassim (CM1)</p><p>texte AVEC les erreurs de l'élève, numérotation de lignes si besoin</p><p class="annot">annotation de l'enseignant</p></div>
- figures : <figure class="fig"><svg viewBox="…" role="img" aria-label="description" xmlns="http://www.w3.org/2000/svg">…</svg><figcaption>…</figcaption></figure> ; classes SVG : stroke, thin, thick, dash, grid, axis, shade, tile, fillink, c1 c2 c3 (couleurs de trait), l1 l2 (textes colorés), c-blue c-yellow c-red (remplissages) ; <text> hérite de la police.
- fractions : <span class="frac"><span>3</span><span>4</span></span>
- tableaux : <table class="tab"><tr><th>…</th></tr><tr><td>…</td></tr></table>
- Scratch : décris le script en liste <ol> ou <pre> (pas de blocs graphiques).
Échappe correctement le JSON (guillemets). Apostrophe typographique ’ de préférence. Pas d'emoji.

## Exigences de contenu
- Tout est ORIGINAL et « adapté » des sujets officiels : même structure, mêmes types de questions, thèmes proches mais renouvelés. Ne recopie pas les sujets officiels.
- Textes littéraires : UNIQUEMENT domaine public (auteur mort avant 1950 : Hugo, Vallès, Daudet, Zola, Maupassant, Pergaud, Jules Renard, George Sand, Rousseau, Montaigne, Anatole France, Jules Verne, Alain-Fournier, Proust, La Fontaine, Rimbaud…), citation EXACTE vérifiée sur Wikisource (WebFetch fr.wikisource.org) — sinon ne cite pas. Textes didactiques/documentaires : rédige toi-même un texte original (« Texte rédigé pour Belamis, d’après les travaux de … ») ou cite de courts extraits de textes officiels (programmes, BO, guides Eduscol) vérifiés.
- Contexte mahorais bienvenu et respectueux : prénoms mahorais (Anli, Nassim, Faïza, Zaïnaba, Ibrahim, Riziki, Mouhamadi, Nafissa, Soilihi, Hadidja…), lieux (Mamoudzou, Dzaoudzi, Petite-Terre, Sada, Chirongui, lagon, barge, mangrove, maki, tortues, ylang-ylang, vanille), plurilinguisme (shimaoré, kibushi, français langue de scolarisation), crise de l’eau, rotations scolaires… Les données chiffrées sur Mayotte doivent être VÉRIFIÉES (WebSearch/WebFetch, INSEE, ARS, académie) ou explicitement signalées « données simplifiées pour l’exercice ».
- Corrigés détaillés, justes, pédagogiques, conformes aux programmes 2024-2025 (cycles 1 à 3, nouveaux programmes de français et de maths de cycles 1-2 entrés en vigueur à la rentrée 2025 pour la maternelle, CP, CE1, CE2 ; vérifie ce que tu affirmes), avec les références institutionnelles utiles (guides fondamentaux « orange » CP, « rouge » maths CP, « pour enseigner le vocabulaire », Eduscol, socle commun, évaluations nationales, enseignement explicite). Le rapport 2025 reproche : paraphrase, absence de problématique, confusion programmation/progression, méconnaissance d’Eduscol et des guides : les corrigés doivent montrer ce qui est attendu.
- Chaque calcul vérifié (fais-le en Python si besoin). Chaque QCM : bonnes réponses sans ambiguïté, justifiées dans le corrigé.
- Valide ton fichier : json.load OK, sommes de points OK, types autorisés, ids uniques.
