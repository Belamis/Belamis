# -*- coding: utf-8 -*-
# Génère /home/user/Belamis/revision/data/e2_anglais.json
import json, re, html

OUT = "/home/user/Belamis/revision/data/e2_anglais.json"
SRC_TRAIN = "Text written for training purposes, based on general knowledge"
WORDCOUNTS = []  # (sujet, question, cible, compte)


def wc(text):
    t = re.sub(r"<[^>]+>", " ", text)
    t = html.unescape(t)
    return len([w for w in re.split(r"[\s—–]+", t) if re.search(r"[A-Za-z0-9]", w)])


def doc(title, paras, src=SRC_TRAIN):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return (f'<div class="doc" lang="en"><p class="doc-title">Document – {title}</p>'
            f'{body}<p class="doc-src">{src}</p></div>')


def comp(qid, pts, enonce, answer, note=None):
    c = f'<p class="answer">{answer}</p>'
    if note:
        c += f"<p>{note}</p>"
    return {"id": qid, "type": "comprehension", "points": pts, "enonce": enonce, "corrige": c, "niveau": "c4"}


def expr(sid, qid, pts, enonce, target, production, criteres, lexique):
    n = wc(production)
    WORDCOUNTS.append((sid, qid, target, n))
    c = (f"<p><strong>Exemple de production ({n} mots) :</strong></p>"
         f'<p class="answer">{production}</p>'
         "<p><strong>Critères d’évaluation :</strong></p><ul>"
         + "".join(f"<li>{x}</li>" for x in criteres) + "</ul>"
         "<p><strong>Mots et tournures utiles :</strong></p><ul>"
         + "".join(f"<li><em>{x}</em></li>" for x in lexique) + "</ul>")
    return {"id": qid, "type": "expression", "points": pts, "enonce": enonce, "corrige": c, "niveau": "c4"}


def partie(pid, kind, titre, points, intro, questions):
    label, short = ("Compréhension", "C") if kind == "C" else ("Expression", "E")
    return {"id": pid, "label": label, "short": short, "titre": titre, "points": points,
            "intro": intro, "questions": questions}


def sujet(num, sid, titre, theme, officiel, parties, source=None, remarque=None):
    s = {"id": sid, "num": num, "domaine": "anglais", "titre": titre, "theme": theme, "officiel": officiel}
    if source:
        s["source"] = source
    if remarque:
        s["remarque"] = remarque
    s["total"] = 20
    s["parties"] = parties
    return s


CONSIGNE_C = "<p>Answer the following questions in English and, unless asked to quote, in your own words.</p>"
CONSIGNE_E = "<p>Answer the following questions in English. Respect the number of words indicated (± 10 %).</p>"

SUJETS = []

# =====================================================================
# Sujet 1 — sujet 0 officiel
# =====================================================================
S = "ang-sujet0"
intro_off = (
    "<p><strong>Document (non reproduit ici) :</strong> « The Guardian view on the arts in schools: classrooms need more creativity », "
    "éditorial adapté de <em>The Guardian</em>, 20 mars 2025.</p>"
    "<p><strong>Résumé en français.</strong> Dans cet éditorial, le <em>Guardian</em> salue le rapport intermédiaire de la commission "
    "d’examen des programmes scolaires anglais dirigée par la professeure Becky Francis, qui prend au sérieux la crainte que les arts "
    "aient été marginalisés dans les apprentissages. Le journal rappelle que, depuis 2010, les établissements ont été incités à orienter "
    "les élèves vers une combinaison de matières « académiques » au GCSE (anglais, mathématiques, sciences, une langue, histoire ou "
    "géographie), reléguant les arts au second plan. Il défend l’idée que la créativité et l’imagination font partie de ce qui nous rend "
    "humains et que les industries créatives comptent beaucoup pour le Royaume-Uni, économiquement comme culturellement. Enfin, il note "
    "qu’à l’école primaire aussi, sous les gouvernements travaillistes comme conservateurs, la volonté d’élever le niveau en lecture-écriture "
    "et en mathématiques a réduit la place du jeu et de la créativité.</p>"
    "<p><em>Pour le texte intégral, reporte-toi au sujet 0 officiel (CRPE BAC+3, seconde épreuve d’admissibilité, partie 4.2 Anglais, "
    "pages 12-13), publié sur devenirenseignant.gouv.fr.</em></p>"
    + CONSIGNE_C.replace("and, unless asked to quote, in your own words", "in your own words")
)
q_off_c = [
    comp("a", 3, "<p>What source is <em>The Guardian</em> using as a basis for this article?</p>",
         "The article is an editorial (“The Guardian view”) based on the interim report of an official review of the curriculum in "
         "English schools. This review is led by an expert in education, Professor Becky Francis. The newspaper comments on this report "
         "and hopes that it will lead to more room for the arts in schools.",
         "Attendu : identifier le <strong>rapport intermédiaire</strong> (<em>interim report</em>) de la commission présidée par "
         "<strong>Prof. Becky Francis</strong> sur les programmes scolaires en Angleterre ; bonus si le candidat signale qu’il s’agit d’un "
         "éditorial (point de vue du journal). Pénaliser la simple recopie de la première phrase."),
    comp("b", 4, "<p>According to the article, what evolution has affected the arts in British schools since 2010 and for what reasons?</p>",
         "Since 2010, the arts have become less important in schools: they have been pushed aside and are now a secondary subject. "
         "The main reason is that schools were asked to steer pupils towards a set of “academic” GCSE subjects: English, maths, science, "
         "a foreign language and history or geography. Art, music or drama were not part of this group. In primary schools too, successive "
         "governments, both Labour and Conservative, wanted to raise standards in reading, writing and maths, so there was less time for "
         "play and creative activities.",
         "Attendu : 1) le constat (les arts relégués au second plan, « évincés » des apprentissages) ; 2) la cause au secondaire (combinaison "
         "de matières encouragée au GCSE, connue sous le nom d’<em>English Baccalaureate</em> ou EBacc, introduite en 2010) ; 3) la cause au "
         "primaire (priorité à la lecture-écriture et aux mathématiques, sous les deux grands partis). Reformulation exigée : expliquer "
         "<em>second fiddle</em> (rôle secondaire) plutôt que le recopier."),
    comp("c", 3, "<p>“In the UK, the creative industries are hugely important economically as well as culturally” – explain this assertion.</p>",
         "Economically, the creative industries (music, cinema, television, video games, fashion, design, publishing, theatre…) create "
         "a lot of jobs – more than two million people work in them – and bring billions of pounds to the country, partly through exports. "
         "Culturally, they give the UK a strong image in the world: think of the Beatles, Adele, Harry Potter, the BBC or London’s West End "
         "theatres. They shape British identity and attract tourists. So, if schools neglect the arts, they may weaken a sector that matters "
         "for the future of the country.",
         "Attendu : distinguer les deux dimensions (économique : emplois, richesse, exportations ; culturelle : rayonnement, identité, "
         "<em>soft power</em>) et donner au moins un exemple concret. Valoriser le lien avec l’argument de l’article (former ces compétences "
         "dès l’enfance)."),
]
q_off_e = [
    expr(S, "d", 4, "<p>In your experience, can the arts (music, drama, etc.) support the learning of a language? (40 words)</p>", 40,
         "Yes, definitely. When I was at school, we learnt English with songs and I still remember the words today. Music helps you memorise "
         "vocabulary and pronunciation, and drama gives you real situations to speak in. Besides, it is fun, so you feel less shy.",
         ["Réponse claire à la question (prise de position) et appui sur une expérience personnelle.",
          "Au moins un argument développé (mémorisation, prononciation, motivation, prise de parole).",
          "Correction de la langue : prétérit (<em>learnt, remember</em>), comparatifs, connecteurs.",
          "Respect du nombre de mots (environ 40)."],
         ["to memorise / to remember", "a nursery rhyme, a chant, a song", "to act out a scene, role-play",
          "pronunciation, rhythm, intonation", "to feel confident / less shy", "besides, what is more"]),
    expr(S, "e", 6, "<p>In your opinion, what part should “play and creativity” have in a child’s life? Give examples. (80 words)</p>", 80,
         "In my opinion, play and creativity should have a central place in a child’s life, at home and at school. By playing, children "
         "learn to cooperate, to follow rules and to solve problems. For example, building a hut with friends develops teamwork, and "
         "inventing a story develops language. At school, teachers can use board games in maths or drama in English lessons. Of course, "
         "children also need structured learning, but a good balance makes them happier and more curious learners.",
         ["Opinion clairement exprimée et nuancée (équilibre jeu / apprentissages structurés).",
          "Exemples concrets et variés (maison, école, loisirs), dont au moins un lié à l’école.",
          "Organisation du propos : introduction, arguments reliés par des connecteurs, conclusion.",
          "Richesse et correction de la langue (gérondif après préposition : <em>by playing</em> ; modaux <em>should, can</em>).",
          ],
         ["in my opinion / as far as I am concerned", "by + V-ing (by playing, children learn…)", "to develop, to foster",
          "teamwork, to cooperate", "board games, role-play, arts and crafts", "a good balance between… and…", "of course… but…"]),
]
SUJETS.append(sujet(1, S, "Sujet 0 officiel – The arts in schools", "Les arts et la créativité à l’école (Angleterre)", True, [
    partie("E1", "C", "Compréhension – The Guardian view on the arts in schools", 10, intro_off, q_off_c),
    partie("E2", "E", "Expression", 10, CONSIGNE_E, q_off_e),
], source="Sujet 0 du CRPE BAC+3 (2025), seconde épreuve d’admissibilité, partie 4.2 Anglais – document : The Guardian, 20 March 2025 (adapté).",
   remarque="Le sujet officiel ne précise pas le barème des questions : la répartition des points proposée ici (10 + 10) est indicative. "
            "Le texte de l’article n’est pas reproduit (droits d’auteur) : travaille avec le sujet officiel sous les yeux."))

# =====================================================================
# Sujet 2 — Forest Schools
# =====================================================================
S = "ang-forest-school"
D2 = doc("Into the woods: why British pupils are learning outdoors", [
    "Every Tuesday morning, whatever the weather, a Year 1 class in a primary school in the south-west of England puts on waterproof "
    "trousers and wellies and walks to a small wood behind the playground. There are no tables, no worksheets and no interactive "
    "whiteboard. Instead, the six-year-olds build dens, look for insects under logs and learn to use simple tools under the careful eye "
    "of a trained Forest School leader.",
    "The idea is not new. It comes from Scandinavia, where outdoor learning has long been part of early childhood education. In 1993, "
    "a group of staff from Bridgwater College, in Somerset, visited Denmark and were so impressed that they brought the approach back "
    "to Britain. Today, thousands of nurseries and primary schools across the UK offer Forest School sessions, and the Forest School "
    "Association, created in 2012, supports the people who lead them.",
    "What makes Forest School different from a simple nature walk? First, it is regular and long-term: children go out every week for "
    "months, not just once a year. Second, it is child-led: adults suggest activities, but children are encouraged to follow their own "
    "curiosity. Finally, children are allowed to take “supported risks”, such as climbing a tree or helping to light a small fire, "
    "because learning to manage risk builds confidence.",
    "Teachers often notice changes back in the classroom. “Some children who hardly speak inside become leaders in the woods,” says one "
    "teacher. “They cooperate, they solve problems, and they come back full of words to describe what they have seen.”",
    "Not everyone is convinced. Some parents worry about muddy clothes and scratched knees, and some head teachers say that, with a busy "
    "curriculum, it is hard to find the time. But for supporters, a morning in the woods is not time lost: it is learning of a different kind.",
])
q2c = [
    comp("a", 2, "<p>Where does the Forest School approach come from, and how did it arrive in the UK?</p>",
         "Forest School comes from Scandinavia, where children have been learning outdoors for a long time. It arrived in the UK in 1993, "
         "when some staff from a college in Somerset (Bridgwater College) went to Denmark, liked what they saw and decided to use the same "
         "method in Britain.",
         "Deux éléments attendus : l’origine scandinave (1 pt) et la visite au Danemark de l’équipe du Bridgwater College en 1993 (1 pt)."),
    comp("b", 3, "<p>According to the text, what makes Forest School different from a simple nature walk? Explain the three features in your own words.</p>",
         "First, it happens very often and over a long period: the children go to the woods every week for several months, not only on a "
         "special day. Second, the children decide what they do: adults give ideas, but the children explore what interests them. Third, "
         "the children can do slightly dangerous things, like climbing trees, with an adult nearby, because this helps them to feel more "
         "confident.",
         "1 pt par caractéristique correctement reformulée (régularité / durée ; activités choisies par l’enfant ; prise de risque encadrée). "
         "Ne pas accepter la simple recopie de <em>regular and long-term</em>, <em>child-led</em>, <em>supported risks</em>."),
    comp("c", 3, "<p>What are the benefits of Forest School for children, according to the article? Justify your answer with two quotations.</p>",
         "Forest School helps children to become more confident and more sociable. Shy children can take responsibilities, work with others "
         "and find solutions together, and it also improves their language. Quotations: “Some children who hardly speak inside become leaders "
         "in the woods”; “They cooperate, they solve problems, and they come back full of words to describe what they have seen.” "
         "Also: “learning to manage risk builds confidence”.",
         "2 pts pour l’explication (confiance en soi, coopération, résolution de problèmes, langage), 1 pt pour deux citations exactes "
         "et pertinentes, entre guillemets."),
    comp("d", 2, "<p>Explain the following words or expressions in context: “wellies” (§1), “child-led” (§3), “not time lost” (§5).</p>",
         "“Wellies” are wellington boots, rubber boots that you wear when it is wet or muddy. “Child-led” means that the children guide the "
         "activity: they choose what to do, not the adults. “Not time lost” means that the time spent in the woods is useful, not wasted, "
         "even if the children are not doing traditional lessons.",
         "Barème indicatif : 0,75 + 0,5 + 0,75. <em>Wellies</em> (abréviation familière de <em>wellington boots</em>) est un mot très britannique."),
]
q2e = [
    expr(S, "e", 4, "<p>Did you learn outside the classroom when you were a child? Describe one memory. (40 words)</p>", 40,
         "When I was nine, my class spent a week in the mountains. We walked every day, observed birds and drew plants in a notebook. "
         "I learnt more about nature in five days than in a whole year of lessons!",
         ["Récit au passé cohérent (prétérit simple, éventuellement <em>used to</em>).",
          "Un souvenir précis (lieu, âge, activité) et une courte appréciation personnelle.",
          "Correction de la langue (verbes irréguliers : <em>spent, drew, learnt</em>).",
          "Respect du nombre de mots (environ 40)."],
         ["when I was… years old", "a school trip, a field trip", "to observe, to collect, to draw",
          "I used to…", "I will never forget…", "more… than…"]),
    expr(S, "f", 6, "<p>You are a primary school teacher in France. Describe an outdoor activity you could organise to teach English to your "
                    "pupils, and explain its benefits. (80 words)</p>", 80,
         "I would organise a “nature treasure hunt” in the school garden with my Year 4 pupils. In small groups, they would receive a list in "
         "English: “Find something green, something round, two leaves, a stone…”. They would have to read the instructions, collect the objects "
         "and then present them to the class: “We found a big brown leaf.” This activity is fun and active. It helps pupils memorise colours, "
         "shapes and nature words, and it encourages them to speak English together.",
         ["Activité concrète, réaliste et adaptée à l’âge des élèves (cycle 2 ou 3), décrite étape par étape.",
          "Lien explicite avec l’apprentissage de l’anglais (lexique, structures, compréhension de consignes, prise de parole).",
          "Justification des bénéfices (motivation, mémorisation par le mouvement, travail en groupe).",
          "Langue correcte : conditionnel (<em>I would…, they would…</em>), impératif pour les consignes, connecteurs."],
         ["I would organise…", "a treasure hunt, a scavenger hunt", "in small groups / in pairs", "to collect, to find, to point to",
          "leaves, sticks, stones, a tree, a bug", "this activity helps pupils (to) + verbe", "it encourages them to…"]),
]
SUJETS.append(sujet(2, S, "Forest Schools – learning outdoors", "Forest School et apprentissages en plein air (Royaume-Uni)", False, [
    partie("E1", "C", "Compréhension – Into the woods", 10, D2 + CONSIGNE_C, q2c),
    partie("E2", "E", "Expression", 10, CONSIGNE_E, q2e),
], source="Sujet d’entraînement original (document rédigé pour l’entraînement)."))

# =====================================================================
# Sujet 3 — Bonfire Night
# =====================================================================
S = "ang-bonfire-night"
D3 = doc("“Remember, remember”: Bonfire Night in my classroom (blog post)", [
    "Every year, in the first week of November, my Year 2 classroom is covered in paper fireworks and my pupils ask the same question: "
    "“Miss, are we doing the fireworks poem again?” Of course we are!",
    "Bonfire Night, also called Guy Fawkes Night, is celebrated in Britain on 5 November. It remembers the Gunpowder Plot of 1605, when "
    "a small group of Catholic conspirators planned to blow up the Houses of Parliament in London and kill King James I. One of them, "
    "Guy Fawkes, was arrested in a cellar under the House of Lords, next to barrels of gunpowder. The plot failed, and Londoners lit "
    "bonfires to celebrate the King’s survival. The tradition has continued for more than four hundred years.",
    "Today, most families simply enjoy the show: public firework displays, bonfires, sparklers and warm food like jacket potatoes, "
    "toffee apples or, in the north of England, parkin, a sticky ginger cake. When I was little, children made a “guy” out of old clothes "
    "and newspaper and asked passers-by for “a penny for the guy”. You rarely see that nowadays.",
    "At school, I use the celebration to teach history, but also safety. We learn the rhyme “Remember, remember the fifth of November”, "
    "we write poems full of sound words like “whoosh”, “bang” and “crackle”, and a local firefighter visits us to explain how to stay "
    "safe around fireworks.",
    "Some colleagues feel uncomfortable celebrating a story about a man who was sentenced to death, or burning a figure on a fire. "
    "I understand. That is why I don’t present it as a party but as a story full of questions: Why did the plotters act? Was it fair? "
    "How do we remember the past? My pupils, aged six and seven, have surprisingly strong opinions!",
])
q3c = [
    comp("a", 2, "<p>Who is the author of this blog post and who are her pupils? Justify with elements from the text.</p>",
         "The author is a primary school teacher in Britain. We know it because she talks about “my Year 2 classroom” and her pupils call "
         "her “Miss”. Her pupils are young children: they are “aged six and seven”.",
         "1 pt pour l’identification (enseignante du primaire en Grande-Bretagne), 1 pt pour la justification (<em>Year 2</em>, <em>Miss</em>, "
         "<em>aged six and seven</em>). Remarque culturelle : en Angleterre, les élèves appellent leur enseignante <em>Miss</em>."),
    comp("b", 3, "<p>Explain in your own words what happened in 1605 and why people still light bonfires on 5 November.</p>",
         "In 1605, some Catholic men wanted to destroy Parliament with explosives and kill the King, James I. Guy Fawkes, one of them, was "
         "caught under the building with the gunpowder, so the attack never happened. People in London were happy that the King was alive, "
         "so they made big fires. Since then, the British have lit bonfires and set off fireworks every 5 November to remember that event.",
         "Attendu : le complot (qui, quoi, contre qui) – 1 pt ; l’échec et l’arrestation de Guy Fawkes – 1 pt ; l’origine des feux "
         "(célébrer la survie du roi) et la continuité de la tradition – 1 pt."),
    comp("c", 3, "<p>How does the author use Bonfire Night at school? Give three activities, then explain how she answers colleagues who "
                 "feel uncomfortable with this celebration.</p>",
         "She teaches a traditional rhyme, “Remember, remember the fifth of November”; the children write poems with onomatopoeias; and a "
         "firefighter comes to talk about safety with fireworks. To colleagues who don’t like celebrating the execution of a man, she answers "
         "that she does not treat it as a celebration: she uses the story to make children think and debate about history and justice.",
         "1,5 pt pour les trois activités, 1,5 pt pour la réponse aux réserves (approche critique, questionnement, pas une fête)."),
    comp("d", 2, "<p>Find in the text: (1) a word meaning “people walking past in the street”; (2) three onomatopoeias. "
                 "(3) Explain: “You rarely see that nowadays.”</p>",
         "(1) “passers-by”. (2) “whoosh”, “bang”, “crackle”. (3) It means that today children almost never make a “guy” or ask for money "
         "for it: this old custom has nearly disappeared.",
         "Barème : 0,5 + 0,5 + 1."),
]
q3e = [
    expr(S, "e", 4, "<p>Which festival from an English-speaking country would you like to share with your pupils? Explain why. (40 words)</p>", 40,
         "I would choose Halloween because children love dressing up and it is a perfect way to learn vocabulary: witch, ghost, pumpkin. "
         "We could carve a pumpkin, sing songs and compare it with French traditions, such as All Saints’ Day.",
         ["Choix d’une fête réellement anglophone, correctement nommée (<em>Halloween, Thanksgiving, St Patrick’s Day, Burns Night…</em>).",
          "Au moins deux justifications, dont une pédagogique.",
          "Langue correcte : conditionnel (<em>I would choose, we could…</em>), <em>because</em>, comparaison.",
          "Respect du nombre de mots (environ 40)."],
         ["I would choose… because…", "to dress up (as)", "to carve a pumpkin", "to share a tradition",
          "to compare… with…", "such as…"]),
    expr(S, "f", 6, "<p>Some people think that schools should not celebrate traditions linked to history, religion or politics. "
                    "What is your opinion? Give examples. (80 words)</p>", 80,
         "I think schools can talk about traditions, but they should not simply celebrate them. In France, state schools are secular, "
         "so teachers must stay neutral. However, studying a festival like Bonfire Night or Thanksgiving is an excellent way to discover "
         "another culture and its history. For example, pupils can learn songs, taste typical food and ask questions about the past. "
         "The teacher’s role is to explain, not to promote. This way, children learn to respect differences and to think critically.",
         ["Opinion claire, argumentée et nuancée (étudier / célébrer).",
          "Prise en compte du contexte français (laïcité, neutralité) et exemples précis tirés de l’aire anglophone.",
          "Cohérence : connecteurs d’opposition et de conséquence (<em>however, so, this way</em>).",
          "Correction et variété de la langue (modaux <em>should, must, can</em> ; vocabulaire de l’école)."],
         ["I think / I believe that…", "state schools are secular", "to stay neutral", "however / on the other hand",
          "to discover another culture", "to respect differences", "to think critically", "the teacher’s role is to…"]),
]
SUJETS.append(sujet(3, S, "Bonfire Night at school", "Bonfire Night : une tradition britannique à l’école", False, [
    partie("E1", "C", "Compréhension – Bonfire Night in my classroom", 10, D3 + CONSIGNE_C, q3c),
    partie("E2", "E", "Expression", 10, CONSIGNE_E, q3e),
], source="Sujet d’entraînement original (document rédigé pour l’entraînement)."))

# =====================================================================
# Sujet 4 — Screens and reading for pleasure
# =====================================================================
S = "ang-reading-pleasure"
D4 = doc("Reading for pleasure in a digital world (podcast transcript, extract)", [
    "<strong>HOST:</strong> Welcome back. Today I’m talking to Sarah, a librarian in a primary school in Manchester. Sarah, are children "
    "reading less than before?",
    "<strong>SARAH:</strong> Sadly, yes. Every year, the National Literacy Trust, a UK charity, asks thousands of young people about reading. "
    "In 2024, only about one in three children and young people aged 8 to 18 said they enjoyed reading in their free time. That’s the "
    "lowest figure since the charity started asking the question in 2005.",
    "<strong>HOST:</strong> Are screens to blame?",
    "<strong>SARAH:</strong> Partly. Tablets and phones are designed to keep us watching. A video gives you instant pleasure; a book asks "
    "for a bit of effort at the beginning. But I don’t think screens are the enemy. Many children discover stories through films or "
    "audiobooks, and some reluctant readers love e-readers because they can make the text bigger.",
    "<strong>HOST:</strong> So what works?",
    "<strong>SARAH:</strong> Choice, first of all. Children must be allowed to choose what they read: comics, joke books, football "
    "magazines, anything! Reading for pleasure is not the same as reading for a test. Second, time: in our school, every class has fifteen "
    "minutes of quiet reading after lunch, and the teachers read too. And third, adults who read aloud. Even eleven-year-olds love being "
    "read to.",
    "<strong>HOST:</strong> And parents?",
    "<strong>SARAH:</strong> I tell them: don’t feel guilty, just be a model. If your child sees you scrolling all evening, why would they "
    "pick up a book? Put the phones in a basket at dinner time and share a story at bedtime. And on World Book Day, in March, come to "
    "school dressed as your favourite character. The children love it!",
], src=SRC_TRAIN + " (fictional interview; figures from the National Literacy Trust annual survey)")
q4c = [
    comp("a", 2, "<p>Who is Sarah, and what worrying fact does she mention at the beginning of the interview?</p>",
         "Sarah works as a librarian in a primary school in Manchester. She explains that fewer and fewer young people like reading: in 2024, "
         "only one child out of three between 8 and 18 said they read for pleasure, which is the worst result since 2005.",
         "1 pt pour l’identité de Sarah, 1 pt pour le constat chiffré (reformulé, avec la notion de record à la baisse)."),
    comp("b", 3, "<p>Why are screens only “partly” responsible, according to Sarah? Explain both sides of her answer in your own words.</p>",
         "On the one hand, screens are responsible because they are made to hold our attention and they give immediate pleasure, while a book "
         "needs some effort before you enjoy it. On the other hand, screens can also help: children find stories in films or audiobooks, and "
         "children who don’t like reading can use an e-reader to read the text in a bigger size.",
         "1,5 pt par versant de l’argument. Valoriser les connecteurs <em>on the one hand / on the other hand</em>."),
    comp("c", 3, "<p>Sarah gives three keys to help children enjoy reading. Explain them and justify each one with a quotation.</p>",
         "1) Freedom of choice: children should read what they like – “Children must be allowed to choose what they read”. "
         "2) Regular time for reading at school – “every class has fifteen minutes of quiet reading after lunch”. "
         "3) Reading aloud by adults, even for older children – “Even eleven-year-olds love being read to”.",
         "1 pt par clé (0,5 explication + 0,5 citation exacte)."),
    comp("d", 2, "<p>Explain the following expressions in context: “reluctant readers”, “be a model”, “scrolling”.</p>",
         "“Reluctant readers” are children who don’t want to read or who find reading difficult and boring. “Be a model” means that parents "
         "should show a good example, because children copy adults. “Scrolling” means moving quickly through content on a phone screen with "
         "your finger, for example on social media.",
         "Barème indicatif : 0,75 + 0,5 + 0,75."),
]
q4e = [
    expr(S, "e", 4, "<p>What is your best memory of a book from your childhood? (40 words)</p>", 40,
         "My best memory is “Matilda” by Roald Dahl. My mother read it to me every evening when I was eight. I loved Matilda because she was "
         "clever and brave, and I laughed a lot at the terrible headmistress, Miss Trunchbull.",
         ["Un livre identifié (titre, auteur) et un souvenir situé (âge, circonstances).",
          "Expression des sentiments et justification (<em>I loved… because…</em>).",
          "Correction du récit au passé.",
          "Respect du nombre de mots (environ 40)."],
         ["my favourite book was…", "to read aloud / to be read to", "at bedtime", "the main character",
          "I could not put it down", "it made me laugh / cry"]),
    expr(S, "f", 6, "<p>As a primary school teacher in France, how would you help your pupils to enjoy stories in English? "
                    "Give concrete examples. (80 words)</p>", 80,
         "First, I would read picture books aloud with lots of repetition, like “The Very Hungry Caterpillar” or “Brown Bear, Brown Bear, "
         "What Do You See?”. Pupils can join in with the repeated sentences and use flashcards or puppets. Then, I would create an English "
         "reading corner with simple books and audiobooks. Finally, pupils could act out a story or make their own mini-book. The goal is "
         "pleasure, not a test: when children feel successful, they want to discover more stories.",
         ["Propositions concrètes, réalistes et adaptées à des élèves débutants (albums à structure répétitive, supports visuels).",
          "Démarche progressive et organisée (<em>first, then, finally</em>).",
          "Lien avec le texte ou avec la notion de plaisir de lire (motivation, réussite).",
          "Correction de la langue : conditionnel, modaux, lexique de la classe."],
         ["a picture book, a big book", "to read aloud", "to join in", "flashcards, puppets", "a reading corner",
          "to act out a story", "repetitive structure / a repeated sentence", "the goal is…"]),
]
SUJETS.append(sujet(4, S, "Screens and reading for pleasure", "Écrans, lecture plaisir et enfance (Royaume-Uni)", False, [
    partie("E1", "C", "Compréhension – Reading for pleasure in a digital world", 10, D4 + CONSIGNE_C, q4c),
    partie("E2", "E", "Expression", 10, CONSIGNE_E, q4e),
], source="Sujet d’entraînement original (document rédigé pour l’entraînement ; interview fictive).",
   remarque="Chiffre cité : enquête annuelle du National Literacy Trust (2024) – environ 35 % des 8-18 ans disaient aimer lire pendant leur temps libre, le niveau le plus bas depuis 2005."))

# =====================================================================
# Sujet 5 — Bilingual education in Wales
# =====================================================================
S = "ang-wales-bilingual"
D5 = doc("“Bore da!”: growing up bilingual in Wales", [
    "At 8.45 on a Monday morning, the playground of a primary school in Cardiff is full of noise. “Bore da!” (“Good morning!”) says the "
    "head teacher at the gate. Most children answer in Welsh, although many of them speak only English at home. This is a Welsh-medium "
    "school: maths, science and history are all taught in Welsh, and English lessons usually start a little later, around the age of seven.",
    "Welsh is one of the oldest living languages in Europe. But in the nineteenth and twentieth centuries, the number of speakers fell "
    "dramatically. In some schools in the 1800s, children caught speaking Welsh were punished with the “Welsh Not”, a piece of wood hung "
    "around their neck. The first state-funded Welsh-medium school only opened in 1947, in Llanelli.",
    "Today, around a quarter of primary pupils in Wales attend a Welsh-medium school, and all pupils learn Welsh until the age of sixteen. "
    "The Welsh Government has an ambitious target called Cymraeg 2050: one million Welsh speakers by 2050. In the 2021 census, about "
    "538,000 people – 17.8% of the population aged three or over – said they could speak Welsh.",
    "Parents give different reasons for their choice. “Neither my husband nor I speak Welsh,” explains one mother. “But we wanted our son "
    "to feel part of the culture of the country he lives in. And we read that bilingual children often find it easier to learn a third "
    "language.” Others admit that helping with homework can be difficult, so many schools run Welsh classes for families.",
    "Outside the classroom, the language is very much alive: children compete in singing, dancing and poetry at the Urdd Eisteddfod, one "
    "of the largest youth festivals in Europe, and watch cartoons on S4C, the Welsh-language TV channel.",
])
q5c = [
    comp("a", 2, "<p>What is a “Welsh-medium school”? Explain in your own words, using the example of the school in Cardiff.</p>",
         "It is a school where Welsh is the language used to teach most subjects: children learn maths, science or history in Welsh, not in "
         "English. English is taught as a subject, but usually only from about seven. In the Cardiff school, even children from "
         "English-speaking families use Welsh every day.",
         "1 pt pour la définition (langue d’enseignement ≠ langue enseignée), 1 pt pour l’exemple (salutation en gallois, élèves "
         "anglophones à la maison, anglais introduit vers 7 ans)."),
    comp("b", 3, "<p>Show how the situation of the Welsh language has changed from the past to the present, and what the future goal is. "
                 "Use precise elements from the text.</p>",
         "In the past, Welsh was in danger: fewer and fewer people spoke it, and in the 1800s some schools even punished children for using it "
         "with the “Welsh Not”. The first public Welsh-medium school did not open until 1947. Today, the language is supported by schools: "
         "about 25% of primary pupils go to Welsh-medium schools and everyone studies Welsh until 16. In 2021, 17.8% of the population could "
         "speak it. For the future, the government wants one million Welsh speakers by 2050 (the Cymraeg 2050 plan).",
         "1 pt par période (passé : déclin et répression ; présent : place à l’école et chiffres du recensement ; futur : objectif "
         "<em>Cymraeg 2050</em>)."),
    comp("c", 3, "<p>Why do some parents choose a Welsh-medium school although they don’t speak Welsh? What difficulty can they face, and how "
                 "do schools help? Quote the text.</p>",
         "They want their child to belong to Welsh culture – “to feel part of the culture of the country he lives in” – and they think "
         "bilingualism helps with other languages: “bilingual children often find it easier to learn a third language”. The difficulty is "
         "that they cannot always help with homework in Welsh; that is why “many schools run Welsh classes for families”.",
         "1 pt par élément (deux raisons, une difficulté et la réponse des écoles), citations exactes exigées."),
    comp("d", 2, "<p>Find in the text a word or expression meaning: (1) “decreased a lot”; (2) “goal”; (3) “take part in a competition”. "
                 "(4) Explain: “the language is very much alive”.</p>",
         "(1) “fell dramatically”. (2) “target”. (3) “compete”. (4) It means that Welsh is not only a school subject: people really use it "
         "in their free time, in festivals, music, poetry and on television.",
         "Barème : 0,5 par réponse. Culture : l’<em>Urdd</em> (mouvement de jeunesse gallois fondé en 1922) organise chaque année son "
         "Eisteddfod, festival de concours artistiques en gallois."),
]
q5e = [
    expr(S, "e", 4, "<p>Would you like your own children to grow up bilingual? Why or why not? (40 words)</p>", 40,
         "Yes, I would love my children to grow up bilingual. Speaking two languages opens your mind to other cultures and makes travelling "
         "easier. It can also help at school and later at work. However, parents must be patient and consistent.",
         ["Réponse claire et justifiée par au moins deux arguments.",
          "Nuance ou limite évoquée (<em>however…</em>).",
          "Correction de la langue : <em>would like / would love + to</em>, gérondif sujet (<em>speaking two languages…</em>).",
          "Respect du nombre de mots (environ 40)."],
         ["I would love my children to…", "to grow up bilingual", "to open your mind", "a mother tongue / a native language",
          "however", "to be patient and consistent"]),
    expr(S, "f", 6, "<p>In many French classrooms, some pupils speak another language at home. As a primary school teacher, how could you make "
                    "these languages visible and use them to help all your pupils learn? (80 words)</p>", 80,
         "I think home languages are a treasure for the whole class. First, I could display a “hello” poster with all the languages spoken "
         "by my pupils, and we could greet each other in a different language every morning. Then, I would invite parents to read a short "
         "story in their language. In English lessons, pupils could compare words in several languages. This way, bilingual children feel "
         "proud, and the others become curious and more open to learning languages.",
         ["Propositions concrètes et réalistes pour une classe de primaire (affichage, rituels, participation des familles).",
          "Justification des bénéfices pour tous les élèves (estime de soi, curiosité, conscience linguistique).",
          "Organisation logique (<em>first, then, this way</em>) et lien possible avec l’enseignement de l’anglais.",
          "Correction de la langue : modaux (<em>could, would</em>), lexique de l’école."],
         ["a home language", "to display a poster", "to greet each other", "to invite parents to…",
          "to compare words", "to feel proud", "to be open to…", "language awareness"]),
]
SUJETS.append(sujet(5, S, "Growing up bilingual in Wales", "Le bilinguisme gallois-anglais à l’école (pays de Galles)", False, [
    partie("E1", "C", "Compréhension – Growing up bilingual in Wales", 10, D5 + CONSIGNE_C, q5c),
    partie("E2", "E", "Expression", 10, CONSIGNE_E, q5e),
], source="Sujet d’entraînement original (document rédigé pour l’entraînement)."))

# =====================================================================
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"sujets": SUJETS}, f, ensure_ascii=False, indent=1)
    f.write("\n")

# Vérifications
for s in SUJETS:
    tp = 0
    for p in s["parties"]:
        sq = sum(q["points"] for q in p["questions"])
        assert abs(sq - p["points"]) < 1e-9, (s["id"], p["id"], sq)
        for q in p["questions"]:
            assert (q["points"] * 4) == int(q["points"] * 4)
        tp += p["points"]
    assert tp == s["total"] == 20, s["id"]
    for p in s["parties"]:
        if 'class="doc"' in p["intro"]:
            m = re.search(r'<p class="doc-title">.*?</p>(.*)<p class="doc-src">', p["intro"])
            print(s["id"], "document :", wc(m.group(1)), "mots")
for sid, qid, target, n in WORDCOUNTS:
    ok = abs(n - target) <= target * 0.1
    print(sid, qid, "cible", target, "compte", n, "OK" if ok else "HORS PLAGE")
