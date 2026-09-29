import json, re
from html.parser import HTMLParser
import xml.dom.minidom

d = json.load(open("/home/user/Belamis/revision/data/e2_sciences.json", encoding="utf-8"))
ALLOWED = {"p", "ul", "ol", "li", "strong", "em", "sub", "sup", "br", "table", "thead", "tbody", "tr", "th", "td",
           "div", "figure", "svg"}
TYPES = {"physique", "svt", "techno", "demarche", "conceptions"}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.bad, self.insvg = [], [], 0

    def handle_starttag(self, t, a):
        if t == "svg":
            self.insvg += 1
        if not self.insvg and t not in ALLOWED:
            self.bad.append(t)
        if t != "br" and not (self.insvg and t in ("line", "circle", "rect", "path", "ellipse")):
            self.stack.append(t)
        if t == "svg":
            pass

    def handle_startendtag(self, t, a):
        pass

    def handle_endtag(self, t):
        if not self.stack or self.stack[-1] != t:
            self.bad.append("close:" + t + " stack=" + "/".join(self.stack[-3:]))
        else:
            self.stack.pop()
        if t == "svg":
            self.insvg -= 1


ok = True
for s in d["sujets"]:
    tot = 0
    nq = 0
    types = {}
    for p in s["parties"]:
        sq = sum(q["points"] for q in p["questions"])
        if abs(sq - p["points"]) > 1e-9:
            print("ERR partie", s["id"], p["id"], sq, p["points"]); ok = False
        tot += p["points"]
        for field in ("intro",):
            pp = P(); pp.feed(p[field]); pp.close()
            if pp.bad or pp.stack:
                print("HTML", s["id"], p["id"], field, pp.bad, pp.stack); ok = False
        for m in re.findall(r"<svg.*?</svg>", p["intro"], re.S):
            try:
                xml.dom.minidom.parseString(m)
            except Exception as e:
                print("SVG XML", s["id"], p["id"], e); ok = False
        for q in p["questions"]:
            nq += 1
            types[q["type"]] = types.get(q["type"], 0) + 1
            assert q["type"] in TYPES, q["type"]
            assert (q["points"] * 4) == int(q["points"] * 4)
            for field in ("enonce", "corrige"):
                pp = P(); pp.feed(q[field]); pp.close()
                if pp.bad or pp.stack:
                    print("HTML", s["id"], p["id"], q["id"], field, pp.bad, pp.stack); ok = False
    if abs(tot - 20) > 1e-9 or s["total"] != 20:
        print("ERR total", s["id"], tot); ok = False
    print(s["id"], "parties", len(s["parties"]), "questions", nq, "total", tot, types)
print("OK" if ok else "PROBLÈMES")
