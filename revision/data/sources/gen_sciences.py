import json
import re
import sys

sys.path.insert(0, ".")
import s0, s1, s2, s3

OUT = "/home/user/Belamis/revision/data/e2_sciences.json"
NNBSP = " "


def typo(html):
    """Espace fine insécable dans les milliers, hors balises."""
    parts = re.split(r"(<[^>]+>)", html)
    for i, p in enumerate(parts):
        if not p.startswith("<"):
            prev = None
            while prev != p:
                prev = p
                p = re.sub(r"(\d) (\d{3})(?!\d)", r"\1" + NNBSP + r"\2", p)
            parts[i] = p
    return "".join(parts)


def walk(o):
    if isinstance(o, dict):
        return {k: walk(v) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(v) for v in o]
    if isinstance(o, str):
        return typo(o)
    return o


sujets = [walk(m.build()) for m in (s0, s1, s2, s3)]
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"sujets": sujets}, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("écrit", OUT)
