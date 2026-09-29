# Belamis — Révision des notions (une fiche par notion, français et mathématiques)

Bibliothèque commune aux trois concours (CRPE BAC+3, 2nd concours interne Mayotte, 1er concours interne).
Chaque fiche = UNE notion précise (ex. « Le théorème de Pythagore », « L'accord du participe passé avec avoir »),
à réviser en 10 à 25 minutes : rappel de cours, exemples résolus, pièges, un encart « À l’école » (comment la notion
s’enseigne à l’école primaire, erreurs typiques des élèves, programmes en vigueur), puis quiz et applications.

Format JSON identique aux séances de révision : lis /home/user/Belamis/revision/data/revisions/SPEC.md (structure,
classes HTML, règles de validation) et prends exemple sur /home/user/Belamis/revision/data/revisions/bac3_fm.json
(déjà relu : niveau, ton, terminologie officielle). Différences :
- "id" préfixé « not-ma- » (maths) ou « not-fr- » (français) ; "revision": true ; "duree" entre 600 et 1500 ;
- "domaine" = la sous-catégorie : maths → "nombres", "calcul", "geometrie", "grandeurs", "donnees" ;
  français → "grammaire", "conjugaison", "orthographe", "lexique", "texte" ;
- "num" = ordre d’apparition dans la sous-catégorie (du plus simple au plus avancé) ;
- partie R (Rappel, 0 point) : cours complet mais concis (définitions, propriétés, méthode pas à pas, 2 ou 3 exemples
  résolus, pièges fréquents des candidats), puis un encadré <div class="doc"><p class="doc-title">À l’école</p>…</div> ;
- partie Q (Quiz) : 6 questions "quiz" à 1 point (une ou plusieurs bonnes réponses, indices à partir de 0) ;
- partie A (Application) : 2 questions "application" à 2 points, corrigés détaillés (une peut être une analyse d’erreur d’élève).
Exigences : exactitude absolue (calculs vérifiés en Python avec asserts ; terminologie de la Grammaire du français,
Eduscol 2021 : COD, COI (pas « COS »), attribut du sujet, complément circonstanciel, complément du nom, épithète,
apposition ; le conditionnel est un temps de l’indicatif) ; programmes en vigueur en 2026-2027 (cycles 1-2 : BO n° 41
du 31/10/2024 ; cycle 3 français et maths : BO n° 16 du 17/04/2025 — au cours moyen : pas de tableau de
proportionnalité, pas de coefficient ni de produit en croix ; division posée par un diviseur à un chiffre ; décimaux
jusqu’aux centièmes au CM1, millièmes au CM2 ; la résolution de problèmes suit « comprendre, modéliser, calculer,
répondre » et utilise les schémas en barres) ; ne cite un texte officiel que si tu l’as vérifié (WebSearch/WebFetch),
sinon reformule sans guillemets. Figures SVG propres (classes .fig) quand utiles (Pythagore, Thalès, angles, aires,
solides, repère, diagrammes). Aucune donnée personnelle dans les requêtes web.
Valide le fichier en Python : json.load, ids uniques, sommes de points (R=0, Q=6, A=4, total=10), types, bonnes ⊂ options,
HTML équilibré, domaines autorisés.
