# Belamis — « Séances de révision » (rappels de cours conseillés, facultatifs)

Pour chaque concours, l'élève peut choisir un THÈME et faire une courte séance de révision (20 à 40 min) AVANT les sujets :
un rappel de cours clair (l'essentiel à savoir, méthodes, exemples, pièges), puis un quiz auto-corrigé et 1 à 3 exercices d'application corrigés.
Ce n'est pas obligatoire : c'est conseillé. Le ton : tutoiement bienveillant, phrases courtes, exemples concrets.

## Fichier JSON UTF-8 : {"sujets": [ ... ]}   (chaque « sujet » = une séance)
{
 "id": "rev-bac3-fr-classes",        // unique ; préfixe imposé par ta consigne
 "num": 1,
 "domaine": "francais",              // groupe de thèmes (voir ta consigne)
 "titre": "Classes grammaticales et fonctions",
 "theme": "une ligne : ce que la séance fait réviser",
 "revision": true,
 "duree": 1800,                      // secondes conseillées (1200 à 2400)
 "total": 10,                        // = somme des points
 "parties": [
   {"id": "R", "label": "Rappel", "short": "R", "titre": "L’essentiel à retenir", "points": 0,
    "intro": "HTML : le cours (h4, p, ul, tableaux <table class=\"tab\">, exemples, encadré <div class=\"doc\"><p class=\"doc-title\">À retenir</p>…</div>, figures SVG <figure class=\"fig\">…</figure>)",
    "questions": []},
   {"id": "Q", "label": "Quiz", "short": "Q", "titre": "Vérifie que tu as compris", "points": 6,
    "questions": [
      {"id": "1", "type": "quiz", "points": 1, "enonce": "HTML", "options": ["…", "…", "…"], "bonnes": [1], "corrige": "HTML : bonne réponse + explication courte"}
    ]},
   {"id": "A", "label": "Application", "short": "A", "titre": "Applique", "points": 4,
    "questions": [
      {"id": "1", "type": "application", "points": 2, "enonce": "HTML", "corrige": "HTML détaillé"}
    ]}
 ]
}
Règles : 5 à 8 questions "quiz" (1 point chacune, « une ou plusieurs bonnes réponses », indices à partir de 0) ; 1 à 3 questions "application" ; points de chaque partie = somme de ses questions ; total = somme des parties. La partie R a points 0 et questions [].
Classes HTML disponibles : doc, doc-title, doc-src, tab, fig (SVG : stroke, thin, thick, dash, grid, axis, shade, tile, fillink, c1 c2 c3, l1 l2, c-blue c-yellow c-red), frac (<span class="frac"><span>3</span><span>4</span></span>), copie-eleve. Pas d'emoji. Apostrophe ’.
Exactitude absolue : programmes en vigueur en 2026-2027 (nous sommes le 29/09/2026 : cycles 1-2 français/maths BO n° 41 du 31/10/2024 ; cycle 3 français/maths BO n° 16 du 17/04/2025 ; maternelle BO n° 19 du 7/05/2026 ; sciences BO n° 24 du 11/06/2026 (CP, CM1) ; EPS et histoire-géo BO n° 22 du 28/05/2026 (CP, CM1) — vérifie par WebSearch ce que tu cites), terminologie grammaticale officielle (Grammaire du français, Eduscol 2020-2021), faits et dates vérifiés. Calculs vérifiés en Python. Valide ton JSON en Python (json.load, sommes, ids uniques, bonnes ⊂ options, HTML équilibré).
N'envoie JAMAIS de donnée personnelle dans une requête web (User-Agent générique).
