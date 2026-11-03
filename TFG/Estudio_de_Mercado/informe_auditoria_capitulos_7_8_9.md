# Informe de Auditoría Técnica, Matemática y Documental: Capítulos 7, 8 y 9

**Proyecto:** Biorrefinería Oleícola por Vía Enzimática y Organosolv  
**Documento:** Memoria de Estudio de Mercado, Estacionalidad y Capacidad (`estudio_mercado2.tex`)  
**Autor:** Christian Pérez Hita (Grado en Ingeniería Química, UGR)  
**Fecha de auditoría:** Noviembre 2026  
**Auditor:** Revisor Académico Especializado en Ingeniería Química y Documentación Técnica  

---

## 1. Alcance y Metodología de la Auditoría

Se ha realizado una verificación exhaustiva, independiente y reproducible de todos los contenidos técnicos, modelos matemáticos, balances de materia/energía, caudales envolventes de diseño y citas bibliográficas presentes en los capítulos finales de la memoria de mercado:
- **Capítulo 7:** Estudio de Capacidad y Bases de Dimensionamiento Industrial.
- **Capítulo 8:** Esquema General de Procesos e Integración.
- **Capítulo 9:** Conclusiones del Estudio de Mercado.

Todos los cálculos numéricos han sido contrastados contra los modelos tecnoeconómicos primarios de la literatura científica (Jafari-Gohargan et al., 2026; Ronda et al., 2027; Padilla-Rascón et al., 2022; Romero-García et al., 2022) y contra los aforos estadísticos oficiales (AICA, MITECO, CORES, DOUE 2026 y CAP 2008), reproduciéndose íntegramente en el script independiente [`auditoria_calculos_capitulos_7_8_9.py`](file:///f:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/auditoria_calculos_capitulos_7_8_9.py).

---

## 2. Auditoría Técnica y Matemática de los Cálculos

### 2.1. Capítulo 7: Selección y Balances del Escenario Multibiomasa $\text{B-5}^*$

#### A. Definición de la Capacidad Nominal y Agregación de Corrientes (Tabla 7.1)
- **Base de partida:** Modelos B-1 (hueso, $15\,000\text{ t b.s./año}$), B-2 (hoja, $40\,000\text{ t b.s./año}$) y B-4 (madera de poda, $65\,000\text{ t b.s./año}$) de Jafari-Gohargan et al. (2026, Tablas 8 y 13), excluyendo el orujo agotado B-3 ($40\,000\text{ t b.s./año}$).
- **Comprobación de balances de producción agregada anual:**
  $$\text{Biomasa procesada} = 15\,000 + 40\,000 + 65\,000 = 120\,000\text{ t b.s./año} \quad \mathbf{[CORRECTO]}$$
  $$\text{Bioetanol 2G} = 2\,028 + 4\,166 + 9\,478 = 15\,672\text{ t/año} \quad \mathbf{[CORRECTO]}$$
  $$\text{Lignina técnica pura} = 2\,093 + 2\,489 + 5\,265 = 9\,847\text{ t/año} \quad \mathbf{[CORRECTO]}$$
  $$\text{Fracción rica en lignina} = 9\,503 + 20\,843 + 57\,401 = 87\,747\text{ t/año} \quad \mathbf{[CORRECTO]}$$
  $$\text{Dióxido de carbono biogénico} = 5\,904 + 20\,459 + 24\,850 = 51\,213\text{ t/año} \quad \mathbf{[CORRECTO]}$$
  $$\text{Biogás depurado} = 3\,912\,361 + 12\,119\,149 + 19\,118\,558 = 35\,150\,068\text{ m}^3\text{/año} \quad \mathbf{[CORRECTO]}$$
  $$\text{Biofertilizante sólido} = 650 + 1\,700 + 2\,823 = 5\,173\text{ t/año} \quad \mathbf{[CORRECTO]}$$
- **Estado:** **CORRECTO**. La suma ponderada coincide exactamente con los valores de simulación en Aspen Plus reportados por los autores en la Tabla 8 del artículo original.

#### B. Superación de la Capacidad Mínima Económica ($C_{\text{mín}}$)
- **Base de partida:** Jafari-Gohargan et al. (2026, Tabla 13) definen el umbral de viabilidad económica ($\text{PI} = 1.0$) de la biorrefinería multibiomasa integrada en $C_{\text{mín, B-5}} = 88\,000\text{ t/año}$.
- **Cálculo de holgura:**
  $$\Delta C = \frac{120\,000 - 88\,000}{88\,000} \times 100 = \frac{32\,000}{88\,000} \times 100 = +36{,}3636\,\% \approx \mathbf{+36{,}36\,\%}$$
- **Estado:** **CORRECTO**. Proporciona un margen holgado frente a escenarios de caída de precios o sobrecostes logísticos.

#### C. Cuotas de Absorción sobre el Recurso Regional Disponible
- **Base de partida:** Disponibilidad neta en el eje Córdoba--Granada--Jaén calculada en el Capítulo 2 (Tabla 2.6): Hueso ($339\,602\text{ t b.s.}$), Hoja ($311\,038\text{ t b.s.}$), Madera mecanizable ($583\,411\text{ t b.s.}$), Total ($1\,234\,051\text{ t b.s./año}$).
- **Cálculos:**
  * Cuota de hueso: $15\,000 / 339\,602 = 4{,}4169\,\% \approx \mathbf{4{,}42\,\%}$ **[CORRECTO]**
  * Cuota de hoja: $40\,000 / 311\,038 = 12{,}8601\,\% \approx \mathbf{12{,}86\,\%}$ **[CORRECTO]**
  * Cuota de madera: $65\,000 / 583\,411 = 11{,}1413\,\% \approx \mathbf{11{,}14\,\%}$ **[CORRECTO]**
  * Cuota global: $120\,000 / 1\,234\,051 = 9{,}7240\,\% \approx \mathbf{9{,}72\,\%}$ **[CORRECTO]**
- **Estado:** **CORRECTO**.

#### D. Facturación Anual Bruta Estimada (Tabla 7.2)
- **Base de precios:** Vector internacional de la Tabla 5 de Jafari-Gohargan et al. (2026): Bioetanol ($1\,200\text{ \$/t}$), Lignina pura ($630\text{ \$/t}$), Rich-Lignin ($42\text{ \$/t}$), $\text{CO}_2$ ($38\text{ \$/t}$), Biofertilizante ($4{,}5\text{ \$/t}$), Biogás (autoconsumo térmico/cogeneración).
- **Cálculos:**
  $$V_{\text{etoh}} = 15\,672 \times 1\,200 = \$18\,806\,400{,}00$$
  $$V_{\text{lig}} = 9\,847 \times 630 = \$6\,203\,610{,}00$$
  $$V_{\text{rich}} = 87\,747 \times 42 = \$3\,685\,374{,}00$$
  $$V_{\text{co2}} = 51\,213 \times 38 = \$1\,946\,094{,}00$$
  $$V_{\text{fert}} = 5\,173 \times 4{,}5 = \$23\,278{,}50$$
  $$V_{\text{total, USD}} = \$30\,664\,756{,}50/\text{año} \quad \mathbf{[CORRECTO]}$$
  $$V_{\text{total, EUR}} = \frac{\$30\,664\,756{,}50}{1{,}09\text{ \$/€}} = 28\,132\,804{,}13\text{ €/año} \approx \mathbf{28{,}13\text{ M€/año}} \quad \mathbf{[CORRECTO]}$$
- **Estado:** **CORRECTO**.

#### E. Consumo y Coste Anual de Insumos Químicos y Enzimáticos (Cajetín pág. 27)
- **Base de partida:** Jafari-Gohargan et al. (2026, Tablas 5 y 8) para B-1, B-2 y B-4:
  * Enzima Cellic CTec2: $70 + 155 + 343 = 568{,}0\text{ kg/año} \times 1\,000\text{ \$/kg} = \$568\,000{,}00/\text{año}$ **[CORRECTO]**
  * Ácido sulfúrico $\mathrm{H_2SO_4}$: $137 + 368 + 602 = 1\,107{,}0\text{ t/año} \times 262\text{ \$/t} = \$290\,034{,}00/\text{año}$ **[CORRECTO]**
  * Amoniaco $\mathrm{NH_3}$: $48 + 132 + 212 = 392{,}0\text{ t/año} \times 300\text{ \$/t} = \$117\,600{,}00/\text{año}$ **[CORRECTO]**
  * Coste total reactivos: $\$568\,000 + \$290\,034 + \$117\,600 = \$975\,634{,}00/\text{año}$ ($\approx \mathbf{0{,}895\text{ M€/año}} \approx \mathbf{0{,}90\text{ M€/año}}$) **[CORRECTO]**
- **Estado:** **CORRECTO**.

#### F. Caudales Horarios Estacionales y Envolvente de Diseño $Q_{\text{máx}}$ (Tabla 7.3)
- **Régimen de operación:** Caudal seco nominal continuo de $15\,000\text{ kg b.s./h}$ ($15{,}00\text{ t b.s./h}$) durante $8\,000\text{ h/año}$:
  * Campaña Hueso: $15\,000 / 15 = 1\,000{,}0\text{ h}$
  * Campaña Hoja: $40\,000 / 15 = 2\,666{,}67\text{ h} \approx 2\,666{,}7\text{ h}$
  * Campaña Madera: $65\,000 / 15 = 4\,333{,}33\text{ h} \approx 4\,333{,}3\text{ h}$
  * Total horas operativas: $1\,000{,}0 + 2\,666{,}7 + 4\,333{,}3 = 8\,000{,}0\text{ h/año}$ **[CORRECTO]**
- **Auditoría de caudales envolventes $Q_{\text{máx}}$:**
  1. *Biomasa húmeda recibida:*
     - Hueso (8 % hum): $15\,000 / 0{,}92 = 16\,304{,}35\text{ kg/h}$
     - Hoja (40 % hum): $15\,000 / 0{,}60 = 25\,000{,}00\text{ kg/h}$
     - Madera (20 % hum): $15\,000 / 0{,}80 = 18\,750{,}00\text{ kg/h}$
     - Envolvente: $Q_{\text{máx}} = \mathbf{25\,000\text{ kg/h}}$ (Campaña de hoja) **[CORRECTO]**
  2. *Agua evaporada en secador rotatorio (hasta 8 % hum. final):*
     - Hueso: $0\text{ kg/h}$ (humedad de recepción ya es del 8 %)
     - Hoja: entra con $10\,000\text{ kg/h}$ de agua; el producto seco al 8 % contiene $1\,304{,}35\text{ kg/h}$ de agua residual. Agua evaporada = $10\,000 - 1\,304{,}35 = 8\,695{,}65\text{ kg/h} \approx \mathbf{8\,696\text{ kg/h}}$ **[CORRECTO]**
     - Madera: entra con $3\,750\text{ kg/h}$ de agua. Agua evaporada = $3\,750 - 1\,304{,}35 = 2\,445{,}65\text{ kg/h} \approx \mathbf{2\,446\text{ kg/h}}$ **[CORRECTO]**
     - Envolvente: $Q_{\text{máx}} = \mathbf{8\,696\text{ kg/h}}$ (Campaña de hoja) **[CORRECTO]**
  3. *Bioetanol 2G anhidro:*
     - Hueso: $2\,028\text{ t} / 1\,000\text{ h} = 2\,028{,}0\text{ kg/h}$
     - Hoja: $4\,166\text{ t} / 2\,666{,}67\text{ h} = 1\,562{,}25\text{ kg/h} \approx 1\,562\text{ kg/h}$
     - Madera: $9\,478\text{ t} / 4\,333{,}33\text{ h} = 2\,187{,}23\text{ kg/h} \approx 2\,187\text{ kg/h}$
     - Envolvente: $Q_{\text{máx}} = \mathbf{2\,187\text{ kg/h}}$ (Campaña de madera) **[CORRECTO]**
     - Caudal volumétrico a 20 °C ($\rho = 0{,}7893\text{ kg/L}$): $2\,187{,}23 / 0{,}7893 = 2\,771{,}1\text{ L/h} \approx \mathbf{2\,771\text{ L/h}}$ **[CORRECTO]**
  4. *Lignina técnica pura:*
     - Hueso: $2\,093\text{ t} / 1\,000\text{ h} = 2\,093{,}0\text{ kg/h}$
     - Hoja: $2\,489\text{ t} / 2\,666{,}67\text{ h} = 933{,}38\text{ kg/h} \approx 933\text{ kg/h}$
     - Madera: $5\,265\text{ t} / 4\,333{,}33\text{ h} = 1\,215{,}0\text{ kg/h}$
     - Envolvente: $Q_{\text{máx}} = \mathbf{2\,093\text{ kg/h}}$ (Campaña de hueso) **[CORRECTO]**
  5. *Fracción rica en lignina:*
     - Hueso: $9\,503\text{ kg/h}$; Hoja: $7\,816\text{ kg/h}$; Madera: $13\,246\text{ kg/h}$. Envolvente: $Q_{\text{máx}} = \mathbf{13\,246\text{ kg/h}}$ **[CORRECTO]**
  6. *$\text{CO}_2$ biogénico:*
     - Hueso: $5\,904\text{ kg/h}$; Hoja: $7\,672\text{ kg/h}$; Madera: $5\,735\text{ kg/h}$. Envolvente: $Q_{\text{máx}} = \mathbf{7\,672\text{ kg/h}}$ **[CORRECTO]**
  7. *Biogás depurado:*
     - Hueso: $3\,912{,}4\text{ m}^3\text{/h}$; Hoja: $4\,544{,}7\text{ m}^3\text{/h}$; Madera: $4\,412{,}0\text{ m}^3\text{/h}$. Envolvente: $Q_{\text{máx}} = \mathbf{4\,544{,}7\text{ m}^3\text{/h}}$ **[CORRECTO]**

---

### 2.2. Capítulo 8: Esquema de Procesos y Capacidad de Almacenamiento

- **Inventarios máximos estacionales (Sección 8.2):**
  * Silos de hueso de aceituna: $I_{\text{máx}} = 12\,900\text{ t b.s.}$ (cubre el acopio estacional otoñal y el enlace veraniego).
  * Nave de hoja fresca: $I_{\text{máx}} = 3\,400\text{ t b.s.}$ (almacenamiento de pulmón técnico para 2 semanas de molturación máxima).
  * Parque de astilla de poda: $I_{\text{máx}} = 34\,000\text{ t b.s.}$ (acopio escalonado de primavera para procesado estival continuo).
- **Asignación de equipos críticos a caudales punta ($Q_{\text{máx}}$):**
  * Cinta de recepción `CT-01`: dimensionada a $25{,}0\text{ t/h}$ (marcada por hoja húmeda).
  * Secador rotatorio: dimensionado a $8\,696\text{ kg/h}$ de vapor evaporado (marcado por hoja húmeda).
  * Filtro prensa de lignina `F-02`: dimensionado a $2\,093\text{ kg/h}$ (marcado por hueso).
  * Fermentadores PSSF y columnas `Z-01`: dimensionados a $2\,187\text{ kg/h}$ ($2\,771\text{ L/h}$) de bioetanol (marcados por madera de poda).
  * Digestor anaerobio `DA-01` y antorcha/upgrading: dimensionado a $4\,544{,}7\text{ m}^3\text{/h}$ de biogás (marcado por hoja).
- **Estado:** **CORRECTO**. La correspondencia entre el diagrama de bloques (Figura 8.1), la lista de equipos y los caudales horarios es total.

---

### 2.3. Capítulo 9: Conclusiones Macroeconómicas y Validación de Precios

- **Cuota de absorción sobre el Consumo Nacional Aparente (CNA 2025):**
  $$\text{Cuota CNA} = \frac{15\,672\text{ t}}{225\,136\text{ t}} \times 100 = 6{,}9613\,\% \approx \mathbf{6{,}96\,\%} \quad \mathbf{[CORRECTO]}$$
- **Cuota sobre la demanda comunitaria europea (DOUE 2026):**
  $$\text{Cuota UE} = \frac{15\,672\text{ t}}{4\,987\,906\text{ t}} \times 100 = 0{,}3142\,\% \approx \mathbf{0{,}314\,\%} \quad \mathbf{[CORRECTO]}$$
- **Prima verde del bioetanol 2G sobre el etanol 1G convencional europeo:**
  * Precio convencional 1G proyectado por Massey-Black (2026): $991{,}66\text{ €/t}$.
  * Precio de diseño 2G: $1\,200\text{ \$/t} / 1{,}09\text{ \$/€} = 1\,100{,}92\text{ €/t}$.
  * Prima verde relativa:
    $$\Delta P = \frac{1\,100{,}92 - 991{,}66}{991{,}66} \times 100 = \frac{109{,}26}{991{,}66} \times 100 = +11{,}018\,\% \approx \mathbf{+11{,}0\,\%}$$
  * Prima verde absoluta: $109{,}26\text{ €/t} \approx \mathbf{109\text{ €/t}}$.
- **Estado:** **CORRECTO**. Representa una prima verde moderada y conservadora justificada plenamente por los subobjetivos de bioalcoholes avanzados del Real Decreto 611/2026.

---

## 3. Auditoría Documental y de Citas Bibliográficas (Capítulos 7, 8 y 9)

| Cita en Texto | Clave BibTeX | Documento Local Contrastado | Apartado / Tabla Fuente | Concordancia Técnica | Veredicto |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Jafari-Gohargan et al. (2026)** | `Jafari-Gohargan2026` | `Articulos/Jafari-Gohargan (2026)...pdf` | Tablas 5, 6, 8, 12, 13 | Balances de masa, flujos B-1 a B-5, reactivos y precios de mercado. | **CORRECTO** |
| **Ronda et al. (2027)** | `Ronda2027` | `Articulos/Ronda (2027)...pdf` | Pág. 5, Sec. 2.5, Tabla 3, Fig. 11 | Coste transporte pesado $1{,}3079\text{ €/km}$ y radio óptimo $< 65\text{ km}$. | **CORRECTO** |
| **Padilla-Rascón et al. (2022)** | `Padilla-Rascon2022` | `Articulos/Padilla-Rascon (2022)...pdf` | Tabla 1, Fig. 1 | Eficacia de deslignificación organosolv ($52{,}5\,\%$) y PSSF. | **CORRECTO** |
| **Romero-García et al. (2022)** | `RomeroGarcia2022` | `Articulos/Romero-Garcia (2022)...pdf` | Sec. 2.1, Fig. 2 | Hidrólisis y fermentación de azúcares hemicelulósicos. | **CORRECTO** |
| **APPA (2026)** | `APPA2026` | `Datos_y_Fuentes_Oficiales/Informe-Potencial-Biometano-2026.pdf` | Sección 4.2.3 | Complejo orujero y plantas de cogeneración de orujillo en Andalucía. | **CORRECTO** |
| **AAE (2026)** | `AAE2026` | `Datos_y_Fuentes_Oficiales/Informe_ANDALUZ_MIEA.pdf` | Sección 7, Nota 4 | Censo 11 plantas biocarburantes en Andalucía, 0 de bioetanol, importación ETBE. | **CORRECTO** |
| **MITECO (2026)** | `MITECO2026` | `Datos_y_Fuentes_Oficiales/202610_ESTADISTICAS-BIOS...xlsx` | Hoja `Sost_Tipo MP_Bioet`, Balance bioetanol | $99{,}19\,\%$ bioetanol 1G en España y CNA 2025 ($225\,136\text{ t}$). | **CORRECTO** |
| **MAPA (2025)** | `MAPA2025` | `Datos_y_Fuentes_Oficiales/OLIVAR CAMPAÑA 2025.xlsx` | Hoja `TABLA PROVINCIAL CULTIVOS` | Superficie productiva olivar en Córdoba, Granada y Jaén ($1\,169\,577\text{ ha}$). | **CORRECTO** |
| **AICA (2026)** | `AICA2026` | `Datos_y_Fuentes_Oficiales/INFORME MENSUAL...Septiembre 2026...xlsx` | Cuadro 1, Datos provinciales | $3\,885\,605{,}3\text{ t}$ aceituna molturada en 620 almazaras del triángulo. | **CORRECTO** |
| **DOUE (2026)** | `DOUE2026` | `Datos_y_Fuentes_Oficiales/L00001-00004.pdf` | Considerandos 5, 8, 9, 10, Cuadro 1 | Consumo UE $4{,}99\text{ Mt}$, precios de importación y venta europea. | **CORRECTO** |

- **Detección de alucinaciones o citas espurias en Capítulos 7, 8 y 9:** **NINGUNA**. Todas las referencias corresponden a archivos locales físicos y las cifras citadas concuerdan exactamente con las tablas y páginas indicadas.

---

## 4. Observaciones Técnicas y Recomendaciones

1. **Robustez del diseño estacional:** La variación estacional de las biomasas queda absorbida por la sobredimensión selectiva de las unidades críticas ($Q_{\text{máx}}$) sin encarecer el reactor principal de organosolv (`R-02`), el cual opera a régimen nominal estacionario ($15{,}00\text{ t b.s./h}$) durante las $8\,000\text{ h/año}$.
2. **Coherencia económica del biofertilizante:** El coproducto biofertilizante agrícola genera ingresos secundarios modestos ($\$23\,278{,}50/\text{año}$), lo que resulta coherente con su naturaleza de lodo digerido estabilizado, evitando sobreestimaciones optimistas de ingresos.
3. **Consistencia dimensional:** Se ha verificado que todas las densidades de referencia ($0{,}7893\text{ t/m}^3$ a 20 °C y $0{,}7937\text{ t/m}^3$ a 15 °C) están explícitamente contextualizadas en las conversiones entre masa y volumen.

---

## 5. Veredicto Final de la Auditoría Técnica

- **Precisión matemática:** **100 %**. Cero discrepancias numéricas en balances y caudales.
- **Rigor documental:** **100 %**. Todas las citas están respaldadas por fuentes primarias verificadas.
- **Estado global:** **APROBADO SIN RESERVAS TÉCNICAS**.

