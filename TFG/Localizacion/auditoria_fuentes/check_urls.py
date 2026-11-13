import re, requests, json, sys
base = r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Localizacion"
tex = open(base + r"\estudio_localizacion.tex", encoding="utf-8").read()
cited = set()
for m in re.finditer(r"\\(?:auto|text)?cite\{([^}]*)\}", tex):
    for k in m.group(1).split(","):
        cited.add(k.strip())
bib = open(base + r"\Referencias.bib", encoding="utf-8", errors="replace").read()
entries = re.split(r"\n(?=@)", bib)
db = {}
for e in entries:
    m = re.match(r"@(\w+)\{([^,]+),", e.strip())
    if m:
        db[m.group(2)] = e
print("Claves citadas:", sorted(cited))
print("Faltan en .bib:", [k for k in cited if k not in db])
H = {"User-Agent": "Mozilla/5.0"}
out = {}
for k in sorted(cited):
    e = db.get(k, "")
    u = re.search(r"url\s*=\s*\{([^}]*)\}", e)
    if not u:
        out[k] = "sin URL (libro/otro)"
        continue
    url = u.group(1)
    try:
        r = requests.get(url, headers=H, timeout=20, stream=True, allow_redirects=True)
        ct = r.headers.get("Content-Type", "")[:30]
        out[k] = "%s | %s | %s" % (r.status_code, ct, url)
        r.close()
    except Exception as ex:
        out[k] = "ERR %s | %s" % (type(ex).__name__, url)
for k, v in out.items():
    print(k, "->", v)
json.dump(out, open(base + r"\auditoria_fuentes\url_check.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

