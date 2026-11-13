import requests, os
H = {"User-Agent": "Mozilla/5.0"}
d = r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Localizacion\auditoria_fuentes"
urls = {
 "BOP_20091106_213.pdf": "https://bop.dipgra.es/export/sites/bop/publica/boletines-anteriores/.galleries/Boletines-Anteriores/20091106-2009213.pdf",
 "Memoria_Adaptacion_Loja.pdf": "http://aytoloja.org/ayuntamiento/MEMORIA/MEM_JUSTIF_ADAPTACION_LOJA.pdf",
 "PV_2_2.pdf": "http://www.aytoloja.org/ayuntamiento/PLANOS/1_PV_PLANEAMIENTO%20VIGENTE/PV_2_2.pdf",
 "PV_2_3.pdf": "http://www.aytoloja.org/ayuntamiento/PLANOS/1_PV_PLANEAMIENTO%20VIGENTE/PV_2_3.pdf",
}
for n, u in urls.items():
    p = os.path.join(d, n)
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        print(n, "ya descargado", os.path.getsize(p)); continue
    try:
        r = requests.get(u, headers=H, timeout=120)
        open(p, "wb").write(r.content)
        print(n, r.status_code, len(r.content))
    except Exception as e:
        print(n, "ERR", type(e).__name__, e)

