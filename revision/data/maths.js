/* Généré par sujets_maths.py : sujets de mathématiques du CRPE BAC+3 (1re épreuve, partie B). */
window.BELAMIS_MATHS = {
 "types": {
  "nombres": "Nombres, fractions, décimaux",
  "arithmetique": "Arithmétique (multiples, diviseurs)",
  "proportionnalite": "Proportionnalité, pourcentages",
  "litteral": "Calcul littéral, équations",
  "fonctions": "Fonctions",
  "geometrie": "Géométrie (angles, Pythagore, Thalès)",
  "grandeurs": "Grandeurs et mesures",
  "stats": "Statistiques",
  "probas": "Probabilités",
  "algo": "Algorithmique, tableur",
  "suites": "Suites (lycée)"
 },
 "sujets": [
  {
   "id": "m-sujet0",
   "num": 0,
   "officiel": true,
   "titre": "Sujet 0 officiel",
   "source": "Sujet 0 du CRPE BAC+3 (juin 2025), partie B",
   "theme": "Nombres, formules d’un musée, aire, enquête, QCM et Scratch",
   "calculatrice": true,
   "parties": [
    {
     "id": "E1",
     "label": "Exercice 1",
     "short": "Ex. 1",
     "titre": "Ranger des nombres, probabilités",
     "points": 4,
     "intro": "<div class=\"table-wrap\"><table class=\"mtable nums\"><tbody><tr><td>1,5</td><td><span class=\"frac\"><span>8</span><span>4</span></span></td><td><span class=\"frac\"><span>3</span><span>4</span></span></td><td>0,7</td><td>1</td><td><span class=\"frac\"><span>4</span><span>3</span></span></td><td>1,33</td><td>1 + <span class=\"frac\"><span>3</span><span>100</span></span></td></tr></tbody></table></div>",
     "questions": [
      {
       "id": "1",
       "type": "nombres",
       "points": 2,
       "enonce": "Ranger les nombres ci-dessus dans l’ordre croissant.",
       "corrige": "<p>On écrit chaque nombre sous forme décimale (ou on compare les fractions) :</p>\n<ul><li><span class=\"frac\"><span>8</span><span>4</span></span> = 2 ; <span class=\"frac\"><span>3</span><span>4</span></span> = 0,75 ; 1 + <span class=\"frac\"><span>3</span><span>100</span></span> = 1,03 ;</li>\n<li><span class=\"frac\"><span>4</span><span>3</span></span> ≈ 1,333… : ce n’est <strong>pas</strong> un nombre décimal, et <span class=\"frac\"><span>4</span><span>3</span></span> &gt; 1,33 car <span class=\"frac\"><span>4</span><span>3</span></span> − 1,33 = <span class=\"frac\"><span>4</span><span>3</span></span> − <span class=\"frac\"><span>133</span><span>100</span></span> = <span class=\"frac\"><span>1</span><span>300</span></span> &gt; 0.</li></ul>\n<p class=\"answer\">0,7 &lt; <span class=\"frac\"><span>3</span><span>4</span></span> &lt; 1 &lt; 1 + <span class=\"frac\"><span>3</span><span>100</span></span> &lt; 1,33 &lt; <span class=\"frac\"><span>4</span><span>3</span></span> &lt; 1,5 &lt; <span class=\"frac\"><span>8</span><span>4</span></span></p>",
       "niveau": "c4"
      },
      {
       "id": "2a",
       "type": "probas",
       "points": 1,
       "enonce": "On choisit au hasard un de ces nombres, chacun avec la même probabilité. Quelle est la probabilité que le nombre choisi soit un nombre entier ?",
       "corrige": "<p>Il y a 8 nombres équiprobables. Les entiers sont 1 et <span class=\"frac\"><span>8</span><span>4</span></span> = 2, soit 2 issues favorables.</p><p class='answer'>P = <span class=\"frac\"><span>2</span><span>8</span></span> = <span class=\"frac\"><span>1</span><span>4</span></span></p>",
       "niveau": "c4"
      },
      {
       "id": "2b",
       "type": "probas",
       "points": 1,
       "enonce": "Quelle est la probabilité que le nombre choisi soit un nombre décimal ?",
       "corrige": "<p>Tous les nombres sont décimaux sauf <span class=\"frac\"><span>4</span><span>3</span></span> (son écriture décimale est illimitée : 1,333…). Les entiers sont aussi des décimaux. 7 issues favorables.</p><p class='answer'>P = <span class=\"frac\"><span>7</span><span>8</span></span></p><p><strong>Piège :</strong> un nombre entier est un nombre décimal ; une fraction peut être décimale (<span class=\"frac\"><span>3</span><span>4</span></span> = 0,75).</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E2",
     "label": "Exercice 2",
     "short": "Ex. 2",
     "titre": "Trois formules de visites au musée",
     "points": 5,
     "intro": "<p>Un musée propose trois formules de visites guidées pour des classes durant l’année scolaire.</p><ul class='box'><li><strong>Formule A :</strong> 45 € par visite de classe.</li><li><strong>Formule B :</strong> abonnement annuel de 90 € par école, auquel s’ajoutent 25,50 € par visite de classe.</li><li><strong>Formule C :</strong> abonnement annuel de 300 €, qui permet autant de visites que l’école le souhaite.</li></ul><figure class=\"fig\"><svg viewBox=\"0 0 600 290\" role=\"img\" aria-label=\"Représentation graphique des prix des trois formules en fonction du nombre de visites\" xmlns=\"http://www.w3.org/2000/svg\"><line x1=\"50.0\" y1=\"250\" x2=\"50.0\" y2=\"30\" class=\"grid\"/><text x=\"50.0\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">0</text><line x1=\"93.3\" y1=\"250\" x2=\"93.3\" y2=\"30\" class=\"grid\"/><text x=\"93.33333333333334\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">1</text><line x1=\"136.7\" y1=\"250\" x2=\"136.7\" y2=\"30\" class=\"grid\"/><text x=\"136.66666666666669\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">2</text><line x1=\"180.0\" y1=\"250\" x2=\"180.0\" y2=\"30\" class=\"grid\"/><text x=\"180.0\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">3</text><line x1=\"223.3\" y1=\"250\" x2=\"223.3\" y2=\"30\" class=\"grid\"/><text x=\"223.33333333333334\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">4</text><line x1=\"266.7\" y1=\"250\" x2=\"266.7\" y2=\"30\" class=\"grid\"/><text x=\"266.6666666666667\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">5</text><line x1=\"310.0\" y1=\"250\" x2=\"310.0\" y2=\"30\" class=\"grid\"/><text x=\"310.0\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">6</text><line x1=\"353.3\" y1=\"250\" x2=\"353.3\" y2=\"30\" class=\"grid\"/><text x=\"353.33333333333337\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">7</text><line x1=\"396.7\" y1=\"250\" x2=\"396.7\" y2=\"30\" class=\"grid\"/><text x=\"396.6666666666667\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">8</text><line x1=\"440.0\" y1=\"250\" x2=\"440.0\" y2=\"30\" class=\"grid\"/><text x=\"440.0\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">9</text><line x1=\"483.3\" y1=\"250\" x2=\"483.3\" y2=\"30\" class=\"grid\"/><text x=\"483.33333333333337\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">10</text><line x1=\"526.7\" y1=\"250\" x2=\"526.7\" y2=\"30\" class=\"grid\"/><text x=\"526.6666666666667\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">11</text><line x1=\"570.0\" y1=\"250\" x2=\"570.0\" y2=\"30\" class=\"grid\"/><text x=\"570.0\" y=\"266\" text-anchor=\"middle\" font-size=\"11\" class=\"\">12</text><line x1=\"50\" y1=\"250.0\" x2=\"570\" y2=\"250.0\" class=\"grid\"/><text x=\"44\" y=\"254.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">0</text><line x1=\"50\" y1=\"215.6\" x2=\"570\" y2=\"215.6\" class=\"grid\"/><text x=\"44\" y=\"219.625\" text-anchor=\"end\" font-size=\"11\" class=\"\">50</text><line x1=\"50\" y1=\"181.2\" x2=\"570\" y2=\"181.2\" class=\"grid\"/><text x=\"44\" y=\"185.25\" text-anchor=\"end\" font-size=\"11\" class=\"\">100</text><line x1=\"50\" y1=\"146.9\" x2=\"570\" y2=\"146.9\" class=\"grid\"/><text x=\"44\" y=\"150.875\" text-anchor=\"end\" font-size=\"11\" class=\"\">150</text><line x1=\"50\" y1=\"112.5\" x2=\"570\" y2=\"112.5\" class=\"grid\"/><text x=\"44\" y=\"116.5\" text-anchor=\"end\" font-size=\"11\" class=\"\">200</text><line x1=\"50\" y1=\"78.1\" x2=\"570\" y2=\"78.1\" class=\"grid\"/><text x=\"44\" y=\"82.125\" text-anchor=\"end\" font-size=\"11\" class=\"\">250</text><line x1=\"50\" y1=\"43.8\" x2=\"570\" y2=\"43.8\" class=\"grid\"/><text x=\"44\" y=\"47.75\" text-anchor=\"end\" font-size=\"11\" class=\"\">300</text><line x1=\"50\" y1=\"250\" x2=\"570\" y2=\"250\" class=\"axis\"/><line x1=\"50\" y1=\"250\" x2=\"50\" y2=\"30\" class=\"axis\"/><line x1=\"50.0\" y1=\"250.0\" x2=\"358.1\" y2=\"30.0\" class=\"c1\"/><line x1=\"50.0\" y1=\"188.1\" x2=\"440.8\" y2=\"30.0\" class=\"c2\"/><line x1=\"50.0\" y1=\"43.8\" x2=\"570.0\" y2=\"43.8\" class=\"c3\"/><text x=\"570\" y=\"282\" text-anchor=\"end\" font-size=\"11\" class=\"\">nombre de visites de classe</text><text x=\"10\" y=\"22\" text-anchor=\"start\" font-size=\"11\" class=\"\">prix (€)</text></svg></figure><p class='legend'><span class='k1'></span> formule A <span class='k2'></span> formule B <span class='k3'></span> formule C</p>",
     "questions": [
      {
       "id": "1a",
       "type": "fonctions",
       "points": 1,
       "enonce": "Une école a quatre classes. Si chaque classe effectue une visite, quelle formule est la plus avantageuse ?",
       "corrige": "<p>4 visites : A : 4 × 45 = 180 € ; B : 90 + 4 × 25,50 = 192 € ; C : 300 €.</p><p class='answer'>La formule A est la plus avantageuse (180 €).</p>",
       "niveau": "c4"
      },
      {
       "id": "1b",
       "type": "fonctions",
       "points": 1,
       "enonce": "Si chaque classe effectue deux visites, quelle formule est la plus avantageuse ?",
       "corrige": "<p>8 visites : A : 8 × 45 = 360 € ; B : 90 + 8 × 25,50 = 294 € ; C : 300 €.</p><p class='answer'>La formule B est la plus avantageuse (294 €).</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "litteral",
       "points": 1,
       "enonce": "À partir de combien de visites de classe la formule C est-elle plus économique que la formule B ?",
       "corrige": "<p>On cherche le nombre de visites <em>n</em> tel que 90 + 25,5<em>n</em> &gt; 300, soit 25,5<em>n</em> &gt; 210, donc <em>n</em> &gt; 210 ÷ 25,5 ≈ 8,24.</p><p class='answer'>La formule C est plus économique à partir de 9 visites.</p><p>Vérification : 8 visites → B coûte 294 € (&lt; 300) ; 9 visites → B coûte 319,50 € (&gt; 300).</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "fonctions",
       "points": 1,
       "enonce": "En vous aidant du graphique, déterminer graphiquement le nombre de visites à partir duquel la formule B est plus économique que la formule A.",
       "corrige": "<p>Les droites de A et de B se coupent pour une abscisse comprise entre 4 et 5 (environ 4,6). Au-delà, la droite de B est en dessous de celle de A.</p><p class='answer'>La formule B est plus économique à partir de 5 visites.</p><p>Vérification : 5 visites → A : 225 €, B : 217,50 €.</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "L’école de quatre classes organise deux visites par classe. Elle choisit la formule la plus avantageuse et la mairie lui accorde une subvention de 15 % du prix à payer. Quel montant l’école doit-elle prévoir ?",
       "corrige": "<p>8 visites : formule B, 294 €. Réduire de 15 %, c’est multiplier par 1 − 0,15 = 0,85 : 294 × 0,85 = 249,90.</p><p class='answer'>L’école doit prévoir 249,90 €.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E3",
     "label": "Exercice 3",
     "short": "Ex. 3",
     "titre": "Un carré et deux demi-cercles",
     "points": 4,
     "intro": "<p>La figure est constituée d’un carré de côté 8 cm dans lequel sont inscrits deux demi-cercles dont le diamètre est un côté du carré.</p><figure class=\"fig\"><svg viewBox=\"0 0 240 220\" role=\"img\" aria-label=\"Carré de 8 cm dans lequel sont inscrits deux demi-cercles ; la zone grisée est le reste du carré\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"20\" y=\"10\" width=\"200\" height=\"200\" class=\"shade\"/><path d=\"M20,10 A100.0,100.0 0 0 1 20,210 Z\" class=\"paper\"/><path d=\"M220,10 A100.0,100.0 0 0 0 220,210 Z\" class=\"paper\"/><rect x=\"20\" y=\"10\" width=\"200\" height=\"200\" class=\"stroke\"/><path d=\"M20,10 A100.0,100.0 0 0 1 20,210\" class=\"stroke\"/><path d=\"M220,10 A100.0,100.0 0 0 0 220,210\" class=\"stroke\"/></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "grandeurs",
       "points": 0.5,
       "enonce": "Déterminer l’aire du carré.",
       "corrige": "<p class='answer'>8 × 8 = 64 cm²</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Déterminer la valeur exacte de l’aire grisée, en cm².",
       "corrige": "<p>Les deux demi-disques ont un rayon de 4 cm ; ensemble, ils forment un disque d’aire π × 4² = 16π cm².</p><p class='answer'>Aire grisée = 64 − 16π cm² (≈ 13,73 cm²)</p><p>La « valeur exacte » demande de garder π.</p>",
       "niveau": "c4"
      },
      {
       "id": "3a",
       "type": "grandeurs",
       "points": 0.5,
       "enonce": "On reproduit la figure sur le sol de la cour à l’échelle 125 : 1. Quel sera le côté du nouveau carré, en mètres ?",
       "corrige": "<p>Échelle 125 : 1 : les longueurs sont multipliées par 125. 8 cm × 125 = 1 000 cm.</p><p class='answer'>10 m</p>",
       "niveau": "c4"
      },
      {
       "id": "3b",
       "type": "geometrie",
       "points": 1,
       "enonce": "Quelle sera la longueur de la diagonale de ce nouveau carré ? Donner le résultat en mètres, arrondi au centimètre.",
       "corrige": "<p>Dans le triangle rectangle formé par deux côtés et la diagonale, d’après le théorème de Pythagore : d² = 10² + 10² = 200, donc d = √200 = 10√2.</p><p class='answer'>d ≈ 14,14 m</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "grandeurs",
       "points": 1,
       "enonce": "On peint la zone grisée de la cour avec deux couches. La peinture couvre 7 m² par litre et se vend en pots de 750 mL. Combien de pots faut-il prévoir ?",
       "corrige": "<p>Aire grisée réelle : les aires sont multipliées par 125², ou directement avec le carré de 10 m : 100 − π × 5² = 100 − 25π ≈ 21,46 m².</p><p>Deux couches : ≈ 42,92 m². Volume : 42,92 ÷ 7 ≈ 6,13 L. Nombre de pots : 6,13 ÷ 0,75 ≈ 8,18.</p><p class='answer'>Il faut prévoir 9 pots.</p><p><strong>Piège :</strong> on arrondit à l’entier <em>supérieur</em>.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E4",
     "label": "Exercice 4",
     "short": "Ex. 4",
     "titre": "Une enquête sur les jeux de cour",
     "points": 3,
     "intro": "<p>« Utilisez-vous les jeux de cour ? » 160 élèves ont répondu, dont 55 % de filles. La moitié des filles a déclaré utiliser les jeux de cour, ainsi que les trois quarts des garçons.</p>",
     "questions": [
      {
       "id": "1",
       "type": "proportionnalite",
       "points": 1.5,
       "enonce": "Compléter le tableau : filles, garçons, total ; utilisent / n’utilisent pas les jeux de cour.",
       "corrige": "<p>Filles : 55 % de 160 = 88 ; garçons : 72. Filles qui utilisent : 88 ÷ 2 = 44 ; garçons qui utilisent : 72 × 3 ÷ 4 = 54.</p><div class=\"table-wrap\"><table class=\"mtable\"><thead><tr><th></th><th>Filles</th><th>Garçons</th><th>Total</th></tr></thead><tbody><tr><th>Utilisent</th><td>44</td><td>54</td><td>98</td></tr><tr><th>N’utilisent pas</th><td>44</td><td>18</td><td>62</td></tr><tr><th>Total</th><td>88</td><td>72</td><td>160</td></tr></tbody></table></div>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "proportionnalite",
       "points": 0.75,
       "enonce": "Calculer le pourcentage d’élèves qui utilisent les jeux de cour.",
       "corrige": "<p>98 ÷ 160 = 0,6125.</p><p class='answer'>61,25 % des élèves</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "proportionnalite",
       "points": 0.75,
       "enonce": "Parmi les élèves qui utilisent les jeux de cour, quel est le pourcentage de filles ? Arrondir à l’unité.",
       "corrige": "<p>44 ÷ 98 ≈ 0,449.</p><p class='answer'>environ 45 %</p><p><strong>Piège :</strong> la population de référence est celle des 98 utilisateurs, pas les 160 élèves.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E5",
     "label": "Exercice 5",
     "short": "Ex. 5",
     "titre": "QCM (aucune justification demandée)",
     "points": 4,
     "intro": "<p>Pour chaque question, une seule réponse est exacte. Une réponse fausse ou l’absence de réponse ne rapporte ni n’enlève de point.</p>",
     "questions": [
      {
       "id": "1",
       "type": "algo",
       "points": 1,
       "enonce": "À l’issue de ce script, quelles valeurs sont affectées à <em>a</em> et <em>b</em> ?<div class=\"scratch\" aria-label=\"Script Scratch\"><div class=\"sb sb-var\">mettre <span class=\"sb-v\">a</span> à <span class=\"sb-v\">4</span></div><div class=\"sb sb-var\">mettre <span class=\"sb-v\">b</span> à <span class=\"sb-v\">a</span> + <span class=\"sb-v\">2</span></div></div><p>A : a = 4 et b = 2 &nbsp;·&nbsp; B : a = 4 et b = 6 &nbsp;·&nbsp; C : a = 2 et b = 6 &nbsp;·&nbsp; D : a = 2 et b = 2</p>",
       "corrige": "<p class='answer'>Réponse B</p><p><em>a</em> reçoit 4, puis <em>b</em> reçoit la valeur de <em>a</em> + 2 = 6.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "algo",
       "points": 1,
       "enonce": "À l’issue de ce script, quelle valeur est affectée à <em>a</em> ?<div class=\"scratch\" aria-label=\"Script Scratch\"><div class=\"sb sb-var\">mettre <span class=\"sb-v\">a</span> à <span class=\"sb-v\">2</span></div><div class=\"sb sb-ctrl sb-c\"><div class=\"sb-h\">répéter <span class=\"sb-v\">4</span> fois</div><div class=\"sb-in\"><div class=\"sb sb-var\">mettre <span class=\"sb-v\">a</span> à <span class=\"sb-v\">a</span> + <span class=\"sb-v\">3</span></div></div><div class=\"sb-f\"></div></div></div><p>A : 20 &nbsp;·&nbsp; B : 12 &nbsp;·&nbsp; C : 14 &nbsp;·&nbsp; D : 2</p>",
       "corrige": "<p class='answer'>Réponse C</p><p>2 → 5 → 8 → 11 → 14 : on ajoute 3 quatre fois, 2 + 4 × 3 = 14.</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Un pavé droit subit une réduction de rapport 0,4. Son volume est : A : multiplié par 0,4³ &nbsp;·&nbsp; B : multiplié par 0,4² &nbsp;·&nbsp; C : divisé par 0,4³ &nbsp;·&nbsp; D : divisé par 0,4².",
       "corrige": "<p class='answer'>Réponse A</p><p>Dans un agrandissement ou une réduction de rapport k, les longueurs sont multipliées par k, les aires par k² et les volumes par k³.</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Un réservoir en forme de pavé droit mesure 1,5 m × 1,5 m × 2 m. Son volume en litres est : A : 450 L &nbsp;·&nbsp; B : 4 500 L &nbsp;·&nbsp; C : 4 500 000 L &nbsp;·&nbsp; D : 4,5 L.",
       "corrige": "<p class='answer'>Réponse B</p><p>V = 1,5 × 1,5 × 2 = 4,5 m³ et 1 m³ = 1 000 L, donc 4 500 L.</p>",
       "niveau": "c4"
      }
     ]
    }
   ],
   "total": 20
  },
  {
   "id": "m-2026-g2",
   "num": 1,
   "officiel": true,
   "titre": "Session 2026 · groupement 2",
   "source": "CRPE BAC+3, session 2026 (1er avril 2026), groupement 2, partie B",
   "theme": "Dés, programmes de calcul et fonctions, ombres chinoises, JO de Paris, vrai-faux",
   "calculatrice": true,
   "noteSur": 10,
   "remarque": "Au concours 2026, la partie maths était notée directement sur 10 : le barème ci-dessous est celui du sujet. La répartition des points entre les questions d’un même exercice est indicative.",
   "parties": [
    {
     "id": "E1",
     "label": "Exercice 1",
     "short": "Ex. 1",
     "titre": "Deux dés à quatre faces",
     "points": 1.25,
     "intro": "<p>Dans cet exercice, les probabilités sont données sous forme de fraction irréductible. Enzo lance deux dés identiques à quatre faces, numérotées de 1 à 4, puis additionne les deux nombres obtenus (par exemple 4 et 4 donnent 8).</p>",
     "questions": [
      {
       "id": "1",
       "type": "probas",
       "points": 0.5,
       "enonce": "Montrer qu’il y a 7 sommes possibles et les préciser.",
       "corrige": "<p>Le tableau à double entrée donne les 4 × 4 = 16 issues équiprobables :</p><div class=\"table-wrap\"><table class=\"mtable\"><thead><tr><th>+</th><th>1</th><th>2</th><th>3</th><th>4</th></tr></thead><tbody><tr><th>1</th><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><th>2</th><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><th>3</th><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><th>4</th><td>5</td><td>6</td><td>7</td><td>8</td></tr></tbody></table></div><p class='answer'>Sommes possibles : 2, 3, 4, 5, 6, 7, 8 (7 sommes).</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "probas",
       "points": 0.35,
       "enonce": "La probabilité d’obtenir une somme égale à 2 est-elle égale à <span class=\"frac\"><span>1</span><span>7</span></span> ?",
       "corrige": "<p>Non : les 7 sommes ne sont pas équiprobables. La somme 2 n’est obtenue que par (1 ; 1), soit 1 issue sur 16.</p><p class='answer'>P(somme = 2) = <span class=\"frac\"><span>1</span><span>16</span></span> ≠ <span class=\"frac\"><span>1</span><span>7</span></span></p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "probas",
       "points": 0.4,
       "enonce": "L’événement « obtenir 5 » est-il plus probable que « obtenir 6 » ?",
       "corrige": "<p>Somme 5 : (1;4), (2;3), (3;2), (4;1) → <span class=\"frac\"><span>4</span><span>16</span></span> = <span class=\"frac\"><span>1</span><span>4</span></span>. Somme 6 : (2;4), (3;3), (4;2) → <span class=\"frac\"><span>3</span><span>16</span></span>.</p><p class='answer'>Oui, obtenir 5 est plus probable.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E2",
     "label": "Exercice 2",
     "short": "Ex. 2",
     "titre": "Deux programmes de calcul",
     "points": 2.5,
     "intro": "<div class='two'><ul class='box'><li><strong>Programme A</strong></li><li>Choisir un nombre</li><li>Ajouter 4</li><li>Multiplier le résultat par 3</li><li>Retrancher 11</li></ul><ul class='box'><li><strong>Programme B</strong></li><li>Choisir un nombre</li><li>Multiplier par −4</li><li>Ajouter 5</li></ul></div>",
     "questions": [
      {
       "id": "1",
       "type": "litteral",
       "points": 0.3,
       "enonce": "Nombre obtenu avec le programme A en choisissant −5 ?",
       "corrige": "<p>−5 + 4 = −1 ; −1 × 3 = −3 ; −3 − 11 = −14.</p><p class='answer'>−14</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "litteral",
       "points": 0.4,
       "enonce": "Quel nombre choisir au départ pour obtenir −25 avec le programme B ?",
       "corrige": "<p>−4<em>x</em> + 5 = −25 ⇔ −4<em>x</em> = −30 ⇔ <em>x</em> = 7,5. (Ou on remonte le programme : −25 − 5 = −30 ; −30 ÷ (−4) = 7,5.)</p><p class='answer'>7,5</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "litteral",
       "points": 0.4,
       "enonce": "On note <em>x</em> le nombre de départ. Montrer que le résultat du programme A est 3<em>x</em> + 1.",
       "corrige": "<p>(<em>x</em> + 4) × 3 − 11 = 3<em>x</em> + 12 − 11 = 3<em>x</em> + 1.</p>",
       "niveau": "c4"
      },
      {
       "id": "4a",
       "type": "fonctions",
       "points": 0.5,
       "enonce": "On pose <em>f</em>(<em>x</em>) = 3<em>x</em> + 1 et <em>g</em>(<em>x</em>) = −4<em>x</em> + 5. Construire leurs représentations graphiques (unité 1 cm).",
       "corrige": "<p>Ce sont des fonctions affines : leurs courbes sont des droites. Deux points suffisent pour chacune.</p><ul><li><em>f</em> : (0 ; 1) et (1 ; 4) ;</li><li><em>g</em> : (0 ; 5) et (2 ; −3).</li></ul>",
       "niveau": "c4"
      },
      {
       "id": "4b",
       "type": "fonctions",
       "points": 0.4,
       "enonce": "Déterminer graphiquement l’antécédent de −3 par <em>g</em>.",
       "corrige": "<p>On repère −3 sur l’axe des ordonnées, on rejoint la droite de <em>g</em>, puis on lit l’abscisse. Vérification : −4<em>x</em> + 5 = −3 ⇔ <em>x</em> = 2.</p><p class='answer'>L’antécédent de −3 par <em>g</em> est 2.</p>",
       "niveau": "c4"
      },
      {
       "id": "4c",
       "type": "litteral",
       "points": 0.5,
       "enonce": "Déterminer algébriquement l’abscisse du point d’intersection des deux droites. Que représente-t-elle pour les programmes A et B ?",
       "corrige": "<p>3<em>x</em> + 1 = −4<em>x</em> + 5 ⇔ 7<em>x</em> = 4 ⇔ <em>x</em> = <span class=\"frac\"><span>4</span><span>7</span></span>.</p><p class='answer'><em>x</em> = <span class=\"frac\"><span>4</span><span>7</span></span> : c’est le nombre de départ pour lequel les deux programmes donnent le même résultat (<span class=\"frac\"><span>19</span><span>7</span></span>).</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E3",
     "label": "Exercice 3",
     "short": "Ex. 3",
     "titre": "Un spectacle d’ombres chinoises",
     "points": 1.5,
     "intro": "<p>Un objet [DE] de 20 cm doit avoir une ombre [BC] de 1,2 m sur l’écran. La source lumineuse A est à 9 m de l’écran (figure non à l’échelle).</p><figure class=\"fig\"><svg viewBox=\"0 0 520 245\" role=\"img\" aria-label=\"Source lumineuse en A, objet [DE] de 0,2 m, écran [BC] de 1,2 m à 9 m de A ; figure non à l’échelle\" xmlns=\"http://www.w3.org/2000/svg\"><polygon points=\"40,200 460,200 460,40\" class=\"stroke\"/><line x1=\"180\" y1=\"200\" x2=\"180\" y2=\"160\" class=\"thick\"/><line x1=\"460\" y1=\"200\" x2=\"460\" y2=\"40\" class=\"thick\"/><rect x=\"180\" y=\"190\" width=\"10\" height=\"10\" class=\"stroke\"/><rect x=\"450\" y=\"190\" width=\"10\" height=\"10\" class=\"stroke\"/><text x=\"40\" y=\"218\" text-anchor=\"middle\" font-size=\"13\" class=\"\">A</text><text x=\"180\" y=\"218\" text-anchor=\"middle\" font-size=\"13\" class=\"\">D</text><text x=\"460\" y=\"218\" text-anchor=\"middle\" font-size=\"13\" class=\"\">B</text><text x=\"170\" y=\"156\" text-anchor=\"middle\" font-size=\"13\" class=\"\">E</text><text x=\"472\" y=\"40\" text-anchor=\"middle\" font-size=\"13\" class=\"\">C</text><text x=\"210\" y=\"186\" text-anchor=\"middle\" font-size=\"12\" class=\"\">0,2 m</text><text x=\"496\" y=\"124\" text-anchor=\"middle\" font-size=\"12\" class=\"\">1,2 m</text><text x=\"250.0\" y=\"234\" text-anchor=\"middle\" font-size=\"12\" class=\"\">9 m</text><line x1=\"40\" y1=\"222\" x2=\"460\" y2=\"222\" class=\"stroke\" marker-end=\"url(#ar)\" marker-start=\"url(#ar)\"/><defs><marker id=\"ar\" viewBox=\"0 0 10 10\" refX=\"5\" refY=\"5\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto-start-reverse\"><path d=\"M0,0 L10,5 L0,10 z\" class=\"fillink\"/></marker></defs></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "geometrie",
       "points": 0.4,
       "enonce": "Justifier que les droites (BC) et (DE) sont parallèles.",
       "corrige": "<p>(DE) et (BC) sont toutes deux perpendiculaires à la droite (AB). Or deux droites perpendiculaires à une même droite sont parallèles.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "geometrie",
       "points": 0.6,
       "enonce": "En déduire la distance AD à laquelle placer l’objet.",
       "corrige": "<p>D ∈ [AB], E ∈ [AC] et (DE) // (BC) : d’après le théorème de Thalès, AD/AB = DE/BC, donc AD = 9 × 0,2 ÷ 1,2 = 1,5.</p><p class='answer'>AD = 1,5 m</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "grandeurs",
       "points": 0.5,
       "enonce": "L’objet est une plaque rectangulaire de 20 cm sur 10 cm, parallèle à l’écran. Par quel nombre multiplier son aire pour obtenir celle de l’ombre ?",
       "corrige": "<p>L’ombre est un agrandissement de rapport k = 1,2 ÷ 0,2 = 6. Les aires sont multipliées par k².</p><p class='answer'>6² = 36</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E4",
     "label": "Exercice 4",
     "short": "Ex. 4",
     "titre": "Les Jeux olympiques de Paris 2024",
     "points": 1.75,
     "intro": "<p><strong>Partie A.</strong> 63 pays ont reçu au moins une médaille d’or.</p><div class=\"table-wrap\"><table class=\"mtable\"><thead><tr><th>Médailles d’or</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>8</th><th>9</th><th>10</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>18</th><th>20</th><th>40</th></tr></thead><tbody><tr><th>Nombre de pays</th><td>23</td><td>12</td><td>9</td><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td></tr></tbody></table></div><p><strong>Partie B.</strong> Une médaille d’or pèse 529 g ; elle est en argent recouvert d’or pur, qui représente 1,13 % de sa masse.</p><p><strong>Partie C.</strong> L’insert de la médaille est un hexagone régulier, que l’on veut tracer avec Scratch (côté 50 pas). Nina a écrit ce script, qui ne trace pas l’hexagone :</p><div class=\"scratch\" aria-label=\"Script Scratch\"><div class=\"sb sb-event\">quand le drapeau est cliqué</div><div class=\"sb sb-pen\">stylo en position d’écriture</div><div class=\"sb sb-move\">s’orienter à <span class=\"sb-v\">60</span></div><div class=\"sb sb-ctrl sb-c\"><div class=\"sb-h\">répéter <span class=\"sb-v\">6</span> fois</div><div class=\"sb-in\"><div class=\"sb sb-move\">avancer de <span class=\"sb-v\">50</span> pas</div><div class=\"sb sb-move\">tourner ↺ de <span class=\"sb-v\">120</span> degrés</div></div><div class=\"sb-f\"></div></div><div class=\"sb sb-pen\">relever le stylo</div></div><figure class=\"fig\"><svg viewBox=\"0 0 240 220\" role=\"img\" aria-label=\"Hexagone régulier de côté 50 pas\" xmlns=\"http://www.w3.org/2000/svg\"><polygon points=\"120.0,30.0 50.7,70.0 50.7,150.0 120.0,190.0 189.3,150.0 189.3,70.0\" class=\"stroke\"/><text x=\"120\" y=\"114\" text-anchor=\"middle\" font-size=\"12\" class=\"\">côté : 50 pas</text></svg></figure>",
     "questions": [
      {
       "id": "A1",
       "type": "stats",
       "points": 0.5,
       "enonce": "Calculer le nombre moyen de médailles d’or par pays, arrondi au dixième.",
       "corrige": "<p>Somme des médailles : 1 × 23 + 2 × 12 + 3 × 9 + … + 40 × 2 = 328. Moyenne : 328 ÷ 63 ≈ 5,206.</p><p class='answer'>≈ 5,2 médailles d’or par pays</p>",
       "niveau": "c4"
      },
      {
       "id": "A2",
       "type": "stats",
       "points": 0.5,
       "enonce": "Le Canada a obtenu 9 médailles d’or. Ce nombre est-il supérieur à la médiane ?",
       "corrige": "<p>63 valeurs : la médiane est la 32e valeur de la série rangée. Les 23 premières valent 1, les 12 suivantes (24e à 35e) valent 2 : la médiane vaut 2.</p><p class='answer'>Oui : 9 &gt; 2.</p><p>La moyenne (5,2) est bien plus grande que la médiane : quelques pays ont beaucoup de médailles.</p>",
       "niveau": "c4"
      },
      {
       "id": "B",
       "type": "proportionnalite",
       "points": 0.35,
       "enonce": "Calculer la masse d’or pur d’une médaille, à l’unité près.",
       "corrige": "<p>529 × 1,13 ÷ 100 = 5,9777.</p><p class='answer'>≈ 6 g</p>",
       "niveau": "c4"
      },
      {
       "id": "C",
       "type": "algo",
       "points": 0.4,
       "enonce": "Indiquer la correction à faire dans la boucle (aucune justification attendue).",
       "corrige": "<p class='answer'>Remplacer « tourner de 120 degrés » par « tourner de 60 degrés ».</p><p>Explication : pour tracer un polygone régulier à <em>n</em> côtés, le lutin tourne de l’angle extérieur 360° ÷ <em>n</em>, soit 60° pour l’hexagone (et non de l’angle intérieur, 120°).</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E5",
     "label": "Exercice 5",
     "short": "Ex. 5",
     "titre": "Vrai ou faux ? (réponses justifiées)",
     "points": 3,
     "intro": "",
     "questions": [
      {
       "id": "1",
       "type": "nombres",
       "points": 0.5,
       "enonce": "Affirmation 1 : <span class=\"frac\"><span>22</span><span>25</span></span> est un nombre décimal.",
       "corrige": "<p><span class=\"frac\"><span>22</span><span>25</span></span> = <span class=\"frac\"><span>88</span><span>100</span></span> = 0,88.</p><p class='answer'>Vraie.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "proportionnalite",
       "points": 0.5,
       "enonce": "Affirmation 2 : un prix augmente de 50 % puis baisse de 40 % ; il a donc augmenté de 10 %.",
       "corrige": "<p>Coefficients multiplicateurs : 1,5 × 0,6 = 0,9 : le prix a <strong>baissé</strong> de 10 %.</p><p class='answer'>Fausse.</p><p>Les pourcentages successifs ne s’additionnent pas.</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "nombres",
       "points": 0.5,
       "enonce": "Affirmation 3 : le nombre de dizaines de 6 727 est 112 fois plus grand que son nombre de milliers.",
       "corrige": "<p>Nombre de dizaines : 672 ; nombre de milliers : 6 ; 6 × 112 = 672.</p><p class='answer'>Vraie.</p><p>Attention : « nombre de dizaines » (672) ≠ « chiffre des dizaines » (2).</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "nombres",
       "points": 0.5,
       "enonce": "Affirmation 4 : ajouter 13 dixièmes à 25,606 donne 25,736.",
       "corrige": "<p>13 dixièmes = 1,3 ; 25,606 + 1,3 = 26,906.</p><p class='answer'>Fausse.</p><p>25,736 correspond à l’ajout de 13 <em>centièmes</em>.</p>",
       "niveau": "c4"
      },
      {
       "id": "5",
       "type": "nombres",
       "points": 0.5,
       "enonce": "Affirmation 5 : il existe au moins un entier dont le chiffre des unités est au moins 4, le chiffre des dizaines au moins 3, et dont le produit de ces deux chiffres est égal au nombre de centaines.",
       "corrige": "<p>Exemple : 1 234. Chiffre des unités 4, chiffre des dizaines 3, produit 12 ; nombre de centaines de 1 234 : 12.</p><p class='answer'>Vraie (un seul exemple suffit).</p>",
       "niveau": "c4"
      },
      {
       "id": "6",
       "type": "geometrie",
       "points": 0.5,
       "enonce": "Affirmation 6 : le triangle ABC tel que AB = 24 cm, BC = 18 cm et AC = 30 cm n’est pas rectangle.<figure class=\"fig\"><svg viewBox=\"0 0 300 210\" role=\"img\" aria-label=\"Triangle ABC : AB = 24 cm, BC = 18 cm, AC = 30 cm\" xmlns=\"http://www.w3.org/2000/svg\"><polygon points=\"230,30 60,80 110,190\" class=\"stroke\"/><text x=\"240\" y=\"30\" text-anchor=\"middle\" font-size=\"13\" class=\"\">A</text><text x=\"48\" y=\"80\" text-anchor=\"middle\" font-size=\"13\" class=\"\">B</text><text x=\"106\" y=\"206\" text-anchor=\"middle\" font-size=\"13\" class=\"\">C</text><text x=\"145.0\" y=\"47.0\" text-anchor=\"middle\" font-size=\"12\" class=\"\">24 cm</text><text x=\"55.0\" y=\"139.0\" text-anchor=\"middle\" font-size=\"12\" class=\"\">18 cm</text><text x=\"200.0\" y=\"116.0\" text-anchor=\"middle\" font-size=\"12\" class=\"\">30 cm</text></svg></figure>",
       "corrige": "<p>Le plus grand côté est [AC]. AC² = 900 ; AB² + BC² = 576 + 324 = 900. D’après la réciproque du théorème de Pythagore, ABC est rectangle en B.</p><p class='answer'>Fausse.</p>",
       "niveau": "c4"
      }
     ]
    }
   ],
   "total": 10
  },
  {
   "id": "m-2026-g1",
   "num": 2,
   "officiel": true,
   "titre": "Session 2026 · groupement 1",
   "source": "CRPE BAC+3, session 2026 (1er avril 2026), groupement 1, partie B (d’après un relevé du sujet)",
   "theme": "Tableau à double entrée, motif évolutif et tableur, pentagone, vrai-faux, axe gradué",
   "calculatrice": true,
   "noteSur": 10,
   "remarque": "Sujet reconstitué à partir d’une photographie : le barème est celui du sujet, la répartition entre questions est indicative.",
   "parties": [
    {
     "id": "E1",
     "label": "Exercice 1",
     "short": "Ex. 1",
     "titre": "Activités extrascolaires",
     "points": 2,
     "intro": "<p>Dans une école de 300 élèves : 40 % pratiquent un sport ; 75 pratiquent un instrument de musique ; parmi ces derniers, 60 % pratiquent aussi un sport.</p>",
     "questions": [
      {
       "id": "1",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Compléter un tableau à double entrée (sport / pas de sport ; instrument / pas d’instrument).",
       "corrige": "<p>Sport : 40 % de 300 = 120. Musique et sport : 60 % de 75 = 45.</p><div class=\"table-wrap\"><table class=\"mtable\"><thead><tr><th></th><th>Instrument</th><th>Pas d’instrument</th><th>Total</th></tr></thead><tbody><tr><th>Sport</th><td>45</td><td>75</td><td>120</td></tr><tr><th>Pas de sport</th><td>30</td><td>150</td><td>180</td></tr><tr><th>Total</th><td>75</td><td>225</td><td>300</td></tr></tbody></table></div>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "probas",
       "points": 0.5,
       "enonce": "On choisit un élève au hasard. Probabilité qu’il pratique au moins l’une des deux activités ?",
       "corrige": "<p>Seuls 150 élèves ne pratiquent ni sport ni instrument : 300 − 150 = 150 en pratiquent au moins une.</p><p class='answer'><span class=\"frac\"><span>150</span><span>300</span></span> = <span class=\"frac\"><span>1</span><span>2</span></span></p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "probas",
       "points": 0.5,
       "enonce": "On choisit au hasard un élève qui pratique un sport. Probabilité qu’il joue aussi d’un instrument (fraction irréductible) ?",
       "corrige": "<p>On se restreint aux 120 sportifs, dont 45 jouent d’un instrument.</p><p class='answer'><span class=\"frac\"><span>45</span><span>120</span></span> = <span class=\"frac\"><span>3</span><span>8</span></span></p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E2",
     "label": "Exercice 2",
     "short": "Ex. 2",
     "titre": "Un motif évolutif",
     "points": 2,
     "intro": "<figure class=\"fig\"><svg viewBox=\"0 0 620 130\" role=\"img\" aria-label=\"Motif évolutif : étape 1 : 1 carreau ; étape 2 : 4 ; étape 3 : 7 ; étape 4 : 10 carreaux\" xmlns=\"http://www.w3.org/2000/svg\"><text x=\"75\" y=\"22\" text-anchor=\"middle\" font-size=\"13\" class=\"\">Étape 1</text><rect x=\"20\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><text x=\"225\" y=\"22\" text-anchor=\"middle\" font-size=\"13\" class=\"\">Étape 2</text><rect x=\"170\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"188\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"188\" y=\"58\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"188\" y=\"76\" width=\"18\" height=\"18\" class=\"tile\"/><text x=\"375\" y=\"22\" text-anchor=\"middle\" font-size=\"13\" class=\"\">Étape 3</text><rect x=\"320\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"338\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"338\" y=\"58\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"338\" y=\"76\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"356\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"356\" y=\"58\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"356\" y=\"76\" width=\"18\" height=\"18\" class=\"tile\"/><text x=\"525\" y=\"22\" text-anchor=\"middle\" font-size=\"13\" class=\"\">Étape 4</text><rect x=\"470\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"488\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"488\" y=\"58\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"488\" y=\"76\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"506\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"506\" y=\"58\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"506\" y=\"76\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"524\" y=\"40\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"524\" y=\"58\" width=\"18\" height=\"18\" class=\"tile\"/><rect x=\"524\" y=\"76\" width=\"18\" height=\"18\" class=\"tile\"/></svg></figure><div class=\"table-wrap\"><table class=\"mtable\"><thead><tr><th></th><th>A</th><th>B</th></tr></thead><tbody><tr><th>1</th><td>Étape</td><td>Nombre de carreaux</td></tr><tr><th>2</th><td>1</td><td>1</td></tr><tr><th>3</th><td>2</td><td>4</td></tr><tr><th>4</th><td>3</td><td>7</td></tr><tr><th>5</th><td>4</td><td>10</td></tr></tbody></table></div>",
     "questions": [
      {
       "id": "1",
       "type": "algo",
       "points": 0.3,
       "enonce": "Décrire comment on passe d’une étape à la suivante.",
       "corrige": "<p>Le motif est formé de trois lignes : une ligne de <em>k</em> carreaux en haut et deux lignes de <em>k</em> − 1 carreaux en dessous, alignées à droite. Pour passer à l’étape suivante, on ajoute un carreau au bout gauche de chacune des trois lignes.</p><p class='answer'>+3 carreaux à chaque étape.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "nombres",
       "points": 0.4,
       "enonce": "Nombre de carreaux aux étapes 5 et 20 ?",
       "corrige": "<p>Étape 5 : 10 + 3 = 13. Étape 20 : 1 + 19 × 3 = 58.</p><p class='answer'>13 et 58</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "algo",
       "points": 0.3,
       "enonce": "Quelle formule, à étirer vers le bas, saisir en B3 ?",
       "corrige": "<p class='answer'>=B2+3</p><p>(Ou =3*A3-2, qui utilise le numéro d’étape.)</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "litteral",
       "points": 0.5,
       "enonce": "Exprimer, en fonction de <em>n</em>, le nombre de carreaux à l’étape <em>n</em>.",
       "corrige": "<p>On part de 1 et on ajoute 3 à chaque étape, (<em>n</em> − 1) fois : 1 + 3(<em>n</em> − 1).</p><p class='answer'>3<em>n</em> − 2</p>",
       "niveau": "c4"
      },
      {
       "id": "5",
       "type": "litteral",
       "points": 0.5,
       "enonce": "Le motif compte-t-il exactement 100 carreaux à une étape ? Et 2 000 ?",
       "corrige": "<p>3<em>n</em> − 2 = 100 ⇔ <em>n</em> = 34 : oui, à l’étape 34.</p><p>3<em>n</em> − 2 = 2 000 ⇔ <em>n</em> = <span class=\"frac\"><span>2002</span><span>3</span></span>, qui n’est pas entier (2 002 n’est pas divisible par 3 : 2 + 0 + 0 + 2 = 4).</p><p class='answer'>100 : oui (étape 34) ; 2 000 : non.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E3",
     "label": "Exercice 3",
     "short": "Ex. 3",
     "titre": "Des pentagones",
     "points": 2.5,
     "intro": "<p>Un pentagone régulier ABCDE est inscrit dans un cercle de centre O. <em>Rappel : un polygone régulier a tous ses côtés de même longueur et tous ses angles de même mesure.</em></p><figure class=\"fig\"><svg viewBox=\"0 0 300 240\" role=\"img\" aria-label=\"Pentagone régulier ABCDE inscrit dans un cercle de centre O\" xmlns=\"http://www.w3.org/2000/svg\"><circle cx=\"150\" cy=\"120\" r=\"90\" class=\"stroke thin\"/><polygon points=\"150.0,30.0 235.6,92.2 202.9,192.8 97.1,192.8 64.4,92.2\" class=\"stroke\"/><line x1=\"150\" y1=\"120\" x2=\"150.0\" y2=\"30.0\" class=\"stroke thin\"/><text x=\"150.0\" y=\"20.0\" text-anchor=\"middle\" font-size=\"13\" class=\"\">A</text><line x1=\"150\" y1=\"120\" x2=\"235.6\" y2=\"92.2\" class=\"stroke thin\"/><text x=\"248.90987769469598\" y=\"91.86223258500547\" text-anchor=\"middle\" font-size=\"13\" class=\"\">B</text><line x1=\"150\" y1=\"120\" x2=\"202.9\" y2=\"192.8\" class=\"stroke thin\"/><text x=\"211.1296662384172\" y=\"208.13776741499453\" text-anchor=\"middle\" font-size=\"13\" class=\"\">C</text><line x1=\"150\" y1=\"120\" x2=\"97.1\" y2=\"192.8\" class=\"stroke thin\"/><text x=\"88.8703337615828\" y=\"208.13776741499453\" text-anchor=\"middle\" font-size=\"13\" class=\"\">D</text><line x1=\"150\" y1=\"120\" x2=\"64.4\" y2=\"92.2\" class=\"stroke thin\"/><text x=\"51.09012230530402\" y=\"91.86223258500549\" text-anchor=\"middle\" font-size=\"13\" class=\"\">E</text><text x=\"160\" y=\"136\" text-anchor=\"middle\" font-size=\"12\" class=\"\">O</text></svg></figure>",
     "questions": [
      {
       "id": "a",
       "type": "geometrie",
       "points": 0.6,
       "enonce": "Justifier que l’angle DOC mesure 72°.",
       "corrige": "<p>Les 5 angles au centre AOB, BOC, COD, DOE, EOA interceptent des côtés de même longueur : ils sont égaux et leur somme fait un tour complet.</p><p class='answer'>360° ÷ 5 = 72°</p>",
       "niveau": "c4"
      },
      {
       "id": "b",
       "type": "geometrie",
       "points": 0.6,
       "enonce": "Quelle est la nature du triangle OCD ?",
       "corrige": "<p>OC = OD (rayons du cercle).</p><p class='answer'>OCD est isocèle en O.</p>",
       "niveau": "c4"
      },
      {
       "id": "c",
       "type": "geometrie",
       "points": 0.7,
       "enonce": "Déterminer la mesure de l’angle DCB.",
       "corrige": "<p>Dans OCD isocèle en O, les angles à la base mesurent (180° − 72°) ÷ 2 = 54°. De même dans OCB : angle OCB = 54°.</p><p class='answer'>DCB = 54° + 54° = 108°</p>",
       "niveau": "c4"
      },
      {
       "id": "d",
       "type": "geometrie",
       "points": 0.6,
       "enonce": "Déterminer la somme des angles de ce pentagone.",
       "corrige": "<p>5 angles de 108°.</p><p class='answer'>5 × 108° = 540°</p><p>Formule générale : (n − 2) × 180° pour un polygone à n côtés.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E4",
     "label": "Exercice 4",
     "short": "Ex. 4",
     "titre": "Vrai ou faux ? (réponses justifiées)",
     "points": 1.75,
     "intro": "",
     "questions": [
      {
       "id": "1",
       "type": "nombres",
       "points": 0.5,
       "enonce": "X s’écrit avec quatre chiffres, tous différents de 0. Son nombre de dizaines est 12 et son chiffre des unités est le triple de son chiffre des dixièmes. Affirmation : il y a exactement deux valeurs possibles pour X.",
       "corrige": "<p>Nombre de dizaines 12 : X s’écrit 12<em>u</em>,<em>d</em> avec <em>u</em> = 3<em>d</em> et des chiffres non nuls : (<em>u</em> ; <em>d</em>) = (3 ; 1), (6 ; 2) ou (9 ; 3).</p><p>X ∈ {123,1 ; 126,2 ; 129,3} : trois valeurs.</p><p class='answer'>Fausse.</p><p>(Si l’on comprend « chiffres tous différents », seule 129,3 convient : l’affirmation reste fausse.)</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "arithmetique",
       "points": 0.4,
       "enonce": "Affirmation : un entier multiple à la fois de 4 et de 10 est nécessairement multiple de 40.",
       "corrige": "<p>Contre-exemple : 20 est multiple de 4 et de 10, mais pas de 40. (Les multiples communs de 4 et 10 sont les multiples de 20.)</p><p class='answer'>Fausse.</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "proportionnalite",
       "points": 0.45,
       "enonce": "Offre 1 : pour un produit acheté, le deuxième à −50 %. Offre 2 : pour un produit acheté, 50 % de produit en plus offert. Affirmation : ces promotions sont équivalentes.",
       "corrige": "<p>Prix unitaire P. Offre 1 : 2 produits pour 1,5P, soit 0,75P par produit (−25 %). Offre 2 : 1,5 produit pour P, soit P ÷ 1,5 ≈ 0,667P par produit (−33 %).</p><p class='answer'>Fausse : l’offre 2 est plus avantageuse.</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "nombres",
       "points": 0.4,
       "enonce": "Affirmation : le quotient d’un nombre décimal par 4 est un nombre décimal.",
       "corrige": "<p>Diviser par 4, c’est multiplier par 0,25. Le produit de deux décimaux est un décimal (d × 0,25 = d × 25 ÷ 100).</p><p class='answer'>Vraie.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E5",
     "label": "Exercice 5",
     "short": "Ex. 5",
     "titre": "Un axe gradué",
     "points": 1.75,
     "intro": "<p>Sur l’axe gradué d’origine O, le point U a pour abscisse 1.</p><figure class=\"fig\"><svg viewBox=\"0 0 570 100\" role=\"img\" aria-label=\"Axe gradué : O d’abscisse 0, U d’abscisse 1, chaque unité est partagée en 8 ; A est à 4 graduations de O, B à 11 graduations\" xmlns=\"http://www.w3.org/2000/svg\"><line x1=\"10\" y1=\"60\" x2=\"560\" y2=\"60\" class=\"stroke\"/><line x1=\"20.0\" y1=\"54\" x2=\"20.0\" y2=\"66\" class=\"stroke\"/><line x1=\"60.0\" y1=\"54\" x2=\"60.0\" y2=\"66\" class=\"stroke\"/><line x1=\"100.0\" y1=\"54\" x2=\"100.0\" y2=\"66\" class=\"stroke\"/><line x1=\"140.0\" y1=\"54\" x2=\"140.0\" y2=\"66\" class=\"stroke\"/><line x1=\"180.0\" y1=\"54\" x2=\"180.0\" y2=\"66\" class=\"stroke\"/><line x1=\"220.0\" y1=\"54\" x2=\"220.0\" y2=\"66\" class=\"stroke\"/><line x1=\"260.0\" y1=\"54\" x2=\"260.0\" y2=\"66\" class=\"stroke\"/><line x1=\"300.0\" y1=\"54\" x2=\"300.0\" y2=\"66\" class=\"stroke\"/><line x1=\"340.0\" y1=\"54\" x2=\"340.0\" y2=\"66\" class=\"stroke\"/><line x1=\"380.0\" y1=\"54\" x2=\"380.0\" y2=\"66\" class=\"stroke\"/><line x1=\"420.0\" y1=\"54\" x2=\"420.0\" y2=\"66\" class=\"stroke\"/><line x1=\"460.0\" y1=\"54\" x2=\"460.0\" y2=\"66\" class=\"stroke\"/><line x1=\"500.0\" y1=\"54\" x2=\"500.0\" y2=\"66\" class=\"stroke\"/><line x1=\"540.0\" y1=\"54\" x2=\"540.0\" y2=\"66\" class=\"stroke\"/><line x1=\"580.0\" y1=\"54\" x2=\"580.0\" y2=\"66\" class=\"stroke\"/><text x=\"60.0\" y=\"44\" text-anchor=\"middle\" font-size=\"13\" class=\"\">O</text><text x=\"60.0\" y=\"86\" text-anchor=\"middle\" font-size=\"13\" class=\"\">0</text><text x=\"220.0\" y=\"44\" text-anchor=\"middle\" font-size=\"13\" class=\"\">A</text><text x=\"220.0\" y=\"86\" text-anchor=\"middle\" font-size=\"13\" class=\"\"><tspan font-style='italic'>a</tspan></text><text x=\"380.0\" y=\"44\" text-anchor=\"middle\" font-size=\"13\" class=\"\">U</text><text x=\"380.0\" y=\"86\" text-anchor=\"middle\" font-size=\"13\" class=\"\">1</text><text x=\"500.0\" y=\"44\" text-anchor=\"middle\" font-size=\"13\" class=\"\">B</text><text x=\"500.0\" y=\"86\" text-anchor=\"middle\" font-size=\"13\" class=\"\"><tspan font-style='italic'>b</tspan></text></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "nombres",
       "points": 0.5,
       "enonce": "Déterminer les abscisses <em>a</em> et <em>b</em> des points A et B.",
       "corrige": "<p>L’unité est partagée en 8 : chaque graduation vaut <span class=\"frac\"><span>1</span><span>8</span></span> = 0,125. A est à 4 graduations de O, B à 11.</p><p class='answer'><em>a</em> = <span class=\"frac\"><span>4</span><span>8</span></span> = 0,5 et <em>b</em> = <span class=\"frac\"><span>11</span><span>8</span></span> = 1,375</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "nombres",
       "points": 0.5,
       "enonce": "Abscisse du milieu de [OA], puis de [OB] ?",
       "corrige": "<p>Le milieu a pour abscisse la moyenne des abscisses.</p><p class='answer'>[OA] : 0,25 ; [OB] : <span class=\"frac\"><span>11</span><span>16</span></span> = 0,6875</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "nombres",
       "points": 0.75,
       "enonce": "C et D ont pour abscisses <em>c</em> = 0,45 et <em>d</em> = <span class=\"frac\"><span>4</span><span>3</span></span>. Proposer une démarche, sans calculatrice, pour savoir si chacun appartient à [AB].",
       "corrige": "<p>C : 0,45 &lt; 0,5 = <em>a</em>, donc C ∉ [AB].</p><p>D : on compare <span class=\"frac\"><span>4</span><span>3</span></span> et <span class=\"frac\"><span>11</span><span>8</span></span> en les mettant au même dénominateur : <span class=\"frac\"><span>4</span><span>3</span></span> = <span class=\"frac\"><span>32</span><span>24</span></span> et <span class=\"frac\"><span>11</span><span>8</span></span> = <span class=\"frac\"><span>33</span><span>24</span></span>. Donc 0,5 &lt; <span class=\"frac\"><span>4</span><span>3</span></span> &lt; <span class=\"frac\"><span>11</span><span>8</span></span>.</p><p class='answer'>C n’appartient pas à [AB] ; D appartient à [AB].</p>",
       "niveau": "c4"
      }
     ]
    }
   ],
   "total": 10
  },
  {
   "id": "m-kermesse",
   "num": 3,
   "titre": "Sujet A · La kermesse de l’école",
   "theme": "Arithmétique, pourcentages, Pythagore et trigonométrie, probabilités, Scratch et tableur",
   "calculatrice": true,
   "remarque": "Sujet original, inspiré des annales du CRPE et du brevet. Les questions marquées « Lycée » dépassent le cycle 4 (programme du concours) : ce sont des approfondissements.",
   "parties": [
    {
     "id": "E1",
     "label": "Exercice 1",
     "short": "Ex. 1",
     "titre": "Les sachets de friandises",
     "points": 4,
     "intro": "<p>Pour la kermesse, l’école a reçu 252 bonbons et 168 sucettes. On veut préparer des sachets <strong>identiques</strong> (même nombre de bonbons et même nombre de sucettes dans chaque sachet) en utilisant toutes les friandises.</p>",
     "questions": [
      {
       "id": "1",
       "type": "arithmetique",
       "points": 1,
       "enonce": "Décomposer 252 et 168 en produits de facteurs premiers.",
       "corrige": "<p class='answer'>252 = 2² × 3² × 7 &nbsp;;&nbsp; 168 = 2³ × 3 × 7</p><p>Méthode : divisions successives par 2, 3, 5, 7… (252 → 126 → 63 → 21 → 7).</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "arithmetique",
       "points": 1.5,
       "enonce": "Quel est le nombre maximal de sachets ? Quelle sera alors leur composition ?",
       "corrige": "<p>Le nombre de sachets doit diviser 252 et 168 : on cherche leur plus grand diviseur commun. On garde les facteurs communs avec le plus petit exposant : 2² × 3 × 7 = 84.</p><p class='answer'>84 sachets, contenant chacun 3 bonbons et 2 sucettes.</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "arithmetique",
       "points": 0.5,
       "enonce": "Peut-on préparer 12 sachets ?",
       "corrige": "<p>252 = 12 × 21 et 168 = 12 × 14 : 12 divise les deux nombres.</p><p class='answer'>Oui : 12 sachets de 21 bonbons et 14 sucettes.</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "arithmetique",
       "points": 1,
       "enonce": "Donner tous les nombres de sachets possibles.",
       "corrige": "<p>Ce sont les diviseurs communs à 252 et 168, c’est-à-dire les diviseurs de 84.</p><p class='answer'>1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E2",
     "label": "Exercice 2",
     "short": "Ex. 2",
     "titre": "Les tickets de jeu",
     "points": 4,
     "intro": "<p>Un ticket de jeu coûte 1,50 €. Un carnet de 10 tickets coûte 12 €.</p>",
     "questions": [
      {
       "id": "1",
       "type": "proportionnalite",
       "points": 0.5,
       "enonce": "Combien économise-t-on en achetant un carnet plutôt que 10 tickets à l’unité ?",
       "corrige": "<p>10 × 1,50 = 15 € ; 15 − 12 = 3.</p><p class='answer'>3 €</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Quel pourcentage de réduction le carnet représente-t-il ?",
       "corrige": "<p>3 ÷ 15 = 0,2.</p><p class='answer'>20 %</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Léa veut exactement 24 tickets. Quelle est la dépense minimale ?",
       "corrige": "<p>2 carnets + 4 tickets : 24 + 6 = 30 €. 3 carnets (30 tickets) coûteraient 36 €.</p><p class='answer'>30 €</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "proportionnalite",
       "points": 1.5,
       "enonce": "L’an dernier, le carnet coûtait 10 € ; il a augmenté de 20 %. L’an prochain, il baissera de 20 %. Reviendra-t-il à 10 € ? Quel pourcentage de baisse faudrait-il pour revenir exactement à 10 € ?",
       "corrige": "<p>12 × 0,8 = 9,60 € : non, il sera moins cher qu’il y a deux ans (évolution globale 1,2 × 0,8 = 0,96, soit −4 %).</p><p>Pour revenir de 12 € à 10 € : coefficient 10 ÷ 12 ≈ 0,833, soit une baisse d’environ 16,7 %.</p><p class='answer'>Non (9,60 €) ; il faudrait une baisse d’environ 16,7 %.</p>",
       "niveau": "lycee"
      }
     ]
    },
    {
     "id": "E3",
     "label": "Exercice 3",
     "short": "Ex. 3",
     "titre": "Le mât des fanions",
     "points": 4,
     "intro": "<p>Un mât vertical [MH] de 6 m est tenu par une corde [MS] fixée au sol en S, à 8 m du pied H du mât. Un fanion F est accroché sur la corde à 4 m de S ; K est le point du sol situé à la verticale de F.</p><figure class=\"fig\"><svg viewBox=\"0 0 420 235\" role=\"img\" aria-label=\"Mât vertical [MH] de 6 m, point d’ancrage S au sol à 8 m de H, fanion F sur la corde [MS] et K son projeté au sol\" xmlns=\"http://www.w3.org/2000/svg\"><polygon points=\"80,200 80,50 380,200\" class=\"stroke\"/><line x1=\"260.0\" y1=\"140.0\" x2=\"260.0\" y2=\"200\" class=\"stroke dash\"/><rect x=\"80\" y=\"190\" width=\"10\" height=\"10\" class=\"stroke\"/><rect x=\"260.0\" y=\"190\" width=\"10\" height=\"10\" class=\"stroke\"/><text x=\"68\" y=\"204\" text-anchor=\"middle\" font-size=\"13\" class=\"\">H</text><text x=\"68\" y=\"50\" text-anchor=\"middle\" font-size=\"13\" class=\"\">M</text><text x=\"392\" y=\"204\" text-anchor=\"middle\" font-size=\"13\" class=\"\">S</text><text x=\"260.0\" y=\"218\" text-anchor=\"middle\" font-size=\"13\" class=\"\">K</text><text x=\"264.0\" y=\"132.0\" text-anchor=\"middle\" font-size=\"13\" class=\"\">F</text><text x=\"50\" y=\"130\" text-anchor=\"middle\" font-size=\"12\" class=\"\">6 m</text><text x=\"155\" y=\"220\" text-anchor=\"middle\" font-size=\"12\" class=\"\">8 m</text></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "geometrie",
       "points": 1,
       "enonce": "Calculer la longueur de la corde MS.",
       "corrige": "<p>Le triangle MHS est rectangle en H. D’après le théorème de Pythagore : MS² = 6² + 8² = 100.</p><p class='answer'>MS = 10 m</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "geometrie",
       "points": 1,
       "enonce": "Calculer l’angle MSH que fait la corde avec le sol, au dixième de degré.",
       "corrige": "<p>Dans MHS rectangle en H : tan(MSH) = MH ÷ HS = 6 ÷ 8 = 0,75.</p><p class='answer'>MSH ≈ 36,9°</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "geometrie",
       "points": 1,
       "enonce": "À quelle hauteur FK se trouve le fanion ?",
       "corrige": "<p>(FK) et (MH) sont perpendiculaires au sol, donc parallèles. Dans le triangle SMH, d’après le théorème de Thalès : SF ÷ SM = FK ÷ MH, soit FK = 6 × 4 ÷ 10.</p><p class='answer'>FK = 2,4 m</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "geometrie",
       "points": 1,
       "enonce": "Un triangle de renfort a des côtés de 1,2 m, 1,6 m et 2,1 m. Est-il rectangle ?",
       "corrige": "<p>Plus grand côté : 2,1² = 4,41. Somme des carrés des deux autres : 1,44 + 2,56 = 4,00. 4,41 ≠ 4,00.</p><p class='answer'>Non (d’après la contraposée du théorème de Pythagore).</p><p>Avec 2 m au lieu de 2,1 m, il le serait.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E4",
     "label": "Exercice 4",
     "short": "Ex. 4",
     "titre": "La roue de la fortune",
     "points": 4,
     "intro": "<p>La roue est partagée en trois secteurs. On gagne un lot si la flèche s’arrête sur le jaune.</p><figure class=\"fig\"><svg viewBox=\"0 0 220 220\" role=\"img\" aria-label=\"Roue partagée en trois secteurs : bleu 90°, jaune 120°, rouge 150°\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M110,110 L110.0,20.0 A90,90 0 0 1 200.0,110.0 Z\" class=\"c-blue\"/><text x=\"148.18376618407356\" y=\"75.81623381592644\" text-anchor=\"middle\" font-size=\"11\" class=\"\">Bleu (90°)</text><path d=\"M110,110 L200.0,110.0 A90,90 0 0 1 65.0,187.9 Z\" class=\"c-yellow\"/><text x=\"137.0\" y=\"160.7653718043597\" text-anchor=\"middle\" font-size=\"11\" class=\"\">Jaune (120°)</text><path d=\"M110,110 L65.0,187.9 A90,90 0 0 1 110.0,20.0 Z\" class=\"c-red\"/><text x=\"57.84000538039031\" y=\"100.02377156446387\" text-anchor=\"middle\" font-size=\"11\" class=\"\">Rouge (150°)</text><polygon points=\"103,6 117,6 110,22\" class=\"fillink\"/></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "probas",
       "points": 1,
       "enonce": "Calculer la probabilité de chaque couleur.",
       "corrige": "<p>La probabilité est proportionnelle à l’angle du secteur.</p><p class='answer'>P(bleu) = <span class=\"frac\"><span>90</span><span>360</span></span> = <span class=\"frac\"><span>1</span><span>4</span></span> ; P(jaune) = <span class=\"frac\"><span>120</span><span>360</span></span> = <span class=\"frac\"><span>1</span><span>3</span></span> ; P(rouge) = <span class=\"frac\"><span>150</span><span>360</span></span> = <span class=\"frac\"><span>5</span><span>12</span></span></p><p>Vérification : <span class=\"frac\"><span>3</span><span>12</span></span> + <span class=\"frac\"><span>4</span><span>12</span></span> + <span class=\"frac\"><span>5</span><span>12</span></span> = 1.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "probas",
       "points": 1,
       "enonce": "Sur 300 parties, combien de lots peut-on s’attendre à distribuer ?",
       "corrige": "<p>300 × <span class=\"frac\"><span>1</span><span>3</span></span> = 100.</p><p class='answer'>environ 100 lots</p><p>C’est une estimation : la fréquence observée se rapproche de la probabilité quand le nombre de parties augmente.</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "probas",
       "points": 2,
       "enonce": "Pour le gros lot, il faut obtenir deux fois jaune en deux lancers. Calculer cette probabilité, puis celle d’obtenir au moins une fois jaune.",
       "corrige": "<p>Les lancers sont indépendants : P(jaune puis jaune) = <span class=\"frac\"><span>1</span><span>3</span></span> × <span class=\"frac\"><span>1</span><span>3</span></span> = <span class=\"frac\"><span>1</span><span>9</span></span>.</p><p>« Au moins un jaune » est le contraire de « aucun jaune » : 1 − <span class=\"frac\"><span>2</span><span>3</span></span> × <span class=\"frac\"><span>2</span><span>3</span></span> = 1 − <span class=\"frac\"><span>4</span><span>9</span></span> = <span class=\"frac\"><span>5</span><span>9</span></span>.</p><p class='answer'><span class=\"frac\"><span>1</span><span>9</span></span> et <span class=\"frac\"><span>5</span><span>9</span></span></p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E5",
     "label": "Exercice 5",
     "short": "Ex. 5",
     "titre": "Un programme sur la tablette",
     "points": 4,
     "intro": "<p>Voici un script Scratch :</p><div class=\"scratch\" aria-label=\"Script Scratch\"><div class=\"sb sb-event\">quand le drapeau est cliqué</div><div class=\"sb sb-sense\">demander « Choisis un nombre » et attendre</div><div class=\"sb sb-var\">mettre <span class=\"sb-v\">x</span> à <span class=\"sb-v\">réponse</span></div><div class=\"sb sb-var\">mettre <span class=\"sb-v\">résultat</span> à <span class=\"sb-v\">x</span> × <span class=\"sb-v\">x</span> − <span class=\"sb-v\">4</span> × <span class=\"sb-v\">x</span></div><div class=\"sb sb-look\">dire <span class=\"sb-v\">résultat</span></div></div>",
     "questions": [
      {
       "id": "1",
       "type": "algo",
       "points": 0.5,
       "enonce": "Qu’affiche le lutin si l’on choisit 5 ?",
       "corrige": "<p>5 × 5 − 4 × 5 = 25 − 20 = 5.</p><p class='answer'>5</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "algo",
       "points": 0.5,
       "enonce": "Et si l’on choisit −3 ?",
       "corrige": "<p>(−3) × (−3) − 4 × (−3) = 9 + 12 = 21.</p><p class='answer'>21</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "litteral",
       "points": 1.5,
       "enonce": "Quels nombres faut-il choisir pour que le lutin dise 0 ?",
       "corrige": "<p><em>x</em>² − 4<em>x</em> = 0 ⇔ <em>x</em>(<em>x</em> − 4) = 0. Un produit est nul si l’un de ses facteurs est nul : <em>x</em> = 0 ou <em>x</em> = 4.</p><p class='answer'>0 ou 4</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "algo",
       "points": 0.5,
       "enonce": "Dans un tableur, les nombres choisis sont en colonne A. Quelle formule saisir en B2 pour obtenir le résultat ?",
       "corrige": "<p class='answer'>=A2*A2-4*A2</p><p>(ou =A2^2-4*A2)</p>",
       "niveau": "c4"
      },
      {
       "id": "5",
       "type": "fonctions",
       "points": 1,
       "enonce": "Montrer que le résultat s’écrit (<em>x</em> − 2)² − 4. Quel est le plus petit résultat possible ?",
       "corrige": "<p>(<em>x</em> − 2)² − 4 = <em>x</em>² − 4<em>x</em> + 4 − 4 = <em>x</em>² − 4<em>x</em>. Un carré est toujours positif ou nul, donc le résultat est toujours supérieur ou égal à −4, et vaut −4 pour <em>x</em> = 2.</p><p class='answer'>Le plus petit résultat est −4 (pour <em>x</em> = 2).</p>",
       "niveau": "lycee"
      }
     ]
    }
   ],
   "total": 20
  },
  {
   "id": "m-potager",
   "num": 4,
   "titre": "Sujet B · Le potager pédagogique",
   "theme": "Aires et périmètres, fonctions affines, volumes, statistiques, vrai-faux",
   "calculatrice": true,
   "remarque": "Sujet original, inspiré des annales du CRPE et du brevet. Les questions marquées « Lycée » sont des approfondissements hors programme du concours.",
   "parties": [
    {
     "id": "E1",
     "label": "Exercice 1",
     "short": "Ex. 1",
     "titre": "Le plan du potager",
     "points": 4,
     "intro": "<p>Le potager a la forme d’un rectangle de 12 m sur 7 m, prolongé par un demi-disque de diamètre 7 m.</p><figure class=\"fig\"><svg viewBox=\"0 0 360 190\" role=\"img\" aria-label=\"Potager : rectangle de 12 m sur 7 m prolongé par un demi-disque de diamètre 7 m\" xmlns=\"http://www.w3.org/2000/svg\"><rect x=\"30\" y=\"20\" width=\"240\" height=\"140\" class=\"stroke\"/><path d=\"M270,20 A70.0,70.0 0 0 1 270,160\" class=\"stroke\"/><line x1=\"270\" y1=\"20\" x2=\"270\" y2=\"160\" class=\"stroke dash\"/><text x=\"150.0\" y=\"178\" text-anchor=\"middle\" font-size=\"12\" class=\"\">12 m</text><text x=\"24\" y=\"94.0\" text-anchor=\"end\" font-size=\"12\" class=\"\">7 m</text></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Calculer la longueur de la clôture qui fait le tour du potager, au dixième de mètre.",
       "corrige": "<p>Trois côtés du rectangle (12 + 12 + 7 = 31 m) + un demi-cercle de diamètre 7 m (π × 7 ÷ 2 = 3,5π m).</p><p class='answer'>31 + 3,5π ≈ 42,0 m</p><p><strong>Piège :</strong> le côté commun au rectangle et au demi-disque n’est pas clôturé.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Calculer l’aire du potager, au dixième de m².",
       "corrige": "<p>Rectangle : 12 × 7 = 84 m². Demi-disque de rayon 3,5 m : π × 3,5² ÷ 2 ≈ 19,24 m².</p><p class='answer'>≈ 103,2 m²</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Il faut 5 L de terreau par m². Le terreau est vendu en sacs de 40 L. Combien de sacs acheter ?",
       "corrige": "<p>103,24 × 5 ≈ 516,2 L ; 516,2 ÷ 40 ≈ 12,91.</p><p class='answer'>13 sacs</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Sur un plan à l’échelle 1/200, quelle longueur représente le côté de 12 m ?",
       "corrige": "<p>12 m = 1 200 cm ; 1 200 ÷ 200 = 6.</p><p class='answer'>6 cm</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E2",
     "label": "Exercice 2",
     "short": "Ex. 2",
     "titre": "Deux cuves d’arrosage",
     "points": 4,
     "intro": "<p>La cuve A contient 300 L et on y puise 20 L par jour. La cuve B contient 180 L et on y puise 8 L par jour. On note <em>x</em> le nombre de jours écoulés.</p><figure class=\"fig\"><svg viewBox=\"0 0 580 270\" role=\"img\" aria-label=\"Volume d’eau des cuves A et B en fonction du nombre de jours\" xmlns=\"http://www.w3.org/2000/svg\"><line x1=\"50.0\" y1=\"230\" x2=\"50.0\" y2=\"30\" class=\"grid\"/><text x=\"50.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">0</text><line x1=\"100.0\" y1=\"230\" x2=\"100.0\" y2=\"30\" class=\"grid\"/><text x=\"100.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">2</text><line x1=\"150.0\" y1=\"230\" x2=\"150.0\" y2=\"30\" class=\"grid\"/><text x=\"150.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">4</text><line x1=\"200.0\" y1=\"230\" x2=\"200.0\" y2=\"30\" class=\"grid\"/><text x=\"200.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">6</text><line x1=\"250.0\" y1=\"230\" x2=\"250.0\" y2=\"30\" class=\"grid\"/><text x=\"250.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">8</text><line x1=\"300.0\" y1=\"230\" x2=\"300.0\" y2=\"30\" class=\"grid\"/><text x=\"300.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">10</text><line x1=\"350.0\" y1=\"230\" x2=\"350.0\" y2=\"30\" class=\"grid\"/><text x=\"350.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">12</text><line x1=\"400.0\" y1=\"230\" x2=\"400.0\" y2=\"30\" class=\"grid\"/><text x=\"400.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">14</text><line x1=\"450.0\" y1=\"230\" x2=\"450.0\" y2=\"30\" class=\"grid\"/><text x=\"450.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">16</text><line x1=\"500.0\" y1=\"230\" x2=\"500.0\" y2=\"30\" class=\"grid\"/><text x=\"500.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">18</text><line x1=\"550.0\" y1=\"230\" x2=\"550.0\" y2=\"30\" class=\"grid\"/><text x=\"550.0\" y=\"246\" text-anchor=\"middle\" font-size=\"11\" class=\"\">20</text><line x1=\"50\" y1=\"230.0\" x2=\"550\" y2=\"230.0\" class=\"grid\"/><text x=\"44\" y=\"234.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">0</text><line x1=\"50\" y1=\"205.0\" x2=\"550\" y2=\"205.0\" class=\"grid\"/><text x=\"44\" y=\"209.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">40</text><line x1=\"50\" y1=\"180.0\" x2=\"550\" y2=\"180.0\" class=\"grid\"/><text x=\"44\" y=\"184.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">80</text><line x1=\"50\" y1=\"155.0\" x2=\"550\" y2=\"155.0\" class=\"grid\"/><text x=\"44\" y=\"159.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">120</text><line x1=\"50\" y1=\"130.0\" x2=\"550\" y2=\"130.0\" class=\"grid\"/><text x=\"44\" y=\"134.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">160</text><line x1=\"50\" y1=\"105.0\" x2=\"550\" y2=\"105.0\" class=\"grid\"/><text x=\"44\" y=\"109.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">200</text><line x1=\"50\" y1=\"80.0\" x2=\"550\" y2=\"80.0\" class=\"grid\"/><text x=\"44\" y=\"84.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">240</text><line x1=\"50\" y1=\"55.0\" x2=\"550\" y2=\"55.0\" class=\"grid\"/><text x=\"44\" y=\"59.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">280</text><line x1=\"50\" y1=\"30.0\" x2=\"550\" y2=\"30.0\" class=\"grid\"/><text x=\"44\" y=\"34.0\" text-anchor=\"end\" font-size=\"11\" class=\"\">320</text><line x1=\"50\" y1=\"230\" x2=\"550\" y2=\"230\" class=\"axis\"/><line x1=\"50\" y1=\"230\" x2=\"50\" y2=\"30\" class=\"axis\"/><line x1=\"50.0\" y1=\"42.5\" x2=\"425.0\" y2=\"230.0\" class=\"c1\"/><line x1=\"50.0\" y1=\"117.5\" x2=\"550.0\" y2=\"217.5\" class=\"c2\"/><text x=\"125.0\" y=\"73.75\" text-anchor=\"start\" font-size=\"12\" class=\"l1\">cuve A</text><text x=\"425.0\" y=\"183.125\" text-anchor=\"start\" font-size=\"12\" class=\"l2\">cuve B</text><text x=\"550\" y=\"262\" text-anchor=\"end\" font-size=\"11\" class=\"\">nombre de jours</text><text x=\"10\" y=\"22\" text-anchor=\"start\" font-size=\"11\" class=\"\">volume d’eau (L)</text></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "fonctions",
       "points": 0.5,
       "enonce": "Quelle quantité reste-t-il dans la cuve A après 5 jours ?",
       "corrige": "<p>300 − 20 × 5 = 200.</p><p class='answer'>200 L</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "fonctions",
       "points": 1,
       "enonce": "Exprimer les volumes <em>f</em>(<em>x</em>) de la cuve A et <em>g</em>(<em>x</em>) de la cuve B. S’agit-il de fonctions linéaires ?",
       "corrige": "<p class='answer'><em>f</em>(<em>x</em>) = 300 − 20<em>x</em> et <em>g</em>(<em>x</em>) = 180 − 8<em>x</em></p><p>Ce sont des fonctions affines, mais pas linéaires (l’ordonnée à l’origine n’est pas nulle : les droites ne passent pas par l’origine).</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "fonctions",
       "points": 1,
       "enonce": "Au bout de combien de jours la cuve A est-elle vide ? (lecture graphique puis vérification)",
       "corrige": "<p>La droite de A coupe l’axe des abscisses en 15. Vérification : 300 − 20<em>x</em> = 0 ⇔ <em>x</em> = 15.</p><p class='answer'>15 jours</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "litteral",
       "points": 1.5,
       "enonce": "Au bout de combien de jours les deux cuves contiennent-elles la même quantité ? Laquelle ?",
       "corrige": "<p>300 − 20<em>x</em> = 180 − 8<em>x</em> ⇔ 120 = 12<em>x</em> ⇔ <em>x</em> = 10. Volume : 300 − 200 = 100.</p><p class='answer'>Après 10 jours, avec 100 L chacune.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E3",
     "label": "Exercice 3",
     "short": "Ex. 3",
     "titre": "Le récupérateur d’eau de pluie",
     "points": 4,
     "intro": "<p>Le récupérateur est un cylindre de rayon 40 cm et de hauteur 1,20 m. Il récupère l’eau d’un toit de 20 m².</p>",
     "questions": [
      {
       "id": "1",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Calculer le volume du récupérateur, en litres, au litre près.",
       "corrige": "<p>V = π × r² × h = π × 0,4² × 1,2 ≈ 0,6032 m³, et 1 m³ = 1 000 L.</p><p class='answer'>≈ 603 L</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Une pluie de 12 mm tombe sur le toit (12 mm d’eau sur toute la surface). Quel volume d’eau est recueilli ?",
       "corrige": "<p>12 mm = 0,012 m ; 20 × 0,012 = 0,24 m³.</p><p class='answer'>240 L</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Combien de pluies de ce type faut-il pour remplir le récupérateur vide ?",
       "corrige": "<p>603,2 ÷ 240 ≈ 2,51.</p><p class='answer'>3 pluies</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Avec le récupérateur plein, combien d’arrosoirs de 11 L peut-on remplir entièrement ?",
       "corrige": "<p>603,2 ÷ 11 ≈ 54,84.</p><p class='answer'>54 arrosoirs</p><p>Ici on arrondit à l’entier <em>inférieur</em> : le 55e ne serait pas plein.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E4",
     "label": "Exercice 4",
     "short": "Ex. 4",
     "titre": "La récolte de tomates",
     "points": 4,
     "intro": "<p>Masse de tomates récoltée chaque semaine (en kg), pendant 11 semaines :</p><div class=\"table-wrap\"><table class=\"mtable\"><thead><tr><th>Semaine</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th></tr></thead><tbody><tr><th>Masse (kg)</th><td>2</td><td>5</td><td>3</td><td>8</td><td>6</td><td>4</td><td>9</td><td>7</td><td>5</td><td>12</td><td>5</td></tr></tbody></table></div>",
     "questions": [
      {
       "id": "1",
       "type": "stats",
       "points": 1,
       "enonce": "Calculer la masse moyenne récoltée par semaine.",
       "corrige": "<p>Somme : 66 kg ; 66 ÷ 11 = 6.</p><p class='answer'>6 kg</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "stats",
       "points": 1,
       "enonce": "Déterminer la médiane et l’interpréter.",
       "corrige": "<p>Série rangée : 2 ; 3 ; 4 ; 5 ; 5 ; <strong>5</strong> ; 6 ; 7 ; 8 ; 9 ; 12. 11 valeurs : la médiane est la 6e.</p><p class='answer'>Médiane : 5 kg. Au moins la moitié des semaines, on a récolté 5 kg ou moins (et au moins la moitié, 5 kg ou plus).</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "stats",
       "points": 0.5,
       "enonce": "Calculer l’étendue.",
       "corrige": "<p class='answer'>12 − 2 = 10 kg</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "stats",
       "points": 1.5,
       "enonce": "Déterminer le premier et le troisième quartile, puis l’écart interquartile.",
       "corrige": "<p>Q1 : plus petite valeur telle qu’au moins 25 % des valeurs lui soient inférieures ou égales ; 11 × 0,25 = 2,75 → 3e valeur. Q3 : 11 × 0,75 = 8,25 → 9e valeur.</p><p class='answer'>Q1 = 4 kg ; Q3 = 8 kg ; écart interquartile : 4 kg</p>",
       "niveau": "lycee"
      }
     ]
    },
    {
     "id": "E5",
     "label": "Exercice 5",
     "short": "Ex. 5",
     "titre": "Vrai ou faux ? (réponses justifiées)",
     "points": 4,
     "intro": "",
     "questions": [
      {
       "id": "1",
       "type": "arithmetique",
       "points": 0.8,
       "enonce": "Affirmation 1 : 91 est un nombre premier.",
       "corrige": "<p>91 = 7 × 13.</p><p class='answer'>Fausse.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "nombres",
       "points": 0.8,
       "enonce": "Affirmation 2 : <span class=\"frac\"><span>2</span><span>3</span></span> + <span class=\"frac\"><span>1</span><span>6</span></span> = <span class=\"frac\"><span>3</span><span>9</span></span>.",
       "corrige": "<p><span class=\"frac\"><span>2</span><span>3</span></span> + <span class=\"frac\"><span>1</span><span>6</span></span> = <span class=\"frac\"><span>4</span><span>6</span></span> + <span class=\"frac\"><span>1</span><span>6</span></span> = <span class=\"frac\"><span>5</span><span>6</span></span>. On n’additionne pas les dénominateurs.</p><p class='answer'>Fausse.</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "litteral",
       "points": 0.8,
       "enonce": "Affirmation 3 : pour tout nombre <em>x</em>, (<em>x</em> + 3)² = <em>x</em>² + 9.",
       "corrige": "<p>Contre-exemple : <em>x</em> = 1 donne 16 d’un côté et 10 de l’autre. En fait (<em>x</em> + 3)² = <em>x</em>² + 6<em>x</em> + 9.</p><p class='answer'>Fausse.</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "nombres",
       "points": 0.8,
       "enonce": "Affirmation 4 : 0,2 × 0,3 = 0,6.",
       "corrige": "<p>0,2 × 0,3 = 0,06 (2 × 3 = 6, et deux chiffres après la virgule au total).</p><p class='answer'>Fausse.</p>",
       "niveau": "c4"
      },
      {
       "id": "5",
       "type": "nombres",
       "points": 0.8,
       "enonce": "Affirmation 5 : 3,5 × 10⁻² = 0,035.",
       "corrige": "<p>Multiplier par 10⁻², c’est diviser par 100.</p><p class='answer'>Vraie.</p>",
       "niveau": "c4"
      }
     ]
    }
   ],
   "total": 20
  },
  {
   "id": "m-decouverte",
   "num": 5,
   "titre": "Sujet C · La classe de découverte",
   "theme": "Vitesses et durées, échelles, calcul littéral, tableau à double entrée, QCM",
   "calculatrice": true,
   "remarque": "Sujet original, inspiré des annales du CRPE et du brevet.",
   "parties": [
    {
     "id": "E1",
     "label": "Exercice 1",
     "short": "Ex. 1",
     "titre": "Le trajet en car",
     "points": 4,
     "intro": "<p>Le car part à 7 h 45 et parcourt 360 km. Il fait une pause de 30 minutes et arrive à 13 h 15.</p>",
     "questions": [
      {
       "id": "1",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Calculer la durée totale du voyage, puis la durée de conduite.",
       "corrige": "<p>De 7 h 45 à 13 h 15 : 5 h 30 min. Sans la pause : 5 h.</p><p class='answer'>5 h 30 min de voyage, 5 h de conduite.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Calculer la vitesse moyenne du car pendant la conduite.",
       "corrige": "<p>v = d ÷ t = 360 ÷ 5.</p><p class='answer'>72 km/h</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Convertir cette vitesse en m/s.",
       "corrige": "<p>72 km/h = 72 000 m en 3 600 s ; 72 000 ÷ 3 600 = 20.</p><p class='answer'>20 m/s</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Au retour, le car roule à 90 km/h sur les trois quarts du trajet et à 60 km/h sur le reste, avec la même pause. À quelle heure arrive-t-il s’il part à 7 h 45 ?",
       "corrige": "<p>3/4 de 360 km = 270 km à 90 km/h : 3 h. Reste 90 km à 60 km/h : 1,5 h = 1 h 30. Total : 4 h 30 + 30 min de pause = 5 h.</p><p class='answer'>12 h 45</p><p><strong>Piège :</strong> la vitesse moyenne n’est pas la moyenne des vitesses (75 km/h).</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E2",
     "label": "Exercice 2",
     "short": "Ex. 2",
     "titre": "Cartes et maquettes",
     "points": 4,
     "intro": "",
     "questions": [
      {
       "id": "1",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Sur une carte au 1/250 000, deux villages sont à 4,8 cm. Quelle est la distance réelle ?",
       "corrige": "<p>4,8 × 250 000 = 1 200 000 cm = 12 km.</p><p class='answer'>12 km</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "La classe construit une maquette du chalet au 1/50. Le chalet mesure 15 m de long. Longueur sur la maquette ?",
       "corrige": "<p>1 500 cm ÷ 50 = 30 cm.</p><p class='answer'>30 cm</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Le plancher du chalet a une aire de 120 m². Quelle est son aire sur la maquette, en cm² ?",
       "corrige": "<p>Les aires sont divisées par 50² = 2 500. 120 m² = 1 200 000 cm² ; 1 200 000 ÷ 2 500 = 480.</p><p class='answer'>480 cm²</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "grandeurs",
       "points": 1,
       "enonce": "Le volume intérieur du chalet est de 450 m³. Quel est celui de la maquette, en litres ?",
       "corrige": "<p>Les volumes sont divisés par 50³ = 125 000 : 450 ÷ 125 000 = 0,003 6 m³ = 3,6 dm³.</p><p class='answer'>3,6 L</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E3",
     "label": "Exercice 3",
     "short": "Ex. 3",
     "titre": "Deux programmes de calcul",
     "points": 4,
     "intro": "<div class='two'><ul class='box'><li><strong>Programme 1</strong></li><li>Choisir un nombre</li><li>Calculer son carré</li><li>Soustraire 9</li></ul><ul class='box'><li><strong>Programme 2</strong></li><li>Choisir un nombre</li><li>Lui ajouter 3</li><li>Multiplier par le nombre de départ diminué de 3</li></ul></div>",
     "questions": [
      {
       "id": "1",
       "type": "litteral",
       "points": 0.5,
       "enonce": "Appliquer le programme 1 au nombre 5.",
       "corrige": "<p>5² − 9 = 16.</p><p class='answer'>16</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "litteral",
       "points": 0.5,
       "enonce": "Appliquer le programme 2 au nombre 5.",
       "corrige": "<p>(5 + 3) × (5 − 3) = 8 × 2 = 16.</p><p class='answer'>16</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "litteral",
       "points": 1.5,
       "enonce": "Montrer que les deux programmes donnent toujours le même résultat.",
       "corrige": "<p>Programme 1 : <em>x</em>² − 9. Programme 2 : (<em>x</em> + 3)(<em>x</em> − 3) = <em>x</em>² − 3<em>x</em> + 3<em>x</em> − 9 = <em>x</em>² − 9.</p><p class='answer'>Les deux expressions sont égales pour tout <em>x</em>.</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "litteral",
       "points": 1.5,
       "enonce": "Quels nombres de départ donnent 0 ? Et 16 ?",
       "corrige": "<p>(<em>x</em> + 3)(<em>x</em> − 3) = 0 ⇔ <em>x</em> = −3 ou <em>x</em> = 3. <em>x</em>² − 9 = 16 ⇔ <em>x</em>² = 25 ⇔ <em>x</em> = 5 ou <em>x</em> = −5.</p><p class='answer'>0 : −3 ou 3 ; 16 : −5 ou 5.</p><p><strong>Piège :</strong> ne pas oublier la solution négative.</p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E4",
     "label": "Exercice 4",
     "short": "Ex. 4",
     "titre": "Ski ou raquettes ?",
     "points": 4,
     "intro": "<p>Les 56 élèves choisissent une activité : ski ou raquettes. 32 choisissent le ski ; parmi eux, les trois quarts ont déjà skié. Parmi ceux qui choisissent les raquettes, 10 ont déjà skié.</p>",
     "questions": [
      {
       "id": "1",
       "type": "proportionnalite",
       "points": 1.5,
       "enonce": "Construire un tableau à double entrée (activité / a déjà skié ou non).",
       "corrige": "<p>Ski : 3/4 de 32 = 24 ont déjà skié. Raquettes : 56 − 32 = 24 élèves.</p><div class=\"table-wrap\"><table class=\"mtable\"><thead><tr><th></th><th>Ski</th><th>Raquettes</th><th>Total</th></tr></thead><tbody><tr><th>A déjà skié</th><td>24</td><td>10</td><td>34</td></tr><tr><th>N’a jamais skié</th><td>8</td><td>14</td><td>22</td></tr><tr><th>Total</th><td>32</td><td>24</td><td>56</td></tr></tbody></table></div>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "probas",
       "points": 1,
       "enonce": "On choisit un élève au hasard. Probabilité qu’il n’ait jamais skié ?",
       "corrige": "<p class='answer'><span class=\"frac\"><span>22</span><span>56</span></span> = <span class=\"frac\"><span>11</span><span>28</span></span></p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "probas",
       "points": 1.5,
       "enonce": "On choisit au hasard un élève qui n’a jamais skié. Probabilité qu’il ait choisi le ski ?",
       "corrige": "<p>On se restreint aux 22 élèves qui n’ont jamais skié, dont 8 ont choisi le ski.</p><p class='answer'><span class=\"frac\"><span>8</span><span>22</span></span> = <span class=\"frac\"><span>4</span><span>11</span></span></p>",
       "niveau": "c4"
      }
     ]
    },
    {
     "id": "E5",
     "label": "Exercice 5",
     "short": "Ex. 5",
     "titre": "QCM (aucune justification demandée)",
     "points": 4,
     "intro": "<p>Une seule réponse exacte par question.</p>",
     "questions": [
      {
       "id": "1",
       "type": "nombres",
       "points": 1,
       "enonce": "L’écriture scientifique de 0,000 72 est : A : 72 × 10⁻⁵ · B : 7,2 × 10⁻⁴ · C : 7,2 × 10⁴ · D : 0,72 × 10⁻³",
       "corrige": "<p class='answer'>Réponse B</p><p>L’écriture scientifique a un seul chiffre non nul avant la virgule.</p>",
       "niveau": "c4"
      },
      {
       "id": "2",
       "type": "nombres",
       "points": 1,
       "enonce": "(2³)² est égal à : A : 2⁵ · B : 32 · C : 64 · D : 2⁹",
       "corrige": "<p class='answer'>Réponse C</p><p>(2³)² = 2⁶ = 64 : on multiplie les exposants.</p>",
       "niveau": "c4"
      },
      {
       "id": "3",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Un article passe de 80 € à 60 €. La réduction est de : A : 20 % · B : 25 % · C : 33 % · D : 75 %",
       "corrige": "<p class='answer'>Réponse B</p><p>20 ÷ 80 = 0,25. Le pourcentage se calcule par rapport au prix de départ.</p>",
       "niveau": "c4"
      },
      {
       "id": "4",
       "type": "geometrie",
       "points": 1,
       "enonce": "Un triangle isocèle a un angle au sommet principal de 40°. Ses angles à la base mesurent : A : 40° · B : 50° · C : 70° · D : 140°",
       "corrige": "<p class='answer'>Réponse C</p><p>(180° − 40°) ÷ 2 = 70°.</p>",
       "niveau": "c4"
      }
     ]
    }
   ],
   "total": 20
  },
  {
   "id": "m-lycee",
   "num": 6,
   "titre": "Sujet D · Approfondissement lycée (2de–1re)",
   "theme": "Suites, second degré, probabilités conditionnelles, évolutions, géométrie repérée",
   "calculatrice": true,
   "lycee": true,
   "remarque": "Ce sujet va au-delà du programme officiel du concours (cycle 4). Il sert à consolider les bases et à prendre de l’aisance : ne le traite qu’une fois les sujets de niveau cycle 4 maîtrisés.",
   "parties": [
    {
     "id": "E1",
     "label": "Exercice 1",
     "short": "Ex. 1",
     "titre": "Deux façons d’épargner",
     "points": 4,
     "intro": "<p>Léo possède 500 € et ajoute 50 € chaque mois : <em>u<sub>n</sub></em> est son épargne après <em>n</em> mois. Emma place 1 000 € à 3 % d’intérêts composés par an : <em>v<sub>n</sub></em> est son capital après <em>n</em> années.</p>",
     "questions": [
      {
       "id": "1",
       "type": "suites",
       "points": 1,
       "enonce": "Calculer <em>u</em><sub>12</sub>.",
       "corrige": "<p><em>u<sub>n</sub></em> = 500 + 50<em>n</em>, donc <em>u</em><sub>12</sub> = 500 + 600.</p><p class='answer'>1 100 €</p>",
       "niveau": "lycee"
      },
      {
       "id": "2",
       "type": "suites",
       "points": 1,
       "enonce": "Quelle est la nature de chaque suite ? Préciser la raison.",
       "corrige": "<p class='answer'>(<em>u<sub>n</sub></em>) est arithmétique de raison 50 ; (<em>v<sub>n</sub></em>) est géométrique de raison 1,03.</p><p>On ajoute 50 à chaque étape pour <em>u</em> ; on multiplie par 1 + 3/100 = 1,03 pour <em>v</em>.</p>",
       "niveau": "lycee"
      },
      {
       "id": "3",
       "type": "suites",
       "points": 1,
       "enonce": "Calculer <em>v</em><sub>10</sub>, au centime près.",
       "corrige": "<p><em>v<sub>n</sub></em> = 1 000 × 1,03<sup><em>n</em></sup>, donc <em>v</em><sub>10</sub> = 1 000 × 1,03<sup>10</sup>.</p><p class='answer'>≈ 1 343,92 €</p>",
       "niveau": "lycee"
      },
      {
       "id": "4",
       "type": "suites",
       "points": 1,
       "enonce": "Au bout de combien d’années le capital d’Emma dépasse-t-il 1 500 € ?",
       "corrige": "<p>Par essais à la calculatrice (ou avec un tableur) : <em>v</em><sub>13</sub> ≈ 1 468,53 € et <em>v</em><sub>14</sub> ≈ 1 512,59 €.</p><p class='answer'>Au bout de 14 ans.</p>",
       "niveau": "lycee"
      }
     ]
    },
    {
     "id": "E2",
     "label": "Exercice 2",
     "short": "Ex. 2",
     "titre": "L’enclos des poules",
     "points": 4,
     "intro": "<p>On construit un enclos rectangulaire le long d’un mur avec 20 m de grillage (le mur forme le quatrième côté). On note <em>x</em> la largeur (en m) des deux côtés perpendiculaires au mur.</p>",
     "questions": [
      {
       "id": "1",
       "type": "fonctions",
       "points": 0.5,
       "enonce": "Calculer l’aire de l’enclos pour <em>x</em> = 3.",
       "corrige": "<p>Longueur : 20 − 2 × 3 = 14 m ; aire : 3 × 14.</p><p class='answer'>42 m²</p>",
       "niveau": "lycee"
      },
      {
       "id": "2",
       "type": "fonctions",
       "points": 1,
       "enonce": "Exprimer l’aire <em>A</em>(<em>x</em>) et préciser les valeurs possibles de <em>x</em>.",
       "corrige": "<p class='answer'><em>A</em>(<em>x</em>) = <em>x</em>(20 − 2<em>x</em>) = −2<em>x</em>² + 20<em>x</em>, pour 0 &lt; <em>x</em> &lt; 10.</p>",
       "niveau": "lycee"
      },
      {
       "id": "3",
       "type": "fonctions",
       "points": 1.5,
       "enonce": "Vérifier que <em>A</em>(<em>x</em>) = −2(<em>x</em> − 5)² + 50. En déduire l’aire maximale et les dimensions correspondantes.",
       "corrige": "<p>−2(<em>x</em>² − 10<em>x</em> + 25) + 50 = −2<em>x</em>² + 20<em>x</em>. Comme −2(<em>x</em> − 5)² ≤ 0, <em>A</em>(<em>x</em>) ≤ 50, avec égalité pour <em>x</em> = 5.</p><p class='answer'>Aire maximale 50 m², pour un enclos de 5 m sur 10 m.</p>",
       "niveau": "lycee"
      },
      {
       "id": "4",
       "type": "litteral",
       "points": 1,
       "enonce": "Pour quelles valeurs de <em>x</em> l’aire vaut-elle 32 m² ?",
       "corrige": "<p>−2<em>x</em>² + 20<em>x</em> = 32 ⇔ <em>x</em>² − 10<em>x</em> + 16 = 0 ⇔ (<em>x</em> − 2)(<em>x</em> − 8) = 0. (Discriminant : 100 − 64 = 36.)</p><p class='answer'><em>x</em> = 2 ou <em>x</em> = 8</p>",
       "niveau": "lycee"
      }
     ]
    },
    {
     "id": "E3",
     "label": "Exercice 3",
     "short": "Ex. 3",
     "titre": "Un test de dépistage visuel",
     "points": 4,
     "intro": "<p>8 % des élèves d’une école ont un trouble visuel (événement T). Un test est positif (événement P) pour 95 % des élèves qui ont un trouble, et pour 10 % de ceux qui n’en ont pas.</p><figure class=\"fig\"><svg viewBox=\"0 0 380 220\" role=\"img\" aria-label=\"Arbre pondéré : T (0,08) puis P (0,95) ; non T (0,92) puis P (0,10)\" xmlns=\"http://www.w3.org/2000/svg\"><line x1=\"30\" y1=\"110\" x2=\"162\" y2=\"55\" class=\"stroke\"/><text x=\"95.0\" y=\"76.5\" text-anchor=\"middle\" font-size=\"12\" class=\"\">0,08</text><line x1=\"30\" y1=\"110\" x2=\"162\" y2=\"165\" class=\"stroke\"/><text x=\"95.0\" y=\"131.5\" text-anchor=\"middle\" font-size=\"12\" class=\"\">0,92</text><text x=\"170\" y=\"59\" text-anchor=\"start\" font-size=\"13\" class=\"\">T</text><text x=\"170\" y=\"169\" text-anchor=\"start\" font-size=\"13\" class=\"\"><tspan text-decoration='overline'>T</tspan></text><line x1=\"188\" y1=\"55\" x2=\"322\" y2=\"25\" class=\"stroke\"/><text x=\"258.0\" y=\"34.0\" text-anchor=\"middle\" font-size=\"12\" class=\"\">0,95</text><line x1=\"188\" y1=\"55\" x2=\"322\" y2=\"85\" class=\"stroke\"/><text x=\"258.0\" y=\"86.0\" text-anchor=\"middle\" font-size=\"12\" class=\"\">0,05</text><text x=\"330\" y=\"29\" text-anchor=\"start\" font-size=\"13\" class=\"\">P</text><text x=\"330\" y=\"89\" text-anchor=\"start\" font-size=\"13\" class=\"\"><tspan text-decoration='overline'>P</tspan></text><line x1=\"188\" y1=\"165\" x2=\"322\" y2=\"135\" class=\"stroke\"/><text x=\"258.0\" y=\"144.0\" text-anchor=\"middle\" font-size=\"12\" class=\"\">0,10</text><line x1=\"188\" y1=\"165\" x2=\"322\" y2=\"195\" class=\"stroke\"/><text x=\"258.0\" y=\"196.0\" text-anchor=\"middle\" font-size=\"12\" class=\"\">0,90</text><text x=\"330\" y=\"139\" text-anchor=\"start\" font-size=\"13\" class=\"\">P</text><text x=\"330\" y=\"199\" text-anchor=\"start\" font-size=\"13\" class=\"\"><tspan text-decoration='overline'>P</tspan></text></svg></figure>",
     "questions": [
      {
       "id": "1",
       "type": "probas",
       "points": 1,
       "enonce": "Justifier les probabilités 0,92, 0,05 et 0,90 inscrites sur l’arbre. Que représente la probabilité 0,95 ?",
       "corrige": "<p>La somme des probabilités issues d’un même nœud vaut 1 : 1 − 0,08 = 0,92 ; 1 − 0,95 = 0,05 ; 1 − 0,10 = 0,90.</p><p>0,95 est une probabilité <strong>conditionnelle</strong> : la probabilité que le test soit positif <em>sachant que</em> l’élève a un trouble, notée P<sub>T</sub>(P).</p>",
       "niveau": "lycee"
      },
      {
       "id": "2",
       "type": "probas",
       "points": 1,
       "enonce": "Calculer la probabilité qu’un élève ait un trouble et un test positif.",
       "corrige": "<p>On multiplie le long du chemin : 0,08 × 0,95.</p><p class='answer'>P(T ∩ P) = 0,076</p>",
       "niveau": "lycee"
      },
      {
       "id": "3",
       "type": "probas",
       "points": 1,
       "enonce": "Calculer la probabilité qu’un test soit positif.",
       "corrige": "<p>Formule des probabilités totales : 0,08 × 0,95 + 0,92 × 0,10 = 0,076 + 0,092.</p><p class='answer'>P(P) = 0,168</p>",
       "niveau": "lycee"
      },
      {
       "id": "4",
       "type": "probas",
       "points": 1,
       "enonce": "Un élève a un test positif. Quelle est la probabilité qu’il ait réellement un trouble ?",
       "corrige": "<p>P<sub>P</sub>(T) = P(T ∩ P) ÷ P(P) = 0,076 ÷ 0,168 ≈ 0,452.</p><p class='answer'>≈ 0,45</p><p>Moins d’une chance sur deux : un test positif doit être confirmé par un examen.</p>",
       "niveau": "lycee"
      }
     ]
    },
    {
     "id": "E4",
     "label": "Exercice 4",
     "short": "Ex. 4",
     "titre": "L’évolution des effectifs",
     "points": 4,
     "intro": "<p>Une école comptait 500 élèves en 2020. L’effectif a augmenté de 8 % en 2021, puis baissé de 5 % en 2022.</p>",
     "questions": [
      {
       "id": "1",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Calculer l’effectif en 2022.",
       "corrige": "<p>500 × 1,08 = 540 ; 540 × 0,95 = 513.</p><p class='answer'>513 élèves</p>",
       "niveau": "lycee"
      },
      {
       "id": "2",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Quel est le taux d’évolution global entre 2020 et 2022 ?",
       "corrige": "<p>Coefficient global : 1,08 × 0,95 = 1,026.</p><p class='answer'>+2,6 %</p>",
       "niveau": "lycee"
      },
      {
       "id": "3",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Quel taux d’évolution faudrait-il en 2023 pour revenir à 500 élèves ?",
       "corrige": "<p>Coefficient : 500 ÷ 513 ≈ 0,9747.</p><p class='answer'>≈ −2,5 %</p>",
       "niveau": "lycee"
      },
      {
       "id": "4",
       "type": "proportionnalite",
       "points": 1,
       "enonce": "Quel est le taux d’évolution annuel moyen entre 2020 et 2022 ?",
       "corrige": "<p>On cherche <em>t</em> tel que (1 + <em>t</em>)² = 1,026 : 1 + <em>t</em> = √1,026 ≈ 1,0129.</p><p class='answer'>≈ +1,3 % par an</p><p>Ce n’est pas la moyenne de +8 % et −5 %.</p>",
       "niveau": "lycee"
      }
     ]
    },
    {
     "id": "E5",
     "label": "Exercice 5",
     "short": "Ex. 5",
     "titre": "Dans un repère",
     "points": 4,
     "intro": "<p>Dans un repère orthonormé, on considère A(−2 ; 1), B(4 ; 3) et C(2 ; −3).</p>",
     "questions": [
      {
       "id": "1",
       "type": "geometrie",
       "points": 1,
       "enonce": "Calculer les coordonnées du milieu I de [AC].",
       "corrige": "<p>((−2 + 2) ÷ 2 ; (1 + (−3)) ÷ 2).</p><p class='answer'>I(0 ; −1)</p>",
       "niveau": "lycee"
      },
      {
       "id": "2",
       "type": "geometrie",
       "points": 1,
       "enonce": "Calculer la longueur AB.",
       "corrige": "<p>AB = √((4 − (−2))² + (3 − 1)²) = √(36 + 4) = √40 = 2√10.</p><p class='answer'>AB = 2√10 ≈ 6,32</p>",
       "niveau": "lycee"
      },
      {
       "id": "3",
       "type": "fonctions",
       "points": 1,
       "enonce": "Déterminer une équation de la droite (AB).",
       "corrige": "<p>Coefficient directeur : (3 − 1) ÷ (4 − (−2)) = <span class=\"frac\"><span>2</span><span>6</span></span> = <span class=\"frac\"><span>1</span><span>3</span></span>. Ordonnée à l’origine : 1 = <span class=\"frac\"><span>1</span><span>3</span></span> × (−2) + <em>p</em> ⇔ <em>p</em> = <span class=\"frac\"><span>5</span><span>3</span></span>.</p><p class='answer'><em>y</em> = <span class=\"frac\"><span>1</span><span>3</span></span><em>x</em> + <span class=\"frac\"><span>5</span><span>3</span></span></p>",
       "niveau": "lycee"
      },
      {
       "id": "4",
       "type": "geometrie",
       "points": 1,
       "enonce": "Déterminer les coordonnées de D tel que ABCD soit un parallélogramme.",
       "corrige": "<p>ABCD est un parallélogramme si ses diagonales [AC] et [BD] ont le même milieu I(0 ; −1) : <em>x</em><sub>D</sub> = 2 × 0 − 4 = −4 et <em>y</em><sub>D</sub> = 2 × (−1) − 3 = −5.</p><p class='answer'>D(−4 ; −5)</p><p>Vérification : les vecteurs AB et DC ont les mêmes coordonnées (6 ; 2).</p>",
       "niveau": "lycee"
      }
     ]
    }
   ],
   "total": 20
  }
 ]
};
