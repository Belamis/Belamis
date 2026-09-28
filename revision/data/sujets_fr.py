# -*- coding: utf-8 -*-
# Sujets de français (CRPE BAC+3, 1re épreuve, partie A) : questions + corrigés.
# Lancer : python3 data/sujets_fr.py  (régénère data/francais.js)
# Les textes viennent de extraits.json (Wikisource) ; la Barbe bleue vient du sujet 0 officiel.
# Balisage : [[mot]] = mot souligné dans l'énoncé.
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ex = json.load(open(os.path.join(HERE, "extraits.json")))
ex = {k: re.sub(r"[  ]{2,}", " ", v) for k, v in ex.items()}

BARBE = """Il revint de son voyage dès le soir même, et dit qu’il avait reçu des lettres dans le chemin, qui lui avaient appris que l’affaire pour laquelle il était parti venait d’être terminée à son avantage. Sa femme fit tout ce qu’elle put pour lui témoigner qu’elle était ravie de son prompt retour. Le lendemain, il lui redemanda les clefs, et elle les lui donna, mais d’une main si tremblante qu’il devina sans peine tout ce qui s’était passé. « D’où vient, lui dit-il, que la clef du cabinet n’est point avec les autres ? – Il faut, dit-elle, que je l’aie laissée là-haut sur ma table. – Ne manquez pas, dit-il, de me la donner tantôt. » Après plusieurs remises, il fallut apporter la clef. La Barbe bleue, l’ayant considérée, dit à sa femme : « Pourquoi y a-t-il du sang sur cette clef ? – Je n’en sais rien, répondit la pauvre femme, plus pâle que la mort. – Vous n’en savez rien ? reprit la Barbe bleue ; je le sais bien, moi ! Vous avez voulu entrer dans le cabinet ? Hé bien, Madame, vous y entrerez, et irez prendre votre place auprès des dames que vous y avez vues. » Elle se jeta aux pieds de son mari, en pleurant et en lui demandant pardon, avec toutes les marques d’un vrai repentir de n’avoir pas été obéissante.
Elle aurait attendri un rocher, belle et affligée comme elle était ; mais la Barbe bleue avait le cœur plus dur qu’un rocher. « Il faut mourir, Madame, et tout à l’heure*. – Puisqu’il faut mourir, répondit-elle en le regardant les yeux baignés de larmes, donnez-moi un peu de temps pour prier Dieu. – Je vous donne un demi-quart d’heure, mais pas un instant davantage. » Lorsqu’elle fut seule, elle appela sa sœur et lui dit : « Ma sœur Anne (car elle s’appelait ainsi), monte, je te prie, sur le haut de la tour, pour voir si mes frères ne viennent point ; ils m’ont promis qu’ils me viendraient voir aujourd’hui, et si tu les vois, fais-leur signe de se hâter. » La sœur Anne monta sur le haut de la tour, et la pauvre affligée lui criait de temps en temps : « Anne, ma sœur Anne, ne vois-tu rien venir ? »"""

def paras(s):
    return [p.strip() for p in s.split("\n") if p.strip()]

A1 = "Étude de la langue (syntaxe, grammaire, orthographe)"
A2 = "Lexique et compréhension lexicale"
A3 = "Expression écrite (réflexion argumentée)"

CRITERES_A3 = """<p><strong>Ce que le jury attend (critères de réussite)</strong></p>
<ul>
<li>Une <strong>introduction</strong> qui présente le texte (auteur, œuvre, date, situation de l’extrait), pose la problématique et annonce le plan.</li>
<li>Un <strong>développement structuré</strong> en deux ou trois parties, chacune avec une idée directrice, des arguments et des <strong>exemples précis tirés du texte</strong> (citations courtes) et de la culture personnelle.</li>
<li>Une <strong>conclusion</strong> qui répond clairement à la question et peut ouvrir la réflexion (par exemple vers l’école).</li>
<li>Une langue <strong>correcte et soignée</strong> : orthographe, syntaxe, connecteurs logiques, vocabulaire précis. Environ une trentaine de lignes.</li>
</ul>"""

SUJETS = []

# ---------------------------------------------------------------- Sujet 0
SUJETS.append({
 "id": "barbe-bleue", "num": 0, "officiel": True,
 "auteur": "Charles Perrault", "oeuvre": "La Barbe bleue", "date": "1697", "genre": "Conte",
 "theme": "L’égalité entre les femmes et les hommes",
 "contexte": "Sujet 0 officiel du CRPE BAC+3 (juin 2025). La Barbe bleue a interdit à sa femme d’ouvrir un cabinet ; elle a désobéi et y a découvert les corps de ses précédentes épouses.",
 "texte": paras(BARBE),
 "notes": ["* <em>Tout à l’heure</em> signifie <em>sur-le-champ</em> en français du XVIIe siècle.", "Par rapport au sujet officiel, la ponctuation du dialogue est rétablie et « que je l’ai laissée » est corrigé en « que je l’aie laissée » (subjonctif après <em>il faut que</em>)."],
 "parties": [
  {"id": "A1", "titre": A1, "points": 6, "questions": [
   {"id": "1", "type": "reecriture", "points": 1.5,
    "enonce": "Récrire le passage suivant en mettant les sujets des verbes au pluriel.",
    "passage": "« Il revint de son voyage dès le soir même, et dit qu’il avait reçu des lettres dans le chemin, qui lui avaient appris que l’affaire pour laquelle il était parti venait d’être terminée à son avantage. »",
    "corrige": """<p class="answer">« <strong>Ils revinrent</strong> de <strong>leur</strong> voyage dès le soir même, et <strong>dirent</strong> qu’<strong>ils avaient</strong> reçu des lettres dans le chemin, qui <strong>leur</strong> avaient appris que <strong>les affaires</strong> pour <strong>lesquelles ils étaient partis venaient</strong> d’être <strong>terminées</strong> à <strong>leur</strong> avantage. »</p>
<p><strong>Points de vigilance</strong></p>
<ul>
<li>Passé simple au pluriel : <em>revinrent</em>, <em>dirent</em> (et non « revenèrent », « dîmes »).</li>
<li>« qui lui avaient appris » : le sujet <em>qui</em> (mis pour <em>des lettres</em>) est déjà au pluriel ; seul le pronom <em>lui</em> devient <em>leur</em>.</li>
<li>Accord du participe passé avec <em>être</em> : <em>ils étaient partis</em>, <em>les affaires venaient d’être terminées</em>.</li>
<li>Le pronom relatif s’accorde avec son antécédent : <em>pour lesquelles</em>.</li>
<li>Les déterminants possessifs suivent : <em>leur voyage</em>, <em>leur avantage</em> (<em>leurs voyages</em> est aussi accepté).</li>
</ul>"""},
   {"id": "2", "type": "nature", "points": 1.5,
    "enonce": "Donner la nature des six mots soulignés. Justifier les réponses.",
    "passage": "« Le lendemain, il [[lui]] redemanda les clefs, et elle [[les]] lui donna, mais d’une main si tremblante qu’il devina sans peine tout ce qui s’était passé. « D’où vient, lui dit-il, que [[la]] clef du cabinet n’est point avec les autres ? – Il faut, dit-elle, que je l’aie laissée là-haut sur [[ma]] table. – Ne manquez pas, dit-il, de me [[la]] donner tantôt. » […] « Pourquoi y a-t-il [[du]] sang sur cette clef ? »",
    "corrige": """<ul>
<li><strong>lui</strong> (il lui redemanda) : <strong>pronom personnel</strong> de 3e personne du singulier ; il remplace « à sa femme » et est complément d’objet second (COS) de <em>redemanda</em>.</li>
<li><strong>les</strong> (elle les lui donna) : <strong>pronom personnel</strong> ; placé devant le verbe, il remplace « les clefs » (COD de <em>donna</em>).</li>
<li><strong>la</strong> (la clef du cabinet) : <strong>déterminant</strong> (article défini) ; il introduit le nom <em>clef</em>.</li>
<li><strong>la</strong> (me la donner) : <strong>pronom personnel</strong> ; placé devant le verbe, il remplace « la clef » (COD de <em>donner</em>).</li>
<li><strong>ma</strong> (ma table) : <strong>déterminant possessif</strong> (1re personne du singulier) ; il introduit le nom <em>table</em>.</li>
<li><strong>du</strong> (du sang) : <strong>déterminant (article partitif)</strong> ; il désigne une quantité indéterminée d’une réalité non comptable (<em>du sang</em> ≠ <em>le sang</em>). Ce n’est pas ici la contraction de « de + le ».</li>
</ul>
<p><strong>Méthode :</strong> un déterminant introduit un nom, avec lequel il forme un groupe nominal (un adjectif peut s’intercaler : <em>la belle clef</em>). Un pronom se substitue à un groupe nominal et en prend la fonction. Les pronoms personnels compléments se placent devant le verbe, sauf à l’impératif affirmatif (<em>donnez-la</em>).</p>"""},
   {"id": "3a", "type": "fonction", "points": 1,
    "enonce": "En vous fondant sur la phrase <em>Le facteur distribue le courrier tous les matins</em>, citer les deux caractéristiques syntaxiques majeures des compléments circonstanciels.",
    "corrige": """<ul>
<li><strong>Ils sont supprimables</strong> : <em>Le facteur distribue le courrier.</em> La phrase reste correcte et garde son sens de base.</li>
<li><strong>Ils sont déplaçables</strong> : <em>Tous les matins, le facteur distribue le courrier.</em></li>
</ul>
<p>À l’inverse, le COD <em>le courrier</em> ne peut ni être déplacé en tête de phrase ni être supprimé sans changer la construction du verbe. Dans la terminologie grammaticale de 2020, on parle de <strong>complément de phrase</strong>.</p>"""},
   {"id": "3b", "type": "fonction", "points": 1,
    "enonce": "Identifier les compléments circonstanciels présents dans la phrase suivante. Donner pour chacun d’eux la nuance de sens exprimée.",
    "passage": "« Puisqu’il faut mourir, répondit-elle en le regardant les yeux baignés de larmes, donnez-moi un peu de temps pour prier Dieu. »",
    "corrige": """<ul>
<li><strong>Puisqu’il faut mourir</strong> : proposition subordonnée conjonctive circonstancielle de <strong>cause</strong> (introduite par <em>puisque</em>, cause présentée comme évidente).</li>
<li><strong>en le regardant</strong> : gérondif, complément circonstanciel de <strong>manière</strong> et de <strong>simultanéité</strong> (temps) de <em>répondit</em>.</li>
<li><strong>les yeux baignés de larmes</strong> : construction absolue (groupe nominal suivi d’un participe), complément circonstanciel de <strong>manière</strong>.</li>
<li><strong>pour prier Dieu</strong> : groupe infinitif prépositionnel, complément circonstanciel de <strong>but</strong>.</li>
</ul>
<p>Attention : <em>un peu de temps</em> est COD de <em>donnez</em>, ce n’est pas un complément circonstanciel.</p>"""},
   {"id": "4", "type": "propositions", "points": 1,
    "enonce": "Donner la nature et la fonction des deux propositions suivantes introduites par <em>si</em>.",
    "passage": "« [monte] pour voir si mes frères ne viennent point » ; « et si tu les vois, fais-leur signe de se hâter »",
    "corrige": """<ul>
<li><strong>si mes frères ne viennent point</strong> : proposition subordonnée <strong>interrogative indirecte</strong> (on peut la transformer en question directe : « Mes frères ne viennent-ils point ? »). Elle est <strong>COD</strong> du verbe <em>voir</em>.</li>
<li><strong>si tu les vois</strong> : proposition subordonnée conjonctive <strong>circonstancielle de condition</strong> (hypothèse). Elle est <strong>complément circonstanciel</strong> (complément de phrase) de <em>fais-leur signe</em> ; elle est déplaçable et supprimable.</li>
</ul>"""},
  ]},
  {"id": "A2", "titre": A2, "points": 4, "questions": [
   {"id": "1a", "type": "formation", "points": 1,
    "enonce": "Analyser la formation du verbe <em>redemander</em> et préciser, dans cet emploi, le sens du préfixe <em>re-</em>.",
    "corrige": """<p><em>Redemander</em> est formé par <strong>dérivation préfixale</strong> : préfixe <strong>re-</strong> + base verbale <strong>demander</strong>.</p>
<p>Dans ce contexte, le préfixe exprime le <strong>retour</strong> à une situation antérieure : la Barbe bleue avait confié les clefs à sa femme avant de partir, il les réclame à son retour (demander <em>en retour</em>). <em>Redemander</em> signifie ici « demander que l’on rende ce que l’on a confié ». L’idée de simple répétition (demander une seconde fois) est moins pertinente : c’est la première fois qu’il réclame les clefs.</p>"""},
   {"id": "1b", "type": "formation", "points": 1,
    "enonce": "Citer d’autres mots de votre choix présentant des orthographes différentes pour ce même préfixe.",
    "corrige": """<ul>
<li><strong>re-</strong> : refaire, relire, repartir</li>
<li><strong>ré-</strong> (devant une voyelle) : réécrire, réapparaître, réunir</li>
<li><strong>r-</strong> (devant une voyelle) : rouvrir, rapporter, ravoir</li>
<li><strong>res-</strong> (devant un <em>s</em>, pour garder le son [s]) : ressortir, ressaisir, ressembler</li>
</ul>"""},
   {"id": "2", "type": "commentaire-lexical", "points": 2,
    "enonce": "Commenter, depuis « Je n’en sais rien » jusqu’à « belle et affligée comme elle était », le choix du vocabulaire caractérisant la femme de la Barbe bleue.",
    "corrige": """<p>Le vocabulaire fait de l’épouse une <strong>victime pathétique</strong>, soumise et culpabilisée :</p>
<ul>
<li><strong>La peur et la souffrance</strong> : « la pauvre femme » (<em>pauvre</em> antéposé = digne de pitié), « plus pâle que la mort » (comparaison hyperbolique), « en pleurant », « affligée ».</li>
<li><strong>La soumission et la faute</strong> : « se jeta aux pieds de son mari », « demandant pardon », « vrai repentir », « n’avoir pas été obéissante ». C’est un lexique moral et religieux : la curiosité de la femme est présentée comme une faute qu’elle doit expier.</li>
<li><strong>La beauté</strong> : « belle et affligée » associe la beauté et la douleur. L’hyperbole « Elle aurait attendri un rocher » prépare l’opposition avec le mari, qui a « le cœur plus dur qu’un rocher ».</li>
</ul>
<p>Ce vocabulaire met en scène un rapport de domination : l’épouse n’a d’autre recours que la supplication.</p>"""},
  ]},
  {"id": "A3", "titre": A3, "points": 10, "questions": [
   {"id": "1", "type": "expression", "points": 10,
    "enonce": "Qu’est-ce qui rend cette page d’un conte du XVIIe siècle toujours significative dans le cadre d’une réflexion sur l’égalité entre homme et femme ? Votre réponse prendra la forme d’un développement structuré et argumenté d’une trentaine de lignes.",
    "corrige": """<p><strong>Problématique possible :</strong> en quoi ce conte, qui met en scène une épouse menacée pour avoir désobéi, éclaire-t-il encore les mécanismes de domination entre les femmes et les hommes ?</p>
<p><strong>Plan possible</strong></p>
<ol>
<li><strong>Un rapport de domination et de peur.</strong> Le mari contrôle l’espace (les clefs, le cabinet interdit), le temps (« un demi-quart d’heure ») et la vie de sa femme. Elle est réduite à la supplication (« se jeta aux pieds »). On peut y lire une figure des violences conjugales et de l’emprise.</li>
<li><strong>Une femme accusée plutôt que protégée.</strong> Le texte présente sa curiosité comme une faute (« repentir », « obéissante ») alors que le criminel est le mari. La morale de Perrault vise d’ailleurs la curiosité féminine. Ce renversement de la culpabilité reste un sujet d’actualité.</li>
<li><strong>Une héroïne qui trouve des ressources.</strong> Elle gagne du temps, fait appel à sa sœur Anne et à ses frères : la solidarité la sauve. Le conte peut aujourd’hui servir à parler, avec des élèves, de l’égalité, du respect et du droit de demander de l’aide.</li>
</ol>
""" + CRITERES_A3},
  ]},
 ]})

# ---------------------------------------------------------------- Sujet 1 : Daudet
SUJETS.append({
 "id": "derniere-classe", "num": 1,
 "auteur": "Alphonse Daudet", "oeuvre": "La Dernière Classe (Contes du lundi)", "date": "1872 (recueil 1873)", "genre": "Nouvelle",
 "theme": "L’école, la langue et l’identité",
 "contexte": "Après la défaite de 1870, l’Alsace est annexée par l’Allemagne. Le jeune Franz arrive en retard à l’école le jour où M. Hamel, son maître, donne sa dernière leçon de français.",
 "texte": paras(ex["daudet"]), "notes": [],
 "parties": [
  {"id": "A1", "titre": A1, "points": 6, "questions": [
   {"id": "1", "type": "reecriture", "points": 2,
    "enonce": "Récrire le passage suivant en remplaçant « je » par « nous » (Franz et son camarade). Faire toutes les modifications nécessaires.",
    "passage": "« J’en étais là de mes réflexions, quand j’entendis appeler mon nom. C’était mon tour de réciter. […] mais je m’embrouillai aux premiers mots, et je restai debout à me balancer dans mon banc, le cœur gros, sans oser lever la tête. »",
    "corrige": """<p class="answer">« <strong>Nous en étions</strong> là de <strong>nos</strong> réflexions, quand <strong>nous entendîmes</strong> appeler <strong>nos noms</strong>. C’était <strong>notre</strong> tour de réciter. […] mais <strong>nous nous embrouillâmes</strong> aux premiers mots, et <strong>nous restâmes</strong> debout à <strong>nous</strong> balancer dans <strong>notre banc</strong>, le cœur gros, sans oser lever la tête. »</p>
<p><strong>Points de vigilance</strong></p>
<ul>
<li>Passé simple, 1re personne du pluriel, avec l’<strong>accent circonflexe</strong> : <em>entendîmes</em>, <em>embrouillâmes</em>, <em>restâmes</em>.</li>
<li>Verbe pronominal : <em>nous nous embrouillâmes</em> ; infinitif pronominal : <em>à nous balancer</em>.</li>
<li>Possessifs : <em>nos réflexions</em>, <em>nos noms</em>, <em>notre tour</em>. « Notre banc » (un banc partagé) ou « nos bancs » sont acceptés.</li>
<li>« le cœur gros » et « la tête » peuvent rester au singulier (singulier distributif : chacun a un cœur, une tête).</li>
</ul>"""},
   {"id": "2", "type": "fonction", "points": 2,
    "enonce": "Donner la nature et la fonction des mots et groupes de mots soulignés, puis celles de l’adjectif <em>instruits</em>.",
    "passage": "« Je ne [[te]] gronderai pas, [[mon petit Franz]], tu dois être assez puni… » ; « Vos parents n’ont pas assez tenu [[à vous voir instruits]]. »",
    "corrige": """<ul>
<li><strong>te</strong> : pronom personnel (2e personne du singulier), <strong>COD</strong> du verbe <em>gronderai</em>.</li>
<li><strong>mon petit Franz</strong> : groupe nominal (déterminant + adjectif + nom propre), sa fonction est l’<strong>apostrophe</strong> : il désigne l’interlocuteur et ne dépend syntaxiquement d’aucun autre constituant de la phrase.</li>
<li><strong>à vous voir instruits</strong> : groupe infinitif introduit par la préposition <em>à</em>, <strong>COI</strong> du verbe <em>tenir</em> (tenir <em>à</em> quelque chose).</li>
<li><strong>instruits</strong> : participe passé employé comme adjectif, <strong>attribut du COD</strong> <em>vous</em> (vous voir instruits → vous êtes instruits). Il s’accorde avec <em>vous</em>, masculin pluriel.</li>
</ul>"""},
   {"id": "3", "type": "temps", "points": 1,
    "enonce": "Identifier le temps et le mode de la forme verbale soulignée, puis expliquer sa valeur dans ce contexte.",
    "passage": "« Que [[n’aurais-je pas donné]] pour pouvoir dire tout au long cette fameuse règle des participes, bien haut, bien clair, sans une faute ! »",
    "corrige": """<p><em>N’aurais-je pas donné</em> : verbe <em>donner</em> au <strong>conditionnel passé</strong> (mode conditionnel, ou indicatif selon les grammaires récentes), 1re personne du singulier, à la forme négative, avec inversion du sujet.</p>
<p><strong>Valeur :</strong> <strong>irréel du passé</strong>. Franz exprime un <strong>regret</strong> : il aurait tout donné pour savoir sa leçon, mais c’est trop tard. La tournure exclamative (« Que… ! ») renforce l’intensité du regret.</p>"""},
   {"id": "4", "type": "propositions", "points": 1,
    "enonce": "Donner la nature et la fonction des propositions introduites par <em>parce que</em>, <em>quand</em> et <em>tant que</em>.",
    "passage": "« [il fallait la garder entre nous et ne jamais l’oublier,] parce que, quand un peuple tombe esclave, tant qu’il tient bien sa langue, c’est comme s’il tenait la clef de sa prison… »",
    "corrige": """<ul>
<li><strong>parce que […] c’est comme s’il tenait la clef de sa prison</strong> : proposition subordonnée conjonctive <strong>circonstancielle de cause</strong>, complément circonstanciel de <em>il fallait la garder</em>.</li>
<li><strong>quand un peuple tombe esclave</strong> : proposition subordonnée conjonctive <strong>circonstancielle de temps</strong>, complément circonstanciel de <em>c’est</em>.</li>
<li><strong>tant qu’il tient bien sa langue</strong> : proposition subordonnée conjonctive <strong>circonstancielle de temps</strong> (durée : « aussi longtemps que »), avec une nuance de <strong>condition</strong>, complément circonstanciel de <em>c’est</em>.</li>
</ul>
<p>On remarque l’<strong>enchâssement</strong> : les subordonnées de temps sont à l’intérieur de la subordonnée de cause.</p>"""},
  ]},
  {"id": "A2", "titre": A2, "points": 4, "questions": [
   {"id": "1", "type": "sens", "points": 1.5,
    "enonce": "Donner deux mots de la même famille que <em>instruction</em>. Préciser le sens de ce mot dans « le grand malheur de notre Alsace de toujours remettre son instruction à demain », puis citer un autre sens de <em>instruction</em>.",
    "corrige": """<ul>
<li><strong>Famille</strong> : instruire, instruit, instructeur, instructif, s’instruire.</li>
<li><strong>Sens dans le texte</strong> : le fait d’<strong>acquérir des connaissances</strong>, l’éducation reçue à l’école (s’instruire).</li>
<li><strong>Autres sens</strong> : les <em>instructions</em> (consignes, ordres donnés) ; l’<em>instruction</em> judiciaire (phase d’enquête d’un procès, le juge d’instruction) ; en informatique, une instruction de programme.</li>
</ul>
<p>C’est un mot <strong>polysémique</strong> : le contexte permet de choisir le bon sens.</p>"""},
   {"id": "2", "type": "formation", "points": 1,
    "enonce": "Analyser la formation des mots <em>filatures</em> et <em>(s’)embrouiller</em>.",
    "corrige": """<ul>
<li><strong>filature</strong> : base verbale <em>fil(er)</em> + suffixe nominal <strong>-ature</strong>. Le suffixe forme un nom désignant l’<strong>action</strong> (filer la laine, le coton) puis le <strong>lieu</strong> où elle se fait : l’usine où l’on file.</li>
<li><strong>embrouiller</strong> : préfixe <strong>em-</strong> (forme de <em>en-</em> devant <em>b</em>, <em>m</em>, <em>p</em>) + base verbale <em>brouiller</em>. Le préfixe indique l’entrée dans un état : se retrouver dans la confusion.</li>
</ul>"""},
   {"id": "3", "type": "commentaire-lexical", "points": 1.5,
    "enonce": "Commenter le vocabulaire employé par M. Hamel pour parler de la langue française, depuis « Alors, d’une chose à l’autre » jusqu’à « la clef de sa prison ».",
    "corrige": """<ul>
<li><strong>Un éloge</strong> : trois superlatifs en gradation, « la plus belle langue du monde, la plus claire, la plus solide ». La langue est à la fois esthétique, intellectuelle et solide comme un rempart.</li>
<li><strong>Un devoir de mémoire</strong> : « la garder entre nous », « ne jamais l’oublier ». La langue devient un trésor commun qu’il faut protéger.</li>
<li><strong>Une métaphore de la liberté</strong> : « quand un peuple tombe esclave […] c’est comme s’il tenait la clef de sa prison ». Le champ lexical de l’enfermement (esclave, prison) s’oppose à la clef : parler sa langue, c’est garder la possibilité de se libérer.</li>
</ul>
<p>La langue est ainsi présentée comme le cœur de l’<strong>identité</strong> d’un peuple.</p>"""},
  ]},
  {"id": "A3", "titre": A3, "points": 10, "questions": [
   {"id": "1", "type": "expression", "points": 10,
    "enonce": "Écrite au lendemain de la guerre de 1870, cette page invite-t-elle encore aujourd’hui à réfléchir au rôle de l’école et de la langue dans la construction d’une identité ? Votre réponse prendra la forme d’un développement structuré et argumenté d’une trentaine de lignes.",
    "corrige": """<p><strong>Problématique possible :</strong> au-delà du contexte patriotique de 1870, que nous dit ce texte du lien entre l’école, la maîtrise de la langue et le sentiment d’appartenance ?</p>
<p><strong>Plan possible</strong></p>
<ol>
<li><strong>Un texte de circonstance, patriotique.</strong> Daudet écrit après l’annexion de l’Alsace-Moselle : la langue française devient un symbole national (« la plus belle langue du monde » ; dans la suite de la nouvelle, les modèles d’écriture portent « France, Alsace »). Le maître incarne la patrie qui s’en va.</li>
<li><strong>Une réflexion toujours actuelle sur la langue et l’école.</strong> Maîtriser la langue, c’est pouvoir comprendre, s’exprimer, se défendre : c’est une condition de la liberté (« la clef de sa prison »). Le texte rappelle aussi la responsabilité partagée de l’éducation : parents, élèves et maître (« Nous avons tous notre bonne part de reproches à nous faire »).</li>
<li><strong>Des nuances nécessaires.</strong> L’Alsace avait aussi sa langue régionale, que l’école française a longtemps combattue. Aujourd’hui, l’école valorise le plurilinguisme (langues vivantes, langues régionales, langues des familles) : une identité peut être plurielle. Le texte peut être étudié en classe pour parler d’histoire, de langue et de citoyenneté.</li>
</ol>
""" + CRITERES_A3},
  ]},
 ]})

# ---------------------------------------------------------------- Sujet 2 : Hugo
SUJETS.append({
 "id": "cosette", "num": 2,
 "auteur": "Victor Hugo", "oeuvre": "Les Misérables, tome II « Cosette »", "date": "1862", "genre": "Roman",
 "theme": "L’enfance maltraitée et la protection de l’enfant",
 "contexte": "Un soir de Noël, à Montfermeil, la petite Cosette (8 ans), exploitée par les aubergistes Thénardier, est envoyée seule dans la nuit chercher un seau d’eau à la source du bois.",
 "texte": paras(ex["hugo"]), "notes": [],
 "parties": [
  {"id": "A1", "titre": A1, "points": 6, "questions": [
   {"id": "1", "type": "reecriture", "points": 2,
    "enonce": "Récrire le passage suivant au présent de l’indicatif, en remplaçant « elle » par « les deux enfants » (deux fillettes). Faire toutes les modifications nécessaires.",
    "passage": "« Tant qu’elle eut des maisons et même seulement des murs des deux côtés de son chemin, elle alla assez hardiment. De temps en temps, elle voyait le rayonnement d’une chandelle à travers la fente d’un volet, c’était de la lumière et de la vie, il y avait là des gens, cela la rassurait. »",
    "corrige": """<p class="answer">« Tant que <strong>les deux enfants ont</strong> des maisons et même seulement des murs des deux côtés de <strong>leur</strong> chemin, <strong>elles vont</strong> assez hardiment. De temps en temps, <strong>elles voient</strong> le rayonnement d’une chandelle à travers la fente d’un volet, <strong>c’est</strong> de la lumière et de la vie, il y <strong>a</strong> là des gens, cela <strong>les rassure</strong>. »</p>
<p><strong>Points de vigilance</strong></p>
<ul>
<li>Deux transformations à mener ensemble : le <strong>temps</strong> (passé simple et imparfait → présent) et la <strong>personne</strong> (singulier → pluriel).</li>
<li>Verbes irréguliers : <em>ont</em>, <em>vont</em>, <em>voient</em>.</li>
<li>Les verbes impersonnels ou au sujet neutre restent au singulier : <em>c’est</em>, <em>il y a</em>, <em>cela les rassure</em>.</li>
<li>Pronoms et possessifs : <em>la</em> → <em>les</em>, <em>son chemin</em> → <em>leur chemin</em>. On peut dire « elles » après la première mention.</li>
</ul>"""},
   {"id": "2", "type": "temps", "points": 1.5,
    "enonce": "Relever les verbes conjugués du passage suivant, identifier leur temps et expliquer l’emploi de chacun.",
    "passage": "« Quand elle eut passé l’angle de la dernière maison, Cosette s’arrêta. Aller au delà de la dernière boutique avait été difficile ; aller plus loin que la dernière maison, cela devenait impossible. Elle posa le seau à terre, plongea sa main dans ses cheveux… »",
    "corrige": """<ul>
<li><strong>eut passé</strong> : <strong>passé antérieur</strong>. Dans une subordonnée de temps, il marque une action achevée juste <strong>avant</strong> une action au passé simple (<em>s’arrêta</em>).</li>
<li><strong>s’arrêta, posa, plongea</strong> : <strong>passé simple</strong>. Il présente les actions de <strong>premier plan</strong>, ponctuelles et successives, qui font avancer le récit.</li>
<li><strong>avait été</strong> : <strong>plus-que-parfait</strong>. Il marque l’<strong>antériorité</strong> par rapport au moment du récit (l’étape déjà franchie).</li>
<li><strong>devenait</strong> : <strong>imparfait</strong>. Il exprime une action en cours, un <strong>arrière-plan</strong> : l’état d’esprit de Cosette, dont on ne voit ni le début ni la fin.</li>
</ul>"""},
   {"id": "3", "type": "fonction", "points": 1.5,
    "enonce": "Donner la nature et la fonction des groupes soulignés.",
    "passage": "« Elle regarda [[avec désespoir]] [[cette obscurité]] [[où il n’y avait plus personne]], […] »",
    "corrige": """<ul>
<li><strong>avec désespoir</strong> : groupe prépositionnel (préposition + nom), <strong>complément circonstanciel de manière</strong> du verbe <em>regarda</em>.</li>
<li><strong>cette obscurité</strong> : groupe nominal, <strong>COD</strong> du verbe <em>regarda</em>.</li>
<li><strong>où il n’y avait plus personne</strong> : proposition subordonnée <strong>relative</strong>, introduite par le pronom relatif <em>où</em> ; elle est <strong>complément de l’antécédent</strong> <em>obscurité</em> (expansion du nom). Dans la relative, <em>où</em> est complément de lieu.</li>
</ul>"""},
   {"id": "4", "type": "phrase", "points": 1,
    "enonce": "Identifier le type des phrases suivantes et le mode des verbes. Quel est l’effet produit ?",
    "passage": "« Que faire ? que devenir ? où aller ? »",
    "corrige": """<p>Ce sont trois <strong>phrases interrogatives partielles</strong> (introduites par <em>que</em>, <em>où</em>), construites avec des verbes à l’<strong>infinitif</strong> (infinitif délibératif).</p>
<p><strong>Effet :</strong> les pensées de Cosette sont rapportées sans verbe introducteur ni guillemets (discours indirect libre ou discours direct libre : l’infinitif, sans marque de personne ni de temps, ne permet pas de trancher). Le rythme ternaire, bref et haché, traduit le <strong>désarroi</strong> et l’impossibilité de choisir : l’enfant est prise entre deux peurs.</p>"""},
  ]},
  {"id": "A2", "titre": A2, "points": 4, "questions": [
   {"id": "1", "type": "formation", "points": 1.5,
    "enonce": "Analyser la formation des mots <em>ressaisit</em> et <em>machinalement</em>, puis donner leur sens dans le texte.",
    "corrige": """<ul>
<li><strong>ressaisir</strong> : préfixe <strong>re-</strong> (écrit <em>res-</em> devant <em>s</em> pour garder le son [s]) + <em>saisir</em>. Le préfixe marque la <strong>répétition</strong> ou le retour : Cosette reprend le seau qu’elle avait posé.</li>
<li><strong>machinalement</strong> : nom <em>machine</em> → adjectif <em>machinal</em> (suffixe <strong>-al</strong>) → adverbe <em>machinalement</em> (suffixe <strong>-ment</strong>, adverbe de manière). Sens : sans y penser, de façon automatique, comme une machine.</li>
</ul>"""},
   {"id": "2", "type": "sens", "points": 1,
    "enonce": "Expliquer le sens de l’adjectif <em>éperdue</em> dans « Elle allait devant elle, éperdue » et proposer deux synonymes.",
    "corrige": """<p><em>Éperdue</em> : bouleversée par une émotion violente (ici la peur), au point de perdre la maîtrise de soi. <strong>Synonymes</strong> : affolée, égarée, paniquée, hors d’elle.</p>"""},
   {"id": "3", "type": "commentaire-lexical", "points": 1.5,
    "enonce": "Commenter le vocabulaire qui oppose la petitesse de Cosette à ce qui l’entoure et la menace.",
    "corrige": """<ul>
<li><strong>La petitesse et la fragilité</strong> : « l’enfant », « ce petit être », « un atome », des gestes d’enfant (« se gratter lentement la tête »).</li>
<li><strong>L’immensité et le danger</strong> : « l’espace noir et désert », « l’immense nuit », « toute l’ombre », le « frémissement nocturne de la forêt » qui « l’enveloppait tout entière ».</li>
<li><strong>Le surnaturel et le monstrueux</strong>, vus par les yeux de l’enfant : « revenants », « fantômes », « spectre » ; la Thénardier est animalisée (« bouche d’hyène »).</li>
<li><strong>L’antithèse finale</strong> « D’un côté, toute l’ombre ; de l’autre, un atome » résume le texte : un enfant seul face à un monde écrasant. Hugo suscite la pitié du lecteur.</li>
</ul>"""},
  ]},
  {"id": "A3", "titre": A3, "points": 10, "questions": [
   {"id": "1", "type": "expression", "points": 10,
    "enonce": "En quoi cette page, qui montre une enfant exploitée et livrée à elle-même, peut-elle nourrir aujourd’hui la réflexion sur la protection de l’enfance ? Votre réponse prendra la forme d’un développement structuré et argumenté d’une trentaine de lignes.",
    "corrige": """<p><strong>Problématique possible :</strong> comment un roman du XIXe siècle peut-il faire prendre conscience de la vulnérabilité de l’enfant et de la responsabilité des adultes ?</p>
<p><strong>Plan possible</strong></p>
<ol>
<li><strong>Un tableau saisissant de l’enfance maltraitée.</strong> Travail imposé à une enfant de 8 ans, peur, solitude, maltraitance psychologique (la terreur que lui inspire la Thénardier). Hugo adopte le point de vue de l’enfant pour faire ressentir sa détresse.</li>
<li><strong>Un roman engagé.</strong> Hugo dénonce la misère et l’indifférence de la société (la femme qui la croise ne fait rien). Il a défendu l’instruction gratuite et obligatoire ; la littérature devient un levier pour changer les consciences.</li>
<li><strong>Un écho actuel.</strong> Convention internationale des droits de l’enfant (1989), travail des enfants encore présent dans le monde, maltraitances. Le professeur des écoles a un rôle de vigilance : repérer les signes, écouter, signaler (numéro 119, information préoccupante). Le texte peut aussi être lu en classe pour aborder les droits de l’enfant.</li>
</ol>
""" + CRITERES_A3},
  ]},
 ]})

# ---------------------------------------------------------------- Sujet 3 : Maupassant
SUJETS.append({
 "id": "la-parure", "num": 3,
 "auteur": "Guy de Maupassant", "oeuvre": "La Parure (Contes du jour et de la nuit)", "date": "1884 (recueil 1885)", "genre": "Nouvelle",
 "theme": "Le désir, les apparences et la comparaison sociale",
 "contexte": "Début de la nouvelle : portrait de Mathilde Loisel, épouse d’un petit employé du ministère, qui rêve d’une vie de luxe.",
 "texte": paras(ex["maupassant"]), "notes": [],
 "parties": [
  {"id": "A1", "titre": A1, "points": 6, "questions": [
   {"id": "1", "type": "reecriture", "points": 2,
    "enonce": "a) Récrire le passage suivant en remplaçant « elle » par « elles ». Faire toutes les modifications nécessaires. b) Identifier le mode et le temps de <em>eût désiré</em> et en donner la valeur.",
    "passage": "« Elle n’avait pas de toilettes, pas de bijoux, rien. Et elle n’aimait que cela ; elle se sentait faite pour cela. Elle eût tant désiré plaire, être enviée, être séduisante et recherchée. »",
    "corrige": """<p class="answer">a) « <strong>Elles n’avaient</strong> pas de toilettes, pas de bijoux, rien. Et <strong>elles n’aimaient</strong> que cela ; <strong>elles se sentaient faites</strong> pour cela. <strong>Elles eussent</strong> tant désiré plaire, être <strong>enviées</strong>, être <strong>séduisantes</strong> et <strong>recherchées</strong>. »</p>
<ul>
<li>Accords au féminin pluriel : <em>faites</em>, <em>enviées</em>, <em>séduisantes</em>, <em>recherchées</em>.</li>
<li><em>désiré</em> ne s’accorde pas (auxiliaire <em>avoir</em>, pas de COD placé avant).</li>
</ul>
<p>b) <em>eût désiré</em> : <strong>subjonctif plus-que-parfait</strong>, employé avec la valeur d’un <strong>conditionnel passé</strong> (on parle de « conditionnel passé 2e forme », propre à la langue littéraire). Il exprime l’<strong>irréel</strong> et le <strong>regret</strong> : elle aurait tant voulu plaire, mais cela ne s’est pas réalisé.</p>"""},
   {"id": "2", "type": "propositions", "points": 1.5,
    "enonce": "Dans la phrase suivante : a) donner la nature et la fonction de la proposition introduite par <em>dont</em> ; b) donner la fonction de <em>dont</em> dans cette proposition ; c) donner la nature et la fonction de <em>la</em> et <em>l’</em>.",
    "passage": "« Toutes ces choses, dont une autre femme de sa caste ne se serait même pas aperçue, la torturaient et l’indignaient. »",
    "corrige": """<ul>
<li>a) <strong>dont une autre femme de sa caste ne se serait même pas aperçue</strong> : proposition subordonnée <strong>relative</strong>, complément de l’antécédent <em>choses</em>. Placée entre virgules, elle est explicative : on pourrait la supprimer.</li>
<li>b) <strong>dont</strong> : pronom relatif, <strong>complément du verbe</strong> <em>s’apercevoir</em> (s’apercevoir <em>de</em> ces choses) ; il remplace « de ces choses ».</li>
<li>c) <strong>la</strong> et <strong>l’</strong> : pronoms personnels de 3e personne du singulier, mis pour Mme Loisel, <strong>COD</strong> de <em>torturaient</em> et de <em>indignaient</em>.</li>
</ul>"""},
   {"id": "3", "type": "propositions", "points": 1.5,
    "enonce": "Dans la phrase suivante, donner la classe grammaticale de <em>car</em> et la relation logique qu’il exprime. Identifier ensuite la nature de la proposition soulignée et la relation logique qu’elle exprime.",
    "passage": "« Elle fut simple ne pouvant être parée, mais malheureuse comme une déclassée ; car les femmes n’ont point de caste ni de race, [[leur beauté, leur grâce et leur charme leur servant de naissance et de famille]]. »",
    "corrige": """<ul>
<li><strong>car</strong> : <strong>conjonction de coordination</strong>. Elle introduit une <strong>explication</strong> (justification) de ce qui précède.</li>
<li><strong>leur beauté, leur grâce et leur charme leur servant de naissance et de famille</strong> : proposition <strong>participiale</strong> (verbe au participe présent <em>servant</em>, avec son propre sujet : <em>leur beauté, leur grâce et leur charme</em>). Elle exprime la <strong>cause</strong> : c’est parce que leur beauté leur tient lieu de naissance que les femmes n’ont pas de caste.</li>
</ul>"""},
   {"id": "4", "type": "orthographe", "points": 1,
    "enonce": "Justifier l’orthographe (l’accord) des participes passés soulignés.",
    "passage": "« une de ces jolies et charmantes filles, [[nées]], comme par une erreur du destin, dans une famille d’employés » ; « aux antichambres muettes, [[capitonnées]] avec des tentures orientales » ; « aux grands salons [[vêtus]] de soie ancienne »",
    "corrige": """<p>Ces trois participes passés sont <strong>employés sans auxiliaire</strong>, comme des adjectifs : ils s’accordent en genre et en nombre avec le nom auquel ils se rapportent.</p>
<ul>
<li><strong>nées</strong> : se rapporte à <em>filles</em> → féminin pluriel.</li>
<li><strong>capitonnées</strong> : se rapporte à <em>antichambres</em> → féminin pluriel.</li>
<li><strong>vêtus</strong> : se rapporte à <em>salons</em> → masculin pluriel.</li>
</ul>"""},
  ]},
  {"id": "A2", "titre": A2, "points": 4, "questions": [
   {"id": "1", "type": "formation", "points": 1.5,
    "enonce": "Analyser la formation du mot <em>déclassée</em> et expliquer son sens dans « malheureuse comme une déclassée ».",
    "corrige": """<p><em>déclassée</em> : participe passé du verbe <em>déclasser</em>, employé ici comme nom. <em>Déclasser</em> est formé par <strong>dérivation préfixale</strong> : préfixe <strong>dé-</strong> (privation, inversion) + verbe <em>classer</em>, lui-même dérivé du nom <em>classe</em> (au sens de classe sociale).</p>
<p><strong>Sens :</strong> une personne qui a perdu son rang social, ou qui vit dans une condition inférieure à celle à laquelle elle se croit destinée. Mathilde se vit comme « tombée » d’un monde auquel elle pense appartenir.</p>"""},
   {"id": "2", "type": "sens", "points": 1,
    "enonce": "Expliquer le sens des mots <em>dot</em> et <em>espérances</em> dans la phrase « Elle n’avait pas de dot, pas d’espérances ».",
    "corrige": """<ul>
<li><strong>dot</strong> : biens (argent, terres) qu’une jeune fille apporte à son mari lors du mariage.</li>
<li><strong>espérances</strong> : ici, sens vieilli, l’<strong>héritage</strong> que l’on peut attendre d’un parent. Ce n’est pas le sens courant de « espoir ».</li>
</ul>
<p>Sans dot ni héritage, Mathilde ne peut pas espérer épouser un homme riche : le mariage est présenté comme une affaire d’argent.</p>"""},
   {"id": "3", "type": "commentaire-lexical", "points": 1.5,
    "enonce": "Commenter l’opposition lexicale entre la vie réelle de Mme Loisel et la vie dont elle rêve (troisième et quatrième paragraphes).",
    "corrige": """<ul>
<li><strong>La vie réelle</strong> : vocabulaire de l’usure et de la médiocrité, « pauvreté », « misère des murs », « usure des sièges », « laideur des étoffes », « nappe de trois jours », « pot-au-feu ».</li>
<li><strong>Le rêve</strong> : vocabulaire du luxe, du raffinement et de l’exotisme, « tentures orientales », « torchères de bronze », « soie ancienne », « bibelots inestimables », « argenteries reluisantes », « forêt de féerie », « truite », « gélinotte ».</li>
<li><strong>Les procédés</strong> : l’anaphore « elle songeait » et les longues énumérations au pluriel montrent un rêve envahissant. La réplique enthousiaste du mari sur le pot-au-feu crée un contraste ironique.</li>
</ul>
<p>Maupassant souligne le <strong>décalage</strong> douloureux entre ce que Mathilde vit et ce qu’elle désire.</p>"""},
  ]},
  {"id": "A3", "titre": A3, "points": 10, "questions": [
   {"id": "1", "type": "expression", "points": 10,
    "enonce": "Mme Loisel souffre de ne pas posséder ce qu’elle désire. Dans quelle mesure ce texte éclaire-t-il le rôle du désir, des apparences et de la comparaison sociale, à l’époque de Maupassant comme aujourd’hui ? Votre réponse prendra la forme d’un développement structuré et argumenté d’une trentaine de lignes.",
    "corrige": """<p><strong>Problématique possible :</strong> en quoi le malheur de Mathilde, né de la comparaison avec plus riche qu’elle, reste-t-il une question d’actualité ?</p>
<p><strong>Plan possible</strong></p>
<ol>
<li><strong>Une souffrance née de la comparaison.</strong> Mathilde n’est pas misérable, mais elle se compare (l’amie riche du couvent, les « grandes dames »). Son malheur vient du regard qu’elle porte sur sa vie, pas de sa situation.</li>
<li><strong>Une société des apparences.</strong> Au XIXe siècle, la place sociale se lit dans les toilettes, les bijoux, le mariage (dot). Pour une femme sans fortune, l’apparence semble être le seul moyen de s’élever : Maupassant critique cette société.</li>
<li><strong>Une question toujours actuelle.</strong> Réseaux sociaux, publicité et marques entretiennent la comparaison et le désir de paraître. On peut discuter : le désir peut aussi être un moteur (ambition, projets). À l’école, on peut développer l’esprit critique face aux images et aux modèles.</li>
</ol>
""" + CRITERES_A3},
  ]},
 ]})

# ---------------------------------------------------------------- Sujet 4 : Montesquieu
SUJETS.append({
 "id": "lettres-persanes", "num": 4,
 "auteur": "Montesquieu", "oeuvre": "Lettres persanes, lettre XXX", "date": "1721", "genre": "Littérature d’idées (roman épistolaire)",
 "theme": "Le regard porté sur l’autre et les préjugés",
 "contexte": "Rica, jeune Persan en voyage à Paris, écrit à son ami Ibben. L’orthographe du XVIIIe siècle a été modernisée.",
 "texte": paras(ex["montesquieu"]), "notes": [],
 "parties": [
  {"id": "A1", "titre": A1, "points": 6, "questions": [
   {"id": "1", "type": "reecriture", "points": 2,
    "enonce": "Récrire le passage suivant en remplaçant « je » par « nous » (Rica et son ami Usbek) et « tout le monde » par « les Parisiens ». Faire toutes les modifications nécessaires.",
    "passage": "« Si je sortais, tout le monde se mettait aux fenêtres ; si j’étais aux Tuileries, je voyais aussitôt un cercle se former autour de moi […]. Je souriais quelquefois d’entendre des gens qui n’étaient presque jamais sortis de leur chambre, qui disaient entre eux : Il faut avouer qu’il a l’air bien persan. »",
    "corrige": """<p class="answer">« Si <strong>nous sortions</strong>, <strong>les Parisiens se mettaient</strong> aux fenêtres ; si <strong>nous étions</strong> aux Tuileries, <strong>nous voyions</strong> aussitôt un cercle se former autour de <strong>nous</strong> […]. <strong>Nous souriions</strong> quelquefois d’entendre des gens qui n’étaient presque jamais sortis de leur chambre, qui disaient entre eux : Il faut avouer qu’<strong>ils ont</strong> l’air bien <strong>persans</strong>. »</p>
<p><strong>Points de vigilance</strong></p>
<ul>
<li>Imparfait, 1re personne du pluriel : <em>nous voyions</em> (y + i) et <em>nous souriions</em> (deux i : radical <em>souri-</em> + terminaison <em>-ions</em>). Ce sont des pièges classiques.</li>
<li><em>il a l’air</em> → <em>ils ont l’air</em>. Avec <em>avoir l’air</em> au sens de « sembler », l’adjectif s’accorde en général avec le sujet : <em>persans</em>. L’accord avec <em>air</em> (<em>persan</em>) est aussi admis.</li>
<li>Les éléments qui ne dépendent pas de « je » ne changent pas : <em>des gens qui n’étaient</em>, <em>leur chambre</em>.</li>
</ul>"""},
   {"id": "2", "type": "phrase", "points": 1.5,
    "enonce": "a) Identifier la voix du verbe souligné. b) Récrire la phrase à l’autre voix. c) Donner la nature et la fonction de la proposition introduite par <em>comme si</em>.",
    "passage": "« Lorsque j’arrivai, je [[fus regardé]] comme si j’avais été envoyé du ciel […] »",
    "corrige": """<ul>
<li>a) <strong>Voix passive</strong> (auxiliaire <em>être</em> au passé simple + participe passé <em>regardé</em>). Le complément d’agent n’est pas exprimé.</li>
<li>b) Voix active : « Lorsque j’arrivai, <strong>on me regarda</strong> comme si j’avais été envoyé du ciel. » Faute de complément d’agent, on utilise le pronom <em>on</em> comme sujet.</li>
<li>c) <strong>comme si j’avais été envoyé du ciel</strong> : proposition subordonnée conjonctive <strong>circonstancielle de comparaison</strong>, avec une valeur <strong>hypothétique</strong> (une comparaison imaginaire, d’où le plus-que-parfait). Elle est complément circonstanciel de manière de <em>fus regardé</em>.</li>
</ul>"""},
   {"id": "3", "type": "temps", "points": 1.5,
    "enonce": "Identifier le mode et le temps des verbes soulignés et justifier l’emploi de ce mode dans chaque cas.",
    "passage": "« et, quoique j’[[aie]] très bonne opinion de moi, je ne me serais jamais imaginé que je [[dusse]] troubler le repos d’une grande ville où je n’étais point connu. »",
    "corrige": """<ul>
<li><strong>aie</strong> : verbe <em>avoir</em>, <strong>subjonctif présent</strong>. La conjonction <em>quoique</em>, qui exprime la <strong>concession</strong>, se construit toujours avec le subjonctif.</li>
<li><strong>dusse</strong> : verbe <em>devoir</em>, <strong>subjonctif imparfait</strong>. Le subjonctif est appelé par la principale négative « je ne me serais jamais imaginé » : le fait est présenté comme non réel, comme une idée qu’on n’envisage pas. L’imparfait respecte la <strong>concordance des temps</strong> de la langue classique (principale au passé → subjonctif imparfait). Aujourd’hui, on dirait « que je doive ».</li>
</ul>"""},
   {"id": "4", "type": "phrase", "points": 1,
    "enonce": "Identifier le type de chacune des phrases suivantes et la manière dont les paroles sont rapportées.",
    "passage": "« j’entendais aussitôt autour de moi un bourdonnement : Ah ! ah ! Monsieur est Persan ? c’est une chose bien extraordinaire ! Comment peut-on être Persan ? »",
    "corrige": """<ul>
<li>« Ah ! ah ! » : interjection, phrase <strong>exclamative</strong> non verbale.</li>
<li>« Monsieur est Persan ? » : phrase <strong>interrogative totale</strong> (on peut y répondre par oui ou non), marquée seulement par l’intonation (le point d’interrogation).</li>
<li>« c’est une chose bien extraordinaire ! » : phrase <strong>exclamative</strong>.</li>
<li>« Comment peut-on être Persan ? » : phrase <strong>interrogative partielle</strong> (introduite par <em>comment</em>).</li>
</ul>
<p>Les paroles sont rapportées au <strong>discours direct</strong>, introduit par les deux-points, mais sans guillemets ni tirets. Elles ne sont attribuées à personne en particulier : c’est la voix de la foule (« un bourdonnement »).</p>"""},
  ]},
  {"id": "A2", "titre": A2, "points": 4, "questions": [
   {"id": "1", "type": "sens", "points": 1.5,
    "enonce": "Expliquer le sens de <em>curiosité</em> dans « Les habitants de Paris sont d’une curiosité qui va jusqu’à l’extravagance », puis celui de <em>curieux</em> dans « je ne me croyais pas un homme si curieux et si rare ». Que remarquez-vous ?",
    "corrige": """<ul>
<li><strong>curiosité</strong> (les Parisiens) : le <strong>désir de voir, de savoir</strong>. Le sens est actif : ce sont eux qui regardent.</li>
<li><strong>curieux</strong> (Rica) : <strong>digne d’être vu</strong>, étrange, singulier. Le sens est passif : c’est lui qui est regardé, comme un objet de curiosité.</li>
</ul>
<p>Le même mot a deux sens (<strong>polysémie</strong>). Montesquieu joue sur ce double sens : la curiosité des Parisiens transforme Rica en « curiosité ».</p>"""},
   {"id": "2", "type": "formation", "points": 1,
    "enonce": "Analyser la formation du mot <em>extravagance</em> et en déduire son sens.",
    "corrige": """<p><em>extravagance</em> : nom dérivé de l’adjectif <em>extravagant</em> par <strong>suffixation</strong> (suffixe <strong>-ance</strong>, qui forme des noms de qualité ou d’état). <em>Extravagant</em> est emprunté au latin médiéval <em>extravagans</em>, formé de <em>extra</em> (« hors de ») et <em>vagari</em> (« errer », que l’on retrouve dans <em>vagabond</em> ou <em>divaguer</em>).</p>
<p><strong>Sens :</strong> ce qui « erre hors » des limites de la raison, un comportement déraisonnable, excessif. Ici : une curiosité démesurée, presque folle.</p>"""},
   {"id": "3", "type": "commentaire-lexical", "points": 1.5,
    "enonce": "Commenter le vocabulaire du regard et de la vue dans le premier paragraphe.",
    "corrige": """<ul>
<li><strong>Un champ lexical omniprésent</strong> : « regardé », « voir », « se mettait aux fenêtres », « un cercle se former », « lorgnettes », « vu », « portraits », « me voyais multiplié ».</li>
<li><strong>Des hyperboles</strong> : « cent lorgnettes », « jamais homme n’a tant été vu que moi », « tant on craignait de ne m’avoir pas assez vu ». Rica devient un spectacle, une bête curieuse.</li>
<li><strong>L’ironie</strong> : ceux qui jugent qu’il a « l’air bien persan » ne sont « presque jamais sortis de leur chambre ». Le regard des Parisiens est superficiel : ils voient un costume, pas un homme.</li>
</ul>"""},
  ]},
  {"id": "A3", "titre": A3, "points": 10, "questions": [
   {"id": "1", "type": "expression", "points": 10,
    "enonce": "« Comment peut-on être Persan ? » En quoi cette lettre écrite au XVIIIe siècle invite-t-elle encore à s’interroger sur la manière dont nous regardons celui qui est différent de nous ? Votre réponse prendra la forme d’un développement structuré et argumenté d’une trentaine de lignes.",
    "corrige": """<p><strong>Problématique possible :</strong> comment Montesquieu utilise-t-il le regard d’un étranger pour dénoncer nos préjugés, et en quoi cette critique reste-t-elle actuelle ?</p>
<p><strong>Plan possible</strong></p>
<ol>
<li><strong>Un regard réduit à l’apparence.</strong> Les Parisiens ne voient en Rica qu’un costume : admiré quand il est habillé en Persan, ignoré dès qu’il porte l’habit européen (« un néant affreux »). L’identité est réduite à un signe extérieur.</li>
<li><strong>Le procédé du regard étranger.</strong> En faisant parler un Persan, Montesquieu retourne la situation : ce sont les Parisiens qui deviennent étranges. La question finale, absurde, révèle l’ethnocentrisme, l’incapacité à imaginer qu’on puisse être autrement que soi.</li>
<li><strong>Une leçon toujours actuelle.</strong> Stéréotypes, exotisme, rejet de ce qui est différent : le texte invite à décentrer son regard. À l’école, cela rejoint l’enseignement moral et civique (respect d’autrui, lutte contre les discriminations) et l’ouverture aux autres cultures.</li>
</ol>
""" + CRITERES_A3},
  ]},
 ]})

# ---------------------------------------------------------------- Sujet 5 : Rousseau
SUJETS.append({
 "id": "emile", "num": 5,
 "auteur": "Jean-Jacques Rousseau", "oeuvre": "Émile, ou De l’éducation, livre II", "date": "1762", "genre": "Essai (traité d’éducation)",
 "theme": "L’enfance et le rôle de l’éducateur",
 "contexte": "Dans ce traité, Rousseau imagine l’éducation d’un enfant, Émile. Ici, il s’adresse directement aux adultes, aux parents et aux éducateurs.",
 "texte": paras(ex["rousseau"]), "notes": [],
 "parties": [
  {"id": "A1", "titre": A1, "points": 6, "questions": [
   {"id": "1", "type": "reecriture", "points": 2,
    "enonce": "Récrire le passage suivant en vous adressant à une seule personne que vous tutoyez (« Homme… », « Père… »). Faire toutes les modifications nécessaires.",
    "passage": "« Hommes, soyez humains, c’est votre premier devoir ; soyez-le pour tous les états, pour tous les âges […]. Aimez l’enfance ; favorisez ses jeux, ses plaisirs, son aimable instinct. […] Pères, savez-vous le moment où la mort attend vos enfants ? Ne vous préparez pas des regrets en leur ôtant le peu d’instants que la nature leur donne […] »",
    "corrige": """<p class="answer">« <strong>Homme, sois humain</strong>, c’est <strong>ton</strong> premier devoir ; <strong>sois-le</strong> pour tous les états, pour tous les âges […]. <strong>Aime</strong> l’enfance ; <strong>favorise</strong> ses jeux, ses plaisirs, son aimable instinct. […] <strong>Père, sais-tu</strong> le moment où la mort attend <strong>tes</strong> enfants ? <strong>Ne te prépare</strong> pas des regrets en leur ôtant le peu d’instants que la nature leur donne. »</p>
<p><strong>Points de vigilance</strong></p>
<ul>
<li>Impératif présent, 2e personne du singulier : les verbes du 1er groupe n’ont <strong>pas de -s</strong> : <em>aime</em>, <em>favorise</em>, <em>ne te prépare pas</em>.</li>
<li><em>sois</em> (verbe <em>être</em>) ; accord de l’attribut : <em>humain</em> au singulier.</li>
<li>Impératif négatif pronominal : <em>ne te prépare pas</em> (le pronom se place avant le verbe).</li>
<li><em>leur</em> ne change pas : il désigne les enfants.</li>
</ul>"""},
   {"id": "2", "type": "nature", "points": 1.5,
    "enonce": "Donner la nature et la fonction des mots soulignés.",
    "passage": "« soyez-[[le]] pour tous les états » ; « en [[leur]] ôtant le peu d’instants que la nature leur donne » ; « faites qu’ils [[en]] jouissent »",
    "corrige": """<ul>
<li><strong>le</strong> (soyez-le) : <strong>pronom personnel</strong> neutre, invariable ; il reprend l’adjectif <em>humains</em>. Il est <strong>attribut du sujet</strong> (le sujet sous-entendu de l’impératif : <em>vous</em>).</li>
<li><strong>leur</strong> (en leur ôtant) : <strong>pronom personnel</strong> (3e personne du pluriel), mis pour <em>vos enfants</em> ; <strong>complément d’objet second</strong> (COS) du verbe <em>ôter</em> (ôter quelque chose <em>à</em> quelqu’un). Il est invariable : ce n’est pas le déterminant possessif.</li>
<li><strong>en</strong> (qu’ils en jouissent) : <strong>pronom</strong> (dit adverbial), mis pour « du plaisir d’être » ; <strong>COI</strong> du verbe <em>jouir</em> (jouir <em>de</em> quelque chose).</li>
</ul>"""},
   {"id": "3", "type": "propositions", "points": 1.5,
    "enonce": "a) Relever les deux propositions subordonnées relatives et donner la fonction de chaque pronom relatif. b) Quelle est la valeur de ce type de question dans l’argumentation de Rousseau ?",
    "passage": "« Pourquoi voulez-vous ôter à ces petits innocents la jouissance d’un temps si court qui leur échappe, et d’un bien si précieux dont ils ne sauraient abuser ? »",
    "corrige": """<ul>
<li>a) <strong>qui leur échappe</strong> : relative, antécédent <em>un temps si court</em> ; <em>qui</em> est <strong>sujet</strong> du verbe <em>échappe</em>.</li>
<li><strong>dont ils ne sauraient abuser</strong> : relative, antécédent <em>un bien si précieux</em> ; <em>dont</em> est <strong>COI</strong> du verbe <em>abuser</em> (abuser <em>de</em> ce bien). Remarque : <em>ne sauraient</em> (conditionnel de <em>savoir</em>, sans <em>pas</em>) signifie « ne pourraient ».</li>
<li>b) C’est une <strong>question rhétorique</strong> : elle n’attend pas de réponse, elle affirme une idée (on n’a aucune raison de priver les enfants de leur bonheur). Elle interpelle le lecteur et le met face à ses contradictions.</li>
</ul>"""},
   {"id": "4", "type": "phrase", "points": 1,
    "enonce": "Identifier la construction utilisée dans la phrase suivante et son effet. Préciser ce que reprend le pronom <em>les</em>.",
    "passage": "« c’est dans l’âge de l’enfance, où les peines sont le moins sensibles, qu’il faut les multiplier, pour les épargner dans l’âge de raison »",
    "corrige": """<ul>
<li>Construction <strong>c’est… que</strong> : tournure de <strong>mise en relief</strong> (phrase clivée ou emphatique). Elle met en valeur le complément de temps <em>dans l’âge de l’enfance</em>.</li>
<li><strong>Effet :</strong> Rousseau reproduit, pour mieux la réfuter ensuite, l’affirmation catégorique de ses adversaires.</li>
<li><strong>les</strong> (les multiplier, les épargner) : pronom personnel COD qui reprend <em>les peines</em>.</li>
</ul>"""},
  ]},
  {"id": "A2", "titre": A2, "points": 4, "questions": [
   {"id": "1", "type": "sens", "points": 1.5,
    "enonce": "Expliquer la différence de sens entre <em>licence</em> et <em>liberté</em> dans la dernière phrase. Citer un autre sens du mot <em>licence</em>.",
    "corrige": """<ul>
<li><strong>liberté</strong> : pouvoir d’agir selon sa nature et ses besoins, dans un cadre (Rousseau parle d’une liberté « bien réglée »).</li>
<li><strong>licence</strong> : liberté <strong>excessive</strong>, sans règle ni limite, qui dégénère en désordre. Le chiasme qui suit le confirme (licence / liberté, puis rend heureux / gâte) : l’enfant libre est « l’enfant qu’on rend heureux », l’enfant laissé à la licence est « l’enfant qu’on gâte ».</li>
<li><strong>Autres sens</strong> : un diplôme universitaire (la licence), une autorisation officielle (licence de pêche, licence sportive, licence d’un logiciel).</li>
</ul>"""},
   {"id": "2", "type": "formation", "points": 1,
    "enonce": "Analyser la formation de l’adverbe <em>incessamment</em>. Quel est son sens dans le texte ? Est-ce le sens courant aujourd’hui ?",
    "corrige": """<p><em>incessamment</em> : préfixe négatif <strong>in-</strong> + base <em>cess(er)</em> + suffixe <strong>-ant</strong> → adjectif <em>incessant</em> ; puis suffixe <strong>-ment</strong> → adverbe (<em>-ant</em> devient <em>-amment</em>).</p>
<p><strong>Dans le texte</strong> : « sans cesse, continuellement » (la fausse sagesse nous jette continuellement hors de nous). <strong>Aujourd’hui</strong>, le sens courant est « sans délai, très prochainement » (« il arrivera incessamment »). C’est une <strong>évolution du sens</strong> au fil du temps.</p>"""},
   {"id": "3", "type": "commentaire-lexical", "points": 1.5,
    "enonce": "Commenter le vocabulaire qui caractérise l’enfance et celui qui caractérise les éducateurs critiqués par Rousseau.",
    "corrige": """<ul>
<li><strong>L’enfance</strong> : un vocabulaire du bonheur, de la douceur et de la fragilité, « jeux », « plaisirs », « aimable instinct », « le rire est toujours sur les lèvres », « l’âme est toujours en paix », « petits innocents », « bien si précieux », « temps si court », « faible esprit ».</li>
<li><strong>Les éducateurs</strong> : un vocabulaire de la contrainte et de la souffrance infligée, « amertume », « douleurs », « chagrins que vous lui prodiguez », « accablez », « maux », « soins mal entendus » ; et du mépris pour leur prétendue sagesse : « fausse sagesse », « clameurs », « raisonneurs vulgaires », « malheureuse prévoyance ».</li>
</ul>
<p>Cette <strong>opposition</strong> sert l’argumentation : l’enfance est un temps précieux que des adultes aveuglés gâchent au nom de l’avenir.</p>"""},
  ]},
  {"id": "A3", "titre": A3, "points": 10, "questions": [
   {"id": "1", "type": "expression", "points": 10,
    "enonce": "Rousseau demande d’« aimer l’enfance » et de ne pas sacrifier le présent de l’enfant à son avenir. Dans quelle mesure cette réflexion peut-elle éclairer, aujourd’hui, le métier de professeur des écoles ? Votre réponse prendra la forme d’un développement structuré et argumenté d’une trentaine de lignes.",
    "corrige": """<p><strong>Problématique possible :</strong> comment concilier le respect du bonheur présent de l’enfant et l’exigence de le préparer à sa vie future ?</p>
<p><strong>Plan possible</strong></p>
<ol>
<li><strong>Une idée neuve et toujours féconde.</strong> Rousseau reconnaît l’enfance comme un âge à part, avec ses besoins propres (« la nature veut que les enfants soient enfants avant que d’être hommes »). Cette idée inspire les pédagogies actives (Montessori, Freinet) et les programmes actuels, qui accordent une place au jeu, notamment à l’école maternelle.</li>
<li><strong>Le bien-être, condition des apprentissages.</strong> Un climat de classe serein, la bienveillance, le refus des punitions humiliantes favorisent la confiance et l’envie d’apprendre. Le professeur doit tenir compte du développement de l’enfant.</li>
<li><strong>Les limites.</strong> Rousseau distingue lui-même liberté et « licence » : aimer l’enfance n’est pas tout permettre. L’école doit aussi transmettre des savoirs, poser un cadre et des règles, et préparer l’avenir (l’instruction est obligatoire). Le métier consiste à trouver l’équilibre entre exigence et bienveillance.</li>
</ol>
""" + CRITERES_A3},
  ]},
 ]})

TYPES = {
 "reecriture": "Réécriture",
 "nature": "Nature des mots",
 "fonction": "Fonctions",
 "propositions": "Propositions et subordonnées",
 "temps": "Temps, modes et valeurs",
 "phrase": "Phrase : types, voix, constructions",
 "orthographe": "Accords et orthographe",
 "formation": "Formation des mots",
 "sens": "Sens des mots",
 "commentaire-lexical": "Commentaire du vocabulaire",
 "expression": "Réflexion argumentée",
}

for s in SUJETS:
    tot = sum(q["points"] for p in s["parties"] for q in p["questions"])
    for p in s["parties"]:
        pt = sum(q["points"] for q in p["questions"])
        assert abs(pt - p["points"]) < 1e-9, (s["id"], p["id"], pt)
        for q in p["questions"]:
            assert q["type"] in TYPES, q["type"]
    assert abs(tot - 20) < 1e-9, (s["id"], tot)
    s["mots"] = len(re.findall(r"[\wÀ-ÿœŒ]+", " ".join(s["texte"])))

out = "/* Généré à partir de sujets_fr.py : sujets de français du CRPE BAC+3 (1re épreuve, partie A). */\n"
out += "window.BELAMIS_FRANCAIS = " + json.dumps({"types": TYPES, "sujets": SUJETS}, ensure_ascii=False, indent=1) + ";\n"
open(os.path.join(HERE, "francais.js"), "w").write(out)
for s in SUJETS:
    print(s["num"], s["id"], s["mots"], "mots", sum(len(p["questions"]) for p in s["parties"]), "questions")
