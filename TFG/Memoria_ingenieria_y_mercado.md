# Estudio de Mercado, Localización e Ingeniería de Procesos: Biorrefinería de Hueso de Aceituna

## 1. Fuentes de Información para el Estudio de Mercado
- **SABI (Informa):** Geolocalización de proveedores de materia prima mediante códigos **CNAE 1043** (Fabricación de aceite de oliva) y **CNAE 1039** (Procesado de aceituna de mesa), y competidores químicos con **CNAE 2014**.
- **MAPA / AICA / SIAE (Junta de Andalucía):** Estadísticas de superficie (ESYRCE), producción provincial de aceite y aceituna de mesa.
- **AVEBIOM:** Índices de precios de biomasa térmica. Alrededor del 80 % del hueso de aceituna en España se comercializa para uso térmico y el 20 % se autoconsume en las propias almazaras.
- **Eurostat / CHELEM / Datastream:** Comercio exterior de bioetanol (TARIC `2207.10` / `2207.20`), residuos de extracción de aceite (`2306.90`) y series históricas de precios de *Ethanol T2 FOB Rotterdam* y electricidad industrial.

---

## 2. Criterios de Escala, Precios y Rentabilidad (Base NREL / Jafari-Gohargan et al., 2026)

### 2.1. Escenarios de Capacidad y Capacidad Mínima Viable ($C_{\text{min}}$)
El pretratamiento organosolv catalizado con un 1 % de ácido sulfúrico (Escenarios B) transfiere los oligómeros de azúcar a la fase líquida y fragmenta la estructura lignocelulósica:
- **Escenario B-1 (Solo hueso de aceituna):** 15.000 t/año (base seca). Presenta un Índice de Rentabilidad ($PI$) de **0,8** y una tasa de retorno neta ($NRR$) de **-19,98 %** (no rentable a esa escala pequeña), situándose su **capacidad mínima viable ($C_{\text{min}}$) en 30.000 t/año**. Duplicar la escala incrementa el índice de rendimiento de B-1 en 1,16.
- **Escenario B-2 (Hoja de olivo):** 40.000 t/año ($PI = 1,17$, *Payback* = 10,66 años, $C_{\text{min}} = 32.000\text{ t/año}$).
- **Escenario B-3 (Orujo):** 40.000 t/año ($PI = 1,11$, *Payback* = 12,84 años, $C_{\text{min}} = 40.000\text{ t/año}$).
- **Escenario B-4 (Madera de poda):** 65.000 t/año ($PI = 1,38$, *Payback* = 7,42 años, $C_{\text{min}} = 45.500\text{ t/año}$).
- **Escenario B-5 (Mezcla de todos los residuos del olivar):** 160.000 t/año ($PI = 1,78$, *Payback* = **4,23 años**, $NRR = 79,05\text{ %}$, $C_{\text{min}} = 88.000\text{ t/año}$). Mantiene un $PI > 1,5$ incluso en circunstancias pesimistas de subida simultánea de precios de materia prima y electricidad.

### 2.2. Ecuación de Beneficio Anual
$$\text{YP (\%)} = \left( \frac{\text{PSC} - \text{OPEX}}{\text{CAPEX}} \right) \times 100$$
Donde $\text{YP}$ es el beneficio anual porcentual, $\text{PSC}$ los ingresos por venta de productos y coproductos, $\text{OPEX}$ los costes operativos y $\text{CAPEX}$ la inversión total de capital.

---

## 3. Cierre del Balance de Materia Experimental (Estrategia 3 - Romero-García et al., 2022)
Base de cálculo: **1.000 kg de hueso de aceituna seco**:
- **Composición inicial (1.000 kg):** 209,1 kg glucano, 235,4 kg xilano, 11,5 kg arabinano, 12,7 kg galactano, 356,0 kg lignina, 63,0 kg extractivos, 59,0 kg grupos acetilo y 6,0 kg cenizas.
- **Etapa 1 - Pretratamiento Ácido ($128\text{ °C}$, $60\text{ min}$, $S/L = 33\text{ %}$, $10,5\text{ % }\text{H}_2\text{SO}_4/\text{OS}$):**
  - *Prehidrolizado líquido:* 4,0 kg glucosa, 186,9 kg xilosa, 13,0 kg arabinosa, 11,0 kg galactosa, 7,6 kg furfural y 45,3 kg ácido acético.
  - *Detoxificación (Carbón activo) + Evaporación:* Quedan 3,8 kg glucosa, 177,5 kg xilosa, 12,5 kg arabinosa, 10,5 kg galactosa, 0,8 kg furfural y 4,3 kg ácido acético.
  - *Fermentación de pentosas con E. coli ($96\text{ h}$):* Produce **75,6 kg de bioetanol** (concentración de $25\text{ g/L}$).
- **Etapa 2 - Segundo Pretratamiento (Explosión de Vapor $195\text{ °C}$, $5\text{ min}$ / Organosolv en PFD):**
  - *Sólido ácido de entrada (634 kg):* 201,8 kg glucano, 51,3 kg xilano, 2,7 kg galactano, 333,0 kg lignina, 13,0 kg grupos acetilo, 2,0 kg cenizas.
  - *Filtración y lavado (con el doble de agua respecto al peso de WIS):* Genera **481 kg de fracción sólida insoluble (WIS)** (170,9 kg glucano, 12,4 kg xilano, 279,0 kg lignina) y una corriente líquida (*SE liquid*) que tras detoxificarse aporta 16,5 kg glucosa, 26,7 kg xilosa, 1,4 kg galactosa y 0,3 kg ácido acético.
  - *PSSF con S. cerevisiae ($52\text{ h}$: $4\text{ h}$ presacarificación + $48\text{ h}$ SSF al $20\text{ % p/p}$ WIS):* Produce **86,6 kg de bioetanol** ($36\text{ g/L}$).
- **Producción Total Combinada:** **162,2 kg de bioetanol / 1.000 kg de hueso seco** ($29,9\text{ g/L}$, equivalente al 65 % del rendimiento teórico).

---

## 4. Modelado Matemático de Reactores Enzimáticos y Fermentadores

### 4.1. Modelo Difusional de Chrastil (Hidrólisis Enzimática `R-03`)
Describe la evolución temporal de la concentración de D-glucosa ($P$, en $\text{g/dm}^3$) liberada desde la matriz sólida por acción enzimática:
$$P = P_{\infty} \cdot \left[ 1 - \exp(-k_E \cdot C_{E0} \cdot t) \right]^n$$
- $C_{E0}$: Concentración inicial de enzima ($\approx 1,07 - 1,08\text{ g/dm}^3$).
- $k_E$: Constante específica de velocidad ($0,16 \times 10^{-3}$ a $0,41 \times 10^{-3}\text{ dm}^3/\text{g}\cdot\text{min}$).
- $n$: Parámetro de orden difusional estructural (varía de $0,22$ a baja severidad $\log R_0 = 2,73$, hasta $0,66 - 1,00$ a alta severidad $\log R_0 = 4,39$ cuando desaparece la limitación por transporte físico en el sólido).

### 4.2. Modelo Multivariable de Superficie de Respuesta (Abu Tayeh et al., 2026)
Predice la concentración de glucosa y etanol en función de la Temperatura ($T$, °C), concentración de ácido ($C_{\text{OA}}$, M) y carga enzimática ($E_{\text{load}}$, FPU/g):
$$\text{Glucosa (g/L)} = -0,8400 + 0,0415 \cdot T + 2,0126 \cdot C_{\text{OA}} + 0,4990 \cdot E_{\text{load}} + 0,1261 \cdot (T - 146,25) \cdot (C_{\text{OA}} - 0,4000)$$
$$\text{Etanol (g/L)} = -0,4700 + 0,0160 \cdot T + 0,9100 \cdot C_{\text{OA}} + 0,2480 \cdot E_{\text{load}} + 0,0670 \cdot (T - 146,25) \cdot (C_{\text{OA}} - 0,4000)$$

---

## 5. Especificaciones de Diseño de las 6 Columnas (Escenarios B: B-1 a B-5)

| Columna | Función en la Planta | Nº Etapas / Platos | Plato Alimentación | Temp. (°C) | Presión (bar) | Tipo de Condensador |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Columna 1** | *Scrubber* (Lavador de gases CO2/Etanol) | 7 | 1 | 37,00 | 1,00 | Sin condensador ($-$) |
| **Columna 2** | Destilación primaria (*Beer column*) | 22 | 2 | 60,00 | 0,97 | Parcial |
| **Columna 3** | Rectificación / Deshidratación azeotrópica | 30 | 15 | 80,33 - 80,44 | 0,90 | Parcial |
| **Columna 4** | Recuperación de Etanol (ciclo Organosolv) | 26 | 16 | 60,00 | 0,94 | Total |
| **Columna 5** | Absorbedor de Biogás (*Water Scrubbing*) | 11 | 11 | 20,00 | 10,00 | Sin condensador ($-$) |
| **Columna 6** | Desorbedor / *Stripper* de CO2 (con aire) | 6 | 1 | 20,00 | 1,00 | Sin condensador ($-$) |

---

## 6. Digestor Anaerobio (`DA-01`), Neutralización y Servicios Auxiliares
- **Neutralización de ácido sulfúrico:** El $1\text{ %}$ de $\text{H}_2\text{SO}_4$ usado en el pretratamiento se neutraliza tras la unidad de recuperación de etanol adicionando amoniaco ($\text{NH}_3$) para precipitar sulfato de amonio.
- **Digestión Anaerobia (UASB):** Reactor *Upflow Anaerobic Sludge Blanket* para el abatimiento de la Demanda Química de Oxígeno (COD) de las vinazas y aguas residuales, acoplado a *upgrading* por lavado con agua a alta presión (10 bar en Columna 5 y regeneración a 1 bar en Columna 6).
