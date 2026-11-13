import requests, re, sys
H = {"User-Agent": "Mozilla/5.0"}
base = "https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizaRC/OVCCallejero.asmx/Consulta_DNPRC"
for rc in ["0032503VG0103C0000QR", "0032503VG0103C"]:
    try:
        r = requests.get(base, params={"Provincia": "", "Municipio": "", "RC": rc}, headers=H, timeout=25)
        print("RC", rc, "->", r.status_code, len(r.text))
        t = r.text
        print(t[:3000])
    except Exception as e:
        print("ERR", rc, type(e).__name__, e)
    print("-" * 80)

