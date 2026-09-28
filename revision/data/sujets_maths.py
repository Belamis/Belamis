# -*- coding: utf-8 -*-
# Sujets de mathématiques du CRPE BAC+3 (1re épreuve, partie B) : énoncés, figures, corrigés.
# Lancer : python3 data/sujets_maths.py  (régénère data/maths.js)
# Tous les résultats numériques des corrigés sont recalculés ici (assert) avant d'être écrits.
import json, math, os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- outils d'écriture
def F(a, b):
    """Fraction écrite à la verticale."""
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

def n(x, d=None):
    """Nombre au format français (virgule, espace fine pour les milliers)."""
    if d is not None:
        x = round(x, d)
        s = f"{x:,.{d}f}"
    else:
        s = f"{x:,}" if isinstance(x, int) else ("%g" % x if abs(x) < 1e15 else str(x))
        if "e" in s:
            s = f"{x:,}"
    return s.replace(",", " ").replace(".", ",")

def table(head, rows, cls="mtable"):
    h = "".join(f"<th>{c}</th>" for c in head) if head else ""
    body = "".join("<tr>" + "".join(f"<t{'h' if j == 0 and r[0] is not None and str(r[0]).startswith('§') else 'd'}>{str(c).lstrip('§')}</t{'h' if j == 0 and str(r[0]).startswith('§') else 'd'}>" for j, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="{cls}">{"<thead><tr>" + h + "</tr></thead>" if h else ""}<tbody>{body}</tbody></table></div>'

def svg(w, h, body, label):
    return f'<figure class="fig"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">{body}</svg></figure>'

def txt(x, y, s, anchor="middle", size=13, cls=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" class="{cls}">{s}</text>'

# Blocs Scratch en HTML
def sb(kind, html, inner=None):
    if inner is not None:
        return f'<div class="sb sb-{kind} sb-c"><div class="sb-h">{html}</div><div class="sb-in">{"".join(inner)}</div><div class="sb-f"></div></div>'
    return f'<div class="sb sb-{kind}">{html}</div>'

def val(v):
    return f'<span class="sb-v">{v}</span>'

def scratch(*blocks):
    return f'<div class="scratch" aria-label="Script Scratch">{"".join(blocks)}</div>'

# ---------------------------------------------------------------- figures
def fig_musee():
    # axes : x de 0 à 12 visites, y de 0 à 320 €
    X0, Y0, W, H = 50, 250, 520, 220
    sx, sy = W / 12, H / 320
    P = lambda x, y: (X0 + x * sx, Y0 - y * sy)
    g = []
    for i in range(0, 13):
        x, _ = P(i, 0); g.append(f'<line x1="{x:.1f}" y1="{Y0}" x2="{x:.1f}" y2="{Y0-H}" class="grid"/>')
        g.append(txt(x, Y0 + 16, i, size=11))
    for v in range(0, 301, 50):
        _, y = P(0, v); g.append(f'<line x1="{X0}" y1="{y:.1f}" x2="{X0+W}" y2="{y:.1f}" class="grid"/>')
        g.append(txt(X0 - 6, y + 4, v, "end", 11))
    g.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0+W}" y2="{Y0}" class="axis"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0-H}" class="axis"/>')
    def seg(f, x1, x2, cls):
        a, b = P(x1, f(x1)), P(x2, f(x2))
        return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="{cls}"/>'
    g.append(seg(lambda x: 45 * x, 0, 320 / 45, "c1"))
    g.append(seg(lambda x: 90 + 25.5 * x, 0, (320 - 90) / 25.5, "c2"))
    g.append(seg(lambda x: 300, 0, 12, "c3"))
    g.append(txt(X0 + W, Y0 + 32, "nombre de visites de classe", "end", 11))
    g.append(txt(X0 - 40, Y0 - H - 8, "prix (€)", "start", 11))
    return svg(600, 290, "".join(g), "Représentation graphique des prix des trois formules en fonction du nombre de visites")

def fig_demi_cercles():
    s = 200; x0, y0 = 20, 10
    body = (f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" class="shade"/>'
            f'<path d="M{x0},{y0} A{s/2},{s/2} 0 0 1 {x0},{y0+s} Z" class="paper"/>'
            f'<path d="M{x0+s},{y0} A{s/2},{s/2} 0 0 0 {x0+s},{y0+s} Z" class="paper"/>'
            f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" class="stroke"/>'
            f'<path d="M{x0},{y0} A{s/2},{s/2} 0 0 1 {x0},{y0+s}" class="stroke"/>'
            f'<path d="M{x0+s},{y0} A{s/2},{s/2} 0 0 0 {x0+s},{y0+s}" class="stroke"/>')
    return svg(240, 220, body, "Carré de 8 cm dans lequel sont inscrits deux demi-cercles ; la zone grisée est le reste du carré")

def fig_ombre():
    A, D, B = (40, 200), (180, 200), (460, 200)
    E, C = (180, 160), (460, 40)
    b = (f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" class="stroke"/>'
         f'<line x1="{D[0]}" y1="{D[1]}" x2="{E[0]}" y2="{E[1]}" class="thick"/>'
         f'<line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" class="thick"/>'
         f'<rect x="{D[0]}" y="{D[1]-10}" width="10" height="10" class="stroke"/><rect x="{B[0]-10}" y="{B[1]-10}" width="10" height="10" class="stroke"/>'
         + txt(A[0], A[1] + 18, "A") + txt(D[0], D[1] + 18, "D") + txt(B[0], B[1] + 18, "B") + txt(E[0] - 10, E[1] - 4, "E") + txt(C[0] + 12, C[1], "C")
         + txt(D[0] + 30, 186, "0,2 m", size=12) + txt(B[0] + 36, 124, "1,2 m", size=12) + txt((A[0] + B[0]) / 2, 234, "9 m", size=12)
         + f'<line x1="{A[0]}" y1="222" x2="{B[0]}" y2="222" class="stroke" marker-end="url(#ar)" marker-start="url(#ar)"/>'
         + '<defs><marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fillink"/></marker></defs>')
    return svg(520, 245, b, "Source lumineuse en A, objet [DE] de 0,2 m, écran [BC] de 1,2 m à 9 m de A ; figure non à l’échelle")

def fig_triangle(a, b, c, la, lb, lc, label):
    # triangle schématique ABC avec longueurs sur les côtés
    A, B, C = (230, 30), (60, 80), (110, 190)
    body = (f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" class="stroke"/>'
            + txt(A[0] + 10, A[1], a) + txt(B[0] - 12, B[1], b) + txt(C[0] - 4, C[1] + 16, c)
            + txt((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 - 8, lc, size=12) + txt((B[0] + C[0]) / 2 - 30, (B[1] + C[1]) / 2 + 4, la, size=12)
            + txt((A[0] + C[0]) / 2 + 30, (A[1] + C[1]) / 2 + 6, lb, size=12))
    return svg(300, 210, body, label)

def fig_hexagone():
    cx, cy, r = 120, 110, 80
    pts = [(cx + r * math.cos(math.radians(90 + 60 * k)), cy - r * math.sin(math.radians(90 + 60 * k))) for k in range(6)]
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return svg(240, 220, f'<polygon points="{poly}" class="stroke"/>' + txt(cx, cy + 4, "côté : 50 pas", size=12), "Hexagone régulier de côté 50 pas")

def fig_motif():
    cell = 18; out = []
    for k in range(1, 5):
        ox, oy = 20 + (k - 1) * 150, 40
        out.append(txt(ox + 55, 22, f"Étape {k}", size=13))
        cells = []
        # motif : une ligne de k carreaux en haut, puis deux lignes de k − 1 carreaux alignées à droite (3k − 2)
        for i in range(k):
            cells.append((i, 0))
        for r in (1, 2):
            for i in range(1, k):
                cells.append((i, r))
        for (cx, cy) in sorted(set(cells)):
            out.append(f'<rect x="{ox + cx*cell}" y="{oy + cy*cell}" width="{cell}" height="{cell}" class="tile"/>')
        assert len(set(cells)) == 3 * k - 2
    return svg(620, 130, "".join(out), "Motif évolutif : étape 1 : 1 carreau ; étape 2 : 4 ; étape 3 : 7 ; étape 4 : 10 carreaux")

def fig_pentagone():
    cx, cy, r = 150, 120, 90
    names = ["A", "B", "C", "D", "E"]
    pts = [(cx + r * math.cos(math.radians(90 - 72 * k)), cy - r * math.sin(math.radians(90 - 72 * k))) for k in range(5)]
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" class="stroke thin"/><polygon points="{poly}" class="stroke"/>'
    for (x, y), nm in zip(pts, names):
        b += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" class="stroke thin"/>'
        dx, dy = (x - cx) / r * 14, (y - cy) / r * 14
        b += txt(x + dx, y + dy + 4, nm)
    b += txt(cx + 10, cy + 16, "O", size=12)
    return svg(300, 240, b, "Pentagone régulier ABCDE inscrit dans un cercle de centre O")

def fig_axe():
    X0, U = 60, 320  # 0 en X0, 1 unité = U px, graduation de 1/8
    b = f'<line x1="10" y1="60" x2="560" y2="60" class="stroke"/>'
    for k in range(-1, 14):
        x = X0 + k * U / 8
        b += f'<line x1="{x:.1f}" y1="54" x2="{x:.1f}" y2="66" class="stroke"/>'
    for lab, k, below in (("O", 0, "0"), ("A", 4, "<tspan font-style='italic'>a</tspan>"), ("U", 8, "1"), ("B", 11, "<tspan font-style='italic'>b</tspan>")):
        x = X0 + k * U / 8
        b += txt(x, 44, lab) + txt(x, 86, below)
    return svg(570, 100, b, "Axe gradué : O d’abscisse 0, U d’abscisse 1, chaque unité est partagée en 8 ; A est à 4 graduations de O, B à 11 graduations")

def fig_roue():
    cx, cy, r = 110, 110, 90
    secs = [("Bleu", 0, 90, "c-blue"), ("Jaune", 90, 210, "c-yellow"), ("Rouge", 210, 360, "c-red")]
    b = ""
    for nm, a0, a1, cls in secs:
        p0 = (cx + r * math.cos(math.radians(a0 - 90)), cy + r * math.sin(math.radians(a0 - 90)))
        p1 = (cx + r * math.cos(math.radians(a1 - 90)), cy + r * math.sin(math.radians(a1 - 90)))
        large = 1 if a1 - a0 > 180 else 0
        b += f'<path d="M{cx},{cy} L{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 {large} 1 {p1[0]:.1f},{p1[1]:.1f} Z" class="{cls}"/>'
        m = math.radians((a0 + a1) / 2 - 90)
        b += txt(cx + 0.6 * r * math.cos(m), cy + 0.6 * r * math.sin(m) + 4, f"{nm} ({a1 - a0}°)", size=11)
    b += f'<polygon points="{cx-7},{cy-r-14} {cx+7},{cy-r-14} {cx},{cy-r+2}" class="fillink"/>'
    return svg(220, 220, b, "Roue partagée en trois secteurs : bleu 90°, jaune 120°, rouge 150°")

def fig_mat():
    H, M, S = (80, 200), (80, 50), (380, 200)
    K, Fp = (S[0] - 0.4 * (S[0] - H[0]), 200), (S[0] - 0.4 * (S[0] - H[0]), S[1] - 0.4 * (S[1] - M[1]))  # SF = 4/10 de SM
    b = (f'<polygon points="{H[0]},{H[1]} {M[0]},{M[1]} {S[0]},{S[1]}" class="stroke"/>'
         f'<line x1="{Fp[0]}" y1="{Fp[1]}" x2="{K[0]}" y2="{K[1]}" class="stroke dash"/>'
         f'<rect x="{H[0]}" y="{H[1]-10}" width="10" height="10" class="stroke"/><rect x="{K[0]}" y="{K[1]-10}" width="10" height="10" class="stroke"/>'
         + txt(H[0] - 12, H[1] + 4, "H") + txt(M[0] - 12, M[1], "M") + txt(S[0] + 12, S[1] + 4, "S") + txt(K[0], K[1] + 18, "K") + txt(Fp[0] + 4, Fp[1] - 8, "F")
         + txt(H[0] - 30, 130, "6 m", size=12) + txt(155, 220, "8 m", size=12))
    return svg(420, 235, b, "Mât vertical [MH] de 6 m, point d’ancrage S au sol à 8 m de H, fanion F sur la corde [MS] et K son projeté au sol")

def fig_potager():
    s = 20  # 1 m = 20 px
    x0, y0, L, l = 30, 20, 12 * s, 7 * s
    b = (f'<rect x="{x0}" y="{y0}" width="{L}" height="{l}" class="stroke"/>'
         f'<path d="M{x0+L},{y0} A{l/2},{l/2} 0 0 1 {x0+L},{y0+l}" class="stroke"/>'
         f'<line x1="{x0+L}" y1="{y0}" x2="{x0+L}" y2="{y0+l}" class="stroke dash"/>'
         + txt(x0 + L / 2, y0 + l + 18, "12 m", size=12) + txt(x0 - 6, y0 + l / 2 + 4, "7 m", "end", 12))
    return svg(360, 190, b, "Potager : rectangle de 12 m sur 7 m prolongé par un demi-disque de diamètre 7 m")

def fig_cuves():
    X0, Y0, W, H = 50, 230, 500, 200
    sx, sy = W / 20, H / 320
    P = lambda x, y: (X0 + x * sx, Y0 - y * sy)
    g = []
    for i in range(0, 21, 2):
        x, _ = P(i, 0); g.append(f'<line x1="{x:.1f}" y1="{Y0}" x2="{x:.1f}" y2="{Y0-H}" class="grid"/>'); g.append(txt(x, Y0 + 16, i, size=11))
    for v in range(0, 321, 40):
        _, y = P(0, v); g.append(f'<line x1="{X0}" y1="{y:.1f}" x2="{X0+W}" y2="{y:.1f}" class="grid"/>'); g.append(txt(X0 - 6, y + 4, v, "end", 11))
    g.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0+W}" y2="{Y0}" class="axis"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0-H}" class="axis"/>')
    a1, a2 = P(0, 300), P(15, 0); g.append(f'<line x1="{a1[0]:.1f}" y1="{a1[1]:.1f}" x2="{a2[0]:.1f}" y2="{a2[1]:.1f}" class="c1"/>')
    b1, b2 = P(0, 180), P(20, 20); g.append(f'<line x1="{b1[0]:.1f}" y1="{b1[1]:.1f}" x2="{b2[0]:.1f}" y2="{b2[1]:.1f}" class="c2"/>')
    g.append(txt(P(3, 250)[0], P(3, 250)[1], "cuve A", "start", 12, "l1") + txt(P(15, 75)[0], P(15, 75)[1], "cuve B", "start", 12, "l2"))
    g.append(txt(X0 + W, Y0 + 32, "nombre de jours", "end", 11) + txt(X0 - 40, Y0 - H - 8, "volume d’eau (L)", "start", 11))
    return svg(580, 270, "".join(g), "Volume d’eau des cuves A et B en fonction du nombre de jours")

def fig_arbre():
    b = ""
    def node(x, y, s): return txt(x, y + 4, s, "start", 13)
    R = (20, 110); T, NT = (170, 55), (170, 165)
    for p, lab in ((T, "0,08"), (NT, "0,92")):
        b += f'<line x1="{R[0]+10}" y1="{R[1]}" x2="{p[0]-8}" y2="{p[1]}" class="stroke"/>' + txt((R[0] + p[0]) / 2, (R[1] + p[1]) / 2 - 6, lab, size=12)
    b += node(T[0], T[1], "T") + node(NT[0], NT[1], "<tspan text-decoration='overline'>T</tspan>")
    for p, a, bb in ((T, "0,95", "0,05"), (NT, "0,10", "0,90")):
        up, dn = (330, p[1] - 30), (330, p[1] + 30)
        b += f'<line x1="{p[0]+18}" y1="{p[1]}" x2="{up[0]-8}" y2="{up[1]}" class="stroke"/>' + txt((p[0] + up[0]) / 2 + 8, (p[1] + up[1]) / 2 - 6, a, size=12)
        b += f'<line x1="{p[0]+18}" y1="{p[1]}" x2="{dn[0]-8}" y2="{dn[1]}" class="stroke"/>' + txt((p[0] + dn[0]) / 2 + 8, (p[1] + dn[1]) / 2 + 16, bb, size=12)
        b += node(up[0], up[1], "P") + node(dn[0], dn[1], "<tspan text-decoration='overline'>P</tspan>")
    return svg(380, 220, b, "Arbre pondéré : T (0,08) puis P (0,95) ; non T (0,92) puis P (0,10)")

# ---------------------------------------------------------------- types d'exercices
TYPES = {
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
    "suites": "Suites (lycée)",
}

def Q(id, type, points, enonce, corrige, niveau="c4"):
    return {"id": id, "type": type, "points": points, "enonce": enonce, "corrige": corrige, "niveau": niveau}

def EX(num, points, titre, intro, questions):
    return {"id": f"E{num}", "label": f"Exercice {num}", "short": f"Ex. {num}", "titre": titre, "points": points, "intro": intro, "questions": questions}

SUJETS = []

# ================================================================ Sujet 0 officiel
nums = [Fr(3, 2), Fr(8, 4), Fr(3, 4), Fr(7, 10), Fr(1), Fr(4, 3), Fr(133, 100), 1 + Fr(3, 100)]
assert sorted(nums) == [Fr(7, 10), Fr(3, 4), Fr(1), Fr(103, 100), Fr(133, 100), Fr(4, 3), Fr(3, 2), Fr(2)]
cost = lambda v: (45 * v, 90 + 25.5 * v, 300)
assert cost(4) == (180, 192, 300) and cost(8) == (360, 294.0, 300)
assert min(v for v in range(1, 30) if 300 < 90 + 25.5 * v) == 9
assert min(v for v in range(1, 30) if 90 + 25.5 * v < 45 * v) == 5
assert round(294 * 0.85, 2) == 249.9
aire_grise = 64 - 16 * math.pi
peint_m2 = 2 * (100 - 25 * math.pi)
assert math.ceil(peint_m2 / 7 / 0.75) == 9
filles, garcons = 88, 72
assert filles + garcons == 160 and filles == 0.55 * 160
util = filles // 2 + garcons * 3 // 4
assert util == 98 and round(100 * 44 / 98) == 45

SUJETS.append({
 "id": "m-sujet0", "num": 0, "officiel": True, "titre": "Sujet 0 officiel", "source": "Sujet 0 du CRPE BAC+3 (juin 2025), partie B",
 "theme": "Nombres, formules d’un musée, aire, enquête, QCM et Scratch",
 "calculatrice": True,
 "parties": [
  EX(1, 4, "Ranger des nombres, probabilités",
     table(None, [["1,5", F(8, 4), F(3, 4), "0,7", "1", F(4, 3), "1,33", "1 + " + F(3, 100)]], "mtable nums"),
     [Q("1", "nombres", 2, "Ranger les nombres ci-dessus dans l’ordre croissant.",
        f"""<p>On écrit chaque nombre sous forme décimale (ou on compare les fractions) :</p>
<ul><li>{F(8,4)} = 2 ; {F(3,4)} = 0,75 ; 1 + {F(3,100)} = 1,03 ;</li>
<li>{F(4,3)} ≈ 1,333… : ce n’est <strong>pas</strong> un nombre décimal, et {F(4,3)} &gt; 1,33 car {F(4,3)} − 1,33 = {F(4,3)} − {F(133,100)} = {F(1,300)} &gt; 0.</li></ul>
<p class="answer">0,7 &lt; {F(3,4)} &lt; 1 &lt; 1 + {F(3,100)} &lt; 1,33 &lt; {F(4,3)} &lt; 1,5 &lt; {F(8,4)}</p>"""),
      Q("2a", "probas", 1, "On choisit au hasard un de ces nombres, chacun avec la même probabilité. Quelle est la probabilité que le nombre choisi soit un nombre entier ?",
        f"<p>Il y a 8 nombres équiprobables. Les entiers sont 1 et {F(8,4)} = 2, soit 2 issues favorables.</p><p class='answer'>P = {F(2,8)} = {F(1,4)}</p>"),
      Q("2b", "probas", 1, "Quelle est la probabilité que le nombre choisi soit un nombre décimal ?",
        f"<p>Tous les nombres sont décimaux sauf {F(4,3)} (son écriture décimale est illimitée : 1,333…). Les entiers sont aussi des décimaux. 7 issues favorables.</p><p class='answer'>P = {F(7,8)}</p><p><strong>Piège :</strong> un nombre entier est un nombre décimal ; une fraction peut être décimale ({F(3,4)} = 0,75).</p>"),
     ]),
  EX(2, 5, "Trois formules de visites au musée",
     "<p>Un musée propose trois formules de visites guidées pour des classes durant l’année scolaire.</p>"
     "<ul class='box'><li><strong>Formule A :</strong> 45 € par visite de classe.</li><li><strong>Formule B :</strong> abonnement annuel de 90 € par école, auquel s’ajoutent 25,50 € par visite de classe.</li><li><strong>Formule C :</strong> abonnement annuel de 300 €, qui permet autant de visites que l’école le souhaite.</li></ul>"
     + fig_musee() + "<p class='legend'><span class='k1'></span> formule A <span class='k2'></span> formule B <span class='k3'></span> formule C</p>",
     [Q("1a", "fonctions", 1, "Une école a quatre classes. Si chaque classe effectue une visite, quelle formule est la plus avantageuse ?",
        "<p>4 visites : A : 4 × 45 = 180 € ; B : 90 + 4 × 25,50 = 192 € ; C : 300 €.</p><p class='answer'>La formule A est la plus avantageuse (180 €).</p>"),
      Q("1b", "fonctions", 1, "Si chaque classe effectue deux visites, quelle formule est la plus avantageuse ?",
        "<p>8 visites : A : 8 × 45 = 360 € ; B : 90 + 8 × 25,50 = 294 € ; C : 300 €.</p><p class='answer'>La formule B est la plus avantageuse (294 €).</p>"),
      Q("2", "litteral", 1, "À partir de combien de visites de classe la formule C est-elle plus économique que la formule B ?",
        "<p>On cherche le nombre de visites <em>n</em> tel que 90 + 25,5<em>n</em> &gt; 300, soit 25,5<em>n</em> &gt; 210, donc <em>n</em> &gt; 210 ÷ 25,5 ≈ 8,24.</p><p class='answer'>La formule C est plus économique à partir de 9 visites.</p><p>Vérification : 8 visites → B coûte 294 € (&lt; 300) ; 9 visites → B coûte 319,50 € (&gt; 300).</p>"),
      Q("3", "fonctions", 1, "En vous aidant du graphique, déterminer graphiquement le nombre de visites à partir duquel la formule B est plus économique que la formule A.",
        "<p>Les droites de A et de B se coupent pour une abscisse comprise entre 4 et 5 (environ 4,6). Au-delà, la droite de B est en dessous de celle de A.</p><p class='answer'>La formule B est plus économique à partir de 5 visites.</p><p>Vérification : 5 visites → A : 225 €, B : 217,50 €.</p>"),
      Q("4", "proportionnalite", 1, "L’école de quatre classes organise deux visites par classe. Elle choisit la formule la plus avantageuse et la mairie lui accorde une subvention de 15 % du prix à payer. Quel montant l’école doit-elle prévoir ?",
        "<p>8 visites : formule B, 294 €. Réduire de 15 %, c’est multiplier par 1 − 0,15 = 0,85 : 294 × 0,85 = 249,90.</p><p class='answer'>L’école doit prévoir 249,90 €.</p>"),
     ]),
  EX(3, 4, "Un carré et deux demi-cercles",
     "<p>La figure est constituée d’un carré de côté 8 cm dans lequel sont inscrits deux demi-cercles dont le diamètre est un côté du carré.</p>" + fig_demi_cercles(),
     [Q("1", "grandeurs", 0.5, "Déterminer l’aire du carré.", "<p class='answer'>8 × 8 = 64 cm²</p>"),
      Q("2", "grandeurs", 1, "Déterminer la valeur exacte de l’aire grisée, en cm².",
        f"<p>Les deux demi-disques ont un rayon de 4 cm ; ensemble, ils forment un disque d’aire π × 4² = 16π cm².</p><p class='answer'>Aire grisée = 64 − 16π cm² (≈ {n(aire_grise, 2)} cm²)</p><p>La « valeur exacte » demande de garder π.</p>"),
      Q("3a", "grandeurs", 0.5, "On reproduit la figure sur le sol de la cour à l’échelle 125 : 1. Quel sera le côté du nouveau carré, en mètres ?",
        "<p>Échelle 125 : 1 : les longueurs sont multipliées par 125. 8 cm × 125 = 1 000 cm.</p><p class='answer'>10 m</p>"),
      Q("3b", "geometrie", 1, "Quelle sera la longueur de la diagonale de ce nouveau carré ? Donner le résultat en mètres, arrondi au centimètre.",
        f"<p>Dans le triangle rectangle formé par deux côtés et la diagonale, d’après le théorème de Pythagore : d² = 10² + 10² = 200, donc d = √200 = 10√2.</p><p class='answer'>d ≈ {n(10*math.sqrt(2), 2)} m</p>"),
      Q("4", "grandeurs", 1, "On peint la zone grisée de la cour avec deux couches. La peinture couvre 7 m² par litre et se vend en pots de 750 mL. Combien de pots faut-il prévoir ?",
        f"<p>Aire grisée réelle : les aires sont multipliées par 125², ou directement avec le carré de 10 m : 100 − π × 5² = 100 − 25π ≈ {n(100-25*math.pi, 2)} m².</p><p>Deux couches : ≈ {n(peint_m2, 2)} m². Volume : {n(peint_m2, 2)} ÷ 7 ≈ {n(peint_m2/7, 2)} L. Nombre de pots : {n(peint_m2/7, 2)} ÷ 0,75 ≈ {n(peint_m2/7/0.75, 2)}.</p><p class='answer'>Il faut prévoir 9 pots.</p><p><strong>Piège :</strong> on arrondit à l’entier <em>supérieur</em>.</p>"),
     ]),
  EX(4, 3, "Une enquête sur les jeux de cour",
     "<p>« Utilisez-vous les jeux de cour ? » 160 élèves ont répondu, dont 55 % de filles. La moitié des filles a déclaré utiliser les jeux de cour, ainsi que les trois quarts des garçons.</p>",
     [Q("1", "proportionnalite", 1.5, "Compléter le tableau : filles, garçons, total ; utilisent / n’utilisent pas les jeux de cour.",
        "<p>Filles : 55 % de 160 = 88 ; garçons : 72. Filles qui utilisent : 88 ÷ 2 = 44 ; garçons qui utilisent : 72 × 3 ÷ 4 = 54.</p>"
        + table(["", "Filles", "Garçons", "Total"], [["§Utilisent", 44, 54, 98], ["§N’utilisent pas", 44, 18, 62], ["§Total", 88, 72, 160]])),
      Q("2", "proportionnalite", 0.75, "Calculer le pourcentage d’élèves qui utilisent les jeux de cour.",
        "<p>98 ÷ 160 = 0,6125.</p><p class='answer'>61,25 % des élèves</p>"),
      Q("3", "proportionnalite", 0.75, "Parmi les élèves qui utilisent les jeux de cour, quel est le pourcentage de filles ? Arrondir à l’unité.",
        f"<p>44 ÷ 98 ≈ 0,449.</p><p class='answer'>environ 45 %</p><p><strong>Piège :</strong> la population de référence est celle des 98 utilisateurs, pas les 160 élèves.</p>"),
     ]),
  EX(5, 4, "QCM (aucune justification demandée)",
     "<p>Pour chaque question, une seule réponse est exacte. Une réponse fausse ou l’absence de réponse ne rapporte ni n’enlève de point.</p>",
     [Q("1", "algo", 1, "À l’issue de ce script, quelles valeurs sont affectées à <em>a</em> et <em>b</em> ?" + scratch(sb("var", f"mettre {val('a')} à {val('4')}"), sb("var", f"mettre {val('b')} à {val('a')} + {val('2')}"))
        + "<p>A : a = 4 et b = 2 &nbsp;·&nbsp; B : a = 4 et b = 6 &nbsp;·&nbsp; C : a = 2 et b = 6 &nbsp;·&nbsp; D : a = 2 et b = 2</p>",
        "<p class='answer'>Réponse B</p><p><em>a</em> reçoit 4, puis <em>b</em> reçoit la valeur de <em>a</em> + 2 = 6.</p>"),
      Q("2", "algo", 1, "À l’issue de ce script, quelle valeur est affectée à <em>a</em> ?" + scratch(sb("var", f"mettre {val('a')} à {val('2')}"), sb("ctrl", f"répéter {val('4')} fois", [sb("var", f"mettre {val('a')} à {val('a')} + {val('3')}")]))
        + "<p>A : 20 &nbsp;·&nbsp; B : 12 &nbsp;·&nbsp; C : 14 &nbsp;·&nbsp; D : 2</p>",
        "<p class='answer'>Réponse C</p><p>2 → 5 → 8 → 11 → 14 : on ajoute 3 quatre fois, 2 + 4 × 3 = 14.</p>"),
      Q("3", "grandeurs", 1, "Un pavé droit subit une réduction de rapport 0,4. Son volume est : A : multiplié par 0,4³ &nbsp;·&nbsp; B : multiplié par 0,4² &nbsp;·&nbsp; C : divisé par 0,4³ &nbsp;·&nbsp; D : divisé par 0,4².",
        "<p class='answer'>Réponse A</p><p>Dans un agrandissement ou une réduction de rapport k, les longueurs sont multipliées par k, les aires par k² et les volumes par k³.</p>"),
      Q("4", "grandeurs", 1, "Un réservoir en forme de pavé droit mesure 1,5 m × 1,5 m × 2 m. Son volume en litres est : A : 450 L &nbsp;·&nbsp; B : 4 500 L &nbsp;·&nbsp; C : 4 500 000 L &nbsp;·&nbsp; D : 4,5 L.",
        "<p class='answer'>Réponse B</p><p>V = 1,5 × 1,5 × 2 = 4,5 m³ et 1 m³ = 1 000 L, donc 4 500 L.</p>"),
     ]),
 ]})

# ================================================================ Annale 2026, groupement 2
t = {1: 23, 2: 12, 3: 9, 4: 4, 5: 1, 6: 1, 8: 1, 9: 1, 10: 1, 12: 2, 13: 1, 14: 1, 15: 1, 16: 1, 18: 1, 20: 1, 40: 2}
effectif = sum(t.values()); total_med = sum(k * v for k, v in t.items())
assert effectif == 63 and total_med == 328
serie = sorted(k for k, v in t.items() for _ in range(v)); assert serie[31] == 2
sommes = {}
for a in range(1, 5):
    for b in range(1, 5): sommes[a + b] = sommes.get(a + b, 0) + 1
assert sorted(sommes) == list(range(2, 9)) and sommes[5] == 4 and sommes[6] == 3
assert 3 * (-5 + 4) - 11 == -14 and (-25 - 5) / -4 == 7.5
assert Fr(4, 7) * 3 + 1 == Fr(19, 7) == -4 * Fr(4, 7) + 5
assert 9 * 0.2 / 1.2 == 1.5 or abs(9 * 0.2 / 1.2 - 1.5) < 1e-12
assert round(529 * 0.0113) == 6
assert 18 ** 2 + 24 ** 2 == 30 ** 2 and abs(1.5 * 0.6 - 0.9) < 1e-12 and 6727 // 10 == 112 * (6727 // 1000)
tab_med = table(["Médailles d’or", 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 20, 40], [["§Nombre de pays"] + [t[k] for k in sorted(t)]])

SUJETS.append({
 "id": "m-2026-g2", "num": 1, "officiel": True, "titre": "Session 2026 · groupement 2", "source": "CRPE BAC+3, session 2026 (1er avril 2026), groupement 2, partie B",
 "theme": "Dés, programmes de calcul et fonctions, ombres chinoises, JO de Paris, vrai-faux",
 "calculatrice": True, "noteSur": 10,
 "remarque": "Au concours 2026, la partie maths était notée directement sur 10 : le barème ci-dessous est celui du sujet. La répartition des points entre les questions d’un même exercice est indicative.",
 "parties": [
  EX(1, 1.25, "Deux dés à quatre faces",
     "<p>Dans cet exercice, les probabilités sont données sous forme de fraction irréductible. Enzo lance deux dés identiques à quatre faces, numérotées de 1 à 4, puis additionne les deux nombres obtenus (par exemple 4 et 4 donnent 8).</p>",
     [Q("1", "probas", 0.5, "Montrer qu’il y a 7 sommes possibles et les préciser.",
        "<p>Le tableau à double entrée donne les 4 × 4 = 16 issues équiprobables :</p>" + table(["+", 1, 2, 3, 4], [["§1", 2, 3, 4, 5], ["§2", 3, 4, 5, 6], ["§3", 4, 5, 6, 7], ["§4", 5, 6, 7, 8]]) + "<p class='answer'>Sommes possibles : 2, 3, 4, 5, 6, 7, 8 (7 sommes).</p>"),
      Q("2", "probas", 0.35, f"La probabilité d’obtenir une somme égale à 2 est-elle égale à {F(1,7)} ?",
        f"<p>Non : les 7 sommes ne sont pas équiprobables. La somme 2 n’est obtenue que par (1 ; 1), soit 1 issue sur 16.</p><p class='answer'>P(somme = 2) = {F(1,16)} ≠ {F(1,7)}</p>"),
      Q("3", "probas", 0.4, "L’événement « obtenir 5 » est-il plus probable que « obtenir 6 » ?",
        f"<p>Somme 5 : (1;4), (2;3), (3;2), (4;1) → {F(4,16)} = {F(1,4)}. Somme 6 : (2;4), (3;3), (4;2) → {F(3,16)}.</p><p class='answer'>Oui, obtenir 5 est plus probable.</p>"),
     ]),
  EX(2, 2.5, "Deux programmes de calcul",
     "<div class='two'><ul class='box'><li><strong>Programme A</strong></li><li>Choisir un nombre</li><li>Ajouter 4</li><li>Multiplier le résultat par 3</li><li>Retrancher 11</li></ul><ul class='box'><li><strong>Programme B</strong></li><li>Choisir un nombre</li><li>Multiplier par −4</li><li>Ajouter 5</li></ul></div>",
     [Q("1", "litteral", 0.3, "Nombre obtenu avec le programme A en choisissant −5 ?", "<p>−5 + 4 = −1 ; −1 × 3 = −3 ; −3 − 11 = −14.</p><p class='answer'>−14</p>"),
      Q("2", "litteral", 0.4, "Quel nombre choisir au départ pour obtenir −25 avec le programme B ?", "<p>−4<em>x</em> + 5 = −25 ⇔ −4<em>x</em> = −30 ⇔ <em>x</em> = 7,5. (Ou on remonte le programme : −25 − 5 = −30 ; −30 ÷ (−4) = 7,5.)</p><p class='answer'>7,5</p>"),
      Q("3", "litteral", 0.4, "On note <em>x</em> le nombre de départ. Montrer que le résultat du programme A est 3<em>x</em> + 1.", "<p>(<em>x</em> + 4) × 3 − 11 = 3<em>x</em> + 12 − 11 = 3<em>x</em> + 1.</p>"),
      Q("4a", "fonctions", 0.5, "On pose <em>f</em>(<em>x</em>) = 3<em>x</em> + 1 et <em>g</em>(<em>x</em>) = −4<em>x</em> + 5. Construire leurs représentations graphiques (unité 1 cm).",
        "<p>Ce sont des fonctions affines : leurs courbes sont des droites. Deux points suffisent pour chacune.</p><ul><li><em>f</em> : (0 ; 1) et (1 ; 4) ;</li><li><em>g</em> : (0 ; 5) et (2 ; −3).</li></ul>"),
      Q("4b", "fonctions", 0.4, "Déterminer graphiquement l’antécédent de −3 par <em>g</em>.", "<p>On repère −3 sur l’axe des ordonnées, on rejoint la droite de <em>g</em>, puis on lit l’abscisse. Vérification : −4<em>x</em> + 5 = −3 ⇔ <em>x</em> = 2.</p><p class='answer'>L’antécédent de −3 par <em>g</em> est 2.</p>"),
      Q("4c", "litteral", 0.5, "Déterminer algébriquement l’abscisse du point d’intersection des deux droites. Que représente-t-elle pour les programmes A et B ?",
        f"<p>3<em>x</em> + 1 = −4<em>x</em> + 5 ⇔ 7<em>x</em> = 4 ⇔ <em>x</em> = {F(4,7)}.</p><p class='answer'><em>x</em> = {F(4,7)} : c’est le nombre de départ pour lequel les deux programmes donnent le même résultat ({F(19,7)}).</p>"),
     ]),
  EX(3, 1.5, "Un spectacle d’ombres chinoises",
     "<p>Un objet [DE] de 20 cm doit avoir une ombre [BC] de 1,2 m sur l’écran. La source lumineuse A est à 9 m de l’écran (figure non à l’échelle).</p>" + fig_ombre(),
     [Q("1", "geometrie", 0.4, "Justifier que les droites (BC) et (DE) sont parallèles.", "<p>(DE) et (BC) sont toutes deux perpendiculaires à la droite (AB). Or deux droites perpendiculaires à une même droite sont parallèles.</p>"),
      Q("2", "geometrie", 0.6, "En déduire la distance AD à laquelle placer l’objet.", "<p>D ∈ [AB], E ∈ [AC] et (DE) // (BC) : d’après le théorème de Thalès, AD/AB = DE/BC, donc AD = 9 × 0,2 ÷ 1,2 = 1,5.</p><p class='answer'>AD = 1,5 m</p>"),
      Q("3", "grandeurs", 0.5, "L’objet est une plaque rectangulaire de 20 cm sur 10 cm, parallèle à l’écran. Par quel nombre multiplier son aire pour obtenir celle de l’ombre ?", "<p>L’ombre est un agrandissement de rapport k = 1,2 ÷ 0,2 = 6. Les aires sont multipliées par k².</p><p class='answer'>6² = 36</p>"),
     ]),
  EX(4, 1.75, "Les Jeux olympiques de Paris 2024",
     "<p><strong>Partie A.</strong> 63 pays ont reçu au moins une médaille d’or.</p>" + tab_med
     + "<p><strong>Partie B.</strong> Une médaille d’or pèse 529 g ; elle est en argent recouvert d’or pur, qui représente 1,13 % de sa masse.</p>"
     + "<p><strong>Partie C.</strong> L’insert de la médaille est un hexagone régulier, que l’on veut tracer avec Scratch (côté 50 pas). Nina a écrit ce script, qui ne trace pas l’hexagone :</p>"
     + scratch(sb("event", "quand le drapeau est cliqué"), sb("pen", "stylo en position d’écriture"), sb("move", f"s’orienter à {val('60')}"), sb("ctrl", f"répéter {val('6')} fois", [sb("move", f"avancer de {val('50')} pas"), sb("move", f"tourner ↺ de {val('120')} degrés")]), sb("pen", "relever le stylo")) + fig_hexagone(),
     [Q("A1", "stats", 0.5, "Calculer le nombre moyen de médailles d’or par pays, arrondi au dixième.", f"<p>Somme des médailles : 1 × 23 + 2 × 12 + 3 × 9 + … + 40 × 2 = {total_med}. Moyenne : {total_med} ÷ 63 ≈ {n(total_med/63, 3)}.</p><p class='answer'>≈ 5,2 médailles d’or par pays</p>"),
      Q("A2", "stats", 0.5, "Le Canada a obtenu 9 médailles d’or. Ce nombre est-il supérieur à la médiane ?", "<p>63 valeurs : la médiane est la 32e valeur de la série rangée. Les 23 premières valent 1, les 12 suivantes (24e à 35e) valent 2 : la médiane vaut 2.</p><p class='answer'>Oui : 9 &gt; 2.</p><p>La moyenne (5,2) est bien plus grande que la médiane : quelques pays ont beaucoup de médailles.</p>"),
      Q("B", "proportionnalite", 0.35, "Calculer la masse d’or pur d’une médaille, à l’unité près.", f"<p>529 × 1,13 ÷ 100 = {n(529*0.0113, 4)}.</p><p class='answer'>≈ 6 g</p>"),
      Q("C", "algo", 0.4, "Indiquer la correction à faire dans la boucle (aucune justification attendue).", "<p class='answer'>Remplacer « tourner de 120 degrés » par « tourner de 60 degrés ».</p><p>Explication : pour tracer un polygone régulier à <em>n</em> côtés, le lutin tourne de l’angle extérieur 360° ÷ <em>n</em>, soit 60° pour l’hexagone (et non de l’angle intérieur, 120°).</p>"),
     ]),
  EX(5, 3, "Vrai ou faux ? (réponses justifiées)", "",
     [Q("1", "nombres", 0.5, f"Affirmation 1 : {F(22,25)} est un nombre décimal.", f"<p>{F(22,25)} = {F(88,100)} = 0,88.</p><p class='answer'>Vraie.</p>"),
      Q("2", "proportionnalite", 0.5, "Affirmation 2 : un prix augmente de 50 % puis baisse de 40 % ; il a donc augmenté de 10 %.", "<p>Coefficients multiplicateurs : 1,5 × 0,6 = 0,9 : le prix a <strong>baissé</strong> de 10 %.</p><p class='answer'>Fausse.</p><p>Les pourcentages successifs ne s’additionnent pas.</p>"),
      Q("3", "nombres", 0.5, "Affirmation 3 : le nombre de dizaines de 6 727 est 112 fois plus grand que son nombre de milliers.", "<p>Nombre de dizaines : 672 ; nombre de milliers : 6 ; 6 × 112 = 672.</p><p class='answer'>Vraie.</p><p>Attention : « nombre de dizaines » (672) ≠ « chiffre des dizaines » (2).</p>"),
      Q("4", "nombres", 0.5, "Affirmation 4 : ajouter 13 dixièmes à 25,606 donne 25,736.", "<p>13 dixièmes = 1,3 ; 25,606 + 1,3 = 26,906.</p><p class='answer'>Fausse.</p><p>25,736 correspond à l’ajout de 13 <em>centièmes</em>.</p>"),
      Q("5", "nombres", 0.5, "Affirmation 5 : il existe au moins un entier dont le chiffre des unités est au moins 4, le chiffre des dizaines au moins 3, et dont le produit de ces deux chiffres est égal au nombre de centaines.", "<p>Exemple : 1 234. Chiffre des unités 4, chiffre des dizaines 3, produit 12 ; nombre de centaines de 1 234 : 12.</p><p class='answer'>Vraie (un seul exemple suffit).</p>"),
      Q("6", "geometrie", 0.5, "Affirmation 6 : le triangle ABC tel que AB = 24 cm, BC = 18 cm et AC = 30 cm n’est pas rectangle." + fig_triangle("A", "B", "C", "18 cm", "30 cm", "24 cm", "Triangle ABC : AB = 24 cm, BC = 18 cm, AC = 30 cm"),
        "<p>Le plus grand côté est [AC]. AC² = 900 ; AB² + BC² = 576 + 324 = 900. D’après la réciproque du théorème de Pythagore, ABC est rectangle en B.</p><p class='answer'>Fausse.</p>"),
     ]),
 ]})

# ================================================================ Annale 2026, groupement 1
# tableau : sport 120, musique 75, musique et sport 45
assert 0.4 * 300 == 120 and 0.6 * 75 == 45
assert Fr(300 - 150, 300) == Fr(1, 2) and Fr(45, 120) == Fr(3, 8)
assert 1 + 3 * 19 == 58 and (100 + 2) % 3 == 0 and (2000 + 2) % 3 != 0
assert [x for x in (123.1, 126.2, 129.3)] and Fr(4, 3) < Fr(11, 8)

SUJETS.append({
 "id": "m-2026-g1", "num": 2, "officiel": True, "titre": "Session 2026 · groupement 1", "source": "CRPE BAC+3, session 2026 (1er avril 2026), groupement 1, partie B (d’après un relevé du sujet)",
 "theme": "Tableau à double entrée, motif évolutif et tableur, pentagone, vrai-faux, axe gradué",
 "calculatrice": True, "noteSur": 10,
 "remarque": "Sujet reconstitué à partir d’une photographie : le barème est celui du sujet, la répartition entre questions est indicative.",
 "parties": [
  EX(1, 2, "Activités extrascolaires",
     "<p>Dans une école de 300 élèves : 40 % pratiquent un sport ; 75 pratiquent un instrument de musique ; parmi ces derniers, 60 % pratiquent aussi un sport.</p>",
     [Q("1", "proportionnalite", 1, "Compléter un tableau à double entrée (sport / pas de sport ; instrument / pas d’instrument).",
        "<p>Sport : 40 % de 300 = 120. Musique et sport : 60 % de 75 = 45.</p>" + table(["", "Instrument", "Pas d’instrument", "Total"], [["§Sport", 45, 75, 120], ["§Pas de sport", 30, 150, 180], ["§Total", 75, 225, 300]])),
      Q("2", "probas", 0.5, "On choisit un élève au hasard. Probabilité qu’il pratique au moins l’une des deux activités ?", f"<p>Seuls 150 élèves ne pratiquent ni sport ni instrument : 300 − 150 = 150 en pratiquent au moins une.</p><p class='answer'>{F(150,300)} = {F(1,2)}</p>"),
      Q("3", "probas", 0.5, "On choisit au hasard un élève qui pratique un sport. Probabilité qu’il joue aussi d’un instrument (fraction irréductible) ?", f"<p>On se restreint aux 120 sportifs, dont 45 jouent d’un instrument.</p><p class='answer'>{F(45,120)} = {F(3,8)}</p>"),
     ]),
  EX(2, 2, "Un motif évolutif", fig_motif() + table(["", "A", "B"], [["§1", "Étape", "Nombre de carreaux"], ["§2", 1, 1], ["§3", 2, 4], ["§4", 3, 7], ["§5", 4, 10]]),
     [Q("1", "algo", 0.3, "Décrire comment on passe d’une étape à la suivante.", "<p>Le motif est formé de trois lignes : une ligne de <em>k</em> carreaux en haut et deux lignes de <em>k</em> − 1 carreaux en dessous, alignées à droite. Pour passer à l’étape suivante, on ajoute un carreau au bout gauche de chacune des trois lignes.</p><p class='answer'>+3 carreaux à chaque étape.</p>"),
      Q("2", "nombres", 0.4, "Nombre de carreaux aux étapes 5 et 20 ?", "<p>Étape 5 : 10 + 3 = 13. Étape 20 : 1 + 19 × 3 = 58.</p><p class='answer'>13 et 58</p>"),
      Q("3", "algo", 0.3, "Quelle formule, à étirer vers le bas, saisir en B3 ?", "<p class='answer'>=B2+3</p><p>(Ou =3*A3-2, qui utilise le numéro d’étape.)</p>"),
      Q("4", "litteral", 0.5, "Exprimer, en fonction de <em>n</em>, le nombre de carreaux à l’étape <em>n</em>.", "<p>On part de 1 et on ajoute 3 à chaque étape, (<em>n</em> − 1) fois : 1 + 3(<em>n</em> − 1).</p><p class='answer'>3<em>n</em> − 2</p>"),
      Q("5", "litteral", 0.5, "Le motif compte-t-il exactement 100 carreaux à une étape ? Et 2 000 ?", f"<p>3<em>n</em> − 2 = 100 ⇔ <em>n</em> = 34 : oui, à l’étape 34.</p><p>3<em>n</em> − 2 = 2 000 ⇔ <em>n</em> = {F(2002,3)}, qui n’est pas entier (2 002 n’est pas divisible par 3 : 2 + 0 + 0 + 2 = 4).</p><p class='answer'>100 : oui (étape 34) ; 2 000 : non.</p>"),
     ]),
  EX(3, 2.5, "Des pentagones",
     "<p>Un pentagone régulier ABCDE est inscrit dans un cercle de centre O. <em>Rappel : un polygone régulier a tous ses côtés de même longueur et tous ses angles de même mesure.</em></p>" + fig_pentagone(),
     [Q("a", "geometrie", 0.6, "Justifier que l’angle DOC mesure 72°.", "<p>Les 5 angles au centre AOB, BOC, COD, DOE, EOA interceptent des côtés de même longueur : ils sont égaux et leur somme fait un tour complet.</p><p class='answer'>360° ÷ 5 = 72°</p>"),
      Q("b", "geometrie", 0.6, "Quelle est la nature du triangle OCD ?", "<p>OC = OD (rayons du cercle).</p><p class='answer'>OCD est isocèle en O.</p>"),
      Q("c", "geometrie", 0.7, "Déterminer la mesure de l’angle DCB.", "<p>Dans OCD isocèle en O, les angles à la base mesurent (180° − 72°) ÷ 2 = 54°. De même dans OCB : angle OCB = 54°.</p><p class='answer'>DCB = 54° + 54° = 108°</p>"),
      Q("d", "geometrie", 0.6, "Déterminer la somme des angles de ce pentagone.", "<p>5 angles de 108°.</p><p class='answer'>5 × 108° = 540°</p><p>Formule générale : (n − 2) × 180° pour un polygone à n côtés.</p>"),
     ]),
  EX(4, 1.75, "Vrai ou faux ? (réponses justifiées)", "",
     [Q("1", "nombres", 0.5, "X s’écrit avec quatre chiffres, tous différents de 0. Son nombre de dizaines est 12 et son chiffre des unités est le triple de son chiffre des dixièmes. Affirmation : il y a exactement deux valeurs possibles pour X.",
        "<p>Nombre de dizaines 12 : X s’écrit 12<em>u</em>,<em>d</em> avec <em>u</em> = 3<em>d</em> et des chiffres non nuls : (<em>u</em> ; <em>d</em>) = (3 ; 1), (6 ; 2) ou (9 ; 3).</p><p>X ∈ {123,1 ; 126,2 ; 129,3} : trois valeurs.</p><p class='answer'>Fausse.</p><p>(Si l’on comprend « chiffres tous différents », seule 129,3 convient : l’affirmation reste fausse.)</p>"),
      Q("2", "arithmetique", 0.4, "Affirmation : un entier multiple à la fois de 4 et de 10 est nécessairement multiple de 40.", "<p>Contre-exemple : 20 est multiple de 4 et de 10, mais pas de 40. (Les multiples communs de 4 et 10 sont les multiples de 20.)</p><p class='answer'>Fausse.</p>"),
      Q("3", "proportionnalite", 0.45, "Offre 1 : pour un produit acheté, le deuxième à −50 %. Offre 2 : pour un produit acheté, 50 % de produit en plus offert. Affirmation : ces promotions sont équivalentes.",
        f"<p>Prix unitaire P. Offre 1 : 2 produits pour 1,5P, soit 0,75P par produit (−25 %). Offre 2 : 1,5 produit pour P, soit P ÷ 1,5 ≈ 0,667P par produit (−33 %).</p><p class='answer'>Fausse : l’offre 2 est plus avantageuse.</p>"),
      Q("4", "nombres", 0.4, "Affirmation : le quotient d’un nombre décimal par 4 est un nombre décimal.", "<p>Diviser par 4, c’est multiplier par 0,25. Le produit de deux décimaux est un décimal (d × 0,25 = d × 25 ÷ 100).</p><p class='answer'>Vraie.</p>"),
     ]),
  EX(5, 1.75, "Un axe gradué", "<p>Sur l’axe gradué d’origine O, le point U a pour abscisse 1.</p>" + fig_axe(),
     [Q("1", "nombres", 0.5, "Déterminer les abscisses <em>a</em> et <em>b</em> des points A et B.", f"<p>L’unité est partagée en 8 : chaque graduation vaut {F(1,8)} = 0,125. A est à 4 graduations de O, B à 11.</p><p class='answer'><em>a</em> = {F(4,8)} = 0,5 et <em>b</em> = {F(11,8)} = 1,375</p>"),
      Q("2", "nombres", 0.5, "Abscisse du milieu de [OA], puis de [OB] ?", f"<p>Le milieu a pour abscisse la moyenne des abscisses.</p><p class='answer'>[OA] : 0,25 ; [OB] : {F(11,16)} = 0,6875</p>"),
      Q("3", "nombres", 0.75, f"C et D ont pour abscisses <em>c</em> = 0,45 et <em>d</em> = {F(4,3)}. Proposer une démarche, sans calculatrice, pour savoir si chacun appartient à [AB].",
        f"<p>C : 0,45 &lt; 0,5 = <em>a</em>, donc C ∉ [AB].</p><p>D : on compare {F(4,3)} et {F(11,8)} en les mettant au même dénominateur : {F(4,3)} = {F(32,24)} et {F(11,8)} = {F(33,24)}. Donc 0,5 &lt; {F(4,3)} &lt; {F(11,8)}.</p><p class='answer'>C n’appartient pas à [AB] ; D appartient à [AB].</p>"),
     ]),
 ]})

# ================================================================ Sujet A : la kermesse (original)
assert math.gcd(252, 168) == 84 and 252 // 84 == 3 and 168 // 84 == 2
div84 = [d for d in range(1, 85) if 84 % d == 0]
assert div84 == [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84]
assert 2 * 12 + 4 * 1.5 == 30 and 3 * 12 == 36
assert abs(12 * 0.8 - 9.6) < 1e-9 and abs(1.2 * 0.8 - 0.96) < 1e-9 and round((1 - 10 / 12) * 100, 1) == 16.7
assert round(math.degrees(math.atan(6 / 8)), 1) == 36.9 and 6 * 4 / 10 == 2.4
assert 1.2 ** 2 + 1.6 ** 2 != 2.1 ** 2 and abs(1.2 ** 2 + 1.6 ** 2 - 4) < 1e-9
assert Fr(90, 360) == Fr(1, 4) and Fr(120, 360) == Fr(1, 3) and Fr(150, 360) == Fr(5, 12)
assert 1 - Fr(2, 3) ** 2 == Fr(5, 9)
f = lambda x: x * x - 4 * x
assert f(5) == 5 and f(-3) == 21 and f(0) == 0 == f(4) and min(f(x / 10) for x in range(-100, 100)) == -4

SUJETS.append({
 "id": "m-kermesse", "num": 3, "titre": "Sujet A · La kermesse de l’école",
 "theme": "Arithmétique, pourcentages, Pythagore et trigonométrie, probabilités, Scratch et tableur",
 "calculatrice": True,
 "remarque": "Sujet original, inspiré des annales du CRPE et du brevet. Les questions marquées « Lycée » dépassent le cycle 4 (programme du concours) : ce sont des approfondissements.",
 "parties": [
  EX(1, 4, "Les sachets de friandises",
     "<p>Pour la kermesse, l’école a reçu 252 bonbons et 168 sucettes. On veut préparer des sachets <strong>identiques</strong> (même nombre de bonbons et même nombre de sucettes dans chaque sachet) en utilisant toutes les friandises.</p>",
     [Q("1", "arithmetique", 1, "Décomposer 252 et 168 en produits de facteurs premiers.", "<p class='answer'>252 = 2² × 3² × 7 &nbsp;;&nbsp; 168 = 2³ × 3 × 7</p><p>Méthode : divisions successives par 2, 3, 5, 7… (252 → 126 → 63 → 21 → 7).</p>"),
      Q("2", "arithmetique", 1.5, "Quel est le nombre maximal de sachets ? Quelle sera alors leur composition ?", "<p>Le nombre de sachets doit diviser 252 et 168 : on cherche leur plus grand diviseur commun. On garde les facteurs communs avec le plus petit exposant : 2² × 3 × 7 = 84.</p><p class='answer'>84 sachets, contenant chacun 3 bonbons et 2 sucettes.</p>"),
      Q("3", "arithmetique", 0.5, "Peut-on préparer 12 sachets ?", "<p>252 = 12 × 21 et 168 = 12 × 14 : 12 divise les deux nombres.</p><p class='answer'>Oui : 12 sachets de 21 bonbons et 14 sucettes.</p>"),
      Q("4", "arithmetique", 1, "Donner tous les nombres de sachets possibles.", "<p>Ce sont les diviseurs communs à 252 et 168, c’est-à-dire les diviseurs de 84.</p><p class='answer'>1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84</p>"),
     ]),
  EX(2, 4, "Les tickets de jeu",
     "<p>Un ticket de jeu coûte 1,50 €. Un carnet de 10 tickets coûte 12 €.</p>",
     [Q("1", "proportionnalite", 0.5, "Combien économise-t-on en achetant un carnet plutôt que 10 tickets à l’unité ?", "<p>10 × 1,50 = 15 € ; 15 − 12 = 3.</p><p class='answer'>3 €</p>"),
      Q("2", "proportionnalite", 1, "Quel pourcentage de réduction le carnet représente-t-il ?", "<p>3 ÷ 15 = 0,2.</p><p class='answer'>20 %</p>"),
      Q("3", "proportionnalite", 1, "Léa veut exactement 24 tickets. Quelle est la dépense minimale ?", "<p>2 carnets + 4 tickets : 24 + 6 = 30 €. 3 carnets (30 tickets) coûteraient 36 €.</p><p class='answer'>30 €</p>"),
      Q("4", "proportionnalite", 1.5, "L’an dernier, le carnet coûtait 10 € ; il a augmenté de 20 %. L’an prochain, il baissera de 20 %. Reviendra-t-il à 10 € ? Quel pourcentage de baisse faudrait-il pour revenir exactement à 10 € ?",
        "<p>12 × 0,8 = 9,60 € : non, il sera moins cher qu’il y a deux ans (évolution globale 1,2 × 0,8 = 0,96, soit −4 %).</p><p>Pour revenir de 12 € à 10 € : coefficient 10 ÷ 12 ≈ 0,833, soit une baisse d’environ 16,7 %.</p><p class='answer'>Non (9,60 €) ; il faudrait une baisse d’environ 16,7 %.</p>", "lycee"),
     ]),
  EX(3, 4, "Le mât des fanions",
     "<p>Un mât vertical [MH] de 6 m est tenu par une corde [MS] fixée au sol en S, à 8 m du pied H du mât. Un fanion F est accroché sur la corde à 4 m de S ; K est le point du sol situé à la verticale de F.</p>" + fig_mat(),
     [Q("1", "geometrie", 1, "Calculer la longueur de la corde MS.", "<p>Le triangle MHS est rectangle en H. D’après le théorème de Pythagore : MS² = 6² + 8² = 100.</p><p class='answer'>MS = 10 m</p>"),
      Q("2", "geometrie", 1, "Calculer l’angle MSH que fait la corde avec le sol, au dixième de degré.", f"<p>Dans MHS rectangle en H : tan(MSH) = MH ÷ HS = 6 ÷ 8 = 0,75.</p><p class='answer'>MSH ≈ {n(math.degrees(math.atan(0.75)), 1)}°</p>"),
      Q("3", "geometrie", 1, "À quelle hauteur FK se trouve le fanion ?", "<p>(FK) et (MH) sont perpendiculaires au sol, donc parallèles. Dans le triangle SMH, d’après le théorème de Thalès : SF ÷ SM = FK ÷ MH, soit FK = 6 × 4 ÷ 10.</p><p class='answer'>FK = 2,4 m</p>"),
      Q("4", "geometrie", 1, "Un triangle de renfort a des côtés de 1,2 m, 1,6 m et 2,1 m. Est-il rectangle ?", "<p>Plus grand côté : 2,1² = 4,41. Somme des carrés des deux autres : 1,44 + 2,56 = 4,00. 4,41 ≠ 4,00.</p><p class='answer'>Non (d’après la contraposée du théorème de Pythagore).</p><p>Avec 2 m au lieu de 2,1 m, il le serait.</p>"),
     ]),
  EX(4, 4, "La roue de la fortune", "<p>La roue est partagée en trois secteurs. On gagne un lot si la flèche s’arrête sur le jaune.</p>" + fig_roue(),
     [Q("1", "probas", 1, "Calculer la probabilité de chaque couleur.", f"<p>La probabilité est proportionnelle à l’angle du secteur.</p><p class='answer'>P(bleu) = {F(90,360)} = {F(1,4)} ; P(jaune) = {F(120,360)} = {F(1,3)} ; P(rouge) = {F(150,360)} = {F(5,12)}</p><p>Vérification : {F(3,12)} + {F(4,12)} + {F(5,12)} = 1.</p>"),
      Q("2", "probas", 1, "Sur 300 parties, combien de lots peut-on s’attendre à distribuer ?", f"<p>300 × {F(1,3)} = 100.</p><p class='answer'>environ 100 lots</p><p>C’est une estimation : la fréquence observée se rapproche de la probabilité quand le nombre de parties augmente.</p>"),
      Q("3", "probas", 2, "Pour le gros lot, il faut obtenir deux fois jaune en deux lancers. Calculer cette probabilité, puis celle d’obtenir au moins une fois jaune.", f"<p>Les lancers sont indépendants : P(jaune puis jaune) = {F(1,3)} × {F(1,3)} = {F(1,9)}.</p><p>« Au moins un jaune » est le contraire de « aucun jaune » : 1 − {F(2,3)} × {F(2,3)} = 1 − {F(4,9)} = {F(5,9)}.</p><p class='answer'>{F(1,9)} et {F(5,9)}</p>"),
     ]),
  EX(5, 4, "Un programme sur la tablette",
     "<p>Voici un script Scratch :</p>" + scratch(sb("event", "quand le drapeau est cliqué"), sb("sense", "demander « Choisis un nombre » et attendre"), sb("var", f"mettre {val('x')} à {val('réponse')}"), sb("var", f"mettre {val('résultat')} à {val('x')} × {val('x')} − {val('4')} × {val('x')}"), sb("look", f"dire {val('résultat')}")),
     [Q("1", "algo", 0.5, "Qu’affiche le lutin si l’on choisit 5 ?", "<p>5 × 5 − 4 × 5 = 25 − 20 = 5.</p><p class='answer'>5</p>"),
      Q("2", "algo", 0.5, "Et si l’on choisit −3 ?", "<p>(−3) × (−3) − 4 × (−3) = 9 + 12 = 21.</p><p class='answer'>21</p>"),
      Q("3", "litteral", 1.5, "Quels nombres faut-il choisir pour que le lutin dise 0 ?", "<p><em>x</em>² − 4<em>x</em> = 0 ⇔ <em>x</em>(<em>x</em> − 4) = 0. Un produit est nul si l’un de ses facteurs est nul : <em>x</em> = 0 ou <em>x</em> = 4.</p><p class='answer'>0 ou 4</p>"),
      Q("4", "algo", 0.5, "Dans un tableur, les nombres choisis sont en colonne A. Quelle formule saisir en B2 pour obtenir le résultat ?", "<p class='answer'>=A2*A2-4*A2</p><p>(ou =A2^2-4*A2)</p>"),
      Q("5", "fonctions", 1, "Montrer que le résultat s’écrit (<em>x</em> − 2)² − 4. Quel est le plus petit résultat possible ?", "<p>(<em>x</em> − 2)² − 4 = <em>x</em>² − 4<em>x</em> + 4 − 4 = <em>x</em>² − 4<em>x</em>. Un carré est toujours positif ou nul, donc le résultat est toujours supérieur ou égal à −4, et vaut −4 pour <em>x</em> = 2.</p><p class='answer'>Le plus petit résultat est −4 (pour <em>x</em> = 2).</p>", "lycee"),
     ]),
 ]})

# ================================================================ Sujet B : le potager (original)
perim = 31 + 3.5 * math.pi; aire_pot = 84 + math.pi * 3.5 ** 2 / 2
assert round(perim, 1) == 42.0 and round(aire_pot, 1) == 103.2 and math.ceil(aire_pot * 5 / 40) == 13
assert 1200 / 200 == 6
assert 300 - 20 * 5 == 200 and 300 - 20 * 15 == 0 and 300 - 20 * 10 == 180 - 8 * 10 == 100
vol_cuve = math.pi * 0.4 ** 2 * 1.2 * 1000
assert round(vol_cuve, 1) == 603.2 and 20 * 0.012 * 1000 == 240 and math.ceil(vol_cuve / 240) == 3 and int(vol_cuve // 11) == 54
rec = [2, 5, 3, 8, 6, 4, 9, 7, 5, 12, 5]; srt = sorted(rec)
assert sum(rec) == 66 and sum(rec) / 11 == 6 and srt[5] == 5 and max(rec) - min(rec) == 10 and srt[2] == 4 and srt[8] == 8
assert 91 == 7 * 13 and Fr(2, 3) + Fr(1, 6) == Fr(5, 6) and (1 + 3) ** 2 != 1 + 9 and abs(3.5e-2 - 0.035) < 1e-12

SUJETS.append({
 "id": "m-potager", "num": 4, "titre": "Sujet B · Le potager pédagogique",
 "theme": "Aires et périmètres, fonctions affines, volumes, statistiques, vrai-faux",
 "calculatrice": True,
 "remarque": "Sujet original, inspiré des annales du CRPE et du brevet. Les questions marquées « Lycée » sont des approfondissements hors programme du concours.",
 "parties": [
  EX(1, 4, "Le plan du potager", "<p>Le potager a la forme d’un rectangle de 12 m sur 7 m, prolongé par un demi-disque de diamètre 7 m.</p>" + fig_potager(),
     [Q("1", "grandeurs", 1, "Calculer la longueur de la clôture qui fait le tour du potager, au dixième de mètre.", f"<p>Trois côtés du rectangle (12 + 12 + 7 = 31 m) + un demi-cercle de diamètre 7 m (π × 7 ÷ 2 = 3,5π m).</p><p class='answer'>31 + 3,5π ≈ {n(perim, 1)} m</p><p><strong>Piège :</strong> le côté commun au rectangle et au demi-disque n’est pas clôturé.</p>"),
      Q("2", "grandeurs", 1, "Calculer l’aire du potager, au dixième de m².", f"<p>Rectangle : 12 × 7 = 84 m². Demi-disque de rayon 3,5 m : π × 3,5² ÷ 2 ≈ {n(math.pi*3.5**2/2, 2)} m².</p><p class='answer'>≈ {n(aire_pot, 1)} m²</p>"),
      Q("3", "proportionnalite", 1, "Il faut 5 L de terreau par m². Le terreau est vendu en sacs de 40 L. Combien de sacs acheter ?", f"<p>{n(aire_pot, 2)} × 5 ≈ {n(aire_pot*5, 1)} L ; {n(aire_pot*5, 1)} ÷ 40 ≈ {n(aire_pot*5/40, 2)}.</p><p class='answer'>13 sacs</p>"),
      Q("4", "grandeurs", 1, "Sur un plan à l’échelle 1/200, quelle longueur représente le côté de 12 m ?", "<p>12 m = 1 200 cm ; 1 200 ÷ 200 = 6.</p><p class='answer'>6 cm</p>"),
     ]),
  EX(2, 4, "Deux cuves d’arrosage",
     "<p>La cuve A contient 300 L et on y puise 20 L par jour. La cuve B contient 180 L et on y puise 8 L par jour. On note <em>x</em> le nombre de jours écoulés.</p>" + fig_cuves(),
     [Q("1", "fonctions", 0.5, "Quelle quantité reste-t-il dans la cuve A après 5 jours ?", "<p>300 − 20 × 5 = 200.</p><p class='answer'>200 L</p>"),
      Q("2", "fonctions", 1, "Exprimer les volumes <em>f</em>(<em>x</em>) de la cuve A et <em>g</em>(<em>x</em>) de la cuve B. S’agit-il de fonctions linéaires ?", "<p class='answer'><em>f</em>(<em>x</em>) = 300 − 20<em>x</em> et <em>g</em>(<em>x</em>) = 180 − 8<em>x</em></p><p>Ce sont des fonctions affines, mais pas linéaires (l’ordonnée à l’origine n’est pas nulle : les droites ne passent pas par l’origine).</p>"),
      Q("3", "fonctions", 1, "Au bout de combien de jours la cuve A est-elle vide ? (lecture graphique puis vérification)", "<p>La droite de A coupe l’axe des abscisses en 15. Vérification : 300 − 20<em>x</em> = 0 ⇔ <em>x</em> = 15.</p><p class='answer'>15 jours</p>"),
      Q("4", "litteral", 1.5, "Au bout de combien de jours les deux cuves contiennent-elles la même quantité ? Laquelle ?", "<p>300 − 20<em>x</em> = 180 − 8<em>x</em> ⇔ 120 = 12<em>x</em> ⇔ <em>x</em> = 10. Volume : 300 − 200 = 100.</p><p class='answer'>Après 10 jours, avec 100 L chacune.</p>"),
     ]),
  EX(3, 4, "Le récupérateur d’eau de pluie", "<p>Le récupérateur est un cylindre de rayon 40 cm et de hauteur 1,20 m. Il récupère l’eau d’un toit de 20 m².</p>",
     [Q("1", "grandeurs", 1, "Calculer le volume du récupérateur, en litres, au litre près.", f"<p>V = π × r² × h = π × 0,4² × 1,2 ≈ {n(vol_cuve/1000, 4)} m³, et 1 m³ = 1 000 L.</p><p class='answer'>≈ 603 L</p>"),
      Q("2", "grandeurs", 1, "Une pluie de 12 mm tombe sur le toit (12 mm d’eau sur toute la surface). Quel volume d’eau est recueilli ?", "<p>12 mm = 0,012 m ; 20 × 0,012 = 0,24 m³.</p><p class='answer'>240 L</p>"),
      Q("3", "grandeurs", 1, "Combien de pluies de ce type faut-il pour remplir le récupérateur vide ?", f"<p>{n(vol_cuve, 1)} ÷ 240 ≈ {n(vol_cuve/240, 2)}.</p><p class='answer'>3 pluies</p>"),
      Q("4", "grandeurs", 1, "Avec le récupérateur plein, combien d’arrosoirs de 11 L peut-on remplir entièrement ?", f"<p>{n(vol_cuve, 1)} ÷ 11 ≈ {n(vol_cuve/11, 2)}.</p><p class='answer'>54 arrosoirs</p><p>Ici on arrondit à l’entier <em>inférieur</em> : le 55e ne serait pas plein.</p>"),
     ]),
  EX(4, 4, "La récolte de tomates", "<p>Masse de tomates récoltée chaque semaine (en kg), pendant 11 semaines :</p>" + table(["Semaine", *range(1, 12)], [["§Masse (kg)", *rec]]),
     [Q("1", "stats", 1, "Calculer la masse moyenne récoltée par semaine.", "<p>Somme : 66 kg ; 66 ÷ 11 = 6.</p><p class='answer'>6 kg</p>"),
      Q("2", "stats", 1, "Déterminer la médiane et l’interpréter.", "<p>Série rangée : 2 ; 3 ; 4 ; 5 ; 5 ; <strong>5</strong> ; 6 ; 7 ; 8 ; 9 ; 12. 11 valeurs : la médiane est la 6e.</p><p class='answer'>Médiane : 5 kg. Au moins la moitié des semaines, on a récolté 5 kg ou moins (et au moins la moitié, 5 kg ou plus).</p>"),
      Q("3", "stats", 0.5, "Calculer l’étendue.", "<p class='answer'>12 − 2 = 10 kg</p>"),
      Q("4", "stats", 1.5, "Déterminer le premier et le troisième quartile, puis l’écart interquartile.", "<p>Q1 : plus petite valeur telle qu’au moins 25 % des valeurs lui soient inférieures ou égales ; 11 × 0,25 = 2,75 → 3e valeur. Q3 : 11 × 0,75 = 8,25 → 9e valeur.</p><p class='answer'>Q1 = 4 kg ; Q3 = 8 kg ; écart interquartile : 4 kg</p>", "lycee"),
     ]),
  EX(5, 4, "Vrai ou faux ? (réponses justifiées)", "",
     [Q("1", "arithmetique", 0.8, "Affirmation 1 : 91 est un nombre premier.", "<p>91 = 7 × 13.</p><p class='answer'>Fausse.</p>"),
      Q("2", "nombres", 0.8, f"Affirmation 2 : {F(2,3)} + {F(1,6)} = {F(3,9)}.", f"<p>{F(2,3)} + {F(1,6)} = {F(4,6)} + {F(1,6)} = {F(5,6)}. On n’additionne pas les dénominateurs.</p><p class='answer'>Fausse.</p>"),
      Q("3", "litteral", 0.8, "Affirmation 3 : pour tout nombre <em>x</em>, (<em>x</em> + 3)² = <em>x</em>² + 9.", "<p>Contre-exemple : <em>x</em> = 1 donne 16 d’un côté et 10 de l’autre. En fait (<em>x</em> + 3)² = <em>x</em>² + 6<em>x</em> + 9.</p><p class='answer'>Fausse.</p>"),
      Q("4", "nombres", 0.8, "Affirmation 4 : 0,2 × 0,3 = 0,6.", "<p>0,2 × 0,3 = 0,06 (2 × 3 = 6, et deux chiffres après la virgule au total).</p><p class='answer'>Fausse.</p>"),
      Q("5", "nombres", 0.8, "Affirmation 5 : 3,5 × 10⁻² = 0,035.", "<p>Multiplier par 10⁻², c’est diviser par 100.</p><p class='answer'>Vraie.</p>"),
     ]),
 ]})

# ================================================================ Sujet C : la classe de découverte (original)
assert 360 / 5 == 72 and 72 / 3.6 == 20 and 270 / 90 + 90 / 60 == 4.5
assert 4.8 * 250000 / 100000 == 12 and 15 * 100 / 50 == 30 and round(120 * 10000 / 2500) == 480 and abs(450 / 125000 * 1000 - 3.6) < 1e-9
g = lambda x: (x + 3) * (x - 3)
assert 5 * 5 - 9 == 16 == g(5)
assert Fr(22, 56) == Fr(11, 28) and Fr(8, 22) == Fr(4, 11)
assert (2 ** 3) ** 2 == 64 and (80 - 60) / 80 == 0.25 and (180 - 40) / 2 == 70

SUJETS.append({
 "id": "m-decouverte", "num": 5, "titre": "Sujet C · La classe de découverte",
 "theme": "Vitesses et durées, échelles, calcul littéral, tableau à double entrée, QCM",
 "calculatrice": True,
 "remarque": "Sujet original, inspiré des annales du CRPE et du brevet.",
 "parties": [
  EX(1, 4, "Le trajet en car", "<p>Le car part à 7 h 45 et parcourt 360 km. Il fait une pause de 30 minutes et arrive à 13 h 15.</p>",
     [Q("1", "grandeurs", 1, "Calculer la durée totale du voyage, puis la durée de conduite.", "<p>De 7 h 45 à 13 h 15 : 5 h 30 min. Sans la pause : 5 h.</p><p class='answer'>5 h 30 min de voyage, 5 h de conduite.</p>"),
      Q("2", "grandeurs", 1, "Calculer la vitesse moyenne du car pendant la conduite.", "<p>v = d ÷ t = 360 ÷ 5.</p><p class='answer'>72 km/h</p>"),
      Q("3", "grandeurs", 1, "Convertir cette vitesse en m/s.", "<p>72 km/h = 72 000 m en 3 600 s ; 72 000 ÷ 3 600 = 20.</p><p class='answer'>20 m/s</p>"),
      Q("4", "grandeurs", 1, "Au retour, le car roule à 90 km/h sur les trois quarts du trajet et à 60 km/h sur le reste, avec la même pause. À quelle heure arrive-t-il s’il part à 7 h 45 ?", "<p>3/4 de 360 km = 270 km à 90 km/h : 3 h. Reste 90 km à 60 km/h : 1,5 h = 1 h 30. Total : 4 h 30 + 30 min de pause = 5 h.</p><p class='answer'>12 h 45</p><p><strong>Piège :</strong> la vitesse moyenne n’est pas la moyenne des vitesses (75 km/h).</p>"),
     ]),
  EX(2, 4, "Cartes et maquettes", "",
     [Q("1", "proportionnalite", 1, "Sur une carte au 1/250 000, deux villages sont à 4,8 cm. Quelle est la distance réelle ?", "<p>4,8 × 250 000 = 1 200 000 cm = 12 km.</p><p class='answer'>12 km</p>"),
      Q("2", "proportionnalite", 1, "La classe construit une maquette du chalet au 1/50. Le chalet mesure 15 m de long. Longueur sur la maquette ?", "<p>1 500 cm ÷ 50 = 30 cm.</p><p class='answer'>30 cm</p>"),
      Q("3", "grandeurs", 1, "Le plancher du chalet a une aire de 120 m². Quelle est son aire sur la maquette, en cm² ?", "<p>Les aires sont divisées par 50² = 2 500. 120 m² = 1 200 000 cm² ; 1 200 000 ÷ 2 500 = 480.</p><p class='answer'>480 cm²</p>"),
      Q("4", "grandeurs", 1, "Le volume intérieur du chalet est de 450 m³. Quel est celui de la maquette, en litres ?", "<p>Les volumes sont divisés par 50³ = 125 000 : 450 ÷ 125 000 = 0,003 6 m³ = 3,6 dm³.</p><p class='answer'>3,6 L</p>"),
     ]),
  EX(3, 4, "Deux programmes de calcul",
     "<div class='two'><ul class='box'><li><strong>Programme 1</strong></li><li>Choisir un nombre</li><li>Calculer son carré</li><li>Soustraire 9</li></ul><ul class='box'><li><strong>Programme 2</strong></li><li>Choisir un nombre</li><li>Lui ajouter 3</li><li>Multiplier par le nombre de départ diminué de 3</li></ul></div>",
     [Q("1", "litteral", 0.5, "Appliquer le programme 1 au nombre 5.", "<p>5² − 9 = 16.</p><p class='answer'>16</p>"),
      Q("2", "litteral", 0.5, "Appliquer le programme 2 au nombre 5.", "<p>(5 + 3) × (5 − 3) = 8 × 2 = 16.</p><p class='answer'>16</p>"),
      Q("3", "litteral", 1.5, "Montrer que les deux programmes donnent toujours le même résultat.", "<p>Programme 1 : <em>x</em>² − 9. Programme 2 : (<em>x</em> + 3)(<em>x</em> − 3) = <em>x</em>² − 3<em>x</em> + 3<em>x</em> − 9 = <em>x</em>² − 9.</p><p class='answer'>Les deux expressions sont égales pour tout <em>x</em>.</p>"),
      Q("4", "litteral", 1.5, "Quels nombres de départ donnent 0 ? Et 16 ?", "<p>(<em>x</em> + 3)(<em>x</em> − 3) = 0 ⇔ <em>x</em> = −3 ou <em>x</em> = 3. <em>x</em>² − 9 = 16 ⇔ <em>x</em>² = 25 ⇔ <em>x</em> = 5 ou <em>x</em> = −5.</p><p class='answer'>0 : −3 ou 3 ; 16 : −5 ou 5.</p><p><strong>Piège :</strong> ne pas oublier la solution négative.</p>"),
     ]),
  EX(4, 4, "Ski ou raquettes ?",
     "<p>Les 56 élèves choisissent une activité : ski ou raquettes. 32 choisissent le ski ; parmi eux, les trois quarts ont déjà skié. Parmi ceux qui choisissent les raquettes, 10 ont déjà skié.</p>",
     [Q("1", "proportionnalite", 1.5, "Construire un tableau à double entrée (activité / a déjà skié ou non).", "<p>Ski : 3/4 de 32 = 24 ont déjà skié. Raquettes : 56 − 32 = 24 élèves.</p>" + table(["", "Ski", "Raquettes", "Total"], [["§A déjà skié", 24, 10, 34], ["§N’a jamais skié", 8, 14, 22], ["§Total", 32, 24, 56]])),
      Q("2", "probas", 1, "On choisit un élève au hasard. Probabilité qu’il n’ait jamais skié ?", f"<p class='answer'>{F(22,56)} = {F(11,28)}</p>"),
      Q("3", "probas", 1.5, "On choisit au hasard un élève qui n’a jamais skié. Probabilité qu’il ait choisi le ski ?", f"<p>On se restreint aux 22 élèves qui n’ont jamais skié, dont 8 ont choisi le ski.</p><p class='answer'>{F(8,22)} = {F(4,11)}</p>"),
     ]),
  EX(5, 4, "QCM (aucune justification demandée)", "<p>Une seule réponse exacte par question.</p>",
     [Q("1", "nombres", 1, "L’écriture scientifique de 0,000 72 est : A : 72 × 10⁻⁵ · B : 7,2 × 10⁻⁴ · C : 7,2 × 10⁴ · D : 0,72 × 10⁻³", "<p class='answer'>Réponse B</p><p>L’écriture scientifique a un seul chiffre non nul avant la virgule.</p>"),
      Q("2", "nombres", 1, "(2³)² est égal à : A : 2⁵ · B : 32 · C : 64 · D : 2⁹", "<p class='answer'>Réponse C</p><p>(2³)² = 2⁶ = 64 : on multiplie les exposants.</p>"),
      Q("3", "proportionnalite", 1, "Un article passe de 80 € à 60 €. La réduction est de : A : 20 % · B : 25 % · C : 33 % · D : 75 %", "<p class='answer'>Réponse B</p><p>20 ÷ 80 = 0,25. Le pourcentage se calcule par rapport au prix de départ.</p>"),
      Q("4", "geometrie", 1, "Un triangle isocèle a un angle au sommet principal de 40°. Ses angles à la base mesurent : A : 40° · B : 50° · C : 70° · D : 140°", "<p class='answer'>Réponse C</p><p>(180° − 40°) ÷ 2 = 70°.</p>"),
     ]),
 ]})

# ================================================================ Sujet D : approfondissement lycée (original)
u = lambda k: 500 + 50 * k; v = lambda k: 1000 * 1.03 ** k
assert u(12) == 1100 and round(v(10), 2) == 1343.92 and v(13) < 1500 < v(14)
A = lambda x: x * (20 - 2 * x)
assert A(3) == 42 and A(5) == 50 and A(2) == 32 == A(8)
pT, pP_T, pP_nT = 0.08, 0.95, 0.10
pP = pT * pP_T + (1 - pT) * pP_nT
assert abs(pT * pP_T - 0.076) < 1e-12 and abs(pP - 0.168) < 1e-12 and round(0.076 / 0.168, 2) == 0.45
assert 500 * 1.08 == 540 and abs(540 * 0.95 - 513) < 1e-9 and round((500 / 513 - 1) * 100, 1) == -2.5 and round((math.sqrt(1.026) - 1) * 100, 1) == 1.3
Am, Bm, Cm = (-2, 1), (4, 3), (2, -3)
assert ((Am[0] + Cm[0]) / 2, (Am[1] + Cm[1]) / 2) == (0, -1)
assert (Bm[0] - Am[0]) ** 2 + (Bm[1] - Am[1]) ** 2 == 40
Dm = (Am[0] + Cm[0] - Bm[0], Am[1] + Cm[1] - Bm[1]); assert Dm == (-4, -5)
assert Fr(1, 3) * Am[0] + Fr(5, 3) == Am[1] and Fr(1, 3) * Bm[0] + Fr(5, 3) == Bm[1]

SUJETS.append({
 "id": "m-lycee", "num": 6, "titre": "Sujet D · Approfondissement lycée (2de–1re)",
 "theme": "Suites, second degré, probabilités conditionnelles, évolutions, géométrie repérée",
 "calculatrice": True, "lycee": True,
 "remarque": "Ce sujet va au-delà du programme officiel du concours (cycle 4). Il sert à consolider les bases et à prendre de l’aisance : ne le traite qu’une fois les sujets de niveau cycle 4 maîtrisés.",
 "parties": [
  EX(1, 4, "Deux façons d’épargner",
     "<p>Léo possède 500 € et ajoute 50 € chaque mois : <em>u<sub>n</sub></em> est son épargne après <em>n</em> mois. Emma place 1 000 € à 3 % d’intérêts composés par an : <em>v<sub>n</sub></em> est son capital après <em>n</em> années.</p>",
     [Q("1", "suites", 1, "Calculer <em>u</em><sub>12</sub>.", "<p><em>u<sub>n</sub></em> = 500 + 50<em>n</em>, donc <em>u</em><sub>12</sub> = 500 + 600.</p><p class='answer'>1 100 €</p>", "lycee"),
      Q("2", "suites", 1, "Quelle est la nature de chaque suite ? Préciser la raison.", "<p class='answer'>(<em>u<sub>n</sub></em>) est arithmétique de raison 50 ; (<em>v<sub>n</sub></em>) est géométrique de raison 1,03.</p><p>On ajoute 50 à chaque étape pour <em>u</em> ; on multiplie par 1 + 3/100 = 1,03 pour <em>v</em>.</p>", "lycee"),
      Q("3", "suites", 1, "Calculer <em>v</em><sub>10</sub>, au centime près.", f"<p><em>v<sub>n</sub></em> = 1 000 × 1,03<sup><em>n</em></sup>, donc <em>v</em><sub>10</sub> = 1 000 × 1,03<sup>10</sup>.</p><p class='answer'>≈ {n(v(10), 2)} €</p>", "lycee"),
      Q("4", "suites", 1, "Au bout de combien d’années le capital d’Emma dépasse-t-il 1 500 € ?", f"<p>Par essais à la calculatrice (ou avec un tableur) : <em>v</em><sub>13</sub> ≈ {n(v(13), 2)} € et <em>v</em><sub>14</sub> ≈ {n(v(14), 2)} €.</p><p class='answer'>Au bout de 14 ans.</p>", "lycee"),
     ]),
  EX(2, 4, "L’enclos des poules",
     "<p>On construit un enclos rectangulaire le long d’un mur avec 20 m de grillage (le mur forme le quatrième côté). On note <em>x</em> la largeur (en m) des deux côtés perpendiculaires au mur.</p>",
     [Q("1", "fonctions", 0.5, "Calculer l’aire de l’enclos pour <em>x</em> = 3.", "<p>Longueur : 20 − 2 × 3 = 14 m ; aire : 3 × 14.</p><p class='answer'>42 m²</p>", "lycee"),
      Q("2", "fonctions", 1, "Exprimer l’aire <em>A</em>(<em>x</em>) et préciser les valeurs possibles de <em>x</em>.", "<p class='answer'><em>A</em>(<em>x</em>) = <em>x</em>(20 − 2<em>x</em>) = −2<em>x</em>² + 20<em>x</em>, pour 0 &lt; <em>x</em> &lt; 10.</p>", "lycee"),
      Q("3", "fonctions", 1.5, "Vérifier que <em>A</em>(<em>x</em>) = −2(<em>x</em> − 5)² + 50. En déduire l’aire maximale et les dimensions correspondantes.", "<p>−2(<em>x</em>² − 10<em>x</em> + 25) + 50 = −2<em>x</em>² + 20<em>x</em>. Comme −2(<em>x</em> − 5)² ≤ 0, <em>A</em>(<em>x</em>) ≤ 50, avec égalité pour <em>x</em> = 5.</p><p class='answer'>Aire maximale 50 m², pour un enclos de 5 m sur 10 m.</p>", "lycee"),
      Q("4", "litteral", 1, "Pour quelles valeurs de <em>x</em> l’aire vaut-elle 32 m² ?", "<p>−2<em>x</em>² + 20<em>x</em> = 32 ⇔ <em>x</em>² − 10<em>x</em> + 16 = 0 ⇔ (<em>x</em> − 2)(<em>x</em> − 8) = 0. (Discriminant : 100 − 64 = 36.)</p><p class='answer'><em>x</em> = 2 ou <em>x</em> = 8</p>", "lycee"),
     ]),
  EX(3, 4, "Un test de dépistage visuel",
     "<p>8 % des élèves d’une école ont un trouble visuel (événement T). Un test est positif (événement P) pour 95 % des élèves qui ont un trouble, et pour 10 % de ceux qui n’en ont pas.</p>" + fig_arbre(),
     [Q("1", "probas", 1, "Justifier les probabilités 0,92, 0,05 et 0,90 inscrites sur l’arbre. Que représente la probabilité 0,95 ?", "<p>La somme des probabilités issues d’un même nœud vaut 1 : 1 − 0,08 = 0,92 ; 1 − 0,95 = 0,05 ; 1 − 0,10 = 0,90.</p><p>0,95 est une probabilité <strong>conditionnelle</strong> : la probabilité que le test soit positif <em>sachant que</em> l’élève a un trouble, notée P<sub>T</sub>(P).</p>", "lycee"),
      Q("2", "probas", 1, "Calculer la probabilité qu’un élève ait un trouble et un test positif.", "<p>On multiplie le long du chemin : 0,08 × 0,95.</p><p class='answer'>P(T ∩ P) = 0,076</p>", "lycee"),
      Q("3", "probas", 1, "Calculer la probabilité qu’un test soit positif.", "<p>Formule des probabilités totales : 0,08 × 0,95 + 0,92 × 0,10 = 0,076 + 0,092.</p><p class='answer'>P(P) = 0,168</p>", "lycee"),
      Q("4", "probas", 1, "Un élève a un test positif. Quelle est la probabilité qu’il ait réellement un trouble ?", "<p>P<sub>P</sub>(T) = P(T ∩ P) ÷ P(P) = 0,076 ÷ 0,168 ≈ 0,452.</p><p class='answer'>≈ 0,45</p><p>Moins d’une chance sur deux : un test positif doit être confirmé par un examen.</p>", "lycee"),
     ]),
  EX(4, 4, "L’évolution des effectifs",
     "<p>Une école comptait 500 élèves en 2020. L’effectif a augmenté de 8 % en 2021, puis baissé de 5 % en 2022.</p>",
     [Q("1", "proportionnalite", 1, "Calculer l’effectif en 2022.", "<p>500 × 1,08 = 540 ; 540 × 0,95 = 513.</p><p class='answer'>513 élèves</p>", "lycee"),
      Q("2", "proportionnalite", 1, "Quel est le taux d’évolution global entre 2020 et 2022 ?", "<p>Coefficient global : 1,08 × 0,95 = 1,026.</p><p class='answer'>+2,6 %</p>", "lycee"),
      Q("3", "proportionnalite", 1, "Quel taux d’évolution faudrait-il en 2023 pour revenir à 500 élèves ?", f"<p>Coefficient : 500 ÷ 513 ≈ {n(500/513, 4)}.</p><p class='answer'>≈ −2,5 %</p>", "lycee"),
      Q("4", "proportionnalite", 1, "Quel est le taux d’évolution annuel moyen entre 2020 et 2022 ?", f"<p>On cherche <em>t</em> tel que (1 + <em>t</em>)² = 1,026 : 1 + <em>t</em> = √1,026 ≈ {n(math.sqrt(1.026), 4)}.</p><p class='answer'>≈ +1,3 % par an</p><p>Ce n’est pas la moyenne de +8 % et −5 %.</p>", "lycee"),
     ]),
  EX(5, 4, "Dans un repère", "<p>Dans un repère orthonormé, on considère A(−2 ; 1), B(4 ; 3) et C(2 ; −3).</p>",
     [Q("1", "geometrie", 1, "Calculer les coordonnées du milieu I de [AC].", "<p>((−2 + 2) ÷ 2 ; (1 + (−3)) ÷ 2).</p><p class='answer'>I(0 ; −1)</p>", "lycee"),
      Q("2", "geometrie", 1, "Calculer la longueur AB.", f"<p>AB = √((4 − (−2))² + (3 − 1)²) = √(36 + 4) = √40 = 2√10.</p><p class='answer'>AB = 2√10 ≈ {n(math.sqrt(40), 2)}</p>", "lycee"),
      Q("3", "fonctions", 1, "Déterminer une équation de la droite (AB).", f"<p>Coefficient directeur : (3 − 1) ÷ (4 − (−2)) = {F(2,6)} = {F(1,3)}. Ordonnée à l’origine : 1 = {F(1,3)} × (−2) + <em>p</em> ⇔ <em>p</em> = {F(5,3)}.</p><p class='answer'><em>y</em> = {F(1,3)}<em>x</em> + {F(5,3)}</p>", "lycee"),
      Q("4", "geometrie", 1, "Déterminer les coordonnées de D tel que ABCD soit un parallélogramme.", "<p>ABCD est un parallélogramme si ses diagonales [AC] et [BD] ont le même milieu I(0 ; −1) : <em>x</em><sub>D</sub> = 2 × 0 − 4 = −4 et <em>y</em><sub>D</sub> = 2 × (−1) − 3 = −5.</p><p class='answer'>D(−4 ; −5)</p><p>Vérification : les vecteurs AB et DC ont les mêmes coordonnées (6 ; 2).</p>", "lycee"),
     ]),
 ]})

# ---------------------------------------------------------------- contrôles et export
for s in SUJETS:
    tot = 0
    for p in s["parties"]:
        pt = round(sum(q["points"] for q in p["questions"]), 6)
        assert abs(pt - p["points"]) < 1e-6, (s["id"], p["id"], pt, p["points"])
        for q in p["questions"]:
            assert q["type"] in TYPES, q["type"]
        tot += p["points"]
    expected = s.get("noteSur", 20)
    assert abs(tot - expected) < 1e-6, (s["id"], tot)
    s["total"] = expected

out = "/* Généré par sujets_maths.py : sujets de mathématiques du CRPE BAC+3 (1re épreuve, partie B). */\n"
out += "window.BELAMIS_MATHS = " + json.dumps({"types": TYPES, "sujets": SUJETS}, ensure_ascii=False, indent=1) + ";\n"
open(os.path.join(HERE, "maths.js"), "w").write(out)
for s in SUJETS:
    print(s["num"], s["id"], "/", s["total"], "|", sum(len(p["questions"]) for p in s["parties"]), "questions")
