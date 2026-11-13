"""
Auditoría Técnica y Verificación de Cálculos Exactos (Sin Redondeo Intermedio)
Documento nº 2: Estudio de Localización, Implantación y Planos Justificativos
TFG Biorrefinería Oleícola - Christian Pérez Hita
"""

import numpy as np
import pandas as pd

def auditoria_completa_localizacion():
    print("=" * 88)
    print("1. AUDITORÍA DE MACROLOCALIZACIÓN: TABLA 2.2 (INDICADORES) Y TABLA 2.3 (MATRIZ EXACTA)")
    print("=" * 88)

    # 1. Normalización Matemática exacta (coma flotante de doble precisión):
    # Criterio beneficio: P = 10 * X / max(X)
    # Criterio coste:     P = 10 * min(X) / X
    bio = np.array([115000.0, 128000.0, 145000.0])
    p_bio = 10.0 * bio / np.max(bio)

    # Ratios SABI exactos de la comarca candidata de cada provincia (Tabla 2.1):
    # Granada (Poniente Granadino): 385.4 / 3 = 128.466667 (128.47)
    # Córdoba (Subbética Cordobesa): 590.8 / 7 = 84.400000 (84.40)
    # Jaén (Sierra Sur de Jaén): 695.0 / 11 = 63.181818 (63.18)
    sabi = np.array([385.4 / 3.0, 590.8 / 7.0, 695.0 / 11.0])
    p_sabi = 10.0 * sabi / np.max(sabi)

    dist = np.array([215.0, 185.0, 265.0])
    p_dist = 10.0 * np.min(dist) / dist

    print("\n--- CÁLCULO DE NORMALIZACIÓN MATEMÁTICA EXACTA (TABLA 2.2) ---")
    print(f"1. Biomasa (máx = {np.max(bio):.0f} t/año):")
    print(f"   Granada: 10 * 115000 / 145000 = {p_bio[0]:.6f} -> Mostrar en tabla: {p_bio[0]:.1f}")
    print(f"   Córdoba: 10 * 128000 / 145000 = {p_bio[1]:.6f} -> Mostrar en tabla: {p_bio[1]:.1f}")
    print(f"   Jaén:    10 * 145000 / 145000 = {p_bio[2]:.6f} -> Mostrar en tabla: {p_bio[2]:.1f}")

    print(f"\n2. Ratio SABI Comarca Candidata (máx = {np.max(sabi):.2f} M€/comp):")
    print(f"   Granada (Poniente):  10 * 128.47 / 128.47 = {p_sabi[0]:.6f} -> Mostrar en tabla: {p_sabi[0]:.1f}")
    print(f"   Córdoba (Subbética): 10 * 84.40  / 128.47 = {p_sabi[1]:.6f} -> Mostrar en tabla: {p_sabi[1]:.1f}")
    print(f"   Jaén (Sierra Sur):   10 * 63.18  / 128.47 = {p_sabi[2]:.6f} -> Mostrar en tabla: {p_sabi[2]:.1f}")

    print(f"\n4. Distancia Refinerías (mín = {np.min(dist):.0f} km):")
    print(f"   Granada: 10 * 185 / 215 = {p_dist[0]:.6f} -> Mostrar en tabla: {p_dist[0]:.1f}")
    print(f"   Córdoba: 10 * 185 / 185 = {p_dist[1]:.6f} -> Mostrar en tabla: {p_dist[1]:.1f}")
    print(f"   Jaén:    10 * 185 / 265 = {p_dist[2]:.6f} -> Mostrar en tabla: {p_dist[2]:.1f}")

    # Matriz de Decisión (Tabla 2.3) empleando calificaciones EXACTAS sin redondear:
    pesos_macro = np.array([0.25, 0.20, 0.20, 0.15, 0.10, 0.10])

    calif_exactas_macro = {
        "Factor": [
            "1. Disponibilidad de materia prima",
            "2. Baja presión competitiva biomasa (SABI)",
            "3. Red eléctrica MT/AT y evacuación",
            "4. Cercanía a refinerías y distribuidoras",
            "5. Logística viaria, ferroviaria e intermodal",
            "6. Disponibilidad de agua y vertido (CHG)"
        ],
        "Peso": pesos_macro,
        "Granada_Exact": [p_bio[0], p_sabi[0], 9.5, p_dist[0], 9.0, 9.0],
        "Cordoba_Exact": [p_bio[1], p_sabi[1], 8.5, p_dist[1], 9.5, 7.5],
        "Jaen_Exact":    [p_bio[2], p_sabi[2], 8.0, p_dist[2], 6.5, 7.0]
    }

    df_macro = pd.DataFrame(calif_exactas_macro)
    df_macro["Granada_Pond_Exact"] = df_macro["Peso"] * df_macro["Granada_Exact"]
    df_macro["Cordoba_Pond_Exact"] = df_macro["Peso"] * df_macro["Cordoba_Exact"]
    df_macro["Jaen_Pond_Exact"]    = df_macro["Peso"] * df_macro["Jaen_Exact"]

    tot_gr = df_macro["Granada_Pond_Exact"].sum()
    tot_co = df_macro["Cordoba_Pond_Exact"].sum()
    tot_ja = df_macro["Jaen_Pond_Exact"].sum()

    print("\n" + "=" * 88)
    print("MATRIZ DE DECISIÓN DE MACROLOCALIZACIÓN (TABLA 2.3 - CÁLCULO EXACTO)")
    print("=" * 88)
    for _, r in df_macro.iterrows():
        print(f"{r['Factor'][:40]:<40} | w={r['Peso']:.2f} | "
              f"Gr: {r['Granada_Exact']:6.3f} -> {r['Granada_Pond_Exact']:.4f} ({r['Granada_Pond_Exact']:.2f}) | "
              f"Co: {r['Cordoba_Exact']:6.3f} -> {r['Cordoba_Pond_Exact']:.4f} ({r['Cordoba_Pond_Exact']:.2f}) | "
              f"Ja: {r['Jaen_Exact']:6.3f} -> {r['Jaen_Pond_Exact']:.4f} ({r['Jaen_Pond_Exact']:.2f})")
    print("-" * 88)
    print(f"{'PUNTUACIÓN TOTAL PONDERADA':<40} | w=1.00 | "
          f"Granada: {tot_gr:.5f} ({tot_gr:.2f}) | Córdoba: {tot_co:.5f} ({tot_co:.2f}) | Jaén: {tot_ja:.5f} ({tot_ja:.2f})")

    # 2. Auditoría de Microlocalización (Tablas 3.1, 3.2 y 3.3)
    print("\n" + "=" * 88)
    print("2. AUDITORÍA DE MICROLOCALIZACIÓN: TABLA 3.1, TABLA 3.2 Y BROWN & GIBSON (TABLA 3.3)")
    print("=" * 88)

    coste_suelo = np.array([58.0, 85.0, 68.0])
    p_suelo = 10.0 * np.min(coste_suelo) / coste_suelo

    pesos_micro = np.array([0.20, 0.20, 0.15, 0.15, 0.15, 0.15])
    calif_exactas_micro = {
        "Factor": [
            "1. Coste y disponibilidad de suelo industrial",
            "2. Accesos viarios directos y logística intermodal",
            "3. Conexión eléctrica MT/AT y evacuación",
            "4. Dotación de agua y saneamiento industrial",
            "5. Disponibilidad de mano de obra y FP técnica",
            "6. Incentivos locales y apoyo institucional"
        ],
        "Peso": pesos_micro,
        "Loja_Exact":   [p_suelo[0], 9.5, 9.5, 9.0, 8.5, 8.5],
        "Lucena_Exact": [p_suelo[1], 8.0, 8.0, 7.5, 9.0, 8.0],
        "Alcala_Exact": [p_suelo[2], 6.5, 7.0, 7.5, 7.5, 10.0]
    }

    df_micro = pd.DataFrame(calif_exactas_micro)
    df_micro["Loja_Pond_Exact"]   = df_micro["Peso"] * df_micro["Loja_Exact"]
    df_micro["Lucena_Pond_Exact"] = df_micro["Peso"] * df_micro["Lucena_Exact"]
    df_micro["Alcala_Pond_Exact"] = df_micro["Peso"] * df_micro["Alcala_Exact"]

    tot_loja   = df_micro["Loja_Pond_Exact"].sum()
    tot_lucena = df_micro["Lucena_Pond_Exact"].sum()
    tot_alcala = df_micro["Alcala_Pond_Exact"].sum()

    for _, r in df_micro.iterrows():
        print(f"{r['Factor'][:40]:<40} | w={r['Peso']:.2f} | "
              f"Loja: {r['Loja_Exact']:6.3f} -> {r['Loja_Pond_Exact']:.4f} ({r['Loja_Pond_Exact']:.2f}) | "
              f"Luc: {r['Lucena_Exact']:6.3f} -> {r['Lucena_Pond_Exact']:.4f} ({r['Lucena_Pond_Exact']:.2f}) | "
              f"Alc: {r['Alcala_Exact']:6.3f} -> {r['Alcala_Pond_Exact']:.4f} ({r['Alcala_Pond_Exact']:.2f})")
    print("-" * 88)
    print(f"{'PUNTUACIÓN TOTAL PONDERADA':<40} | w=1.00 | "
          f"Loja (P.I. San Isidro): {tot_loja:.5f} ({tot_loja:.2f}) | "
          f"Lucena: {tot_lucena:.5f} ({tot_lucena:.2f}) | "
          f"Alcalá: {tot_alcala:.5f} ({tot_alcala:.2f})")

    # Brown & Gibson (Tabla 3.3)
    C_i = np.array([1450000.0, 1520000.0, 1610000.0])
    inv_C = 1.0 / C_i
    FO_i = inv_C / np.sum(inv_C)
    FS_i = np.array([0.3800, 0.3500, 0.2700])
    alpha = 0.70
    MPL_i = alpha * FO_i + (1.0 - alpha) * FS_i

    print("\n--- BROWN Y GIBSON (TABLA 3.3 - CÁLCULO EXACTO) ---")
    nombres_bg = ["P.I. San Isidro / Loja (Granada)", "Los Santos / Lucena (Córdoba)", "Llano Mazuelos / Alcalá la Real (Jaén)"]
    for idx, nombre in enumerate(nombres_bg):
        print(f"  {nombre:<40} | C_i = {C_i[idx]:10.0f} € | FO_i = {FO_i[idx]:.6f} ({FO_i[idx]:.4f}) | FS_i = {FS_i[idx]:.4f} | MPL_i = {MPL_i[idx]:.6f} ({MPL_i[idx]:.4f})")
    print("=" * 88)

if __name__ == "__main__":
    auditoria_completa_localizacion()
