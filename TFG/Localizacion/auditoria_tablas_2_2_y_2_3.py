"""
Auditoría Técnica y Verificación de Cálculos
Documento nº 2: Estudio de Localización, Implantación y Planos Justificativos
TFG Biorrefinería Oleícola - Christian Pérez Hita
"""

import numpy as np
import pandas as pd

def auditoria_tabla_2_2_y_2_3():
    print("=" * 80)
    print("AUDITORÍA DE MACROLOCALIZACIÓN: TABLA 2.2 (INDICADORES) Y TABLA 2.3 (MATRIZ)")
    print("=" * 80)
    
    # Fuentes empíricas de los indicadores:
    # 1. Biomasa (t/año) en radio de 60 km:
    #    Balances comarcales de molturación de AICA y poda leñosa (MAPA / CAP).
    # 2. Ratio SABI de Oportunidad (M€/comp):
    #    Búsqueda en SABI de empresas almazareras ("aceite de oliva" / "almazara")
    #    cruzada con censo de plantas consumidoras de biomasa (AVEBIOM/AAE).
    # 3. Red eléctrica MT/AT y evacuación:
    #    Distancia física y tensión de la subestación transformadora más próxima (Endesa / REE).
    # 4. Cercanía a refinerías / off-takers (km):
    #    Distancia media ponderada por red viaria a Moeve San Roque, CLH/Exolum y Huelva.
    # 5. Logística viaria y FFCC:
    #    Conectividad directa por autovía de gran capacidad y acceso a terminal Adif / Puerto Seco.
    # 6. Recursos hídricos:
    #    Disponibilidad acuífero concesionada (CHG) y capacidad de vertido / depuración.

    indicadores = {
        "Factor": [
            "1. Biomasa (<= 60 km) [t/año]",
            "2. Presión biomasa (SABI) [M€/comp]",
            "3. Red eléctrica MT/AT y evacuación [Cercanía ST]",
            "4. Cercanía refinerías [km transporte]",
            "5. Logística viaria y FFCC [Infraestructura]",
            "6. Recursos hídricos [CHG / Acuífero]"
        ],
        "Tipo_Criterio": ["Beneficio", "Beneficio", "Cualitativo_Tecnico", "Coste_Distancia", "Cualitativo_Tecnico", "Cualitativo_Tecnico"],
        "Granada_Dato": [115000.0, 128.47, "ST Loja 66/20 kV (1.5 km)", 215.0, "A-92 + P. Seco Antequera", "Acuífero Sierra Gorda (Loja)"],
        "Cordoba_Dato": [128000.0, 88.75, "ST Lucena (2.0 km)", 185.0, "A-4/A-45 + Adif El Higuerón", "Cuenca regulada Guadalquivir"],
        "Jaen_Dato":    [145000.0, 55.73, "ST Alcalá (3.2 km)", 265.0, "A-44 (Sin FFCC en comarca)", "Cabecera Guadalquivir"]
    }

    df_ind = pd.DataFrame(indicadores)

    # 1. Normalización Matemática para criterios puramente cuantitativos:
    # Criterio beneficio: P = 10 * X / max(X)
    # Criterio coste:     P = 10 * min(X) / X

    # Biomasa:
    bio = np.array([115000.0, 128000.0, 145000.0])
    p_bio = 10.0 * bio / np.max(bio)

    # SABI:
    sabi = np.array([128.47, 88.75, 55.73])
    p_sabi = 10.0 * sabi / np.max(sabi)

    # Distancia refinerías:
    dist = np.array([215.0, 185.0, 265.0])
    p_dist = 10.0 * np.min(dist) / dist

    print("\n--- CÁLCULO DE NORMALIZACIÓN MATEMÁTICA (TABLA 2.2) ---")
    print(f"1. Biomasa (max = {np.max(bio)} t/año):")
    print(f"   Granada: 10 * 115000 / 145000 = {p_bio[0]:.2f} -> Redondeo: {p_bio[0]:.1f}")
    print(f"   Córdoba: 10 * 128000 / 145000 = {p_bio[1]:.2f} -> Redondeo: {p_bio[1]:.1f}")
    print(f"   Jaén:    10 * 145000 / 145000 = {p_bio[2]:.2f} -> Redondeo: {p_bio[2]:.1f}")

    print(f"\n2. Ratio SABI (max = {np.max(sabi)} M€/comp):")
    print(f"   Granada: 10 * 128.47 / 128.47 = {p_sabi[0]:.2f} -> Redondeo: {p_sabi[0]:.1f}")
    print(f"   Córdoba: 10 * 88.75 / 128.47  = {p_sabi[1]:.2f} -> Redondeo: {p_sabi[1]:.1f}")
    print(f"   Jaén:    10 * 55.73 / 128.47  = {p_sabi[2]:.2f} -> Redondeo: {p_sabi[2]:.1f}")

    print(f"\n4. Distancia Refinerías (min = {np.min(dist)} km):")
    print(f"   Granada: 10 * 185 / 215 = {p_dist[0]:.2f} -> Redondeo: {p_dist[0]:.1f}")
    print(f"   Córdoba: 10 * 185 / 185 = {p_dist[1]:.2f} -> Redondeo: {p_dist[1]:.1f}")
    print(f"   Jaén:    10 * 185 / 265 = {p_dist[2]:.2f} -> Redondeo: {p_dist[2]:.1f}")

    # Tabla 2.3 Matriz de Decisión de Factores Ponderados:
    pesos = np.array([0.25, 0.20, 0.20, 0.15, 0.10, 0.10])
    
    calificaciones = {
        "Factor": [
            "1. Disponibilidad de materia prima",
            "2. Baja presión competitiva biomasa (SABI)",
            "3. Red eléctrica MT/AT y evacuación",
            "4. Cercanía a refinerías y distribuidores",
            "5. Logística viaria, ferroviaria e intermodal",
            "6. Disponibilidad de agua y vertido (CHG)"
        ],
        "Peso (wi)": pesos,
        "Granada_Calif": [7.9, 10.0, 9.5, 8.6, 9.0, 9.0],
        "Cordoba_Calif": [8.8, 6.9, 8.5, 10.0, 9.5, 7.5],
        "Jaen_Calif":    [10.0, 4.3, 8.0, 7.0, 6.5, 7.0]
    }
    
    df_matriz = pd.DataFrame(calificaciones)
    df_matriz["Granada_Pond"] = df_matriz["Peso (wi)"] * df_matriz["Granada_Calif"]
    df_matriz["Cordoba_Pond"] = df_matriz["Peso (wi)"] * df_matriz["Cordoba_Calif"]
    df_matriz["Jaen_Pond"]    = df_matriz["Peso (wi)"] * df_matriz["Jaen_Calif"]

    tot_gr = df_matriz["Granada_Pond"].sum()
    tot_co = df_matriz["Cordoba_Pond"].sum()
    tot_ja = df_matriz["Jaen_Pond"].sum()

    print("\n" + "=" * 80)
    print("MATRIZ DE DECISIÓN MULTICRITERIO (TABLA 2.3)")
    print("=" * 80)
    for _, row in df_matriz.iterrows():
        print(f"{row['Factor'][:42]:<42} | w={row['Peso (wi)']} | Gr: {row['Granada_Calif']:4.1f} (pond {row['Granada_Pond']:.2f}) | Co: {row['Cordoba_Calif']:4.1f} (pond {row['Cordoba_Pond']:.2f}) | Ja: {row['Jaen_Calif']:4.1f} (pond {row['Jaen_Pond']:.2f})")
    
    print("-" * 80)
    print(f"{'PUNTUACIÓN TOTAL PONDERADA':<42} | w=1.00 | Granada: {tot_gr:.2f} (8.97) | Córdoba: {tot_co:.2f} (8.48) | Jaén: {tot_ja:.2f} (7.36)")
    print("=" * 80)
    print("CONCLUSIÓN DE MACROLOCALIZACIÓN: Granada resulta la alternativa óptima (8.97 puntos).")

if __name__ == "__main__":
    auditoria_tabla_2_2_y_2_3()

