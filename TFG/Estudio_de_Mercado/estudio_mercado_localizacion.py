import numpy as np
import pandas as pd

# =====================================================================
# 1. DIMENSIONAMIENTO Y ESTIMACIÓN ECONÓMICA PRELIMINAR (Tabla 5 y 8)
# =====================================================================
def dimensionar_planta(toneladas_materia_prima: float, modo: str = "solo_hueso"):
    """
    Calcula consumos, producción e ingresos anuales escalando los escenarios B-1 (hueso)
    o B-5 (mezcla de residuos del olivar: hueso + hoja + poda) de Jafari-Gohargan et al. (2026).
    """
    # Precios ($/unidad) según Tabla 5 Jafari-Gohargan et al.
    precios = {
        "materia_prima": 17.0,     # $/t
        "enzima": 1000.0,          # $/kg
        "h2so4": 262.0,            # $/t
        "amoniaco": 300.0,         # $/t
        "etanol": 1200.0,          # $/t
        "lignina": 630.0,          # $/t
        "co2": 38.0,               # $/t
        "rich_lignin": 42.0,       # $/t
        "fertilizante": 4.5        # $/t
    }

    # Ratios por tonelada de biomasa seca (calculados de Tabla 8: B-1=15.000 t, B-5=160.000 t)
    if modo == "solo_hueso":
        base_t = 15000.0
        ratios = {
            "enzima_kg": 70.0 / base_t,
            "h2so4_t": 137.0 / base_t,
            "amoniaco_t": 48.0 / base_t,
            "etanol_t": 2028.0 / base_t,
            "lignina_t": 2093.0 / base_t,
            "biogas_m3": 3912361.0 / base_t,
            "co2_t": 5904.0 / base_t,
            "rich_lignin_t": 9503.0 / base_t,
            "fertilizante_t": 650.0 / base_t
        }
    else:  # modo == "mezcla_olivar" (Escenario B-5: hueso + hoja + madera de poda)
        base_t = 160000.0
        ratios = {
            "enzima_kg": 850.0 / base_t,
            "h2so4_t": 1459.0 / base_t,
            "amoniaco_t": 519.0 / base_t,
            "etanol_t": 23444.0 / base_t,
            "lignina_t": 14197.0 / base_t,
            "biogas_m3": 22460957.0 / base_t,
            "co2_t": 66134.0 / base_t,
            "rich_lignin_t": 117501.0 / base_t,
            "fertilizante_t": 6871.0 / base_t
        }

    resultados = {k: v * toneladas_materia_prima for k, v in ratios.items()}
    
    # Ingresos anuales por venta de productos (asumiendo biogás en autoconsumo en caldera Q-01)
    ingresos = {
        "Venta Bioetanol (Corriente 40)": resultados["etanol_t"] * precios["etanol"],
        "Venta Lignina Pura (Corriente 19)": resultados["lignina_t"] * precios["lignina"],
        "Venta CO2 (Corriente 30)": resultados["co2_t"] * precios["co2"],
        "Venta Fracción Rica Lignina": resultados["rich_lignin_t"] * precios["rich_lignin"],
        "Venta Biofertilizante (Corriente 26)": resultados["fertilizante_t"] * precios["fertilizante"]
    }
    
    return resultados, ingresos


# =====================================================================
# 2. ESTUDIO SABI (CNAE 1043 vs DENSIDAD COMPETIDORA)
# =====================================================================
def analisis_ratio_sabi():
    """
    Justificación cuantitativa de localización mediante SABI (Informa), MAPA y AICA:
    Ratio = (Ingresos Explotación Almazaras CNAE 1043 en M€) / (Plantas competidoras de biomasa/orujeras)
    La comarca con mayor ratio dispone de mayor masa crítica de materia prima y menor presión competitiva.
    """
    datos_comarcas = {
        "Comarca": [
            "Poniente Granadino (Loja / Montefrío)",
            "Montes de Granada (Íznalloz / Guadahortuna)",
            "Subbética Cordobesa (Lucena / Priego / Cabra)",
            "Campiña Sur Cordobesa (Puente Genil / Montilla)",
            "Campiña de Jaén (Mengíbar / Andújar)",
            "Sierra Sur de Jaén (Alcalá la Real / Martos)"
        ],
        "Provincia": ["Granada", "Granada", "Córdoba", "Córdoba", "Jaén", "Jaén"],
        "Ingresos_CNAE1043_M€": [385.4, 215.2, 590.8, 410.5, 780.2, 695.0],
        "Almazaras_Activas": [42, 28, 68, 46, 85, 74],
        "Competidores_Biomasa_Orujeras": [3, 2, 7, 5, 14, 11]
    }
    df = pd.DataFrame(datos_comarcas)
    df["Ratio_SABI_M€_por_competidor"] = np.round(df["Ingresos_CNAE1043_M€"] / df["Competidores_Biomasa_Orujeras"], 2)
    df["Puntuacion_Normalizada_10"] = np.round((df["Ratio_SABI_M€_por_competidor"] / df["Ratio_SABI_M€_por_competidor"].max()) * 10.0, 2)
    df = df.sort_values(by="Ratio_SABI_M€_por_competidor", ascending=False)
    return df


# =====================================================================
# 3. MACROLOCALIZACIÓN: MÉTODO DE FACTORES PONDERADOS EXPLICADOS
# =====================================================================
def macrolocalizacion_factores_ponderados():
    """
    Evaluación provincial multicriterio fundamentada en:
    1. Disponibilidad materia prima (MAPA/AICA/SIAE - ESYRCE): Peso 0.25
    2. Baja competencia térmica / Ratio SABI (AVEBIOM/SABI): Peso 0.20
    3. Infraestructura energética AT y Gas (Red Eléctrica / Enagás): Peso 0.20
    4. Cercanía a off-takers y refinerías (CORES/CNMC - Moeve/Repsol): Peso 0.15
    5. Comunicaciones y logística viaria (Autovías A-92 / A-44 / A-45): Peso 0.10
    6. Recursos hídricos y vertido (Confederaciones CHG / Cuenca Mediterránea): Peso 0.10
    """
    factores = [
        "Disponibilidad materia prima (Hueso + Poda - MAPA/AICA)",
        "Baja competencia térmica / Ratio SABI (AVEBIOM/SABI)",
        "Infraestructura energética (Red AT y Gasoducto)",
        "Cercanía a clientes (Off-takers etanol CORES/Moeve)",
        "Comunicaciones y logística viaria (A-92/A-44/A-45)",
        "Disponibilidad de agua y gestión de efluentes (CHG)"
    ]
    pesos = np.array([0.25, 0.20, 0.20, 0.15, 0.10, 0.10])
    
    puntuaciones = {
        "Jaén (Eje Linares-Mengíbar)": [10.0, 4.0, 8.0, 7.0, 8.0, 7.0],
        "Córdoba (Subbética - Lucena/Puente Genil)": [9.0, 7.0, 8.0, 9.0, 9.0, 7.0],
        "Granada (Poniente/Montes - Loja/Íznalloz)": [8.0, 9.5, 9.0, 8.0, 9.0, 8.0]
    }
    
    df = pd.DataFrame(puntuaciones, index=factores)
    df.insert(0, "Peso (wi)", pesos)
    
    totales = {col: np.sum(df[col] * df["Peso (wi)"]) for col in puntuaciones.keys()}
    df.loc["PUNTUACIÓN TOTAL PONDERADA"] = [1.0] + [round(totales[c], 2) for c in puntuaciones.keys()]
    return df


# =====================================================================
# 4. MICROLOCALIZACIÓN: MÉTODO DE BROWN Y GIBSON
# =====================================================================
def microlocalizacion_brown_gibson(
    emplazamientos: list,
    factores_criticos: list,        # 1 si cumple, 0 si no cumple
    costes_anuales_objetivos: list, # Costes totales anuales en € (Transporte + Suelo + Energía)
    factores_subjetivos_Si: list,   # Suma ponderada de factores subjetivos (suma = 1)
    alfa: float = 0.70              # Peso otorgado a los factores objetivos (0.70)
):
    """
    Calcula la Medida de Preferencia de Localización (MPL) según Brown y Gibson:
    FO_i = (1 / C_i) / sum(1 / C_i)
    MPL_i = FC_i * [ alfa * FO_i + (1 - alfa) * FS_i ]
    """
    fc = np.array(factores_criticos, dtype=float)
    costes = np.array(costes_anuales_objetivos, dtype=float)
    fs = np.array(factores_subjetivos_Si, dtype=float)
    
    inversos_coste = 1.0 / costes
    fo = inversos_coste / np.sum(inversos_coste)
    
    mpl = fc * (alfa * fo + (1.0 - alfa) * fs)
    
    df_bg = pd.DataFrame({
        "Emplazamiento": emplazamientos,
        "FC_i (Crítico)": fc,
        "Coste Anual (€)": costes,
        "FO_i (Objetivo)": np.round(fo, 4),
        "FS_i (Subjetivo)": np.round(fs, 4),
        "MPL_i (Índice Final)": np.round(mpl, 4)
    }).sort_values(by="MPL_i (Índice Final)", ascending=False)
    
    return df_bg


if __name__ == "__main__":
    print("=====================================================================")
    print("1. ESCALA B-1: SOLO HUESO (45.000 t/año Hueso Seco)")
    print("=====================================================================")
    prod_hueso, ing_hueso = dimensionar_planta(45000, modo="solo_hueso")
    for k, v in prod_hueso.items():
        print(f"  {k}: {v:,.1f}")
    print(f"  INGRESOS BRUTOS ESTIMADOS: ${sum(ing_hueso.values()):,.2f}/año\n")

    print("=====================================================================")
    print("2. ESCALA B-5: MULTI-BIOMASA (Hueso + Hoja + Poda: 100.000 t/año)")
    print("=====================================================================")
    prod_multi, ing_multi = dimensionar_planta(100000, modo="mezcla_olivar")
    for k, v in prod_multi.items():
        print(f"  {k}: {v:,.1f}")
    print(f"  INGRESOS BRUTOS ESTIMADOS: ${sum(ing_multi.values()):,.2f}/año\n")

    print("=====================================================================")
    print("3. ANÁLISIS CUANTITATIVO SABI / AICA: RATIO PRODUCCIÓN VS COMPETIDORES")
    print("=====================================================================")
    df_sabi = analisis_ratio_sabi()
    print(df_sabi.to_string(index=False), "\n")

    print("=====================================================================")
    print("4. MACROLOCALIZACIÓN POR FACTORES PONDERADOS (FUENTES OFICIALES)")
    print("=====================================================================")
    print(macrolocalizacion_factores_ponderados(), "\n")

    print("=====================================================================")
    print("5. MICROLOCALIZACIÓN POR BROWN Y GIBSON")
    print("=====================================================================")
    candidatos = [
        "Polígono Manzanil II / Loja (Granada)",
        "Polígono Los Santos / Lucena (Córdoba)",
        "Polígono Llano Mazuelos / Alcalá la Real (Jaén)"
    ]
    df_resultado = microlocalizacion_brown_gibson(
        emplazamientos=candidatos,
        factores_criticos=[1, 1, 1],
        costes_anuales_objetivos=[1450000, 1520000, 1610000],
        factores_subjetivos_Si=[0.38, 0.35, 0.27],
        alfa=0.70
    )
    print(df_resultado.to_string(index=False))

