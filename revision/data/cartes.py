# -*- coding: utf-8 -*-
# Fonds de carte SVG pour les sujets de géographie (épreuve 2).
# Données : france-geojson (G. David, d'après IGN / Licence ouverte) et Natural Earth (domaine public).
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "geo")

def _load(name):
    return json.load(open(os.path.join(SRC, name)))

def _rings(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"][0]]
    return [poly[0] for poly in geom["coordinates"]]

class Proj:
    def __init__(self, lon0, lon1, lat0, lat1, width, lat_ref=None):
        self.lon0, self.lat1 = lon0, lat1
        k = math.cos(math.radians(lat_ref)) if lat_ref is not None else 1.0
        self.sx = width / ((lon1 - lon0) * k) * k
        self.sy = width / ((lon1 - lon0) * k)
        self.w = width
        self.h = (lat1 - lat0) * self.sy
    def __call__(self, lon, lat):
        return ((lon - self.lon0) * self.sx, (self.lat1 - lat) * self.sy)

def _path(rings, P, min_d=0.9, min_ring=6):
    out = []
    for ring in rings:
        pts, last = [], None
        for lon, lat in ring:
            x, y = P(lon, lat)
            if last is None or abs(x - last[0]) + abs(y - last[1]) >= min_d:
                pts.append((x, y)); last = (x, y)
        if len(pts) < 3:
            continue
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        if max(xs) - min(xs) + max(ys) - min(ys) < min_ring:
            continue
        out.append("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z")
    return " ".join(out)

def _svg(w, h, body, label, extra_cls="", caption=""):
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (f'<figure class="fig map{extra_cls}"><svg viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-label="{label}" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>{cap}</figure>')

def _t(x, y, s, size=11, anchor="middle", cls=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" class="{cls}">{s}</text>'

# ---------------------------------------------------------------- France
# « diagonale » des faibles densités, des Ardennes et de la Meuse aux Landes, par le Massif central
DIAGONALE = [(4.6, 50.0), (6.2, 49.1), (4.4, 46.6), (3.9, 44.4), (2.2, 44.1), (0.3, 43.9), (-0.9, 44.3), (1.5, 45.9), (2.9, 47.8)]
FR = Proj(-5.4, 9.9, 41.2, 51.3, 520, lat_ref=46.5)

def _france_body():
    g = _load("fr-metro.geojson")
    rings = []
    feats = g["features"] if g.get("type") == "FeatureCollection" else [g]
    for f in feats:
        rings += _rings(f["geometry"])
    return f'<path d="{_path(rings, FR)}" class="land"/>'

VILLES = {  # lon, lat
    "Paris": (2.35, 48.86), "Lyon": (4.84, 45.76), "Marseille": (5.37, 43.30), "Toulouse": (1.44, 43.60),
    "Bordeaux": (-0.58, 44.84), "Lille": (3.06, 50.63), "Nice": (7.26, 43.70), "Nantes": (-1.55, 47.22),
    "Strasbourg": (7.75, 48.58), "Montpellier": (3.88, 43.61), "Rennes": (-1.68, 48.11), "Grenoble": (5.72, 45.19),
    "Le Havre": (0.11, 49.49), "Dunkerque": (2.38, 51.03), "Brest": (-4.49, 48.39), "Clermont-Ferrand": (3.08, 45.78),
    "Dijon": (5.04, 47.32), "Limoges": (1.26, 45.83), "Rouen": (1.10, 49.44), "Metz": (6.18, 49.12),
}

def france_vierge(label="Fond de carte de la France métropolitaine"):
    return _svg(FR.w, FR.h, _france_body(), label)

def carte_population():
    """Corrigé : principales aires urbaines (catégories d'après INSEE, aires d'attraction des villes 2020)."""
    cats = [("Paris", 26), ("Lyon", 13), ("Marseille", 13), ("Lille", 13), ("Toulouse", 13), ("Bordeaux", 13),
            ("Nantes", 8), ("Nice", 8), ("Strasbourg", 8), ("Montpellier", 8), ("Rennes", 8), ("Grenoble", 8)]
    b = _france_body()
    # couloirs de fortes densités (vallées et littoraux), en aplat léger
    for a, z in (("Lille", "Paris"), ("Paris", "Lyon"), ("Lyon", "Marseille"), ("Marseille", "Nice")):
        (x1, y1), (x2, y2) = FR(*VILLES[a]), FR(*VILLES[z])
        b += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="axe-dense"/>'
    for nom, r in cats:
        x, y = FR(*VILLES[nom])
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="ville"/>'
        b += _t(x, y - r - 3, nom, 11)
    # littoral atlantique et méditerranéen attractif
    lx, ly = FR(-1.3, 45.6)
    b += _t(lx - 18, ly, "littoral", 10, "end", "it") + _t(lx - 18, ly + 12, "attractif", 10, "end", "it")
    # diagonale des faibles densités
    pts = [FR(*p) for p in DIAGONALE]
    b += '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" class="faible"/>'
    lg = (f'<g transform="translate({FR.w + 14},{FR.h - 130})"><rect x="-8" y="-14" width="172" height="112" class="legend-box"/>'
          + '<circle cx="8" cy="0" r="9" class="ville"/>' + _t(24, 4, "plus de 10 millions d’hab.", 10, "start")
          + '<circle cx="8" cy="24" r="6" class="ville"/>' + _t(24, 28, "1 à 2,5 millions", 10, "start")
          + '<circle cx="8" cy="46" r="4" class="ville"/>' + _t(24, 50, "0,5 à 1 million", 10, "start")
          + '<line x1="0" y1="68" x2="16" y2="68" class="axe-dense"/>' + _t(24, 72, "axe de fortes densités", 10, "start")
          + '<rect x="0" y="82" width="16" height="10" class="faible"/>' + _t(24, 91, "faibles densités", 10, "start") + "</g>")
    return _svg(FR.w + 200, FR.h, b + lg, "Croquis corrigé : répartition de la population en France métropolitaine",
                caption="La répartition de la population en France métropolitaine (catégories d’après l’INSEE, aires d’attraction des villes)")

def carte_faible_densite():
    b = _france_body()
    pts = [FR(*p) for p in DIAGONALE]
    b += '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" class="faible"/>'
    for nom, (lon, lat, rx, ry, rot) in {"Alpes": (6.5, 45.3, 34, 70, -20), "Pyrénées": (0.6, 42.8, 110, 14, 0), "Massif central": (2.9, 45.3, 46, 40, 0)}.items():
        x, y = FR(lon, lat)
        b += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx}" ry="{ry}" transform="rotate({rot} {x:.1f} {y:.1f})" class="montagne"/>' + _t(x, y + 4, nom, 10, cls="it")
    for nom in ("Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux", "Lille"):
        x, y = FR(*VILLES[nom]); b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="ville"/>' + _t(x, y - 8, nom, 10)
    lg = (f'<g transform="translate({FR.w + 14},{FR.h - 100})"><rect x="-8" y="-14" width="177" height="82" class="legend-box"/>'
          + '<rect x="0" y="-6" width="16" height="10" class="faible"/>' + _t(24, 3, "« diagonale » des faibles densités", 10, "start")
          + '<ellipse cx="8" cy="20" rx="8" ry="6" class="montagne"/>' + _t(24, 24, "espaces de montagne", 10, "start")
          + '<circle cx="8" cy="42" r="5" class="ville"/>' + _t(24, 46, "grande métropole", 10, "start") + "</g>")
    return _svg(FR.w + 200, FR.h, b + lg, "Croquis corrigé : espaces de faible densité en France métropolitaine",
                caption="Les espaces de faible densité en France métropolitaine")

# ---------------------------------------------------------------- Europe
EU = Proj(-25, 45, 34, 71.5, 560, lat_ref=52)
UE27 = {"AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "IRL", "ITA", "LVA",
        "LTU", "LUX", "MLT", "NLD", "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"}
FONDATEURS = {"FRA", "DEU", "ITA", "BEL", "NLD", "LUX"}

def carte_ue():
    g = _load("europe50.geojson")
    b = ""
    for f in g["features"]:
        p = f["properties"]; iso = p.get("ADM0_A3") or p.get("ISO_A3")
        rings = []
        for ring in _rings(f["geometry"]):
            if any(-26 < lon < 46 and 33 < lat < 72 for lon, lat in ring[:: max(1, len(ring) // 20)]):
                # on ne garde que la partie européenne (la Guyane, etc. sont hors cadre)
                if iso == "FRA" and ring[0][0] < -20:
                    continue
                rings.append(ring)
        if not rings:
            continue
        cls = "eu-f" if iso in FONDATEURS else "eu" if iso in UE27 else "land"
        b += f'<path d="{_path(rings, EU, 1.6, 4)}" class="{cls}"/>'
    lg = (f'<g transform="translate(14,{EU.h - 70})"><rect x="-8" y="-14" width="210" height="72" class="legend-box"/>'
          + '<rect x="0" y="-6" width="16" height="10" class="eu-f"/>' + _t(24, 3, "6 États fondateurs (1957)", 10, "start")
          + '<rect x="0" y="14" width="16" height="10" class="eu"/>' + _t(24, 23, "autres États membres (27 en tout)", 10, "start")
          + '<rect x="0" y="34" width="16" height="10" class="land"/>' + _t(24, 43, "États non membres", 10, "start") + "</g>")
    return _svg(EU.w, EU.h, b + lg, "Carte de l’Union européenne à 27 États membres")

# ---------------------------------------------------------------- Monde
WO = Proj(-180, 180, -58, 80, 720)

def _world_body(highlight=None):
    g = _load("world110.geojson")
    b = ""
    for f in g["features"]:
        iso = f["properties"].get("ADM0_A3")
        if iso == "ATA":
            continue
        cls = "hl" if highlight and iso in highlight else "land"
        b += f'<path d="{_path(_rings(f["geometry"]), WO, 1.4, 3)}" class="{cls}"/>'
    return b

OUTREMER = {  # nom : lon, lat, statut
    "Guadeloupe": (-61.5, 16.2, "drom"), "Martinique": (-61.0, 14.6, "drom"), "Guyane": (-53.1, 3.9, "drom"),
    "La Réunion": (55.5, -21.1, "drom"), "Mayotte": (45.1, -12.8, "drom"),
    "Saint-Pierre-et-Miquelon": (-56.3, 46.9, "com"), "Polynésie française": (-149.4, -17.7, "com"),
    "Nouvelle-Calédonie": (165.6, -21.3, "com"), "Wallis-et-Futuna": (-176.2, -13.3, "com"),
    "Terres australes (TAAF)": (69.3, -49.3, "com"),
}

def carte_outremer():
    b = _world_body({"FRA"})
    for nom, (lon, lat, st) in OUTREMER.items():
        x, y = WO(lon, lat)
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" class="{"drom" if st == "drom" else "com"}"/>'
        dy = -8 if lat > 0 else 15
        anchor = "start" if lon < -100 else "end" if lon > 150 else "middle"
        dx = 8 if anchor == "start" else -8 if anchor == "end" else 0
        if nom == "Martinique":
            anchor, dx, dy = "start", 8, 12
        if nom == "Guadeloupe":
            anchor, dx, dy = "end", -8, -4
        if nom == "Guyane":
            anchor, dx, dy = "middle", 0, 17
        if nom == "Wallis-et-Futuna":
            anchor, dx, dy = "start", 8, -8
        if nom == "Polynésie française":
            anchor, dx, dy = "start", 8, 14
        b += _t(x + dx, y + dy, nom, 9, anchor)
    lg = (f'<g transform="translate(14,{WO.h + 22})"><rect x="-8" y="-14" width="310" height="54" class="legend-box"/>'
          + '<circle cx="6" cy="0" r="4.5" class="drom"/>' + _t(18, 4, "départements et régions d’outre-mer (DROM)", 10, "start")
          + '<circle cx="6" cy="22" r="4.5" class="com"/>' + _t(18, 26, "collectivités d’outre-mer, Nouvelle-Calédonie, TAAF", 10, "start") + "</g>")
    return _svg(WO.w, WO.h + 64, b + lg, "Carte des territoires ultramarins français dans le monde")

def carte_mondialisation_maritime():
    b = _world_body()
    ports = {"Shanghai": (121.5, 31.2), "Singapour": (103.8, 1.3), "Rotterdam": (4.5, 51.9), "Los Angeles": (-118.2, 33.7),
             "Busan": (129.0, 35.1), "Dubaï (Jebel Ali)": (55.0, 25.0), "Le Havre": (0.1, 49.5), "Marseille-Fos": (4.9, 43.4)}
    detroits = {"Pas-de-Calais": (1.5, 51.0), "Gibraltar": (-5.6, 36.0), "canal de Suez": (32.3, 30.5), "Bab-el-Mandeb": (43.4, 12.6),
                "Ormuz": (56.4, 26.6), "Malacca": (100.5, 3.5), "canal de Panama": (-79.7, 9.1)}
    routes = [[(-118, 34), (-179.9, 31)], [(179.9, 31), (140, 33), (122, 31)], [(122, 31), (104, 1.3), (80, 6), (43.4, 12.6), (32.3, 30.5), (15, 36), (-5.6, 36), (-9, 43), (0, 49.5), (4.5, 52)],
              [(4.5, 52), (-30, 45), (-74, 40)], [(-79.7, 9.1), (-118, 33.7)]]
    for r in routes:
        pts = [WO(*p) for p in r]
        b += '<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" class="route"/>'
    decal = {"Rotterdam": (14, -6, "start"), "Le Havre": (-8, -8, "end"), "Marseille-Fos": (8, 12, "start"), "Busan": (8, -6, "start"), "Shanghai": (-6, -8, "end")}
    for nom, (lon, lat) in ports.items():
        x, y = WO(lon, lat)
        dx, dy, an = decal.get(nom, (0, -7, "middle"))
        b += f'<rect x="{x-4:.1f}" y="{y-4:.1f}" width="8" height="8" class="port"/>' + _t(x + dx, y + dy, nom, 9, an)
    for nom, (lon, lat) in detroits.items():
        x, y = WO(lon, lat); b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="detroit"/>' + _t(x, y + 15, nom, 8.5, cls="it")
    lg = (f'<g transform="translate(14,{WO.h + 22})"><rect x="-8" y="-14" width="230" height="76" class="legend-box"/>'
          + '<line x1="0" y1="0" x2="18" y2="0" class="route"/>' + _t(26, 4, "grandes routes maritimes", 10, "start")
          + '<rect x="5" y="16" width="8" height="8" class="port"/>' + _t(26, 24, "grand port à conteneurs", 10, "start")
          + '<circle cx="9" cy="42" r="5" class="detroit"/>' + _t(26, 46, "détroit ou canal stratégique", 10, "start") + "</g>")
    return _svg(WO.w, WO.h + 86, b + lg, "Carte des grandes routes maritimes, ports et détroits de la mondialisation")

def carte_migrations():
    b = _world_body()
    fleches = [((-100, 22), (-98, 37), "Amérique latine → États-Unis"), ((5, 12), (8, 45), "Afrique → Europe"),
               ((78, 22), (52, 25), "Asie du Sud → pays du Golfe"), ((30, 50), (12, 51), "Europe de l’Est → Europe de l’Ouest"),
               ((110, 5), (140, -28), "Asie du Sud-Est → Australie")]
    b += '<defs><marker id="fl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="fleche-h"/></marker></defs>'
    for (a, z, lab) in fleches:
        (x1, y1), (x2, y2) = WO(*a), WO(*z)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 18
        b += f'<path d="M{x1:.1f},{y1:.1f} Q{mx:.1f},{my:.1f} {x2:.1f},{y2:.1f}" class="fleche" marker-end="url(#fl)"/>'
        b += _t(mx, my - 4, lab, 9)
    lg = (f'<g transform="translate(14,{WO.h + 22})"><rect x="-8" y="-14" width="240" height="32" class="legend-box"/>'
          + '<line x1="0" y1="0" x2="20" y2="0" class="fleche"/>' + _t(28, 4, "principaux flux migratoires (schéma)", 10, "start") + "</g>")
    return _svg(WO.w, WO.h + 44, b + lg, "Carte schématique des principaux flux migratoires dans le monde")

def monde_vierge():
    return _svg(WO.w, WO.h, _world_body(), "Fond de carte du monde")
