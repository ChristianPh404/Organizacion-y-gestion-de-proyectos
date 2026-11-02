"""
========================================================================================
SCRIPT DE AUDITORÍA Y VERIFICACIÓN MATEMÁTICA: CAPÍTULO 2 (DISPONIBILIDAD Y ACOPIO)
Proyecto: Biorrefinería Multibiomasa Oleícola (120 000 t b.s./año)
Asignatura: Organización y Gestión de Proyectos (OGP) - UGR
========================================================================================

Este script realiza la verificación exhaustiva e independiente de:
1. Tabla 2.1: Superficies agronómicas y rendimientos del olivar (MAPA 2025).
2. Tabla 2.2: Almazaras activas, aceituna molturada y orujo generado (AICA 2026 y MAPA 2025).
3. Tabla 2.3: Generación oficial de poda según índices Junta de Andalucía (CAP 2008) y Romero-García (2014).
4. Tabla 2.4: Balance neto multibiomasa provincial frente a la demanda nominal de la biorrefinería.
5. Tabla 2.5: Distribución estacional mensual oficial de molturación en Córdoba, Granada y Jaén (SIMO / AICA).
6. Tabla 2.6: Planificación de acopio, horas de operación mensual (8 000 h/año) e inventarios (stocks).
"""

import numpy as np
import matplotlib.pyplot as plt

print("="*85)
print(" AUDITORÍA TÉCNICA - CAPÍTULO 2: DISPONIBILIDAD Y ESTACIONALIDAD DE MATERIAS PRIMAS")
print("="*85)

# --------------------------------------------------------------------------------------
# 1. TABLA 2.1: SUPERFICIES DE OLIVAR (MAPA 2025 - OL1000)
# --------------------------------------------------------------------------------------
print("\n" + "-"*85)
print("1. VERIFICACIÓN TABLA 2.1: SUPERFICIES Y RENDIMIENTOS (MAPA 2025)")
print("-"*85)

superficies = {
    "Córdoba": {"sec_tot": 318452, "reg_tot": 62076, "sec_prod": 315789, "reg_prod": 58988, "r_sec": 3146, "r_reg": 8432},
    "Granada": {"sec_tot": 148011, "reg_tot": 62467, "sec_prod": 145257, "reg_prod": 60667, "r_sec": 2583, "r_reg": 4240},
    "Jaén":    {"sec_tot": 353231, "reg_tot": 235645, "sec_prod": 353231, "reg_prod": 235645, "r_sec": 3000, "r_reg": 4942},
}

tot_sec_tot = sum(d["sec_tot"] for d in superficies.values())
tot_reg_tot = sum(d["reg_tot"] for d in superficies.values())
tot_sup_tot = tot_sec_tot + tot_reg_tot

tot_sec_prod = sum(d["sec_prod"] for d in superficies.values())
tot_reg_prod = sum(d["reg_prod"] for d in superficies.values())
tot_prod = tot_sec_prod + tot_reg_prod

for prov, d in superficies.items():
    s_tot = d["sec_tot"] + d["reg_tot"]
    p_tot = d["sec_prod"] + d["reg_prod"]
    print(f"  {prov:10s} -> Sup. Total: {s_tot:7d} ha | Secano Prod: {d['sec_prod']:7d} ha | Regadío Prod: {d['reg_prod']:7d} ha | Total Prod: {p_tot:7d} ha")

print(f"  {'TRIÁNGULO':10s} -> Sup. Total: {tot_sup_tot:7d} ha | Secano Prod: {tot_sec_prod:7d} ha | Regadío Prod: {tot_reg_prod:7d} ha | Total Prod: {tot_prod:7d} ha")

assert tot_sup_tot == 1179882, f"Error en Sup. Total Triángulo: {tot_sup_tot}"
assert tot_prod == 1169577, f"Error en Total Prod Triángulo: {tot_prod}"
print("  [OK] Tabla 2.1 verificada con éxito (coincidencia exacta al 100 %).")

# --------------------------------------------------------------------------------------
# 2. TABLA 2.2: MOLTURACIÓN Y ALMAZARAS (AICA SEPTIEMBRE 2026 Y MAPA 2025)
# --------------------------------------------------------------------------------------
print("\n" + "-"*85)
print("2. VERIFICACIÓN TABLA 2.2: ALMAZARAS, MOLTURACIÓN Y ACEITE (AICA 2026)")
print("-"*85)

molturacion = {
    "Córdoba": {"alm": 182, "molt": 1437381.6, "aceite": 247482.0, "orujo": 1206349},
    "Granada": {"alm": 108, "molt": 507811.6,  "aceite": 107381.0, "orujo": 376985},
    "Jaén":    {"alm": 330, "molt": 1940412.1, "aceite": 390536.6, "orujo": 1666786},
}

tot_alm = sum(d["alm"] for d in molturacion.values())
tot_molt = sum(d["molt"] for d in molturacion.values())
tot_aceite = sum(d["aceite"] for d in molturacion.values())
tot_orujo = sum(d["orujo"] for d in molturacion.values())

esp_molt = 7004000.5
and_molt = 5276173.7

pct_triangulo = (tot_molt / esp_molt) * 100
pct_andalucia = (and_molt / esp_molt) * 100

for prov, d in molturacion.items():
    pct = (d["molt"] / esp_molt) * 100
    print(f"  {prov:10s} -> Almazaras: {d['alm']:3d} | Molturación: {d['molt']:11.1f} t | Aceite: {d['aceite']:10.1f} t | % s/Esp: {pct:5.2f} %")

print(f"  {'TRIÁNGULO':10s} -> Almazaras: {tot_alm:3d} | Molturación: {tot_molt:11.1f} t | Aceite: {tot_aceite:10.1f} t | % s/Esp: {pct_triangulo:5.2f} %")
print(f"  {'ANDALUCÍA':10s} -> Molturación: {and_molt:11.1f} t ({pct_andalucia:5.2f} % s/España)")

assert tot_alm == 620, "Error en almazaras"
assert abs(tot_molt - 3885605.3) < 0.1, "Error en molturación total triángulo"
print("  [OK] Tabla 2.2 verificada con éxito.")

# --------------------------------------------------------------------------------------
# 3. TABLA 2.3: POTENCIAL ANUAL DE PODA DEL OLIVAR (CAP 2008 & ROMERO-GARCÍA 2014)
# --------------------------------------------------------------------------------------
print("\n" + "-"*85)
print("3. VERIFICACIÓN TABLA 2.3: ÍNDICES DE PODA Y FRACCIÓN LEÑOSA MECANIZABLE")
print("-"*85)

# Índices oficiales (t/ha al 20% humedad):
# IR = 1.70 t/ha si rend >= 3000 kg/ha
# IR = 1.40 t/ha si rend < 3000 kg/ha (Granada secano: 2583 kg/ha)
poda_data = {
    "Córdoba": {"sec_prod": 315789, "ir_sec": 1.70, "reg_prod": 58988,  "ir_reg": 1.70},
    "Granada": {"sec_prod": 145257, "ir_sec": 1.40, "reg_prod": 60667,  "ir_reg": 1.70},
    "Jaén":    {"sec_prod": 353231, "ir_sec": 1.70, "reg_prod": 235645, "ir_reg": 1.70},
}

tot_poda_20h = 0
tot_poda_bs = 0
tot_fracc_lenosa = 0
tot_madera_mec = 0

for prov, d in poda_data.items():
    poda_sec = d["sec_prod"] * d["ir_sec"]
    poda_reg = d["reg_prod"] * d["ir_reg"]
    poda_tot = poda_sec + poda_reg
    poda_bs = poda_tot * 0.80  # 20% humedad -> 80% materia seca
    fracc_len = poda_bs * 0.75 # 75% fracción leñosa (50% ramas finas + 25% madera gruesa)
    mad_mec = fracc_len * 0.50 # 50% factor mecanizable
    
    tot_poda_20h += poda_tot
    tot_poda_bs += poda_bs
    tot_fracc_lenosa += fracc_len
    tot_madera_mec += mad_mec
    
    print(f"  {prov:10s} -> Poda 20% hum: {poda_tot:8.0f} t | Poda b.s.: {poda_bs:8.0f} t | Fracc. Leñosa (75%): {fracc_len:8.0f} t | Madera Mec. (50%): {mad_mec:8.0f} t")

print(f"  {'TRIÁNGULO':10s} -> Poda 20% hum: {tot_poda_20h:8.0f} t | Poda b.s.: {tot_poda_bs:8.0f} t | Fracc. Leñosa (75%): {tot_fracc_lenosa:8.0f} t | Madera Mec. (50%): {tot_madera_mec:8.0f} t")

assert round(tot_poda_20h) == 1944704, f"Error Poda 20% hum: {tot_poda_20h}"
assert round(tot_poda_bs) == 1555763, f"Error Poda bs: {tot_poda_bs}"
assert round(tot_fracc_lenosa) == 1166822, f"Error Fracción leñosa: {tot_fracc_lenosa}"
assert round(tot_madera_mec) == 583411, f"Error Madera mecanizable: {tot_madera_mec}"
print("  [OK] Tabla 2.3 verificada con éxito.")

# --------------------------------------------------------------------------------------
# 4. TABLA 2.4: DISPONIBILIDAD NETA MULTIBIOMASA Y DEMANDA (120 000 t b.s./año)
# --------------------------------------------------------------------------------------
print("\n" + "-"*85)
print("4. VERIFICACIÓN TABLA 2.4: SÍNTESIS DE DISPONIBILIDAD NETA FRENTE A DEMANDA")
print("-"*85)

# B-1: Hueso = Molturada * 0.095 * 0.92 = Molturada * 0.0874
# B-2a: Hoja almazara = Molturada * 0.05 * 0.60 = Molturada * 0.0300
# B-2b: Hoja poda = Poda b.s. * 0.25 * 0.50 = Poda b.s. * 0.125
# B-4: Madera mecanizable = Poda b.s. * 0.75 * 0.50 = Poda b.s. * 0.375

disp_multibiomasa = {}
for prov in ["Córdoba", "Granada", "Jaén"]:
    molt = molturacion[prov]["molt"]
    d_poda = poda_data[prov]
    p_tot_bs = (d_poda["sec_prod"]*d_poda["ir_sec"] + d_poda["reg_prod"]*d_poda["ir_reg"]) * 0.80
    
    b1 = round(molt * 0.0874)
    b2a = round(molt * 0.0300)
    b2b = round(p_tot_bs * 0.125)
    b4 = round(p_tot_bs * 0.375)
    total_prov = b1 + b2a + b2b + b4
    
    disp_multibiomasa[prov] = {"B1": b1, "B2a": b2a, "B2b": b2b, "B4": b4, "Total": total_prov}
    print(f"  {prov:10s} -> Hueso (B-1): {b1:6d} t | Hoja Alm (B-2a): {b2a:6d} t | Hoja Poda (B-2b): {b2b:6d} t | Madera (B-4): {b4:6d} t | TOTAL: {total_prov:7d} t b.s.")

tot_b1 = sum(d["B1"] for d in disp_multibiomasa.values())
tot_b2a = sum(d["B2a"] for d in disp_multibiomasa.values())
tot_b2b = sum(d["B2b"] for d in disp_multibiomasa.values())
tot_b4 = sum(d["B4"] for d in disp_multibiomasa.values())
tot_disp = sum(d["Total"] for d in disp_multibiomasa.values())

print(f"  {'TOTAL EJE':10s} -> Hueso (B-1): {tot_b1:6d} t | Hoja Alm (B-2a): {tot_b2a:6d} t | Hoja Poda (B-2b): {tot_b2b:6d} t | Madera (B-4): {tot_b4:6d} t | TOTAL: {tot_disp:7d} t b.s.")

# Demandas nominales de la biorrefinería
demanda_b1 = 15000
demanda_b2 = 40000
demanda_b4 = 65000
demanda_tot = 120000

cap_b1 = (demanda_b1 / tot_b1) * 100
cap_b2_alm = (demanda_b2 / tot_b2a) * 100
cap_b2_tot = (demanda_b2 / (tot_b2a + tot_b2b)) * 100
cap_b4 = (demanda_b4 / tot_b4) * 100
cap_tot = (demanda_tot / tot_disp) * 100

print(f"\n  Captación nominal de la planta:")
print(f"    - Hueso de aceituna (B-1)          : {demanda_b1:6d} t b.s. -> {cap_b1:.2f} % del total disponible en el eje")
print(f"    - Hoja de olivo (B-2)              : {demanda_b2:6d} t b.s. -> {cap_b2_alm:.2f} % de hoja almazara ({cap_b2_tot:.2f} % del potencial foliar total)")
print(f"    - Madera y ramas de poda (B-4)     : {demanda_b4:6d} t b.s. -> {cap_b4:.2f} % de la madera mecanizable")
print(f"    - TOTAL BIOMASA REQUERIDA          : {demanda_tot:6d} t b.s. -> {cap_tot:.2f} % de la biomasa disponible neta")

assert tot_b1 == 339602, f"Error B-1: {tot_b1}"
assert tot_b2a in [116567, 116568], f"Error B-2a: {tot_b2a}"
assert tot_b2b == 194470, f"Error B-2b: {tot_b2b}"
assert tot_b4 == 583411, f"Error B-4: {tot_b4}"
assert tot_disp in [1234050, 1234051], f"Error Total Disp: {tot_disp}"
print("  [OK] Tabla 2.4 verificada con éxito.")

# --------------------------------------------------------------------------------------
# 5. TABLA 2.5: ESTACIONALIDAD MENSUAL DE MOLTURACIÓN (SIMO / AICA 2025/2026)
# --------------------------------------------------------------------------------------
print("\n" + "-"*85)
print("5. VERIFICACIÓN TABLA 2.5: DISTRIBUCIÓN MENSUAL DE MOLTURACIÓN")
print("-"*85)

meses = ["Octubre", "Noviembre", "Diciembre", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio-Sept"]
molt_mensual_triangulo = [76584.2, 609080.2, 1254521.9, 1058761.4, 539440.7, 305036.7, 38354.2, 3826.0, 0.0]

tot_m_mensual = sum(molt_mensual_triangulo)
assert abs(tot_m_mensual - tot_molt) < 0.1, "Error en suma de molturación mensual"

pico_cuatrimestre = sum(molt_mensual_triangulo[1:5]) # Nov, Dic, Ene, Feb
pct_cuatrimestre = (pico_cuatrimestre / tot_m_mensual) * 100

print(f"  Molturación total triángulo: {tot_m_mensual:11.1f} t")
print(f"  Concentración en Nov-Feb    : {pico_cuatrimestre:11.1f} t ({pct_cuatrimestre:.2f} %)")
for m, v in zip(meses, molt_mensual_triangulo):
    pct = (v / tot_m_mensual) * 100
    hueso_m = v * 0.0874
    hoja_m = v * 0.0300
    print(f"    {m:12s}: {v:11.1f} t ({pct:5.2f} %) | Hueso gen.: {hueso_m:8.1f} t b.s. | Hoja gen.: {hoja_m:8.1f} t b.s.")

print("  [OK] Tabla 2.5 verificada con éxito.")

# --------------------------------------------------------------------------------------
# 6. TABLA 2.6: PLANIFICACIÓN DE ACOPIO, ALIMENTACIÓN E INVENTARIO (8 000 h/año)
# --------------------------------------------------------------------------------------
print("\n" + "-"*85)
print("6. VERIFICACIÓN TABLA 2.6: CALENDARIO MENSUAL, ALIMENTACIÓN E INVENTARIOS")
print("-"*85)

# Calendario mensual (Octubre a Septiembre)
meses_op = [
    "Octubre", "Noviembre (Parada)", "Diciembre (Navidad)", "Enero", "Febrero",
    "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto (Vacaciones)", "Septiembre (Enlace)"
]

horas_op = [700, 500, 600, 740, 660, 700, 720, 720, 720, 720, 540, 680]
assert sum(horas_op) == 8000, f"Error en suma de horas operativas: {sum(horas_op)}"

# Acopio mensual recibido en base seca (t b.s.)
acopio_hueso  = [500, 3000, 4500, 4000, 2000, 1000,    0,    0,    0,    0,    0,    0]
acopio_hoja   = [  0, 6000, 15000, 13000, 6000,    0,    0,    0,    0,    0,    0,    0]
acopio_madera = [  0,    0,     0,     0, 14000, 26000, 18000, 7000,    0,    0,    0,    0]

assert sum(acopio_hueso) == 15000, "Error suma acopio hueso"
assert sum(acopio_hoja) == 40000, "Error suma acopio hoja"
assert sum(acopio_madera) == 65000, "Error suma acopio madera"

# Consumo consecutivo a 15.00 t b.s./h
# Octubre: 700 h * 15 = 10 500 t hueso
# Noviembre: 500 h -> 300 h hueso (4500 t) + 200 h hoja (3000 t) = 7500 t
# Diciembre: 600 h * 15 = 9000 t hoja
# Enero: 740 h * 15 = 11100 t hoja
# Febrero: 660 h * 15 = 9900 t hoja
# Marzo: 700 h -> 466.7 h hoja (7000 t) + 233.3 h madera (3500 t) = 10500 t
# Abril: 720 h * 15 = 10800 t madera
# Mayo: 720 h * 15 = 10800 t madera
# Junio: 720 h * 15 = 10800 t madera
# Julio: 720 h * 15 = 10800 t madera
# Agosto: 540 h * 15 = 8100 t madera
# Septiembre: 680 h * 15 = 10200 t madera

alim_hueso  = [10500, 4500,    0,     0,    0,    0,     0,     0,     0,     0,    0,     0]
alim_hoja   = [    0, 3000, 9000, 11100, 9900, 7000,     0,     0,     0,     0,    0,     0]
alim_madera = [    0,    0,    0,     0,    0, 3500, 10800, 10800, 10800, 10800, 8100, 10200]

assert sum(alim_hueso) == 15000, "Error suma consumo hueso"
assert sum(alim_hoja) == 40000, "Error suma consumo hoja"
assert sum(alim_madera) == 65000, "Error suma consumo madera"

# Simulación dinámica de stock / inventario
stock_hueso = 11500 # Stock de seguridad y enlace de campaña (fin de septiembre anterior)
stock_hoja = 0
stock_madera = 0

hist_stock_hueso = []
hist_stock_hoja = []
hist_stock_madera = []
hist_stock_total = []

print(f"  Mes                    Horas  Acopio (t)  Alimentación (t)  Stock Hueso  Stock Hoja  Stock Mad.  STOCK TOTAL")
print("  " + "-"*95)

for i in range(12):
    stock_hueso  += acopio_hueso[i]  - alim_hueso[i]
    stock_hoja   += acopio_hoja[i]   - alim_hoja[i]
    stock_madera += acopio_madera[i] - alim_madera[i]
    stock_tot = stock_hueso + stock_hoja + stock_madera
    
    hist_stock_hueso.append(stock_hueso)
    hist_stock_hoja.append(stock_hoja)
    hist_stock_madera.append(stock_madera)
    hist_stock_total.append(stock_tot)
    
    acop_m = acopio_hueso[i] + acopio_hoja[i] + acopio_madera[i]
    alim_m = alim_hueso[i] + alim_hoja[i] + alim_madera[i]
    
    print(f"  {meses_op[i]:22s} {horas_op[i]:4d} h   {acop_m:7d} t     {alim_m:7d} t      {stock_hueso:7d} t   {stock_hoja:7d} t  {stock_madera:7d} t   {stock_tot:7d} t")
    assert stock_hueso >= 0, f"Ruptura de stock hueso en {meses_op[i]}"
    assert stock_hoja >= 0, f"Ruptura de stock hoja en {meses_op[i]}"
    assert stock_madera >= 0, f"Ruptura de stock madera en {meses_op[i]}"

max_stock_hueso = max(hist_stock_hueso)
max_stock_hoja = max(hist_stock_hoja)
max_stock_madera = max(hist_stock_madera)
max_stock_total = max(hist_stock_total)

print("  " + "-"*95)
print(f"  CAPACIDAD MÁXIMA DE ALMACENAMIENTO REQUERIDA (DISEÑO ÁREA 100):")
print(f"    - Silos cerrados de hueso      : {max_stock_hueso:6d} t b.s. (con 8% hum. -> {max_stock_hueso/0.92:6.0f} t com., Vol: {max_stock_hueso/(0.92*0.68):6.0f} m³)")
print(f"    - Parque cubierto de hoja      : {max_stock_hoja:6d} t b.s. (con 25% hum. -> {max_stock_hoja/0.75:6.0f} t)")
print(f"    - Parque intemperie de madera  : {max_stock_madera:6d} t b.s. (con 20% hum. -> {max_stock_madera/0.80:6.0f} t)")
print(f"    - PICO MÁXIMO COMBINADO EN PLANTA: {max_stock_total:6d} t b.s. (registrado a finales de abril)")

assert max_stock_hueso == 11500, "Error en stock máximo de hueso"
assert max_stock_hoja == 10900, "Error en stock máximo de hoja"
assert max_stock_madera == 43700, "Error en stock máximo de madera"
assert max_stock_total == 55200, "Error en stock total máximo"
assert stock_hueso == 11500, "Error en enlace final de campaña (el stock de hueso debe retornar exactamente a 11 500 t)"
print("  [OK] Tabla 2.6 verificada con éxito (balance dinámico cerrado perfecto).")

# --------------------------------------------------------------------------------------
# 7. GENERACIÓN DE GRÁFICO TÉCNICO DE AUDITORÍA
# --------------------------------------------------------------------------------------
print("\n" + "-"*85)
print("7. GENERANDO GRÁFICO DE VERIFICACIÓN DINÁMICA DE ACOPIO Y STOCKS...")
print("-"*85)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8.5), sharex=True)

x_indices = np.arange(len(meses_op))
meses_cortos = ["Oct", "Nov", "Dic", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep"]

# Subplot 1: Alimentación mensual vs Régimen secuencial de recurso único
width = 0.55
ax1.bar(x_indices, alim_hueso, width, label="Hueso (15 000 t)", color="#C19A6B", edgecolor="black", alpha=0.85)
ax1.bar(x_indices, alim_hoja, width, bottom=alim_hueso, label="Hoja (40 000 t)", color="#556B2F", edgecolor="black", alpha=0.85)
bot_madera = np.array(alim_hueso) + np.array(alim_hoja)
ax1.bar(x_indices, alim_madera, width, bottom=bot_madera, label="Madera poda (65 000 t)", color="#8B5A2B", edgecolor="black", alpha=0.85)

ax1.set_ylabel("Alimentación a planta (t b.s./mes)", fontsize=11, fontweight="bold")
ax1.set_title("Régimen de Operación Secuencial de Recurso Único (8 000 h/año, 15.00 t b.s./h)", fontsize=12, fontweight="bold")
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend(loc="upper right", framealpha=0.9)

# Subplot 2: Evolución de Inventarios a Fin de Mes
ax2.plot(x_indices, hist_stock_hueso, marker="s", color="#C19A6B", linewidth=2, label="Stock Hueso (Silos)")
ax2.plot(x_indices, hist_stock_hoja, marker="^", color="#556B2F", linewidth=2, label="Stock Hoja (Parque cubierto)")
ax2.plot(x_indices, hist_stock_madera, marker="D", color="#8B5A2B", linewidth=2, label="Stock Madera (Parque exterior)")
ax2.plot(x_indices, hist_stock_total, marker="o", color="#1E3F66", linewidth=2.5, linestyle="--", label="INVENTARIO TOTAL EN PLANTA")

ax2.axhline(55200, color="red", linestyle=":", label="Pico Máximo de Diseño (55 200 t)")
ax2.set_ylabel("Inventario fin de mes (t b.s.)", fontsize=11, fontweight="bold")
ax2.set_xlabel("Mes de Campaña", fontsize=11, fontweight="bold")
ax2.set_xticks(x_indices)
ax2.set_xticklabels(meses_cortos, fontsize=10, fontweight="bold")
ax2.set_title("Evolución Dinámica de Existencias (Capacidad Requerida para Área 100)", fontsize=12, fontweight="bold")
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend(loc="upper left", framealpha=0.9)

plt.tight_layout()
graph_path = r"f:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Estudio_de_Mercado\grafico_auditoria_seccion2.png"
plt.savefig(graph_path, dpi=300)
plt.close()

print(f"  [OK] Gráfico generado satisfactoriamente en: {graph_path}")
print("="*85)
print(" TODOS LOS CÁLCULOS, TABLAS Y BALANCES DEL CAPÍTULO 2 ESTÁN 100 % VERIFICADOS")
print("="*85)
