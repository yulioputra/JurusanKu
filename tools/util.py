import re
def slugify(s):
    s = re.sub(r"\(.*?\)", "", s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
def slug_of(m):
    return f"{m['lv'].lower()}-{slugify(m['n'])}"
