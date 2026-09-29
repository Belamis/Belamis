# -*- coding: utf-8 -*-
# Histoire-géographie-EMC (CRPE BAC+3, 2e épreuve) : sujets, repères et guide du programme.
# Utilisé par build_epreuve2.py. Documents : textes officiels ou du domaine public, cités exactement.
import cartes

def doc(n, titre, corps, src=""):
    s = f'<div class="doc"><p class="doc-title">Document {n} – {titre}</p>{corps}'
    if src:
        s += f'<p class="doc-src">{src}</p>'
    return s + "</div>"

def cite(t):
    return f"<blockquote>{t}</blockquote>"

def Q(id, type, points, enonce, corrige, niveau="c4"):
    return {"id": id, "type": type, "points": points, "enonce": enonce, "corrige": corrige, "niveau": niveau}

def P(id, label, short, titre, points, intro, questions):
    return {"id": id, "label": label, "short": short, "titre": titre, "points": points, "intro": intro, "questions": questions}

def H(points, titre, intro, qs):
    return P("H", "Histoire", "Hist.", titre, points, intro, qs)

def G(points, titre, intro, qs):
    return P("G", "Géographie", "Géo.", titre, points, intro, qs)

def E(points, titre, intro, qs):
    return P("C", "Enseignement moral et civique", "EMC", titre, points, intro, qs)

METHODE_QC = ("<p><strong>Méthode de la question de cours :</strong> une courte introduction (contexte, dates, définition, "
              "problématique), deux ou trois parties avec des titres implicites, des dates et du vocabulaire précis, "
              "puis une conclusion qui répond à la question et ouvre (mémoire, prolongements, lien avec l’école).</p>")

# ---------------------------------------------------------------- textes officiels (cités exactement)
DDHC = {
 1: "Les hommes naissent et demeurent libres et égaux en droits. Les distinctions sociales ne peuvent être fondées que sur l’utilité commune.",
 3: "Le principe de toute Souveraineté réside essentiellement dans la Nation. Nul corps, nul individu ne peut exercer d’autorité qui n’en émane expressément.",
 6: "La Loi est l’expression de la volonté générale. Tous les Citoyens ont droit de concourir personnellement, ou par leurs Représentants, à sa formation. Elle doit être la même pour tous, soit qu’elle protège, soit qu’elle punisse. Tous les Citoyens étant égaux à ses yeux sont également admissibles à toutes dignités, places et emplois publics, selon leur capacité, et sans autre distinction que celle de leurs vertus et de leurs talents.",
 10: "Nul ne doit être inquiété pour ses opinions, même religieuses, pourvu que leur manifestation ne trouble pas l’ordre public établi par la Loi.",
 11: "La libre communication des pensées et des opinions est un des droits les plus précieux de l’Homme : tout Citoyen peut donc parler, écrire, imprimer librement, sauf à répondre de l’abus de cette liberté dans les cas déterminés par la Loi.",
 16: "Toute Société dans laquelle la garantie des Droits n’est pas assurée, ni la séparation des Pouvoirs déterminée, n’a point de Constitution.",
}
def ddhc(*arts):
    return "".join(f"<p><strong>Article {a}.</strong> {DDHC[a]}</p>" for a in arts)

CONST_1 = "La France est une République indivisible, laïque, démocratique et sociale. Elle assure l’égalité devant la loi de tous les citoyens sans distinction d’origine, de race ou de religion. Elle respecte toutes les croyances. Son organisation est décentralisée."
CONST_2 = "La langue de la République est le français. L’emblème national est le drapeau tricolore, bleu, blanc, rouge. L’hymne national est la « Marseillaise ». La devise de la République est « Liberté, Égalité, Fraternité ». Son principe est : gouvernement du peuple, par le peuple et pour le peuple."
LOI_1905 = ("<p><strong>Article 1.</strong> La République assure la liberté de conscience. Elle garantit le libre exercice des cultes sous les seules restrictions édictées ci-après dans l’intérêt de l’ordre public.</p>"
            "<p><strong>Article 2.</strong> La République ne reconnaît, ne salarie ni ne subventionne aucun culte. […]</p>")
FERRY_1 = ("La loi du 28 mars se caractérise par deux dispositions qui se complètent sans se contredire : d’une part, elle met en dehors du programme obligatoire l’enseignement de tout dogme particulier ; d’autre part, elle y place au premier plan l’enseignement moral et civique. L’instruction religieuse appartient aux familles et à l’Église, l’instruction morale à l’école. Le législateur n’a donc pas entendu faire une oeuvre purement négative. Sans doute, il a eu pour premier objet de séparer l’école de l’église, d’assurer la liberté de conscience et des maîtres et des élèves, de distinguer enfin deux domaines trop longtemps confondus : celui des croyances, qui sont personnelles, libres et variables, et celui des connaissances, qui sont communes et indispensables à tous, de l’aveu de tous.")
FERRY_2 = ("Au moment de proposer aux élèves un précepte, une maxime quelconque, demandez-vous s’il se trouve à votre connaissance un seul honnête homme qui puisse être froissé de ce que vous allez dire. Demandez-vous si un père de famille, je dis un seul, présent à votre classe et vous écoutant, pourrait de bonne foi refuser son assentiment à ce qu’il vous entendrait dire. Si oui, abstenez-vous de le dire ; sinon, parlez hardiment […].")

SUJETS = []

# ================================================================ Sujet 0 officiel
SUJETS.append({
 "id": "hg-sujet0", "num": 0, "domaine": "hg", "officiel": True, "titre": "Sujet 0 officiel · histoire-géo-EMC",
 "source": "Sujet 0 du CRPE BAC+3, 2e épreuve, domaine 3 (2025)",
 "theme": "Inégalités de développement ; séparation des pouvoirs et laïcité ; la ville industrielle au XIXe siècle",
 "remarque": "Le sujet 0 ne donne pas de barème : la répartition des 20 points est indicative. Les documents 1 et 2 (tableaux) sont décrits, le document 3 (Maupassant, 1883) est reproduit.",
 "parties": [
  G(5, "Mesurer les inégalités de développement", "",
    [Q("3.1", "geographie", 5, "Répondre de façon concise : de quelle manière mesure-t-on les inégalités de développement à l’échelle mondiale ?",
       """<p><strong>Définir :</strong> le développement est l’amélioration des conditions de vie d’une population (revenus, santé, éducation, accès aux services). Il ne se réduit pas à la croissance économique.</p>
<ul><li><strong>Des indicateurs économiques :</strong> le PIB par habitant ou le RNB par habitant, en parité de pouvoir d’achat. Ils sont simples mais ne disent rien de la répartition des richesses.</li>
<li><strong>Un indicateur composite, l’IDH</strong> (indice de développement humain, créé par le PNUD en 1990) : il combine la santé (espérance de vie à la naissance), l’éducation (durée de scolarisation) et le niveau de vie (RNB par habitant). Il varie de 0 à 1 ; la Norvège ou la Suisse dépassent 0,95, certains pays du Sahel restent sous 0,45.</li>
<li><strong>Des indicateurs sociaux complémentaires :</strong> taux de mortalité infantile, accès à l’eau potable, taux d’alphabétisation, part de la population sous le seuil de pauvreté ; indicateurs d’inégalités internes (coefficient de Gini, IDH ajusté aux inégalités, indicateur d’inégalités de genre).</li></ul>
<p><strong>Nuancer :</strong> ces mesures sont des moyennes nationales qui masquent les inégalités à l’intérieur des pays (villes/campagnes, régions, genre) ; on raisonne donc à plusieurs échelles. On distingue aujourd’hui des pays développés, des pays émergents et des pays les moins avancés (PMA) plutôt qu’un simple « Nord » et « Sud ».</p>""")]),
  E(5, "Séparation des pouvoirs et laïcité", "",
    [Q("3.2", "emc", 5, "Répondre de façon concise : quels sont les principes qui définissent la séparation des pouvoirs et la laïcité dans la République française ?",
       f"""<p><strong>La séparation des pouvoirs</strong> (théorisée par Montesquieu, <em>De l’esprit des lois</em>, 1748 : « il faut que, par la disposition des choses, le pouvoir arrête le pouvoir ») :</p>
<ul><li>le pouvoir <strong>législatif</strong> (voter la loi, contrôler le gouvernement) : le Parlement (Assemblée nationale et Sénat) ;</li>
<li>le pouvoir <strong>exécutif</strong> (appliquer la loi) : le président de la République, élu pour 5 ans au suffrage universel direct, et le gouvernement dirigé par le Premier ministre, responsable devant l’Assemblée ;</li>
<li>le pouvoir <strong>judiciaire</strong> (juger) : des magistrats dont l’indépendance est garantie ; le Conseil constitutionnel vérifie la conformité des lois à la Constitution.</li></ul>
<p>Le principe figure dans la DDHC (article 16) : « Toute Société dans laquelle la garantie des Droits n’est pas assurée, ni la séparation des Pouvoirs déterminée, n’a point de Constitution. »</p>
<p><strong>La laïcité</strong> repose sur la loi du 9 décembre 1905 et l’article 1er de la Constitution (« République indivisible, laïque, démocratique et sociale ») :</p>
<ul><li>la <strong>liberté de conscience</strong> : chacun est libre de croire ou de ne pas croire, et de pratiquer son culte dans le respect de l’ordre public ;</li>
<li>la <strong>séparation</strong> des Églises et de l’État : « la République ne reconnaît, ne salarie ni ne subventionne aucun culte » ;</li>
<li>l’<strong>égalité</strong> de tous devant la loi, quelles que soient les croyances, et la <strong>neutralité</strong> de l’État et des services publics (à l’école : neutralité des personnels, loi de 2004 sur les signes religieux ostensibles des élèves).</li></ul>""")]),
  H(10, "La ville industrielle au XIXe siècle (classe de CM2)",
    doc(1, "Vue de la manufacture royale des cristaux et émaux de la reine au Creusot, vers 1782 (anonyme, peinture)", "<p><em>Description :</em> un grand bâtiment en quadrilatère, deux fours coniques qui fument, un paysage encore rural avec des promeneurs.</p>", "Musée de l’Homme et de l’Industrie, Le Creusot")
    + doc(2, "Vue générale des usines du Creusot vers 1838 (Cicéri et Bonhommé, lithographie)", "<p><em>Description :</em> commandée par la famille Schneider, elle montre des dizaines de cheminées d’usines métallurgiques et sidérurgiques, des halles, des voies ferrées et des alignements de logements.</p>", "Musée de l’Homme et de l’Industrie, Le Creusot")
    + doc(3, "Guy de Maupassant, « Petit voyage : Le Creusot », Gil Blas, 28 août 1883", cite("Le ciel est bleu, tout bleu, plein de soleil. Le train vient de passer Montchanin. Là-bas, devant nous, un nuage s’élève, tout noir, opaque, qui semble monter de la terre, qui obscurcit l’azur clair du jour, un nuage lourd, immobile. C’est la fumée du Creusot. On approche, on distingue. Cent cheminées géantes vomissent dans l’air des serpents de fumée, d’autres moins hautes et haletantes crachent des haleines de vapeur ; tout cela se mêle, s’étend, plane, couvre la ville, emplit les rues, cache le ciel, éteint le soleil. Il fait presque sombre maintenant. Une poussière de charbon voltige, pique les yeux, tache la peau, macule le linge. Les maisons sont noires, comme frottées de suie, les pavés sont noirs, les vitres poudrées de charbon. Une odeur de cheminée, de goudron, de houille flotte, contracte la gorge, oppresse la poitrine, et parfois une âcre saveur de fer, de forge, de métal brûlant, d’enfer ardent coupe la respiration, vous fait lever les yeux pour chercher l’air pur, l’air libre, l’air sain du grand ciel ; mais on voit planer là-haut le nuage épais et sombre, et miroiter près de soi les facettes menues du charbon qui voltige. C’est le Creusot. […]"))
    + "<p><em>Programme de cycle 3 (histoire, CM2), thème « L’âge industriel en France » : les énergies majeures (charbon puis pétrole) et les machines ; le travail à la mine, à l’usine, à l’atelier, au grand magasin ; la ville industrielle ; le monde rural.</em></p>",
    [Q("a", "histoire", 6, "À partir des documents, présenter les caractéristiques d’une ville industrielle au XIXe siècle.",
       """<ul><li><strong>Une transformation rapide</strong> (doc. 1 et 2) : en une cinquantaine d’années, un site presque rural (manufacture isolée, promeneurs) devient une ville-usine couverte de cheminées. Le Creusot, contrôlé par la famille Schneider à partir de 1836, symbolise l’industrialisation de la France.</li>
<li><strong>L’usine au cœur de la ville</strong> : industries lourdes (métallurgie, sidérurgie) fondées sur le charbon extrait sur place et la machine à vapeur ; voies ferrées, halles, hauts fourneaux.</li>
<li><strong>Une ville ouvrière</strong> : logements alignés construits par l’entreprise (cités ouvrières), écoles, églises, hôpital : c’est le <em>paternalisme</em> patronal, qui encadre la vie des ouvriers.</li>
<li><strong>Une ville polluée et dure à vivre</strong> (doc. 3) : Maupassant décrit la fumée qui « éteint le soleil », la poussière de charbon qui « pique les yeux », les maisons « noires », l’air irrespirable ; champs lexicaux de l’obscurité, de la saleté et de l’enfer.</li></ul>
<p><strong>Critique des documents :</strong> la lithographie (doc. 2) est une commande des Schneider : elle valorise la puissance de l’entreprise ; le texte de Maupassant est un témoignage littéraire, subjectif mais précieux sur les conditions de vie.</p>"""),
     Q("b", "histoire", 4, "Indiquer ce que les élèves de CM2 doivent retenir de cette période.",
       """<ul><li>Au XIXe siècle, la France s’industrialise : les machines (machine à vapeur) et une nouvelle énergie, le <strong>charbon</strong>, transforment la production ; le chemin de fer se développe.</li>
<li>De nouveaux lieux de travail apparaissent : la <strong>mine</strong>, l’<strong>usine</strong>, puis le grand magasin ; beaucoup d’ouvriers, y compris des enfants, y travaillent dans des conditions très dures (longues journées, accidents). Des lois limitent peu à peu le travail des enfants (1841, 1874, 1892).</li>
<li>Les campagnes se vident en partie (exode rural) et les <strong>villes industrielles</strong> grandissent, avec des quartiers ouvriers et une forte pollution.</li>
<li>Ce processus s’inscrit dans la durée et change toute la société (bourgeoisie industrielle, classe ouvrière, syndicats).</li></ul>
<p>Repères pour la frise : machine à vapeur (fin XVIIIe), premières lignes de chemin de fer (années 1830), essor des grands magasins (Le Bon Marché, 1852).</p>""")]),
 ]})

# ================================================================ Session 2026, groupement 1 (reconstitué)
SUJETS.append({
 "id": "hg-2026-g1", "num": 1, "domaine": "hg", "officiel": True, "titre": "Session 2026 · groupement 1 (histoire-géo-EMC)",
 "source": "CRPE BAC+3, session 2026, 2e épreuve, domaine histoire-géographie-EMC, groupement 1 (d’après les questions publiées dans les corrigés en ligne)",
 "theme": "Le régime de Vichy ; la répartition de la population française ; l’égalité à l’école",
 "remarque": "Les questions sont celles du sujet 2026. Les documents officiels n’étant pas publiés, le dossier d’EMC est reconstitué avec des textes officiels équivalents. Le corrigé est propre à cette plateforme.",
 "parties": [
  H(5, "Le régime de Vichy", "",
    [Q("1", "histoire", 5, "Quelles sont les caractéristiques du régime de Vichy ?" + METHODE_QC,
       """<p><strong>Introduction.</strong> Après la défaite de mai-juin 1940, le maréchal Pétain, président du Conseil, signe l’armistice le 22 juin 1940 : la France est coupée en une zone occupée au nord et à l’ouest et une zone « libre » au sud. Le 10 juillet 1940, à Vichy, les parlementaires votent les pleins pouvoirs à Pétain (569 voix pour, 80 contre) : la IIIe République disparaît au profit de l’« État français ». <em>En quoi ce régime est-il autoritaire, antisémite et collaborationniste ?</em></p>
<p><strong>1. Un régime autoritaire qui rompt avec la République.</strong></p>
<ul><li>Actes constitutionnels du 11 juillet 1940 : Pétain, « chef de l’État français », concentre les pouvoirs exécutif et législatif ; le Parlement est ajourné ; plus d’élections.</li>
<li>La devise « Travail, Famille, Patrie » remplace « Liberté, Égalité, Fraternité » : c’est la <strong>Révolution nationale</strong>, conservatrice, hostile aux partis, aux syndicats et à la démocratie.</li>
<li>Culte du chef (portraits, chant « Maréchal, nous voilà »), propagande en direction de la jeunesse, censure, répression des opposants (communistes, francs-maçons, résistants).</li></ul>
<p><strong>2. Un régime d’exclusion et antisémite.</strong></p>
<ul><li>Statuts des Juifs du 3 octobre 1940 et du 2 juin 1941, adoptés sans demande allemande : exclusion de la fonction publique, de l’enseignement, de nombreuses professions ; recensement ; « aryanisation » des biens.</li>
<li>Internement dans des camps en France (Gurs, Drancy…), y compris de Tsiganes et de réfugiés étrangers.</li></ul>
<p><strong>3. Un régime de collaboration avec l’Allemagne nazie.</strong></p>
<ul><li>Entrevue de Montoire entre Pétain et Hitler (24 octobre 1940) : Pétain annonce entrer « dans la voie de la collaboration ». Pierre Laval en est l’artisan.</li>
<li>Collaboration policière : la police française organise les rafles, dont celle du <strong>Vél d’Hiv</strong> (16-17 juillet 1942, environ 13 000 Juifs arrêtés à Paris) ; environ 75 000 Juifs sont déportés de France, très peu reviennent.</li>
<li>Collaboration économique : réquisitions, puis Service du travail obligatoire (<strong>STO</strong>, février 1943) ; la Milice (1943) traque les résistants. Après novembre 1942, toute la France est occupée.</li></ul>
<p><strong>Conclusion.</strong> Le régime s’effondre à la Libération (été 1944) ; le Gouvernement provisoire rétablit la légalité républicaine. Pétain est condamné à mort en 1945, peine commuée en détention à perpétuité. En 1995, le président Jacques Chirac reconnaît la responsabilité de l’État français dans la déportation des Juifs. À l’école, ce thème s’articule avec la Résistance et la mémoire de la Shoah.</p>
<p><strong>Pièges :</strong> ne pas confondre l’armistice (22 juin 1940) avec une capitulation ; « zone libre » ne signifie pas zone sans collaboration ; ne pas oublier la dimension antisémite propre à Vichy.</p>""")]),
  G(5, "La répartition de la population française", "<p>Un fond de carte de la France métropolitaine est fourni.</p>" + cartes.france_vierge(),
    [Q("2", "geographie", 5, "Représenter sur le fond de carte la répartition de la population française (titre, légende organisée, nomenclature).",
       "<p>Éléments attendus :</p><ul><li><strong>un titre</strong> ;</li><li>les <strong>principales aires urbaines</strong> en cercles proportionnels (Paris, plus de 10 millions d’habitants ; puis Lyon, Marseille, Lille, Toulouse, Bordeaux ; puis Nantes, Nice, Strasbourg, Montpellier, Rennes, Grenoble…) ;</li><li>les <strong>espaces de fortes densités</strong> : région parisienne, axe Lille-Paris-Lyon-Marseille (vallées du Rhône et de la Saône), littoraux atlantique et méditerranéen, Alsace, frontière nord ;</li><li>les <strong>espaces de faibles densités</strong> : une « diagonale » des Ardennes aux Landes par le Massif central, et les espaces de montagne ;</li><li>une <strong>légende organisée</strong> (des villes aux espaces), des figurés adaptés (cercles pour les villes, aplats pour les densités, trait pour les axes) et la nomenclature lisible.</li></ul>"
       + cartes.carte_population()
       + "<p>Chiffres utiles : environ 68 millions d’habitants en France (dont environ 66 millions en métropole), soit une densité moyenne proche de 120 habitants au km² en métropole ; plus de 9 habitants sur 10 vivent dans l’aire d’attraction d’une ville (INSEE).</p>", "c4")]),
  E(10, "L’égalité, principe fondamental de l’école de la République",
    doc(1, "Code de l’éducation, article L. 111-1 (extraits)", cite("Le service public de l’éducation […] contribue à l’égalité des chances et à lutter contre les inégalités sociales et territoriales en matière de réussite scolaire et éducative. […] Il veille à la scolarisation inclusive de tous les enfants, sans aucune distinction. Il veille également à la mixité sociale des publics scolarisés au sein des établissements d’enseignement."), "Code de l’éducation, version en vigueur (extraits)")
    + doc(2, "Évaluation des acquis des élèves de petite section (synthèse)", "<p>Des évaluations nationales menées en petite section de maternelle montrent que, dès la première année d’école, les acquis en langage et en premiers outils mathématiques varient selon le milieu social des familles, le mois de naissance (les enfants nés en début d’année réussissent mieux) et le sexe (léger avantage aux filles).</p>", "D’après une note d’information de la DEPP (ministère de l’Éducation nationale), 2025 — synthèse")
    + doc(3, "Une séance d’EMC en CE2 sur les stéréotypes", "<p>Les élèves trient des images de métiers, de jouets et d’activités en indiquant « pour les filles », « pour les garçons » ou « pour tous », puis débattent de leurs choix et construisent une affiche : « Tous les métiers et tous les jeux sont pour tous ».</p>", "Situation de classe décrite pour l’entraînement"),
    [Q("1", "emc", 3, "Pourquoi l’égalité est-elle considérée comme un principe fondamental de l’école de la République ?",
       """<ul><li>L’égalité est une valeur de la devise républicaine (« Liberté, Égalité, Fraternité ») et un principe de la DDHC (article 1er) et de la Constitution (égalité devant la loi).</li>
<li>L’école républicaine s’est construite sur cette idée : lois Ferry de 1881-1882, école gratuite, obligatoire et laïque pour tous les enfants, filles comme garçons.</li>
<li>Le Code de l’éducation (doc. 1) en fait une mission : égalité des chances, lutte contre les inégalités sociales et territoriales, école inclusive (loi de 2005 sur le handicap, loi de 2019 « pour une école de la confiance »), mixité sociale, égalité filles-garçons.</li>
<li>C’est une condition de la citoyenneté : l’école doit donner à chacun les mêmes droits et les mêmes chances de réussir, quelle que soit son origine.</li></ul>"""),
     Q("2", "emc", 3, "L’égalité des droits est affirmée par la loi. Que nous apprend le document 2 ?",
       """<ul><li>L’égalité en droit ne suffit pas à garantir l’égalité réelle : dès la petite section, les acquis diffèrent selon le milieu social, l’âge (mois de naissance) et le sexe.</li>
<li>Le facteur social est déterminant : les enfants issus de milieux favorisés arrivent avec un langage plus riche.</li>
<li>Conséquence pour l’école : il faut agir tôt (maternelle, scolarisation obligatoire dès 3 ans depuis 2019), différencier, soutenir le langage, et tenir compte du mois de naissance dans l’évaluation.</li>
<li>On distingue ainsi l’<strong>égalité des droits</strong> (formelle) et l’<strong>équité</strong> : donner plus à ceux qui ont moins (éducation prioritaire, dédoublement des classes de CP-CE1).</li></ul>"""),
     Q("3", "emc", 4, "Montrer comment l’école met en œuvre le principe d’égalité entre tous les élèves, quelles que soient leurs différences. Préciser comment l’EMC, par ses finalités, peut contribuer à cet objectif.",
       """<p><strong>Des dispositifs :</strong> école inclusive (AESH, ULIS, PAP), éducation prioritaire, aides personnalisées, gratuité, mixité, lutte contre le harcèlement (programme pHARe), égalité filles-garçons dans les pratiques (répartition de la parole, de la cour, des responsabilités).</p>
<p><strong>L’EMC</strong> vise à respecter autrui, à acquérir et partager les valeurs de la République et à construire une culture civique. Elle contribue à l’égalité :</p>
<ul><li>en faisant connaître les droits (droits de l’enfant, égalité devant la loi) ;</li>
<li>en déconstruisant les préjugés et les stéréotypes (doc. 3 : tri d’images, débat, affiche) ;</li>
<li>en pratiquant le débat réglé, les conseils d’élèves, les responsabilités partagées ;</li>
<li>en luttant contre toutes les discriminations (sexe, origine, handicap, religion) ; l’éducation à la vie affective, relationnelle et à la sexualité (EVAR-S) y participe aussi.</li></ul>""")]),
 ]})

# ================================================================ Sujet A : la Grande Guerre
SUJETS.append({
 "id": "hg-grande-guerre", "num": 2, "domaine": "hg", "titre": "Sujet A · 1914-1918, une guerre totale",
 "theme": "Première Guerre mondiale ; espaces de faible densité ; liberté d’expression et éducation aux médias",
 "remarque": "Sujet original construit sur le modèle de la session 2026 (histoire 5, géographie 5, EMC 10).",
 "parties": [
  H(5, "La Première Guerre mondiale", "",
    [Q("1", "histoire", 5, "En quoi la Première Guerre mondiale est-elle une guerre totale ?" + METHODE_QC,
       """<p><strong>Introduction.</strong> Déclenchée à l’été 1914 après l’assassinat de l’archiduc François-Ferdinand à Sarajevo (28 juin), la guerre oppose la Triple-Entente (France, Royaume-Uni, Russie, rejoints par l’Italie en 1915 et les États-Unis en 1917) aux Empires centraux (Allemagne, Autriche-Hongrie, Empire ottoman). Une <strong>guerre totale</strong> mobilise toutes les ressources humaines, économiques et morales d’une société et n’épargne pas les civils.</p>
<p><strong>1. Une mobilisation des soldats et une violence de masse.</strong> Après l’échec de la guerre de mouvement (bataille de la Marne, septembre 1914), le front se fige : guerre des tranchées. Batailles d’usure : <strong>Verdun</strong> (février-décembre 1916, environ 300 000 morts français et allemands), la Somme (1916). Armes nouvelles : artillerie lourde, gaz (1915), chars, avions. Environ 10 millions de soldats tués, dont 1,4 million de Français.</p>
<p><strong>2. Une mobilisation de l’économie et des sociétés.</strong> Économie de guerre : usines d’armement, emprunts, travail des femmes (munitionnettes, agricultrices), appel aux colonies (soldats et travailleurs). Propagande, censure (« bourrage de crâne »), Union sacrée.</p>
<p><strong>3. Des civils touchés.</strong> Occupation du nord de la France et de la Belgique, déportations de civils, bombardements ; <strong>génocide des Arméniens</strong> par l’Empire ottoman (1915-1916, environ 1,2 million de victimes).</p>
<p><strong>Conclusion.</strong> Armistice du 11 novembre 1918, traité de Versailles (28 juin 1919). La guerre laisse un bilan humain immense (monuments aux morts dans chaque commune), des mutilés (« gueules cassées ») et des rancœurs qui pèsent sur l’entre-deux-guerres. Le 11 novembre est une journée de commémoration.</p>""")]),
  G(5, "Les espaces de faible densité", "<p>Un fond de carte de la France métropolitaine est fourni.</p>" + cartes.france_vierge(),
    [Q("2a", "geographie", 2, "Définir un espace de faible densité et expliquer pourquoi ces espaces ne sont pas des « espaces vides ».",
       "<p>Un espace de faible densité compte peu d’habitants au km² (souvent moins de 30), avec des villes petites et éloignées : espaces ruraux isolés, montagnes, certains espaces ultramarins (Guyane). Ils ne sont pas vides : on y trouve de l’agriculture (céréales, élevage), de la forêt, du tourisme vert et de montagne, des résidences secondaires, des retraités et des néoruraux ; certains gagnent à nouveau des habitants. Leurs difficultés : vieillissement, recul des services publics et des commerces, déserts médicaux, dépendance à la voiture.</p>"),
     Q("2b", "geographie", 3, "Réaliser un croquis simple localisant les principaux espaces de faible densité en France métropolitaine.",
       "<p>Attendus : un titre ; la « diagonale » des faibles densités (des Ardennes et de la Meuse aux Landes, par la Bourgogne, le Massif central et le Limousin) ; les montagnes (Alpes, Pyrénées, Massif central) ; quelques métropoles en contrepoint ; une légende organisée.</p>" + cartes.carte_faible_densite())]),
  E(10, "La liberté d’expression et l’éducation aux médias",
    doc(1, "Déclaration des droits de l’homme et du citoyen, 26 août 1789", ddhc(10, 11))
    + doc(2, "Loi du 29 juillet 1881 sur la liberté de la presse, article 1er", cite("L’imprimerie et la librairie sont libres."))
    + doc(3, "Une situation de classe (CM2)", "<p>Un élève affirme qu’« une vidéo vue des milliers de fois sur un réseau social prouve que c’est vrai ». Une autre élève répond : « Moi, j’ai vu l’inverse sur un autre site. »</p>", "Situation décrite pour l’entraînement"),
    [Q("1", "emc", 3, "Qu’est-ce que la liberté d’expression ? Quelles en sont les limites fixées par la loi ?",
       "<p>C’est le droit de penser, de parler, d’écrire et de publier librement (DDHC, art. 11 ; liberté de la presse, loi de 1881). Elle n’est pas absolue : on doit « répondre de l’abus de cette liberté dans les cas déterminés par la loi ». Sont interdits notamment la diffamation et l’injure, l’incitation à la haine, à la violence ou à la discrimination, l’apologie du terrorisme ou des crimes contre l’humanité, la négation de la Shoah, le harcèlement, l’atteinte à la vie privée. Le blasphème n’est pas un délit en France : on peut critiquer une religion, pas insulter ou appeler à la haine contre des personnes.</p>"),
     Q("2", "emc", 3, "Pourquoi la liberté de la presse est-elle essentielle dans une démocratie ?",
       "<p>Une presse libre et pluraliste informe les citoyens, qui peuvent ainsi se forger une opinion et voter de façon éclairée ; elle contrôle les pouvoirs (enquêtes, révélations) ; elle fait vivre le débat public. Les régimes autoritaires (Vichy, régimes totalitaires) commencent par la censure. Des garanties existent : protection du secret des sources, pluralisme, autorité de régulation (Arcom).</p>"),
     Q("3", "emc", 4, "À partir du document 3, proposer une démarche d’éducation aux médias et à l’information (EMI) pour des élèves de cycle 3.",
       "<ul><li><strong>Partir des représentations</strong> : pourquoi croit-on une information ? Le nombre de vues n’est pas une preuve.</li><li><strong>Vérifier</strong> : identifier la source (qui parle ? un journaliste, un anonyme, une publicité ?), la date, croiser avec d’autres sources fiables, distinguer fait et opinion, repérer une image détournée (recherche d’image inversée, avec l’enseignant).</li><li><strong>Produire</strong> : écrire un article pour le journal de l’école, participer à la Semaine de la presse et des médias dans l’école (CLEMI).</li><li><strong>Débattre</strong> dans un cadre réglé : respecter la parole de l’autre, argumenter.</li><li>Finalité : former des citoyens capables d’esprit critique, ce qui rejoint la liberté d’expression (docs 1 et 2) et ses responsabilités.</li></ul>")]),
 ]})

# ================================================================ Sujet B : la Révolution française
SUJETS.append({
 "id": "hg-revolution", "num": 3, "domaine": "hg", "titre": "Sujet B · La Révolution française",
 "theme": "1789 et la fin de l’Ancien Régime ; les aires urbaines ; la laïcité",
 "parties": [
  H(5, "La Révolution française", doc(1, "Déclaration des droits de l’homme et du citoyen, 26 août 1789", ddhc(1, 3, 6)),
    [Q("1", "histoire", 5, "Montrer comment les années 1789-1792 mettent fin à l’Ancien Régime. Vous pouvez vous appuyer sur le document 1." + METHODE_QC,
       """<p><strong>Introduction.</strong> En 1789, la France est une monarchie absolue de droit divin et une société d’ordres (clergé, noblesse, tiers état) marquée par les privilèges. La crise financière pousse Louis XVI à convoquer les États généraux (5 mai 1789).</p>
<p><strong>1. 1789, la fin de la monarchie absolue et de la société d’ordres.</strong> Le 17 juin, les députés du tiers état se proclament Assemblée nationale ; serment du Jeu de paume (20 juin) : donner une Constitution à la France. Prise de la Bastille (14 juillet). Nuit du 4 août : abolition des privilèges. <strong>DDHC</strong> (26 août) : égalité en droits (art. 1), souveraineté de la Nation (art. 3), loi expression de la volonté générale, égalité devant la loi et accès aux emplois selon les talents (art. 6).</p>
<p><strong>2. Une monarchie constitutionnelle (1791).</strong> La Constitution de 1791 sépare les pouvoirs ; le roi n’a plus qu’un veto suspensif. La fuite du roi (Varennes, juin 1791) ruine la confiance.</p>
<p><strong>3. La naissance de la République (1792).</strong> Guerre contre l’Autriche (avril 1792), prise des Tuileries (10 août 1792), abolition de la royauté et proclamation de la République (21-22 septembre 1792) ; Louis XVI est exécuté le 21 janvier 1793.</p>
<p><strong>Conclusion.</strong> Les principes de 1789 (liberté, égalité, souveraineté nationale) fondent encore la République : la DDHC fait partie du bloc de constitutionnalité. Mais ils excluent alors les femmes (Olympe de Gouges, Déclaration des droits de la femme et de la citoyenne, 1791) et les esclaves des colonies (abolition en 1794, rétablie en 1802, définitive en 1848).</p>""")]),
  G(5, "Les aires urbaines en France", "",
    [Q("2", "geographie", 5, "Qu’est-ce qu’une aire urbaine (aire d’attraction d’une ville) ? Décrire l’organisation d’une grande aire urbaine française et ses dynamiques actuelles.",
       "<ul><li><strong>Définition :</strong> l’INSEE définit l’<em>aire d’attraction d’une ville</em> comme un pôle (ville-centre et banlieue, forte densité d’emplois) et une couronne de communes dont une partie importante des actifs vient travailler dans le pôle. Plus de 9 Français sur 10 vivent dans une telle aire.</li><li><strong>Organisation :</strong> un centre-ville (commerces, administrations, patrimoine), des banlieues (grands ensembles, zones d’activités, zones commerciales en périphérie), une couronne périurbaine de lotissements pavillonnaires, reliés par des axes de transport.</li><li><strong>Dynamiques :</strong> <em>métropolisation</em> (concentration des activités de commandement, d’innovation et des emplois qualifiés dans les grandes villes : Paris, Lyon, Toulouse, Nantes, Bordeaux…) ; <em>périurbanisation</em> (étalement urbain lié à la voiture et au prix du logement) ; gentrification des centres ; politiques de densification, de transports en commun (tramway) et de « ville durable » (lutte contre l’artificialisation des sols).</li></ul>" + cartes.carte_population())]),
  E(10, "La laïcité",
    doc(1, "Loi du 9 décembre 1905 concernant la séparation des Églises et de l’État", LOI_1905)
    + doc(2, "Constitution du 4 octobre 1958, article 1er (premier alinéa)", cite(CONST_1))
    + doc(3, "Charte de la laïcité à l’école (2013), extraits", "<p><strong>Article 3.</strong> La laïcité garantit la liberté de conscience à tous. Chacun est libre de croire ou de ne pas croire. Elle permet la libre expression de ses convictions, dans le respect de celles d’autrui et dans les limites de l’ordre public.</p><p><strong>Article 6.</strong> La laïcité de l’École offre aux élèves les conditions pour forger leur personnalité, exercer leur libre arbitre et faire l’apprentissage de la citoyenneté. Elle les protège de tout prosélytisme et de toute pression qui les empêcheraient de faire leurs propres choix.</p>")
    + doc(4, "Jules Ferry, Lettre aux instituteurs, 17 novembre 1883 (extrait)", cite(FERRY_1)),
    [Q("1", "emc", 3, "À partir des documents 1 et 2, définir la laïcité.",
       "<p>La laïcité est un principe d’organisation de la République qui repose sur : la <strong>liberté de conscience</strong> (croire, ne pas croire, changer de religion) et le libre exercice des cultes dans les limites de l’ordre public ; la <strong>séparation</strong> des Églises et de l’État (aucun culte reconnu, salarié ou subventionné) ; la <strong>neutralité</strong> de l’État et l’<strong>égalité</strong> de tous devant la loi, quelles que soient les croyances. La laïcité n’est pas une opinion contre les religions : elle protège la liberté de chacun.</p>"),
     Q("2", "emc", 3, "Montrer, à partir des documents 3 et 4, pourquoi la laïcité est une condition de l’école républicaine.",
       "<p>Dès les lois Ferry (1882), l’école publique sépare les croyances, « personnelles, libres et variables », et les connaissances, « communes et indispensables à tous » (doc. 4). L’instruction religieuse relève des familles, l’instruction morale et civique de l’école. La Charte de 2013 (doc. 3) rappelle que la laïcité permet aux élèves de « forger leur personnalité » et d’« exercer leur libre arbitre » en les protégeant du prosélytisme. Elle garantit l’égalité de tous les élèves et la neutralité des enseignants ; la loi du 15 mars 2004 interdit aux élèves le port de signes religieux ostensibles à l’école publique.</p>"),
     Q("3", "emc", 4, "Une élève de CM1 demande : « Est-ce qu’à l’école on a le droit de parler de religion ? » Comment lui répondre et quelle séance d’EMC pourriez-vous proposer ?",
       "<p><strong>Réponse :</strong> oui, on peut parler <em>des</em> religions comme faits culturels et historiques (en histoire, en histoire des arts), et chacun peut dire ce qu’il croit ou ne croit pas, dans le respect des autres ; mais l’école ne dit pas ce qu’il faut croire, et l’enseignant reste neutre.</p><p><strong>Séance possible :</strong> lecture et explication de quelques articles de la Charte de la laïcité affichée dans l’école ; étude de cas (« Un camarade se moque de la religion d’un autre », « Peut-on refuser un cours ? ») ; débat réglé ; trace écrite : « La laïcité me permet de croire ou de ne pas croire, elle me protège, elle m’oblige à respecter les convictions des autres. » Journée de la laïcité le 9 décembre.</p>")]),
 ]})

# ================================================================ Sujet C : l'école de la IIIe République
SUJETS.append({
 "id": "hg-republique-ecole", "num": 4, "domaine": "hg", "titre": "Sujet C · La République s’enracine (1870-1914)",
 "theme": "La IIIe République et l’école ; la France et l’Union européenne ; les droits de l’enfant",
 "parties": [
  H(5, "L’enracinement de la République", doc(1, "Jules Ferry, Lettre aux instituteurs, 17 novembre 1883 (extrait)", cite(FERRY_2)),
    [Q("1", "histoire", 5, "Comment la IIIe République s’enracine-t-elle en France entre 1870 et 1914 ? Vous montrerez le rôle de l’école." + METHODE_QC,
       """<p><strong>Introduction.</strong> Proclamée le 4 septembre 1870 après la défaite de Sedan, la IIIe République est d’abord fragile (majorité monarchiste à l’Assemblée, Commune de Paris écrasée en mai 1871). Les lois constitutionnelles de 1875 l’installent (amendement Wallon, adopté à une voix de majorité).</p>
<p><strong>1. Des institutions et des libertés.</strong> Les républicains deviennent majoritaires (1879). Symboles : Marseillaise hymne national (1879), 14 juillet fête nationale (1880), devise sur les frontons. Libertés : réunion et presse (1881), syndicats (1884), associations (1901). Suffrage universel masculin (depuis 1848).</p>
<p><strong>2. L’école, pilier de la République.</strong> Lois Ferry : école primaire <strong>gratuite</strong> (1881), <strong>obligatoire</strong> de 6 à 13 ans et <strong>laïque</strong> dans ses programmes (28 mars 1882), avec une instruction morale et civique ; laïcisation du personnel (loi Goblet, 1886). Les « hussards noirs », instituteurs formés dans les écoles normales, diffusent la langue française, l’amour de la patrie et les valeurs républicaines. Le document 1 montre la prudence demandée aux maîtres : enseigner une morale commune, sans froisser aucune conscience.</p>
<p><strong>3. Une République qui surmonte des crises.</strong> Crise boulangiste (1889), affaire Dreyfus (1894-1906) qui oppose dreyfusards et antidreyfusards (« J’accuse » de Zola, 1898) et renforce les défenseurs des droits ; loi de séparation des Églises et de l’État (1905).</p>
<p><strong>Conclusion.</strong> En 1914, la République est acceptée par la majorité des Français (Union sacrée). Limites : les femmes n’ont pas le droit de vote, et la République mène une politique de colonisation.</p>""")]),
  G(5, "La France dans l’Union européenne", cartes.carte_ue(),
    [Q("2a", "geographie", 2, "À partir de la carte, présenter l’Union européenne : nombre d’États membres, États fondateurs, grandes étapes.",
       "<p>L’UE compte <strong>27 États membres</strong> (depuis la sortie du Royaume-Uni, le 31 janvier 2020). Les six fondateurs sont la France, la RFA (Allemagne), l’Italie, la Belgique, les Pays-Bas et le Luxembourg : CECA (1951), traités de Rome créant la CEE (25 mars 1957). Grandes étapes : traité de Maastricht (1992, naissance de l’UE, citoyenneté européenne), euro (monnaie en 1999, pièces et billets en 2002), élargissements (dont 10 pays en 2004).</p>"),
     Q("2b", "geographie", 3, "Montrer que l’appartenance à l’Union européenne a des effets sur le territoire français.",
       "<ul><li><strong>Des frontières ouvertes :</strong> libre circulation des personnes (espace Schengen), des marchandises, des capitaux et des services ; travailleurs frontaliers (Luxembourg, Suisse hors UE, Allemagne) ; coopérations transfrontalières (eurodistrict Strasbourg-Ortenau, Grand Genève).</li><li><strong>Des financements :</strong> politique agricole commune (la France en est un des premiers bénéficiaires) ; fonds européens de cohésion (FEDER) pour les régions et les territoires ultramarins, qui sont des « régions ultrapériphériques » de l’UE.</li><li><strong>Des axes et des pôles européens :</strong> Strasbourg (Parlement européen), corridors de transport (LGV, tunnel sous la Manche), ports (Le Havre, Marseille-Fos) ouverts sur l’Europe.</li><li><strong>Des normes communes :</strong> environnement (Natura 2000), consommation, euro dans 21 pays.</li></ul>")]),
  E(10, "Les droits de l’enfant",
    doc(1, "Convention internationale des droits de l’enfant (ONU, 20 novembre 1989), repères", "<ul><li>Article 3 : dans toutes les décisions qui le concernent, l’intérêt supérieur de l’enfant doit être une considération primordiale.</li><li>Article 12 : l’enfant capable de discernement a le droit d’exprimer librement son opinion sur toute question l’intéressant.</li><li>Article 19 : l’enfant doit être protégé contre toute forme de violence, d’atteinte ou de brutalités physiques ou mentales, d’abandon ou de négligence, de mauvais traitements.</li><li>Article 28 : l’enfant a droit à l’éducation ; l’enseignement primaire doit être obligatoire et gratuit pour tous.</li></ul>", "Résumé des articles cités (texte intégral disponible sur le site de l’UNICEF)")
    + doc(2, "Le numéro 119", "<p>Le 119 « Allô enfance en danger » est un numéro national gratuit, joignable 24 h/24, pour les enfants en danger ou les adultes qui s’inquiètent pour un enfant.</p>"),
    [Q("1", "emc", 3, "Présenter la Convention internationale des droits de l’enfant : date, origine, portée.",
       "<p>Adoptée à l’unanimité par l’Assemblée générale des Nations unies le <strong>20 novembre 1989</strong> (d’où la journée internationale des droits de l’enfant le 20 novembre), ratifiée par la France en 1990 et par presque tous les États du monde. Elle considère l’enfant (moins de 18 ans) comme une personne titulaire de droits : droits à la survie et au développement (santé, éducation), à la protection (contre les violences, l’exploitation, la guerre), à la participation (s’exprimer, être entendu). Principe clé : l’intérêt supérieur de l’enfant.</p>"),
     Q("2", "emc", 3, "Quel est le rôle de l’école et des enseignants dans la protection de l’enfance ?",
       "<p>L’école garantit le droit à l’éducation (instruction obligatoire de 3 à 16 ans). Les enseignants ont une obligation de vigilance : repérer les signes de maltraitance, écouter l’enfant, et <strong>transmettre une information préoccupante</strong> (cellule départementale, CRIP) ou, en cas de danger grave, faire un <strong>signalement</strong> au procureur de la République. Ils font connaître le 119, luttent contre le harcèlement (programme pHARe) et mettent en œuvre l’éducation à la vie affective et relationnelle. Le Défenseur des droits (et son adjoint Défenseur des enfants) peut être saisi.</p>"),
     Q("3", "emc", 4, "Proposer une séquence d’EMC de trois séances au cycle 3 sur les droits de l’enfant.",
       "<ol><li><strong>Découvrir</strong> : recueillir les représentations (« Qu’est-ce qu’un droit ? »), distinguer besoin, envie et droit ; lire une version adaptée de la CIDE.</li><li><strong>Comprendre</strong> : études de cas (travail des enfants, enfants privés d’école, enfants soldats) ; lien avec l’histoire (travail des enfants au XIXe siècle) ; le 119.</li><li><strong>Agir</strong> : débat réglé « Les droits vont-ils avec des devoirs ? » ; réalisation d’une affiche ou d’une exposition pour le 20 novembre ; élection de délégués ou conseil d’enfants.</li></ol><p>Évaluation : expliquer avec ses mots trois droits de l’enfant et savoir à qui s’adresser en cas de danger.</p>")]),
 ]})

# ================================================================ Sujet D : totalitarismes, Seconde Guerre mondiale, Shoah
SUJETS.append({
 "id": "hg-totalitarismes", "num": 5, "domaine": "hg", "titre": "Sujet D · Totalitarismes et guerre d’anéantissement",
 "theme": "Régimes totalitaires ; Seconde Guerre mondiale et Shoah ; mers et océans dans la mondialisation ; mémoire et commémorations",
 "parties": [
  H(5, "La Seconde Guerre mondiale, une guerre d’anéantissement", "",
    [Q("1", "histoire", 5, "Pourquoi peut-on dire que la Seconde Guerre mondiale est une guerre d’anéantissement ?" + METHODE_QC,
       """<p><strong>Introduction.</strong> De 1939 à 1945, la guerre oppose l’Axe (Allemagne nazie, Italie fasciste, Japon) aux Alliés (Royaume-Uni, puis URSS et États-Unis en 1941, France libre…). Elle fait plus de 60 millions de morts, dont une majorité de civils. Une guerre d’anéantissement vise à détruire totalement l’ennemi, y compris des peuples entiers.</p>
<p><strong>1. Une guerre idéologique menée par des régimes totalitaires.</strong> Le nazisme (Hitler chancelier le 30 janvier 1933) repose sur le racisme et l’antisémitisme (lois de Nuremberg, 1935 ; nuit de Cristal, 1938) et veut conquérir un « espace vital » à l’Est. À l’Est, la guerre contre l’URSS (à partir de juin 1941) est une guerre de destruction : massacres, famine organisée, prisonniers soviétiques laissés mourir.</p>
<p><strong>2. Le génocide des Juifs et des Tsiganes.</strong> Ghettos, fusillades de masse par les <em>Einsatzgruppen</em> (« Shoah par balles »), puis centres de mise à mort (Auschwitz-Birkenau, Treblinka, Sobibor…) après la conférence de Wannsee (janvier 1942) qui organise la « solution finale ». Environ 6 millions de Juifs sont assassinés, ainsi que des centaines de milliers de Tsiganes (Roms et Sinti).</p>
<p><strong>3. Des civils cibles de la guerre.</strong> Bombardements de villes (Londres, Dresde), crimes de guerre japonais, bombes atomiques sur Hiroshima et Nagasaki (6 et 9 août 1945).</p>
<p><strong>Conclusion.</strong> Le procès de Nuremberg (1945-1946) définit le crime contre l’humanité ; l’ONU est créée (1945) ; la Déclaration universelle des droits de l’homme est adoptée (1948). La mémoire de la Shoah est entretenue (27 janvier, libération d’Auschwitz ; Mémorial de la Shoah).</p>""")]),
  G(5, "Mers et océans au cœur de la mondialisation", cartes.monde_vierge(),
    [Q("2", "geographie", 5, "Montrer que les mers et les océans sont au cœur de la mondialisation. Réaliser un schéma localisant les principales routes maritimes, grands ports et détroits.",
       "<ul><li><strong>Des flux :</strong> environ 80 % du volume du commerce mondial de marchandises voyage par mer ; la conteneurisation (depuis les années 1960) et le gigantisme des navires ont fait baisser les coûts.</li><li><strong>Des routes et des passages stratégiques :</strong> la grande route est-ouest relie l’Asie orientale, l’Europe et l’Amérique du Nord par les détroits de Malacca, de Bab-el-Mandeb, le canal de Suez, Gibraltar, le Pas-de-Calais, et le canal de Panama ; ces passages sont fragiles (blocage du canal de Suez en 2021, attaques en mer Rouge).</li><li><strong>Des ports mondiaux :</strong> les plus grands ports à conteneurs sont en Asie (Shanghai, Singapour, Ningbo, Shenzhen, Busan) ; Rotterdam est le premier port européen ; en France, Le Havre (conteneurs) et Marseille-Fos.</li><li><strong>Des ressources et des enjeux :</strong> pêche, hydrocarbures offshore, câbles sous-marins (Internet) ; zones économiques exclusives (la France a la deuxième ZEE du monde grâce à ses outre-mer) ; pollution et protection des océans.</li></ul>" + cartes.carte_mondialisation_maritime())]),
  E(10, "Mémoire, commémorations et citoyenneté",
    doc(1, "Quelques journées nationales de commémoration", "<ul><li>27 janvier : journée de la mémoire des génocides et de la prévention des crimes contre l’humanité.</li><li>8 mai : victoire de 1945.</li><li>10 mai : journée nationale des mémoires de la traite, de l’esclavage et de leurs abolitions.</li><li>Dimanche le plus proche du 16 juillet : journée nationale à la mémoire des victimes des crimes racistes et antisémites de l’État français et d’hommage aux « Justes » de France.</li><li>11 novembre : armistice de 1918, hommage à tous les morts pour la France.</li></ul>"),
    [Q("1", "emc", 3, "Pourquoi la République organise-t-elle des commémorations ?",
       "<p>Pour honorer les victimes et ceux qui ont combattu ou résisté ; pour transmettre une histoire commune et les valeurs qu’elle a défendues (liberté, droits de l’homme) ; pour reconnaître les crimes commis, y compris par l’État (discours de 1995 sur le Vél d’Hiv ; loi Taubira de 2001 sur la traite) ; pour prévenir le retour du racisme, de l’antisémitisme et des crimes de masse. La mémoire n’est pas l’histoire : l’histoire établit les faits avec méthode, la mémoire est un rapport vivant et parfois conflictuel au passé.</p>"),
     Q("2", "emc", 3, "Qu’est-ce qu’un « Juste parmi les nations » ? En quoi ce titre peut-il servir de support à l’EMC ?",
       "<p>C’est le titre décerné par le mémorial Yad Vashem (Israël) à des non-Juifs qui ont sauvé des Juifs pendant la Shoah, au péril de leur vie. La France en compte plus de 4 000 (par exemple les habitants du Chambon-sur-Lignon). En EMC, ces figures montrent qu’il est possible de faire des choix moraux, de désobéir à des lois injustes, et que l’engagement individuel compte : on travaille l’empathie, le courage, la responsabilité.</p>"),
     Q("3", "emc", 4, "Comment préparer avec une classe de CM2 la participation à la cérémonie du 11 novembre ?",
       "<ol><li>Histoire : situer la Grande Guerre sur la frise, étudier des lettres de soldats, des photos, le monument aux morts de la commune (relever les noms, les dates, les âges).</li><li>EMC : réfléchir au sens d’une commémoration, aux symboles (drapeau, Marseillaise, minute de silence, dépôt de gerbe).</li><li>Engagement : lecture de lettres ou de noms par les élèves, chant de la Marseillaise, rencontre avec des élus ou des associations d’anciens combattants.</li><li>Prolongement : écriture d’un texte d’hommage ; réflexion sur la paix et la construction européenne.</li></ol>")]),
 ]})

# ================================================================ Sujet E : refonder la République 1944-1947
SUJETS.append({
 "id": "hg-refonder", "num": 6, "domaine": "hg", "titre": "Sujet E · Refonder la République (1944-1947)",
 "theme": "Résistance et Libération ; vote des femmes ; territoires ultramarins ; le vote et la démocratie",
 "parties": [
  H(5, "Refonder la République",
    doc(1, "Ordonnance du 21 avril 1944 portant organisation des pouvoirs publics en France après la Libération, article 17", cite("Les femmes sont électrices et éligibles dans les mêmes conditions que les hommes."))
    + doc(2, "Préambule de la Constitution du 27 octobre 1946 (extrait)", cite("La loi garantit à la femme, dans tous les domaines, des droits égaux à ceux de l’homme.")),
    [Q("1", "histoire", 5, "Comment la République est-elle refondée entre 1944 et 1947 ?" + METHODE_QC,
       """<p><strong>Introduction.</strong> La Résistance, intérieure et extérieure, a préparé l’après-guerre : le Conseil national de la Résistance (CNR), présidé par Jean Moulin (réunion du 27 mai 1943), adopte son programme le 15 mars 1944. Le Gouvernement provisoire de la République française (GPRF), dirigé par le général de Gaulle, s’installe à Paris libéré (25 août 1944).</p>
<p><strong>1. Rétablir la légalité républicaine.</strong> Le régime de Vichy est déclaré nul ; épuration (procès de Pétain et Laval) ; les femmes obtiennent le droit de vote et d’éligibilité (ordonnance du 21 avril 1944, doc. 1) et votent pour la première fois en avril-mai 1945.</p>
<p><strong>2. Une démocratie sociale.</strong> Programme du CNR : création de la <strong>Sécurité sociale</strong> (ordonnances d’octobre 1945), nationalisations (Renault, houillères, électricité et gaz, grandes banques), comités d’entreprise.</p>
<p><strong>3. De nouvelles institutions.</strong> Référendum d’octobre 1945 (fin de la IIIe République) ; Constitution de la IVe République adoptée par référendum en octobre 1946 ; son préambule proclame des droits économiques et sociaux (travail, santé, éducation) et l’égalité femmes-hommes (doc. 2).</p>
<p><strong>Conclusion.</strong> Ces refondations fondent le modèle social français. La IVe République, instable, laisse place à la Ve République en 1958 ; le préambule de 1946 reste en vigueur dans le bloc de constitutionnalité.</p>""")]),
  G(5, "Les territoires ultramarins", cartes.monde_vierge(),
    [Q("2", "geographie", 5, "Localiser les territoires ultramarins français et présenter leurs atouts et leurs contraintes.",
       "<p>La France ultramarine compte près de 3 millions d’habitants (dont environ 2,2 millions dans les cinq DROM), répartis dans trois océans : cinq départements et régions d’outre-mer (Guadeloupe, Martinique, Guyane, La Réunion, Mayotte depuis 2011) et des collectivités (Saint-Pierre-et-Miquelon, Saint-Martin, Saint-Barthélemy, Polynésie française, Wallis-et-Futuna), la Nouvelle-Calédonie (statut particulier) et les Terres australes et antarctiques françaises.</p><ul><li><strong>Atouts :</strong> une présence dans tous les océans et la deuxième zone économique exclusive du monde (plus de 10 millions de km²) ; biodiversité exceptionnelle ; tourisme ; base spatiale de Kourou (Guyane) ; ressources (nickel en Nouvelle-Calédonie).</li><li><strong>Contraintes :</strong> éloignement de la métropole et insularité (coûts de transport, vie chère) ; risques naturels (cyclones, séismes, volcans) ; chômage et pauvreté plus élevés, notamment à Mayotte et en Guyane ; dépendance aux importations.</li><li><strong>Aménagement :</strong> ce sont des régions ultrapériphériques de l’UE (fonds européens), avec des politiques de rattrapage (équipements, continuité territoriale).</li></ul>" + cartes.carte_outremer())]),
  E(10, "Le vote, fondement de la démocratie",
    doc(1, "Déclaration des droits de l’homme et du citoyen, 1789", ddhc(3, 6))
    + doc(2, "Constitution du 4 octobre 1958, article 3 (extraits)", cite("La souveraineté nationale appartient au peuple qui l’exerce par ses représentants et par la voie du référendum. […] Le suffrage peut être direct ou indirect dans les conditions prévues par la Constitution. Il est toujours universel, égal et secret. Sont électeurs, dans les conditions déterminées par la loi, tous les nationaux français majeurs des deux sexes, jouissant de leurs droits civils et politiques."))
    + doc(3, "Repères", "<ul><li>1848 : suffrage universel masculin.</li><li>1944 : droit de vote des femmes.</li><li>1974 : majorité et droit de vote à 18 ans.</li><li>Depuis 1992 (traité de Maastricht) : les citoyens de l’UE résidant en France votent aux élections municipales et européennes.</li></ul>"),
    [Q("1", "emc", 3, "À partir des documents, expliquer ce qu’est le suffrage universel et comment il s’est élargi.",
       "<p>Le suffrage universel est le droit de vote reconnu à tous les citoyens majeurs, sans condition de fortune ou d’instruction. Il est « universel, égal et secret » (doc. 2) : une personne, une voix, dans l’isoloir. Il s’est élargi par étapes : hommes en 1848 (après le suffrage censitaire), femmes en 1944, jeunes de 18 à 21 ans en 1974, citoyens européens aux élections locales et européennes. Il reste des exclusions : les étrangers non européens ne votent pas ; une peine peut priver du droit de vote.</p>"),
     Q("2", "emc", 3, "Pourquoi voter est-il à la fois un droit et un devoir civique ?",
       "<p>C’est un <strong>droit</strong> : par le vote, les citoyens exercent la souveraineté (doc. 1, art. 3 et 6), choisissent leurs représentants et participent à la loi. C’est un <strong>devoir civique</strong>, non obligatoire en France : voter fait vivre la démocratie et donne sa légitimité aux élus. L’abstention élevée fragilise la représentation. Il existe d’autres formes de participation : référendum, pétition, engagement associatif.</p>"),
     Q("3", "emc", 4, "Proposer une situation d’apprentissage au cycle 3 pour faire comprendre le vote et la démocratie aux élèves.",
       "<p>Organiser l’<strong>élection des délégués de classe</strong> ou du conseil d’enfants comme une vraie élection : candidatures et professions de foi, campagne respectueuse, liste d’émargement, isoloir, urne, dépouillement public, proclamation des résultats. Puis faire le lien avec les élections des adultes (mairie, carte d’électeur, isoloir), comparer avec des régimes sans élections libres (Vichy), et débattre : « Pourquoi le vote est-il secret ? » Évaluation : expliquer les principes du vote (universel, égal, secret) et le rôle d’un représentant.</p>")]),
 ]})

# ================================================================ Sujet F : traites, esclavage, colonisation
SUJETS.append({
 "id": "hg-esclavage", "num": 7, "domaine": "hg", "titre": "Sujet F · Traites, esclavage et abolitions",
 "theme": "Traite atlantique, abolitions (1794, 1848) et colonisation ; mobilités humaines transnationales ; lutte contre le racisme et les discriminations",
 "parties": [
  H(5, "Traites, esclavage et abolitions",
    doc(1, "Décret d’abolition de l’esclavage, 27 avril 1848 (extraits)", cite("Considérant que l’esclavage est un attentat contre la dignité humaine ; qu’en détruisant le libre arbitre de l’homme, il supprime le principe naturel du droit et du devoir ; qu’il est une violation flagrante du dogme républicain : Liberté, Égalité, Fraternité […]") + cite("Article 1er. L’esclavage sera entièrement aboli dans toutes les colonies et possessions françaises, deux mois après la promulgation du présent décret dans chacune d’elles. […]")),
    [Q("1", "histoire", 5, "Présenter la traite atlantique et les étapes de l’abolition de l’esclavage dans les colonies françaises." + METHODE_QC,
       """<p><strong>Introduction.</strong> Du XVIe au XIXe siècle, les Européens déportent des Africains réduits en esclavage vers les Amériques : c’est la traite atlantique (environ 12 millions de personnes déportées).</p>
<p><strong>1. Le commerce triangulaire.</strong> Des navires partent des ports européens (Nantes, premier port négrier français, Bordeaux, La Rochelle, Le Havre) avec des marchandises échangées en Afrique contre des captifs ; la traversée de l’Atlantique (« passage du milieu ») est meurtrière ; aux Antilles (Saint-Domingue, Martinique, Guadeloupe), les esclaves travaillent dans les plantations de canne à sucre, de café ; les navires rapportent ces produits en Europe. Le <strong>Code noir</strong> (1685) fait de l’esclave un bien meuble.</p>
<p><strong>2. Résistances et première abolition.</strong> Marronnage, révoltes (insurrection de Saint-Domingue en 1791, Toussaint Louverture) ; critiques des philosophes des Lumières et de la Société des amis des Noirs. La Convention abolit l’esclavage le <strong>4 février 1794</strong> ; Bonaparte le rétablit en 1802 ; Haïti devient indépendante en 1804.</p>
<p><strong>3. L’abolition définitive.</strong> Sous l’impulsion de <strong>Victor Schœlcher</strong>, le gouvernement provisoire de la IIe République abolit l’esclavage par le décret du <strong>27 avril 1848</strong> (doc. 1), au nom de la dignité humaine et des valeurs républicaines ; environ 250 000 esclaves sont libérés ; les propriétaires sont indemnisés, pas les anciens esclaves.</p>
<p><strong>Conclusion.</strong> La loi Taubira (21 mai 2001) reconnaît la traite et l’esclavage comme crimes contre l’humanité ; le 10 mai est une journée nationale de mémoire. L’abolition n’empêche pas l’expansion coloniale française au XIXe siècle (Algérie à partir de 1830, Afrique, Indochine).</p>""")]),
  G(5, "Les mobilités humaines transnationales", "",
    [Q("2", "geographie", 5, "Présenter les grandes caractéristiques des migrations internationales dans le monde et leurs causes.",
       "<ul><li><strong>Ampleur :</strong> environ 280 millions de migrants internationaux (ONU, 2020), soit environ 3,6 % de la population mondiale ; s’y ajoutent des flux touristiques de plus d’un milliard d’arrivées par an.</li><li><strong>Des flux variés :</strong> migrations de travail, regroupement familial, études, réfugiés et déplacés (guerres, persécutions ; plus de 100 millions de personnes déplacées de force dans le monde, dont une majorité à l’intérieur de leur pays), migrations environnementales.</li><li><strong>Des directions :</strong> une part importante des migrations se fait entre pays du Sud ; grands pôles d’accueil : États-Unis, Europe occidentale, pays du Golfe, Russie ; flux Amérique latine → États-Unis, Afrique → Europe, Asie du Sud → Golfe.</li><li><strong>Effets :</strong> transferts d’argent (remises) vers les pays de départ, fuite des cerveaux, main-d’œuvre pour les pays d’accueil ; frontières de plus en plus contrôlées (Méditerranée, frontière États-Unis-Mexique), routes migratoires dangereuses.</li></ul>" + cartes.carte_migrations())]),
  E(10, "Lutter contre le racisme et les discriminations",
    doc(1, "Constitution du 4 octobre 1958, article 1er (premier alinéa)", cite(CONST_1))
    + doc(2, "Code pénal, article 225-1 (début)", cite("Constitue une discrimination toute distinction opérée entre les personnes physiques sur le fondement de leur origine, de leur sexe, de leur situation de famille, de leur grossesse, de leur apparence physique, […] de leur état de santé, […] de leur handicap, […] de leur orientation sexuelle, de leur identité de genre, de leur âge, de leurs opinions politiques, de leurs activités syndicales, […] de leur appartenance ou de leur non-appartenance, vraie ou supposée, à une ethnie, une Nation, une prétendue race ou une religion déterminée.")),
    [Q("1", "emc", 3, "Distinguer préjugé, stéréotype, racisme et discrimination.",
       "<ul><li><strong>Stéréotype :</strong> image simplifiée et figée attribuée à tout un groupe (« les filles sont… »).</li><li><strong>Préjugé :</strong> jugement porté à l’avance, sans connaître la personne, souvent négatif.</li><li><strong>Racisme :</strong> idéologie qui prétend hiérarchiser des groupes humains (« races », qui n’ont aucune réalité biologique) et justifie le mépris ou la haine ; l’antisémitisme en est une forme.</li><li><strong>Discrimination :</strong> un acte, puni par la loi, qui consiste à traiter différemment une personne selon un critère interdit (doc. 2), par exemple refuser un logement ou un emploi.</li></ul>"),
     Q("2", "emc", 3, "Comment la loi protège-t-elle contre les discriminations ?",
       "<p>La Constitution garantit l’égalité devant la loi « sans distinction d’origine, de race ou de religion » (doc. 1). Le Code pénal définit plus de vingt critères de discrimination interdits (doc. 2) ; la discrimination, l’injure ou la provocation à la haine raciale sont des délits (lois de 1972 et 1990). Le <strong>Défenseur des droits</strong> peut être saisi gratuitement ; des associations accompagnent les victimes. À l’école, le règlement intérieur interdit toute discrimination et le harcèlement.</p>"),
     Q("3", "emc", 4, "Une insulte raciste a été entendue dans la cour. Comment réagir en tant qu’enseignant et quel travail mener ensuite avec la classe ?",
       "<p><strong>Réagir immédiatement :</strong> faire cesser l’insulte, protéger et écouter l’élève victime, rappeler la règle et la loi, informer la direction et les familles, appliquer une sanction éducative ; si les faits sont graves ou répétés, signalement selon les procédures (référent harcèlement, équipe de circonscription).</p><p><strong>Travailler ensuite :</strong> débat réglé ou discussion à visée philosophique sur les différences ; analyse d’albums de jeunesse ou d’affiches ; lien avec l’histoire (esclavage, Shoah) ; rappel de la Charte de la laïcité et des droits de l’enfant ; message final : l’égalité en dignité de tous les êtres humains (DDHC, art. 1er).</p>")]),
 ]})

# ================================================================ Sujet G : guerre froide et construction européenne
SUJETS.append({
 "id": "hg-guerre-froide", "num": 8, "domaine": "hg", "titre": "Sujet G · Le monde depuis 1945",
 "theme": "Guerre froide ; construction européenne ; ressources en eau ; défense et engagement",
 "parties": [
  H(5, "Un monde bipolaire", "",
    [Q("1", "histoire", 5, "Qu’est-ce que la guerre froide ? Présenter ses principales phases de 1947 à 1991." + METHODE_QC,
       """<p><strong>Introduction.</strong> La guerre froide est l’affrontement indirect, de 1947 à 1991, entre deux superpuissances et deux modèles : les États-Unis (démocratie libérale, capitalisme) et l’URSS (régime communiste, économie planifiée). Elle ne débouche pas sur un conflit direct entre eux, en raison notamment de la dissuasion nucléaire (« équilibre de la terreur »).</p>
<p><strong>1. La mise en place de deux blocs (1947-1953).</strong> Doctrine Truman et plan Marshall (1947) ; blocus de Berlin (1948-1949) ; création de deux États allemands (RFA, RDA) et de l’OTAN (1949) ; pacte de Varsovie (1955). Guerre de Corée (1950-1953). Le « rideau de fer » coupe l’Europe.</p>
<p><strong>2. Des crises et une coexistence pacifique (1953-1975).</strong> Construction du mur de Berlin (1961) ; crise des missiles de Cuba (1962), où le monde frôle la guerre nucléaire ; guerre du Vietnam ; téléphone rouge et premiers accords de limitation des armements.</p>
<p><strong>3. De la reprise des tensions à la fin (1975-1991).</strong> Invasion soviétique de l’Afghanistan (1979) ; réformes de Gorbatchev ; chute du mur de Berlin (9 novembre 1989) ; réunification allemande (1990) ; disparition de l’URSS (décembre 1991).</p>
<p><strong>Conclusion.</strong> La fin de la guerre froide ouvre une période dominée par les États-Unis, puis un monde multipolaire. En Europe, elle permet l’élargissement de l’Union européenne aux anciens pays de l’Est (2004, 2007).</p>""")]),
  G(5, "L’eau, une ressource à ménager", "",
    [Q("2", "geographie", 5, "Pourquoi l’accès à l’eau est-il un enjeu majeur ? Présenter les inégalités d’accès et des solutions pour gérer durablement la ressource.",
       "<ul><li><strong>Une ressource inégalement répartie :</strong> l’eau douce ne représente qu’environ 2,5 % de l’eau de la planète, en grande partie gelée ; les disponibilités varient selon les climats (régions arides du Sahel, du Moyen-Orient).</li><li><strong>Des inégalités d’accès :</strong> environ 2 milliards de personnes n’ont pas accès à une eau potable gérée en toute sécurité (OMS-UNICEF) ; conséquences sanitaires (maladies hydriques) et corvée d’eau souvent assurée par les femmes et les filles.</li><li><strong>Des usages en concurrence :</strong> l’agriculture (irrigation) représente environ 70 % des prélèvements mondiaux, puis l’industrie et les usages domestiques ; tensions entre États qui partagent un fleuve (Nil, Tigre et Euphrate).</li><li><strong>Des solutions :</strong> irrigation au goutte-à-goutte, lutte contre les fuites, recyclage des eaux usées, dessalement (coûteux en énergie), protection des nappes, tarification ; en France, gestion par bassins versants (agences de l’eau) et restrictions en période de sécheresse.</li></ul>")]),
  E(10, "La Défense et l’engagement des citoyens",
    doc(1, "Parcours de citoyenneté d’un jeune Français", "<ul><li>À 16 ans : recensement obligatoire à la mairie.</li><li>Avant 25 ans : Journée défense et citoyenneté (JDC), obligatoire pour s’inscrire aux examens et concours publics.</li><li>À 18 ans : inscription automatique sur les listes électorales.</li><li>De 16 à 25 ans (30 ans en situation de handicap) : possibilité d’un service civique, engagement volontaire indemnisé au service de l’intérêt général.</li></ul>")
    + doc(2, "Constitution du 4 octobre 1958, article 2", cite(CONST_2)),
    [Q("1", "emc", 3, "À quoi sert la Défense nationale aujourd’hui ?",
       "<p>Elle protège le territoire et la population, défend les intérêts de la France et participe à la sécurité internationale : dissuasion nucléaire, armées de terre, de l’air et de l’espace, marine ; opérations extérieures et missions de paix (ONU, OTAN, UE) ; protection du territoire (opération Sentinelle contre le terrorisme) ; aide aux populations lors de catastrophes. Le service militaire obligatoire a été suspendu en 1997 ; la défense repose sur une armée professionnelle et sur l’esprit de défense de tous les citoyens.</p>"),
     Q("2", "emc", 3, "À partir du document 1, montrer qu’il existe différentes formes d’engagement citoyen.",
       "<p>Obligations (recensement, JDC) et droits (vote) ; engagements volontaires : service civique, réserve militaire ou citoyenne, sapeurs-pompiers volontaires, associations (humanitaires, sportives, environnementales), bénévolat. À l’école, l’engagement commence tôt : délégués, conseil d’enfants, écodélégués, tutorat entre élèves.</p>"),
     Q("3", "emc", 4, "Comment faire découvrir les symboles de la République (doc. 2) à des élèves de cycle 2 ?",
       "<p>Partir de ce que les élèves voient (drapeau et devise au fronton de l’école, buste de Marianne à la mairie, pièces et timbres) ; apprendre et comprendre la Marseillaise (histoire du chant, sens simple de quelques paroles) ; expliquer le 14 juillet ; associer chaque symbole à une valeur (la devise : liberté, égalité, fraternité). Productions : affiche des symboles, visite de la mairie, participation à une commémoration.</p>")]),
 ]})

# ================================================================ Sujet H : Moyen Âge, monarchie, risques, justice
SUJETS.append({
 "id": "hg-moyen-age", "num": 9, "domaine": "hg", "titre": "Sujet H · Pouvoirs et sociétés du Moyen Âge à Louis XIV",
 "theme": "Société féodale, Église et pouvoir royal ; monarchie absolue ; risques et changement climatique ; la justice",
 "parties": [
  H(5, "Du roi féodal au roi absolu", "",
    [Q("1", "histoire", 5, "Comment le pouvoir royal s’affirme-t-il en France, des Capétiens à Louis XIV ?" + METHODE_QC,
       """<p><strong>Introduction.</strong> En 987, Hugues Capet est élu roi par les grands du royaume ; son pouvoir réel est alors limité à un petit domaine autour de Paris et d’Orléans. Sept siècles plus tard, Louis XIV gouverne en monarque absolu.</p>
<p><strong>1. Un roi dans la société féodale (XIe-XIIIe siècles).</strong> La société est organisée en seigneuries ; les liens d’homme à homme unissent le seigneur (suzerain) et son vassal, qui lui prête hommage en échange d’un fief. L’Église encadre la société (sacrements, clergé, monastères, cathédrales). Le roi, sacré à Reims, est au sommet de la pyramide féodale ; il agrandit le domaine royal (Philippe Auguste, victoire de Bouvines en 1214) et rend la justice (Saint Louis).</p>
<p><strong>2. Un État qui se renforce (XVIe siècle).</strong> François Ier impose le français dans les actes officiels (ordonnance de Villers-Cotterêts, 1539) ; après les guerres de Religion, Henri IV accorde l’édit de Nantes (1598), qui établit une tolérance religieuse.</p>
<p><strong>3. La monarchie absolue de Louis XIV (règne personnel 1661-1715).</strong> Monarchie de droit divin : le roi tient son pouvoir de Dieu et concentre tous les pouvoirs ; il s’appuie sur des ministres (Colbert), des intendants, une armée puissante ; il domestique la noblesse à Versailles (où la cour s’installe en 1682) ; il impose l’unité religieuse (révocation de l’édit de Nantes, 1685).</p>
<p><strong>Conclusion.</strong> Au XVIIIe siècle, les philosophes des Lumières (Montesquieu, Voltaire, Rousseau) critiquent l’absolutisme ; la Révolution de 1789 y met fin.</p>""")]),
  G(5, "Prévenir les risques, s’adapter au changement global", "",
    [Q("2", "geographie", 5, "Définir la notion de risque. À partir d’exemples, montrer comment les sociétés peuvent prévenir les risques et s’adapter au changement climatique.",
       "<ul><li><strong>Définitions :</strong> un <em>aléa</em> est un phénomène potentiellement dangereux (inondation, séisme, cyclone, accident industriel) ; les <em>enjeux</em> sont les personnes et les biens exposés ; la <em>vulnérabilité</em> est la fragilité d’une société face à l’aléa. Le risque naît de la rencontre d’un aléa et d’enjeux vulnérables. Les risques sont naturels, technologiques (Lubrizol à Rouen en 2019) ou sanitaires.</li><li><strong>Des inégalités :</strong> un même aléa fait beaucoup plus de victimes dans un pays pauvre (séisme d’Haïti en 2010) que dans un pays développé qui construit aux normes parasismiques (Japon).</li><li><strong>Prévenir :</strong> connaître et surveiller (Météo-France, vigilance crues), réglementer l’urbanisme (plans de prévention des risques), construire des ouvrages (digues), éduquer (plan particulier de mise en sûreté, PPMS, dans les écoles), alerter et secourir.</li><li><strong>S’adapter au changement climatique :</strong> le réchauffement (environ +1,1 °C depuis l’ère préindustrielle selon le GIEC) accroît les sécheresses, canicules, inondations et la montée du niveau de la mer ; on réduit les émissions (atténuation) et on s’adapte : végétaliser les villes, recul du trait de côte, gestion de l’eau, cultures adaptées.</li></ul>")]),
  E(10, "La justice en France",
    doc(1, "Déclaration des droits de l’homme et du citoyen, 1789, articles 7 à 9 (extraits)", cite("Art. 8. La Loi ne doit établir que des peines strictement et évidemment nécessaires […]") + cite("Art. 9. Tout homme étant présumé innocent jusqu’à ce qu’il ait été déclaré coupable, s’il est jugé indispensable de l’arrêter, toute rigueur qui ne serait pas nécessaire pour s’assurer de sa personne doit être sévèrement réprimée par la loi."))
    + doc(2, "Montesquieu, De l’esprit des lois, 1748, livre XI, chapitre 4 (extrait)", cite("Pour qu’on ne puisse abuser du pouvoir, il faut que, par la disposition des choses, le pouvoir arrête le pouvoir.")),
    [Q("1", "emc", 3, "Quels grands principes garantissent une justice équitable en France ?",
       "<p>Indépendance des juges par rapport aux pouvoirs exécutif et législatif (séparation des pouvoirs, doc. 2) ; <strong>présomption d’innocence</strong> (doc. 1, art. 9) ; droit à un avocat et droits de la défense ; procès public et contradictoire ; légalité des délits et des peines (on ne peut être puni que pour un acte prévu par la loi) et proportionnalité des peines (art. 8) ; droit de faire appel ; égalité de tous devant la justice. La peine de mort a été abolie en 1981 (loi Badinter).</p>"),
     Q("2", "emc", 3, "Présenter l’organisation de la justice et la justice des mineurs.",
       "<p>Deux ordres de juridictions : l’ordre <strong>judiciaire</strong> (litiges entre personnes : justice civile ; infractions : justice pénale, avec contraventions, délits et crimes jugés par la cour d’assises ou la cour criminelle), au sommet la Cour de cassation ; l’ordre <strong>administratif</strong> (litiges avec l’administration), au sommet le Conseil d’État. Les mineurs relèvent d’une justice spécialisée (juge des enfants, tribunal pour enfants) qui privilégie l’éducatif sur le répressif (code de la justice pénale des mineurs, 2021).</p>"),
     Q("3", "emc", 4, "Comment faire comprendre aux élèves la différence entre règle, sanction et punition, à partir de la vie de la classe ?",
       "<p>Élaborer ensemble les règles de vie de la classe (droits et devoirs), en les reliant au règlement de l’école et à la loi ; distinguer la <strong>punition</strong> (réponse à un manquement, mesure d’ordre intérieur) et la <strong>sanction</strong> éducative, proportionnée, expliquée, qui vise la réparation ; organiser un conseil d’élèves où l’on écoute chaque partie (comme dans un procès : entendre les deux versions) ; faire le lien avec la justice des adultes (présomption d’innocence, avocat, juge impartial). Débat : « Est-ce juste de punir toute la classe ? »</p>")]),
 ]})

# ================================================================ Sujet I : Ve République, femmes, espaces productifs, égalité
SUJETS.append({
 "id": "hg-cinquieme", "num": 10, "domaine": "hg", "titre": "Sujet I · La Ve République et l’évolution de la société",
 "theme": "La Ve République de de Gaulle à l’alternance ; la place des femmes ; les espaces productifs ; égalité filles-garçons et harcèlement",
 "parties": [
  H(5, "Femmes et hommes dans la société (1950-1980)", "",
    [Q("1", "histoire", 5, "Comment la place des femmes dans la société française évolue-t-elle des années 1940 aux années 1980 ?" + METHODE_QC,
       """<p><strong>Introduction.</strong> Citoyennes depuis 1944, les Françaises restent en 1950 juridiquement dépendantes de leur mari et peu présentes dans la vie publique.</p>
<p><strong>1. De nouveaux droits civils.</strong> Loi du 13 juillet 1965 : une femme mariée peut exercer une profession et ouvrir un compte bancaire sans l’autorisation de son mari ; autorité parentale partagée (1970) ; divorce par consentement mutuel (1975).</p>
<p><strong>2. Le droit de disposer de son corps.</strong> Loi Neuwirth autorisant la contraception (1967) ; mouvements féministes après 1968 (MLF, manifeste des 343 en 1971) ; loi Veil dépénalisant l’interruption volontaire de grossesse (17 janvier 1975), défendue par Simone Veil, ministre de la Santé.</p>
<p><strong>3. Travail, éducation et égalité.</strong> Mixité scolaire généralisée (loi Haby, 1975) ; hausse de l’activité féminine ; lois sur l’égalité salariale (1972) et professionnelle (loi Roudy, 1983) ; mais inégalités persistantes (salaires, tâches domestiques, faible présence en politique, d’où la révision constitutionnelle de 1999 et la loi sur la parité de 2000).</p>
<p><strong>Conclusion.</strong> En quelques décennies, l’égalité juridique progresse fortement ; l’égalité réelle reste un combat, que l’école accompagne (égalité filles-garçons, lutte contre les stéréotypes). Repères politiques de la période : Constitution de la Ve République (1958), élection du président au suffrage universel direct (réforme de 1962), alternance de 1981 (François Mitterrand).</p>""")]),
  G(5, "Les espaces productifs agricoles", "",
    [Q("2", "geographie", 5, "Présenter les espaces productifs agricoles français et leurs mutations.",
       "<ul><li><strong>Une grande puissance agricole :</strong> la France est le premier producteur agricole de l’Union européenne ; la surface agricole utilisée couvre environ la moitié du territoire ; l’agriculture emploie moins de 3 % des actifs.</li><li><strong>Des espaces spécialisés :</strong> grandes cultures céréalières du Bassin parisien (Beauce), élevage intensif en Bretagne, élevage extensif en montagne, vignobles (Bordelais, Champagne, Bourgogne), fruits et légumes dans le Sud-Est et la vallée du Rhône.</li><li><strong>Une agriculture intégrée à la mondialisation :</strong> exportations (céréales, vins et spiritueux), industries agroalimentaires, soutien de la politique agricole commune.</li><li><strong>Des mutations et des défis :</strong> baisse du nombre d’exploitations et agrandissement, pollution des sols et de l’eau (nitrates, pesticides), sécheresses ; développement de l’agriculture biologique, des circuits courts, des labels (AOP) et de l’agroécologie.</li></ul>")]),
  E(10, "L’égalité filles-garçons et la lutte contre le harcèlement",
    doc(1, "Code de l’éducation, article L. 511-3-1", cite("Aucun élève ne doit subir, de la part d’autres élèves, des faits de harcèlement ayant pour objet ou pour effet une dégradation de ses conditions d’apprentissage susceptible de porter atteinte à ses droits et à sa dignité ou d’altérer sa santé physique ou mentale."))
    + doc(2, "Observation d’une cour de récréation", "<p>Une enseignante observe que le terrain de football, au centre de la cour, est occupé presque uniquement par des garçons, tandis que les filles jouent sur les côtés. Un élève est régulièrement exclu des jeux et moqué sur son apparence depuis plusieurs semaines.</p>", "Situation décrite pour l’entraînement"),
    [Q("1", "emc", 3, "Qu’est-ce que le harcèlement scolaire ? Comment le distinguer d’un conflit ?",
       "<p>Le harcèlement est une violence <strong>répétée</strong>, verbale, physique, psychologique ou en ligne (cyberharcèlement), exercée par un ou plusieurs élèves contre un élève qui ne peut pas se défendre (rapport de force déséquilibré), avec un effet d’isolement. Un conflit est ponctuel et oppose des élèves à égalité. Depuis la loi du 2 mars 2022, le harcèlement scolaire est un délit. Le doc. 1 affirme le droit de chaque élève à une scolarité sans harcèlement.</p>"),
     Q("2", "emc", 3, "Quels dispositifs l’école met-elle en place contre le harcèlement ?",
       "<p>Le programme <strong>pHARe</strong> : formation des personnels, protocole de traitement des situations, élèves ambassadeurs, heures de sensibilisation ; le numéro national <strong>3018</strong> (harcèlement et cyberharcèlement) ; la journée nationale de lutte contre le harcèlement (en novembre) ; l’implication des familles ; des sanctions et un accompagnement de la victime, des auteurs et des témoins.</p>"),
     Q("3", "emc", 4, "À partir du document 2, proposer des actions pour favoriser l’égalité et le respect dans la cour et dans la classe.",
       "<p><strong>Pour l’élève harcelé :</strong> agir sans attendre (écoute, protection, protocole pHARe, information des familles), travail avec les témoins.</p><p><strong>Pour l’égalité :</strong> faire observer et cartographier la cour avec les élèves, puis débattre et co-construire un nouvel aménagement (tournante du terrain, zones calmes, jeux mixtes) ; répartir équitablement la parole et les responsabilités en classe ; travailler sur les stéréotypes (métiers, jouets, albums) ; valoriser des figures féminines en histoire et en sciences. Évaluer : observer de nouveau la cour quelques semaines plus tard.</p>")]),
 ]})

# ================================================================ Sujet J : cycle 3, des Gaulois à Charlemagne
SUJETS.append({
 "id": "hg-antiquite", "num": 11, "domaine": "hg", "titre": "Sujet J · Les temps anciens (cycle 3)",
 "theme": "Préhistoire, Gaule romaine, Clovis et Charlemagne ; la question démographique ; la devise républicaine",
 "remarque": "Le programme du concours est celui du cycle 4, mais les notions des cycles 1 à 3 sont exigibles : ce sujet reprend les repères du cycle 3.",
 "parties": [
  H(5, "Des Gaulois aux Carolingiens", "",
    [Q("1", "histoire", 5, "Présenter les grandes étapes de l’histoire du territoire de la France de la Gaule celtique à l’empire de Charlemagne." + METHODE_QC,
       """<p><strong>1. Avant la Gaule.</strong> Les premiers humains occupent le territoire depuis plus d’un million d’années ; art pariétal (grotte Chauvet, vers 36 000 ans ; Lascaux, vers 18 000 ans) ; au Néolithique, sédentarisation, agriculture, élevage (mégalithes de Carnac).</p>
<p><strong>2. La Gaule celtique puis romaine.</strong> Des peuples gaulois divisés, une civilisation rurale et artisanale (oppida). Conquête par Jules César (58-51 av. J.-C.) ; défaite de Vercingétorix à <strong>Alésia</strong> (52 av. J.-C.). Romanisation : villes (Lutèce, Nîmes, Lyon/Lugdunum), routes, aqueducs (pont du Gard), latin, citoyenneté romaine ; christianisation progressive (IIIe-IVe siècles).</p>
<p><strong>3. Les royaumes francs.</strong> Après la chute de l’Empire romain d’Occident (476), les Francs dominent : <strong>Clovis</strong>, roi des Francs, se fait baptiser à Reims (vers 496-499), ce qui lui vaut le soutien de l’Église. <strong>Charlemagne</strong>, roi des Francs, est couronné empereur à Rome le <strong>25 décembre 800</strong> ; il administre son empire avec les comtes et les missi dominici et favorise l’école et la copie des manuscrits.</p>
<p><strong>Conclusion.</strong> Le partage de l’empire (traité de Verdun, 843) donne naissance à la Francie occidentale, ancêtre du royaume de France. Au cycle 3, on insiste sur les traces du passé et sur le mythe des « ancêtres gaulois », construit au XIXe siècle.</p>""")]),
  G(5, "La question démographique", "",
    [Q("2", "geographie", 5, "Comment la population mondiale évolue-t-elle et quels défis cette évolution pose-t-elle ?",
       "<ul><li><strong>Une croissance très rapide puis qui ralentit :</strong> environ 1 milliard d’humains vers 1800, 2,5 milliards en 1950, 8 milliards en 2022 ; la croissance ralentit car la fécondité baisse (environ 2,3 enfants par femme en moyenne mondiale).</li><li><strong>La transition démographique :</strong> passage de taux de natalité et de mortalité élevés à des taux faibles ; la mortalité baisse d’abord (progrès de la médecine, de l’hygiène), puis la natalité ; entre les deux, la population augmente fortement.</li><li><strong>Des situations contrastées :</strong> vieillissement en Europe et au Japon ; population jeune et croissance forte en Afrique subsaharienne ; l’Inde est devenue le pays le plus peuplé devant la Chine (2023).</li><li><strong>Des défis :</strong> nourrir, loger, scolariser, soigner, créer des emplois ; financer les retraites dans les pays vieillissants ; pressions sur les ressources et l’environnement.</li></ul>")]),
  E(10, "Liberté, égalité, fraternité",
    doc(1, "Constitution du 4 octobre 1958, article 2", cite(CONST_2))
    + doc(2, "Déclaration des droits de l’homme et du citoyen, 1789", ddhc(1)),
    [Q("1", "emc", 3, "Expliquer le sens de chacun des trois termes de la devise républicaine.",
       "<ul><li><strong>Liberté :</strong> pouvoir faire tout ce qui ne nuit pas à autrui (DDHC, art. 4) ; libertés de conscience, d’expression, de réunion, d’aller et venir, dans le respect de la loi.</li><li><strong>Égalité :</strong> tous égaux en droits et devant la loi (DDHC, art. 1er), sans distinction d’origine, de sexe ou de religion ; égalité des chances.</li><li><strong>Fraternité :</strong> solidarité et entraide entre les membres de la Nation (Sécurité sociale, aide aux plus fragiles) ; le Conseil constitutionnel a reconnu en 2018 la valeur constitutionnelle du principe de fraternité.</li></ul>"),
     Q("2", "emc", 3, "Quand et comment la devise s’est-elle imposée ?",
       "<p>Née pendant la Révolution française, elle est inscrite dans la Constitution de 1848 (IIe République), puis s’impose sous la IIIe République : elle est gravée au fronton des bâtiments publics à partir de 1880, en même temps que le 14 juillet devient fête nationale. Le régime de Vichy la remplace par « Travail, Famille, Patrie ». Elle figure dans les Constitutions de 1946 et 1958 (doc. 1). Depuis la loi pour une école de la confiance (2019), le drapeau tricolore, le drapeau européen, la devise et les paroles de l’hymne national sont affichés dans chaque salle de classe.</p>"),
     Q("3", "emc", 4, "Proposer une activité de cycle 2 ou 3 qui fasse vivre la fraternité à l’école.",
       "<p>Exemples : tutorat entre élèves de cycles différents ; conseil d’élèves qui décide d’un projet solidaire (collecte pour une association, correspondance avec des résidents d’une maison de retraite) ; jeux coopératifs en EPS ; discussion à visée philosophique « Qu’est-ce qu’être frères et sœurs quand on n’est pas de la même famille ? » ; trace écrite illustrée des trois mots de la devise avec des situations vécues. Lien avec la « semaine de l’engagement » et les valeurs de la République.</p>")]),
 ]})

# ================================================================ Banque de repères (entraînement rapide)
def R(id, type, q, r):
    return Q(id, type, 1, q, f"<p class='answer'>{r}</p>")

REPERES = [
 ("Temps anciens et Moyen Âge", [
   R("1", "reperes", "Quand et où Vercingétorix est-il vaincu par Jules César ?", "À Alésia, en 52 av. J.-C."),
   R("2", "reperes", "Quelle date retient-on pour le baptême de Clovis ?", "Vers 496-499 (on retient souvent 496), à Reims."),
   R("3", "reperes", "Quand Charlemagne est-il couronné empereur ?", "Le 25 décembre 800, à Rome."),
   R("4", "reperes", "Qui devient roi en 987 et commence quelle dynastie ?", "Hugues Capet : les Capétiens."),
   R("5", "reperes", "Définir la féodalité, le vassal et le fief.", "Organisation fondée sur des liens d’homme à homme : le vassal prête hommage et fidélité à un seigneur (suzerain), qui lui concède une terre, le fief, et sa protection."),
   R("6", "reperes", "En quelle année est fondé l’islam (hégire) ?", "622 : départ de Mahomet de La Mecque pour Médine (début du calendrier musulman)."),
 ]),
 ("Temps modernes", [
   R("7", "reperes", "Que décide l’ordonnance de Villers-Cotterêts (1539) ?", "François Ier impose le français dans les actes officiels et de justice (et crée l’enregistrement des baptêmes)."),
   R("8", "reperes", "Qu’est-ce que l’édit de Nantes et quand est-il révoqué ?", "Édit de tolérance signé par Henri IV en 1598 (liberté de culte limitée pour les protestants), révoqué par Louis XIV en 1685."),
   R("9", "reperes", "Définir la monarchie absolue de droit divin.", "Un régime où le roi, qui tient son pouvoir de Dieu, concentre tous les pouvoirs (faire la loi, gouverner, juger) sans contrôle ; exemple : Louis XIV (1661-1715)."),
   R("10", "reperes", "Citer trois philosophes des Lumières et une idée de chacun.", "Montesquieu (séparation des pouvoirs), Voltaire (tolérance, lutte contre le fanatisme), Rousseau (souveraineté du peuple, contrat social) ; aussi Diderot et d’Alembert (l’Encyclopédie)."),
   R("11", "reperes", "1492 : quel événement ?", "Christophe Colomb atteint l’Amérique (les Bahamas) pour les souverains espagnols."),
   R("12", "reperes", "Qu’est-ce que le commerce triangulaire ?", "Un commerce entre l’Europe, l’Afrique et l’Amérique : marchandises vers l’Afrique, captifs africains réduits en esclavage vers l’Amérique, produits tropicaux (sucre, café) vers l’Europe."),
 ]),
 ("Révolution et XIXe siècle", [
   R("13", "reperes", "Donner les dates du 14 juillet 1789, du 4 août 1789 et du 26 août 1789.", "Prise de la Bastille ; abolition des privilèges ; Déclaration des droits de l’homme et du citoyen."),
   R("14", "reperes", "Quand la République est-elle proclamée pour la première fois ?", "Le 21-22 septembre 1792."),
   R("15", "reperes", "Qu’est-ce que le Code civil de 1804 ?", "Un code de lois voulu par Napoléon Bonaparte, qui unifie le droit (égalité devant la loi, propriété) mais soumet la femme mariée à son mari."),
   R("16", "reperes", "Quand le suffrage universel masculin est-il établi ?", "En 1848 (IIe République), la même année que l’abolition définitive de l’esclavage (27 avril 1848)."),
   R("17", "reperes", "Que prévoient les lois Ferry de 1881-1882 ?", "École primaire gratuite (1881), obligatoire de 6 à 13 ans et laïque (1882)."),
   R("18", "reperes", "Quelle est la date de la loi de séparation des Églises et de l’État ?", "Le 9 décembre 1905."),
   R("19", "reperes", "Qu’est-ce que l’affaire Dreyfus ?", "La condamnation injuste (1894) du capitaine juif Alfred Dreyfus pour espionnage, qui divise la France (« J’accuse » de Zola, 1898) ; il est réhabilité en 1906."),
   R("20", "reperes", "Qu’est-ce que l’exode rural ?", "Le départ massif des habitants des campagnes vers les villes, notamment lors de l’industrialisation au XIXe siècle."),
 ]),
 ("XXe siècle", [
   R("21", "reperes", "Dates de la Première Guerre mondiale et de la bataille de Verdun ?", "1914-1918 (armistice le 11 novembre 1918) ; Verdun : février-décembre 1916."),
   R("22", "reperes", "Définir le totalitarisme et citer deux exemples.", "Un régime qui contrôle tous les aspects de la vie (parti unique, chef, propagande, terreur, embrigadement) : l’URSS de Staline, l’Allemagne nazie d’Hitler (et, dans une certaine mesure, l’Italie de Mussolini)."),
   R("23", "reperes", "Donner les dates de l’armistice de 1940, des pleins pouvoirs à Pétain et de l’appel du général de Gaulle.", "Appel du 18 juin 1940 ; armistice signé le 22 juin 1940 ; pleins pouvoirs votés le 10 juillet 1940."),
   R("24", "reperes", "Qu’est-ce que la rafle du Vél d’Hiv ?", "L’arrestation par la police française de plus de 13 000 Juifs à Paris, les 16 et 17 juillet 1942, avant leur déportation."),
   R("25", "reperes", "Définir la Shoah et le génocide.", "Un génocide est l’extermination organisée d’un peuple parce qu’il est ce qu’il est ; la Shoah est le génocide d’environ 6 millions de Juifs par les nazis et leurs complices."),
   R("26", "reperes", "Qui est Jean Moulin ?", "Représentant du général de Gaulle, il unifie la Résistance intérieure et préside la première réunion du Conseil national de la Résistance (27 mai 1943) ; arrêté, il meurt en 1943."),
   R("27", "reperes", "Quand les femmes obtiennent-elles le droit de vote en France ?", "Par l’ordonnance du 21 avril 1944 ; premier vote en 1945."),
   R("28", "reperes", "Quand la Ve République est-elle fondée ?", "Constitution du 4 octobre 1958 ; élection du président au suffrage universel direct depuis la réforme de 1962 (première élection en 1965)."),
   R("29", "reperes", "Dates de la construction et de la chute du mur de Berlin ?", "Construit en août 1961, il tombe le 9 novembre 1989."),
   R("30", "reperes", "Quelles sont les grandes dates de la construction européenne ?", "Déclaration Schuman (9 mai 1950), CECA (1951), traités de Rome (1957), traité de Maastricht (1992), euro fiduciaire (2002), UE à 27 depuis 2020."),
   R("31", "reperes", "Qu’est-ce que la décolonisation ? Citer deux exemples.", "L’accès à l’indépendance des colonies après 1945 : l’Inde (1947, de façon non violente), l’Algérie (1962, après une guerre de 1954 à 1962)."),
   R("32", "reperes", "Que change la loi Veil de 1975 ?", "Elle dépénalise l’interruption volontaire de grossesse (IVG)."),
 ]),
 ("Géographie", [
   R("33", "geographie", "Combien d’habitants compte la France et quelle est sa densité moyenne ?", "Environ 68 millions d’habitants (dont environ 66 millions en métropole) ; environ 120 hab./km² en métropole."),
   R("34", "geographie", "Qu’est-ce que la métropolisation ?", "La concentration des populations, des activités et des fonctions de commandement dans les grandes villes."),
   R("35", "geographie", "Qu’est-ce que la périurbanisation ?", "L’extension des villes sur les espaces ruraux voisins, sous forme de lotissements et de zones d’activités, liée à l’usage de la voiture."),
   R("36", "geographie", "Définir l’IDH.", "Indice de développement humain (PNUD, 1990) qui combine espérance de vie, éducation et revenu par habitant ; il varie de 0 à 1."),
   R("37", "geographie", "Qu’est-ce que la mondialisation ?", "La mise en relation de toutes les parties du monde par des flux (marchandises, capitaux, personnes, informations) de plus en plus nombreux et rapides."),
   R("38", "geographie", "Qu’est-ce qu’une ZEE et quel est le rang de la France ?", "Zone économique exclusive : espace maritime jusqu’à 200 milles marins des côtes où l’État exploite les ressources ; la France a la 2e ZEE du monde grâce à ses outre-mer."),
   R("39", "geographie", "Citer les cinq DROM.", "Guadeloupe, Martinique, Guyane, La Réunion, Mayotte."),
   R("40", "geographie", "Définir aléa, vulnérabilité et risque.", "L’aléa est le phénomène dangereux ; la vulnérabilité, la fragilité de la société exposée ; le risque, la probabilité qu’un aléa touche des enjeux vulnérables."),
   R("41", "geographie", "Qu’est-ce que le développement durable ?", "Un développement qui répond aux besoins du présent sans compromettre ceux des générations futures (rapport Brundtland, 1987), en conciliant économie, société et environnement."),
   R("42", "geographie", "Citer les principaux massifs montagneux de France métropolitaine.", "Alpes, Pyrénées, Massif central, Jura, Vosges (et la Corse)."),
   R("43", "geographie", "Citer les grands fleuves de France.", "La Seine, la Loire, la Garonne, le Rhône (et le Rhin à la frontière est)."),
   R("44", "geographie", "Qu’est-ce que la transition démographique ?", "Le passage d’une natalité et d’une mortalité élevées à une natalité et une mortalité faibles, avec entre les deux une forte croissance de la population."),
 ]),
 ("EMC", [
   R("45", "emc", "Quelles sont les trois valeurs de la devise et les symboles de la République ?", "Liberté, Égalité, Fraternité ; drapeau tricolore, Marseillaise, Marianne, 14 juillet (article 2 de la Constitution)."),
   R("46", "emc", "Définir la laïcité en une phrase.", "Principe qui garantit la liberté de conscience et l’égalité de tous quelles que soient les croyances, par la séparation des Églises et de l’État et la neutralité des services publics."),
   R("47", "emc", "Qui détient le pouvoir législatif, exécutif et judiciaire en France ?", "Législatif : le Parlement (Assemblée nationale, 577 députés ; Sénat, 348 sénateurs). Exécutif : le président de la République et le gouvernement. Judiciaire : les magistrats."),
   R("48", "emc", "Quelle est la durée du mandat présidentiel et depuis quand ?", "Cinq ans (quinquennat), depuis le référendum de 2000 (appliqué en 2002)."),
   R("49", "emc", "Quand a été adoptée la Convention internationale des droits de l’enfant ?", "Le 20 novembre 1989, par l’ONU."),
   R("50", "emc", "Quel est le numéro pour l’enfance en danger ? Et contre le harcèlement ?", "Le 119 ; le 3018 pour le harcèlement et le cyberharcèlement."),
   R("51", "emc", "Qu’est-ce que la présomption d’innocence ?", "Toute personne est considérée comme innocente tant que sa culpabilité n’a pas été établie par un jugement (DDHC, art. 9)."),
   R("52", "emc", "Qu’est-ce que le Défenseur des droits ?", "Une autorité indépendante (créée en 2011) qui défend les droits des usagers, des enfants, lutte contre les discriminations et protège les lanceurs d’alerte ; elle peut être saisie gratuitement."),
   R("53", "emc", "Qu’est-ce que la citoyenneté européenne ?", "Créée par le traité de Maastricht (1992), elle s’ajoute à la citoyenneté nationale : liberté de circuler et de s’installer dans l’UE, droit de vote aux élections municipales et européennes dans le pays de résidence."),
   R("54", "emc", "Quelle différence entre discrimination et préjugé ?", "Le préjugé est une opinion ; la discrimination est un acte (traitement différent selon un critère interdit), puni par la loi."),
 ]),
]
SUJETS.append({
 "id": "hg-reperes", "num": 12, "domaine": "hg", "titre": "Repères et définitions · histoire-géo-EMC",
 "theme": "54 questions flash : dates, personnages, notions de géographie, institutions et valeurs",
 "entrainement": True,
 "remarque": "Entraînement rapide : réponds de tête, puis vérifie. Chaque question vaut 1 point ; la note ne compte pas pour le concours.",
 "parties": [P(f"R{i+1}", titre, f"R{i+1}", "", float(len(qs)), "", qs) for i, (titre, qs) in enumerate(REPERES)],
})

# ================================================================ Guide « ce qui peut tomber »
GUIDE = """
<p>Le programme de la 2e épreuve en histoire-géographie-EMC est celui du <strong>cycle 4</strong> (5e, 4e, 3e) en vigueur, et le jury attend aussi la maîtrise des notions des cycles 1 à 3. En 2026, la session BAC+3 (groupement 1) a posé : une question de cours d’histoire sur le régime de Vichy (5 points), une carte de la répartition de la population française (5 points) et un dossier d’EMC sur l’égalité à l’école (10 points). Le sujet 0 posait une question sur les inégalités de développement, une sur la séparation des pouvoirs et la laïcité, et une étude de documents sur la ville industrielle au XIXe siècle. <strong>N’importe quel thème du programme peut donc tomber.</strong></p>
<h4>Histoire (cycle 4, avec les repères du cycle 3)</h4>
<ul>
<li><strong>5e :</strong> chrétientés et islam (VIe-XIIIe s.) ; la société féodale, l’Église et le pouvoir royal ; Renaissance, Réformes, grandes découvertes ; du prince de la Renaissance au roi absolu (François Ier, Henri IV, Louis XIV). <em>Sujet H</em></li>
<li><strong>4e :</strong> les Lumières ; la traite atlantique ; la Révolution française et l’Empire ; l’industrialisation ; la conquête coloniale ; voter de 1815 à 1870 ; la IIIe République ; la condition des femmes au XIXe s. <em>Sujets B, C, F, sujet 0</em></li>
<li><strong>3e :</strong> la Première Guerre mondiale ; démocraties fragilisées et totalitarismes ; la Seconde Guerre mondiale, guerre d’anéantissement ; <strong>la France défaite et occupée : Vichy, collaboration, Résistance</strong> ; la guerre froide ; la décolonisation ; la construction européenne ; refonder la République (1944-1947) ; la Ve République ; femmes et hommes dans la société (1950-1980). <em>Sujets A, D, E, G, I, session 2026</em></li>
<li><strong>Cycle 3 :</strong> Préhistoire, Gaule, Clovis, Charlemagne, rois de France, Révolution, école de Ferry, âge industriel, guerres mondiales. <em>Sujet J</em></li>
</ul>
<h4>Géographie</h4>
<ul>
<li><strong>5e :</strong> la question démographique et l’inégal développement ; des ressources limitées (énergie, eau, alimentation) ; prévenir les risques, s’adapter au changement global. <em>Sujets G, H, J, sujet 0</em></li>
<li><strong>4e :</strong> l’urbanisation du monde ; les mobilités humaines transnationales ; mers et océans, espaces transformés par la mondialisation. <em>Sujets D, F</em></li>
<li><strong>3e :</strong> les aires urbaines ; les espaces productifs ; les espaces de faible densité ; aménager le territoire ; les territoires ultramarins ; la France et l’Union européenne. <em>Sujets A, B, C, E, I, session 2026</em></li>
<li><strong>Savoir-faire :</strong> réaliser une carte ou un croquis (titre, légende organisée, figurés adaptés, nomenclature), lire une carte, analyser un paysage, localiser les grands repères (fleuves, massifs, métropoles, DROM, États de l’UE).</li>
</ul>
<h4>EMC</h4>
<ul>
<li>Les valeurs et symboles de la République ; la laïcité ; la citoyenneté et le vote ; les institutions et la séparation des pouvoirs ; la justice ; la Défense et l’engagement.</li>
<li>Les droits de l’enfant ; l’égalité filles-garçons ; la lutte contre le racisme, l’antisémitisme et les discriminations ; le harcèlement.</li>
<li>La liberté d’expression et l’éducation aux médias ; la mémoire et les commémorations ; le développement durable et le bien commun.</li>
<li>Format fréquent : un dossier de textes officiels (DDHC, Constitution, lois, Code de l’éducation) et des questions allant de la définition à la mise en œuvre en classe.</li>
</ul>
<h4>Conseils de méthode</h4>
<ul>
<li>Toujours <strong>définir les notions</strong> de la question et donner des <strong>dates précises</strong>.</li>
<li>Structurer : introduction courte, deux ou trois parties, conclusion ; citer les documents quand il y en a.</li>
<li>En EMC, relier les principes aux textes (DDHC, Constitution, lois) et à la vie de l’école.</li>
<li>Utiliser l’onglet « S’entraîner par type » pour réviser toutes les questions d’histoire, de géographie ou d’EMC d’affilée, et la banque de repères pour les dates.</li>
</ul>"""
