"""
Auditoría numérica EXACTA (sin redondeos intermedios) de estudio_localizacion.tex
Autor del TFG: Christian Pérez Hita

Regla: todos los cálculos se realizan con los valores sin redondear; el redondeo se
aplica únicamente al presentar el resultado final. Se comparan con lo que figura
en las tablas del documento (que usan valores intermedios ya redondeados).
"""
import numpy as np

def hdr(t):
    print("\n" + "=" * 100)
    print(t)
    print("=" * 100)

# ---------------------------------------------------------------------------
# 1. TABLA 2.1 (ratio SABI comarcal)
# ---------------------------------------------------------------------------
hdr("1. TABLA 2.1 - Ratio SABI = ingresos (M EUR) / competidores   [datos TAL COMO figuran en el .tex]")
comarcas = [
    ("Poniente Granadino", "Granada", 385.4, 42, 3, 128.47),
    ("Montes de Granada", "Granada", 215.2, 28, 2, 107.60),
    ("Subbetica Cordobesa", "Cordoba", 590.8, 68, 7, 84.40),
    ("Campina Sur Cordobesa", "Cordoba", 410.5, 46, 5, 82.10),
    ("Sierra Sur de Jaen", "Jaen", 695.0, 74, 11, 63.18),
    ("Campina de Jaen", "Jaen", 780.2, 85, 14, 55.73),
]
for n, p, ing, alm, comp, r_tab in comarcas:
    r = ing / comp
    print(f"{n:<24}{p:<9} {ing:>7.1f}/{comp:<2} = {r:10.5f}   tabla={r_tab:>7.2f}   dif={r - r_tab:+.5f}")

print("\nRatios AGREGADOS por provincia (suma ingresos / suma competidores) con las comarcas de la Tabla 2.1:")
prov = {}
for n, p, ing, alm, comp, r_tab in comarcas:
    a = prov.setdefault(p, [0.0, 0])
    a[0] += ing
    a[1] += comp
for p, (i, c) in prov.items():
    print(f"  {p:<8} {i:8.1f} / {c:2d} = {i / c:9.4f}")
print("\nValores usados en la Tabla 2.2 para el factor 2: Granada 128.47 | Cordoba 88.75 | Jaen 55.73")
print("  -> Granada = mejor comarca de Granada; Jaen = PEOR comarca de Jaen (Campina);")
print("  -> Cordoba 88.75 NO aparece en Tabla 2.1 (Subbetica 84.40, Campina Sur 82.10) y no es reproducible.")

# ---------------------------------------------------------------------------
# 2. TABLA 2.2 - normalización EXACTA
# ---------------------------------------------------------------------------
hdr("2. TABLA 2.2 - Normalización exacta de los criterios cuantitativos")
bio = np.array([115000.0, 128000.0, 145000.0])
sabi = np.array([128.47, 88.75, 55.73])
dist = np.array([215.0, 185.0, 265.0])
p_bio = 10 * bio / bio.max()
p_sabi = 10 * sabi / sabi.max()
p_dist = 10 * dist.min() / dist
tab = {"bio": [7.9, 8.8, 10.0], "sabi": [10.0, 6.9, 4.3], "dist": [8.6, 10.0, 7.0]}
for nom, ex, tb in (("1 Biomasa", p_bio, tab["bio"]), ("2 Ratio SABI", p_sabi, tab["sabi"]), ("4 Dist. refinerias", p_dist, tab["dist"])):
    print(f"{nom:<20} exacto: " + "  ".join(f"{v:8.5f}" for v in ex) + "   | tabla: " + "  ".join(f"{v:5.1f}" for v in tb))
print("Factores 3, 5 y 6 (red electrica, logistica, agua): son JUICIOS asignados (9.5/8.5/8.0 ...), no normalizaciones.")

# ---------------------------------------------------------------------------
# 3. TABLA 2.3 - matriz ponderada EXACTA vs redondeada
# ---------------------------------------------------------------------------
hdr("3. TABLA 2.3 - Matriz macrolocalización: total exacto vs total con calificaciones redondeadas")
w = np.array([0.25, 0.20, 0.20, 0.15, 0.10, 0.10])
subj = {  # factores 3,5,6 (asignados)
    "Granada": {2: 9.5, 4: 9.0, 5: 9.0},
    "Cordoba": {2: 8.5, 4: 9.5, 5: 7.5},
    "Jaen": {2: 8.0, 4: 6.5, 5: 7.0},
}
cols = ["Granada", "Cordoba", "Jaen"]
exact = {}
rounded = {}
for j, c in enumerate(cols):
    v = np.array([p_bio[j], p_sabi[j], subj[c][2], p_dist[j], subj[c][4], subj[c][5]])
    exact[c] = float(np.sum(w * v))
    vr = np.array([tab["bio"][j], tab["sabi"][j], subj[c][2], tab["dist"][j], subj[c][4], subj[c][5]])
    rounded[c] = float(np.sum(w * vr))
    print(f"{c:<8} exacto = {exact[c]:.5f}   con calificaciones redondeadas = {rounded[c]:.5f}   (tabla: "
          f"{ {'Granada': 8.97, 'Cordoba': 8.48, 'Jaen': 7.36}[c] })")
print("Orden:", sorted(exact, key=exact.get, reverse=True))

# ---------------------------------------------------------------------------
# 4. TABLAS 3.1 / 3.2 - microlocalización
# ---------------------------------------------------------------------------
hdr("4. MICROLOCALIZACIÓN - coste del suelo y puntuación")
S = 24637.0
precio = np.array([58.0, 85.0, 68.0])
coste = S * precio
print("Coste suelo (m2 x EUR/m2):", [f"{c:,.0f}" for c in coste], "  (doc: 1428946 / 2094145 / 1675316)")
print("Ahorro Loja vs Lucena:", f"{coste[1] - coste[0]:,.0f}", " vs Alcala:", f"{coste[2] - coste[0]:,.0f}", "(doc: 665199 / 246370)")
p_suelo = 10 * precio.min() / precio
print("P_suelo exacto:", [f"{v:.5f}" for v in p_suelo], "  tabla: 10.0 / 6.8 / 8.5")

wm = np.array([0.20, 0.20, 0.15, 0.15, 0.15, 0.15])
calif = {
    "Loja": [p_suelo[0], 9.5, 9.5, 9.0, 8.5, 8.5],
    "Lucena": [p_suelo[1], 8.0, 8.0, 7.5, 9.0, 8.0],
    "Alcala": [p_suelo[2], 6.5, 7.0, 7.5, 7.5, 10.0],
}
tabm = {"Loja": 9.23, "Lucena": 7.84, "Alcala": 7.80}
calif_r = {k: [round(calif[k][0], 1)] + calif[k][1:] for k in calif}
print("\nPesos micro:", wm.tolist(), "suma =", wm.sum())
for k in calif:
    ex = float(np.sum(wm * np.array(calif[k])))
    rr = float(np.sum(wm * np.array(calif_r[k])))
    print(f"{k:<7} total exacto = {ex:.5f}   con suelo redondeado = {rr:.5f}   tabla = {tabm[k]}")
    pond_tab = [round(x, 2) for x in wm * np.array(calif_r[k])]
    print(f"        ponderadas (2 dec) = {pond_tab}  -> suma de lo mostrado = {sum(pond_tab):.2f}")

# ---------------------------------------------------------------------------
# 5. BROWN & GIBSON
# ---------------------------------------------------------------------------
hdr("5. BROWN Y GIBSON - FO, FS, MPL (alfa = 0.70)")
C = np.array([1450000.0, 1520000.0, 1610000.0])
FS = np.array([0.38, 0.35, 0.27])
FC = np.array([1.0, 1.0, 1.0])
inv = 1 / C
FO = inv / inv.sum()
alfa = 0.70
MPL = FC * (alfa * FO + (1 - alfa) * FS)
for n, f, m in zip(["Loja", "Lucena", "Alcala"], FO, MPL):
    print(f"{n:<7} FO = {f:.7f}   MPL = {m:.7f}")
print("sum FO =", FO.sum(), " sum FS =", FS.sum(), " sum MPL =", MPL.sum())
print("Tabla: FO 0.3503/0.3342/0.3155 ; MPL 0.3592/0.3389/0.3019")
print("\nSensibilidad: MPL(alfa) -> cruces entre curvas")
al = np.linspace(0, 1, 100001)
curv = {n: a_ * FO[i] + (1 - a_) * FS[i] for i, n in enumerate(["Loja", "Lucena", "Alcala"]) for a_ in [al]}
dom = np.all((curv["Loja"] > curv["Lucena"]) & (curv["Loja"] > curv["Alcala"]))
print("Loja domina en todo [0,1]:", bool(dom))
print("MPL(alfa=0): ", [round(float(curv[n][0]), 4) for n in curv], "  MPL(alfa=1):", [round(float(curv[n][-1]), 4) for n in curv])

# ---------------------------------------------------------------------------
# 6. SUPERFICIES / URBANISMO
# ---------------------------------------------------------------------------
hdr("6. SUPERFICIES Y PARÁMETROS URBANÍSTICOS")
areas = [800, 4800, 1600, 5200, 1600, 3600, 2300, 1800, 1100, 1700]
print("Suma de las 10 áreas:", sum(areas), "(doc: 24500)")
print("Holgura parcela - areas:", S - sum(areas))
occ = 13800
print(f"Ocupación: {occ}/{S:.0f} = {100 * occ / S:.4f} %   resto = {S - occ:.0f} m2 = {100 * (S - occ) / S:.4f} %")
print(f"Edificabilidad: 16000/{S:.0f} = {16000 / S:.5f} m2t/m2s (doc 0.65)")
print(f"Fachada x fondo: 122.50 x 201.10 = {122.5 * 201.1:.2f} m2 (parcela: {S:.0f})")
print(f"Plazas aparcamiento exigidas con 1 plaza / 100 m2t sobre 16000 m2t = {16000 / 100:.0f}  (doc: 'minimo 82', proyectadas 85)")
print("  -> 82 plazas correspondería a 8200 m2t, no a 16000 m2t.")

# ---------------------------------------------------------------------------
# 7. Capítulo 1 - capacidad
# ---------------------------------------------------------------------------
hdr("7. CAPÍTULO 1 - capacidad y tasas de captación")
print("Hueso+hoja+poda b.s.:", 15000 + 40000 + 65000, "(doc: 120000)")
print("Horas/año: 289 d x 24 h =", 289 * 24, " ; 120000/6936 =", 120000 / 6936, "t/h (doc 17.30)")
print("Hueso humedo 8 %:", 15000 / 0.92, "(doc 16304);  hoja 20 %:", 40000 / 0.80, "(doc 50000);  madera 20 %:", 65000 / 0.80, "(doc 81250)")
print("Captación hueso: 15000/339602 =", 100 * 15000 / 339602, "% (doc 4.42);  hoja: 40000/311038 =", 100 * 40000 / 311038, "% (doc 12.86);  madera: 65000/583411 =", 100 * 65000 / 583411, "% (doc 11.14)")
print("Biomasa Granada 60 km (tabla 2.2) = 115000 t/año  vs  necesidad 120000 t b.s./año ->", "INSUFICIENTE" if 115000 < 120000 else "ok")

