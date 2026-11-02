import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ==============================================================================
# 1. BASE DE DATOS TERMODINÁMICA Y ESTEQUIOMÉTRICA NREL (Humbird et al., 2011)
# ==============================================================================
class NRELBiomassDB:
    """
    Propiedades físicas y factores estequiométricos estándar de la base de datos NREL
    para simulación de biorrefinerías lignocelulósicas.
    """
    # Pesos moleculares efectivos (g/mol) de unidades monoméricas en polímero vs libres
    MW = {
        "Glucan": 162.14,      # Unidad C6H10O5 en celulosa
        "Xylan": 132.11,       # Unidad C5H8O4 en hemicelulosa
        "Arabinan": 132.11,
        "Galactan": 162.14,
        "Lignin": 180.00,      # Pseudocomponente aromático NREL
        "Glucose": 180.16,     # C6H12O6
        "Xylose": 150.13,      # C5H10O5
        "Ethanol": 46.07,      # C2H5OH
        "Furfural": 96.08,     # C5H4O2
        "AceticAcid": 60.05,   # CH3COOH
        "CO2": 44.01,
        "H2SO4": 98.08,
        "NH3": 17.03,
        "AmmoniumSulfate": 132.14
    }
    
    # Factores estequiométricos de conversión másica NREL
    FACTOR_GLUCAN_A_GLUCOSA = 180.16 / 162.14   # 1.111 g glucosa / g glucano
    FACTOR_XYLAN_A_XILOSA = 150.13 / 132.11     # 1.136 g xilosa / g xilano
    FACTOR_GAY_LUSSAC_ETANOL = (2 * 46.07) / 180.16  # 0.511 g etanol / g azúcar
    FACTOR_CO2_FERMENTACION = (2 * 44.01) / 180.16   # 0.489 g CO2 / g azúcar

    # Composición del hueso de aceituna seco (Fracción másica - Romero-García et al., 2022)
    COMPOSICION_HUESO_SECO = {
        "Glucan": 0.2091,
        "Xylan": 0.2354,
        "Arabinan": 0.0115,
        "Galactan": 0.0127,
        "Lignin": 0.3560,
        "Extractives": 0.0630,
        "Acetyl": 0.0590,
        "Ash": 0.0060
    }


# ==============================================================================
# 2. MODELADO CINÉTICO DEL REACTOR ENZIMÁTICO R-03 (Chrastil + ODEs en Python)
# ==============================================================================
def modelo_chrastil_glucosa(t_horas: np.ndarray, P_inf: float = 67.0, 
                            C_E0: float = 1.07, k_E: float = 0.41e-3, n: float = 0.66):
    """
    Resuelve el modelo difusional de Chrastil (Cuevas et al., Tabla 5: EH200-2)
    para la concentración de D-glucosa liberada en el reactor enzimático R-03.
    - t_horas: vector de tiempo en horas
    - k_E: dm3/(g·min) -> se multiplica por 60 para pasar a horas
    """
    t_min = t_horas * 60.0
    P_t = P_inf * (1.0 - np.exp(-k_E * C_E0 * t_min)) ** n
    return P_t


def ode_pssf_fermentador(t, y, k_hidrolisis, mu_max, K_s, Y_x_s, Y_e_s):
    """
    Sistema de Ecuaciones Diferenciales Ordinarias (ODE) que reemplaza a MATLAB
    para simular la etapa PSSF ( Reactor R-03 + Biorreactor BF-02 ):
    Variables de estado y = [Celulosa_gL, Glucosa_gL, Biomasa_Levadura_gL, Etanol_gL, CO2_gL]
    """
    C_cel, G, X, E, CO2 = y
    
    # Velocidad de hidrólisis enzimática de celulosa a glucosa (g/L·h)
    r_hid = k_hidrolisis * C_cel
    
    # Cinética de Monod con inhibición por etanol para S. cerevisiae (solo activa tras t >= 4h de presacarificación)
    E_max = 95.0  # Concentración inhibitoria crítica de etanol (g/L)
    if t < 4.0:
        # Etapa 1: Presacarificación pura en R-03 (50 °C, primeras 4 horas sin levadura)
        r_crecimiento = 0.0
        r_consumo_glucosa = 0.0
        r_etanol = 0.0
        r_co2 = 0.0
    else:
        # Etapa 2: SSF simultánea en BF-02 (35-37 °C, inoculado con S. cerevisiae)
        inhibicion_etanol = max(0.0, 1.0 - (E / E_max))
        mu = mu_max * (G / (K_s + G + 1e-6)) * inhibicion_etanol
        r_crecimiento = mu * X
        r_consumo_glucosa = r_crecimiento / Y_x_s
        r_etanol = r_consumo_glucosa * Y_e_s
        r_co2 = r_consumo_glucosa * (NRELBiomassDB.FACTOR_CO2_FERMENTACION * 0.90)

    dC_cel_dt = -r_hid / NRELBiomassDB.FACTOR_GLUCAN_A_GLUCOSA
    dG_dt = r_hid - r_consumo_glucosa
    dX_dt = r_crecimiento
    dE_dt = r_etanol
    dCO2_dt = r_co2
    
    return [dC_cel_dt, dG_dt, dX_dt, dE_dt, dCO2_dt]


def simular_reactor_pssf(t_final_h: float = 72.0):
    """Integra numéricamente el reactor PSSF usando Runge-Kutta de orden 4/5 (RK45)"""
    # Condiciones iniciales (20% WIS consistency - Fig. 5 y 6 Romero-García et al.)
    y0 = [
        70.0,  # Celulosa digestible inicial (g/L)
        16.5,  # Glucosa inicial del líquido detoxificado (g/L)
        2.5,   # Inóculo celular S. cerevisiae (g/L)
        0.0,   # Etanol inicial (g/L)
        0.0    # CO2 acumulado (g/L)
    ]
    parametros = (0.045, 0.25, 2.0, 0.08, 0.46) # k_hid, mu_max, Ks, Y_x/s, Y_e/s
    t_eval = np.linspace(0, t_final_h, 200)
    
    sol = solve_ivp(
        ode_pssf_fermentador, 
        [0, t_final_h], 
        y0, 
        args=parametros, 
        t_eval=t_eval, 
        method="RK45"
    )
    return pd.DataFrame({
        "Tiempo_h": sol.t,
        "Celulosa_gL": sol.y[0],
        "Glucosa_gL": sol.y[1],
        "Levadura_gL": sol.y[2],
        "Etanol_gL": sol.y[3],
        "CO2_gL": sol.y[4]
    })


# ==============================================================================
# 3. MODELO EMPÍRICO MULTIVARIABLE (Abu Tayeh et al., 2026)
# ==============================================================================
def predecir_rendimiento_abu_tayeh(T_celsius: float, C_acido_M: float, carga_enzima_FPU: float):
    """Ecuaciones de superficie de respuesta para Glucosa (g/L) y Etanol (g/L)"""
    glucosa_gL = (
        -0.8400 
        + 0.0415 * T_celsius 
        + 2.0126 * C_acido_M 
        + 0.4990 * carga_enzima_FPU 
        + 0.1261 * (T_celsius - 146.25) * (C_acido_M - 0.4000)
    )
    etanol_gL = (
        -0.4700 
        + 0.0160 * T_celsius 
        + 0.9100 * C_acido_M 
        + 0.2480 * carga_enzima_FPU 
        + 0.0670 * (T_celsius - 146.25) * (C_acido_M - 0.4000)
    )
    return glucosa_gL, etanol_gL


# ==============================================================================
# 4. BALANCE DE MATERIA GLOBAL DE LAS CORRIENTES DE TU DIAGRAMA (D-bloques.pdf)
# ==============================================================================
def resolver_balance_planta(caudal_anual_hueso_seco_t: float = 45000.0, horas_operacion_anual: float = 8000.0):
    """
    Calcula los caudales másicos (kg/h y t/año) de las corrientes principales de tu PFD
    combinando los coeficientes experimentales de Romero-García et al. (2022) y 
    los módulos de recuperación de Jafari-Gohargan et al. (2026).
    """
    factor_escala_t = caudal_anual_hueso_seco_t / 1.0  # Base 1 t (1.000 kg) de Romero-García
    
    # Balance en t/año para las corrientes numeradas de tu D-bloques.pdf
    corrientes = {
        "Corriente 1 - Entrada Hueso de Aceituna (Base seca)": caudal_anual_hueso_seco_t,
        "Corriente 5 - Ácido Sulfúrico H2SO4 (R-01, 1% cat. B-1)": caudal_anual_hueso_seco_t * (137.0 / 15000.0),
        "Corriente 9 - Prehidrolizado rico en Xilosa (azúcares)": caudal_anual_hueso_seco_t * 0.2149,
        "Corriente 8 - Sólido pretratado ácido hacia Organosolv (R-02)": caudal_anual_hueso_seco_t * 0.6340,
        "Corriente 14 - Fracción sólida celulósica (WIS a R-03)": caudal_anual_hueso_seco_t * 0.4810,
        "Corriente 15 - Enzima Cellic CTec2 (kg/año)": caudal_anual_hueso_seco_t * (70.0 / 15000.0) * 1000.0,
        "Corriente 19 - Lignina Pura precipitada (Centrífuga C-01)": caudal_anual_hueso_seco_t * (2093.0 / 15000.0),
        "Corriente 33 - Etanol de Pentosas (Fermentador BF-01 E. coli)": caudal_anual_hueso_seco_t * 0.0756,
        "Corriente 36 - Etanol de Hexosas (Reactor PSSF BF-02 S. cerevisiae)": caudal_anual_hueso_seco_t * 0.0866,
        "Corriente 40 - Bioetanol Anhidro Total Producido (Suma 33+36)": caudal_anual_hueso_seco_t * 0.1622,
        "Corriente 35 - Furfural recuperado": caudal_anual_hueso_seco_t * 0.0068,
        "Corriente 22 - Amoniaco NH3 (Tanque neutralización)": caudal_anual_hueso_seco_t * (48.0 / 15000.0),
        "Corriente 20 - Sulfato de Amonio cristalizado (CR-01)": caudal_anual_hueso_seco_t * (137.0 / 15000.0) * (132.14 / 98.08),
        "Corriente 26 - Biofertilizante sólido (Deshidratador CF-01)": caudal_anual_hueso_seco_t * (650.0 / 15000.0),
        "Corriente 27/31 - Biogás / Biometano (m3/año hacia Cogeneración)": caudal_anual_hueso_seco_t * (3912361.0 / 15000.0),
        "Corriente 30 - CO2 purificado (Columna A-02 + Fermentadores)": caudal_anual_hueso_seco_t * (5904.0 / 15000.0)
    }
    
    df_balance = pd.DataFrame([
        {
            "Corriente (D-bloques.pdf)": k,
            "Flujo Anual (t/año o ud/año)": round(v, 2),
            "Flujo Horario (kg/h o ud/h)": round((v * 1000.0) / horas_operacion_anual, 2) if "kg/año" not in k and "m3/año" not in k else round(v / horas_operacion_anual, 2)
        }
        for k, v in corrientes.items()
    ])
    return df_balance


if __name__ == "__main__":
    print("=====================================================================")
    print("1. BALANCE DE MATERIA DE LA PLANTA (Base: 45.000 t/año Hueso Seco)")
    print("=====================================================================")
    df_bal = resolver_balance_planta(45000.0)
    print(df_bal.to_string(index=False))
    
    print("\n=====================================================================")
    print("2. PERFIL DINÁMICO DEL REACTOR PSSF (R-03 + BF-02) EN PYTHON")
    print("=====================================================================")
    df_pssf = simular_reactor_pssf(72.0)
    print(df_pssf.iloc[::25, :].round(2).to_string(index=False))
