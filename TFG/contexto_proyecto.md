# Proyecto: Biorrefinería de Hueso de Aceituna y Poda de Olivo (UGR)

## 1. Datos Base de Materia Prima y Mercado
- **Producción en España:** ~600.000 t/año de hueso de aceituna (aprox. 10% del peso de la aceituna).
- **Competencia actual:** ~80% del hueso se comercializa para uso térmico y ~20% se autoconsume en almazaras.
- **Composición del hueso (base seca):** 20,9% celulosa, 26,0% hemicelulosa (>80% xilosa), 35,6% lignina, 6,3% extractivos, 0,6% cenizas, 5,9% grupos acetilo; humedad 8%, tamaño 1-3,35 mm.
- **Escenarios de capacidad (Base seca - Jafari-Gohargan et al.):**
  - **B-1 (Solo hueso):** 15.000 t/año -> Produce 2.028 t/año etanol, 2.093 t/año lignina, 3.912.361 m3/año biogás, 5.904 t/año CO2, 9.503 t/año fracción rica en lignina, 650 t/año fertilizante.
  - **B-2 (Hoja de olivo):** 40.000 t/año -> Produce 4.166 t/año etanol.
  - **B-3 (Orujo):** 40.000 t/año -> Produce 5.696 t/año etanol.
  - **B-4 (Madera de poda):** 65.000 t/año -> Produce 9.478 t/año etanol.
  - **B-5 (Mezcla total residuos olivar):** 160.000 t/año -> Produce 23.444 t/año etanol, 14.197 t/año lignina, 22.460.957 m3/año biogás, 66.134 t/año CO2, 117.501 t/año fracción rica en lignina, 6.871 t/año fertilizante.

## 2. Precios de Referencia ($/unidad)
- **Materias primas y consumibles:** Residuo de olivar: 17 $/t | Enzima: 1.000 $/kg | Ácido sulfúrico: 262 $/t | Amoniaco: 300 $/t.
- **Productos y Coproductos:** Etanol: 1.200 $/t | Biogás: 1.210 $/unidad | Lignina pura: 630 $/t | CO2: 38 $/t | Fracción rica en lignina: 42 $/t | Fertilizante: 4,5 $/t.
- **Servicios (Utilities):** Vapor HP (40 bar, 250 °C): 13,07 $/t | Vapor LP (3 bar, 135 °C): 7 $/t | Agua: 0,06 $/t | Electricidad: 0,078 $/kWh.

## 3. Arquitectura del Proceso (Diagramas D-bloques y D-flujo)
- **Acondicionamiento:** Cinta (CT-01) -> Secador (S-01) -> Cinta (CT-02) -> Triturador (T-01) -> Tamiz rotativo (TR-01) con recirculación (corriente 6).
- **Etapa 1 (Hidrólisis Ácida + Línea Pentosas):** Reactor pretratamiento ácido (R-01) con H2SO4 (corriente 5) -> Filtración (F-01) -> Líquido (corriente 9) a Adsorción (A-01) con carbón activo (corriente 45) -> Fermentador pentosas (BF-01) con E. coli (corriente 32). Carbón + furfural (corriente 44) a Caldera de Cogeneración.
- **Etapa 2 (Organosolv + Línea Hexosas):** Sólidos (corriente 8) a Reactor Organosolv (R-02) con etanol/agua (corriente 43) -> Separador Flash (V-101) -> Filtración (F-02) -> Fracción sólida (corriente 14) a Presacarificación enzimática (R-03) con Cellic CTec2 (corriente 15) -> SSF (BF-02) con citrato de sodio (corriente 37) y S. cerevisiae (corriente 38).
- **Destilación y Recirculación:** Columna Destilación (Z-01) -> Separa Furfural (corriente 35), Vinazas (corriente 39) y Etanol (corriente 34) -> Divisor (D-01) divide en Etanol final (corriente 40) y Etanol recirculado (corriente 41) hacia Mezclador (M-01) con Agua (corriente 42).
- **Valorización de Efluentes y Lignina:**
  - Licor con lignina (corriente 12) -> Tanque precipitación con agua (corriente 16) -> Centrifugación (C-01) -> Lignina sólida (corriente 19).
  - Vinazas (corriente 39) -> Tanque neutralización con amoniaco (corriente 22) -> Cristalizador (CR-01) -> Sulfato de amonio (corriente 20).
  - Efluentes líquidos (corrientes 21 y 24) -> Digestor Anaerobio (DA-01) -> Lodos a Deshidratador centrífugo (CF-01) para Biofertilizante (corriente 26) y Agua (corriente 44); Biogás (corriente 27) a Absorción/Desorción (A-02) con agua (28) y aire (29) -> Sale CO2 (corriente 30) y Biometano (corriente 31) a Caldera de Cogeneración.


## 4. Criterio Metodológico de Bases Químicas y Transición de Diseño
- **Frontera de transición de cálculo:**
  - **Recepción, almacenamiento y acondicionamiento:** Se utiliza la **caracterización analítica integral bruta** (Morán-Alarcón et al., 2026; Romero-García et al., 2022). Cuantifica la biomasa tal como entra por la báscula de fábrica (humedades reales de campo: 8% hueso, 35-40% hoja, 20% madera; cenizas minerales y lignina Klason bruta con extractivos). Sirve para dimensionar la evaporación de agua en el secador, silos, tolvas y molienda.
  - **Reactores, hidrólisis, fermentación y destilación:** A la salida del acondicionamiento, la corriente de sólidos secos que ingresa al reactor se desglosa según la **base estructural reactiva normalizada de simulación en Aspen Plus** (Jafari-Gohargan et al., 2026: glucano, galactano, xilano y lignina estructural pura sobre el 100% polimérico reactivo). Esta base gobierna las estequiometrías químicas, cinéticas de reacción, consumos de catalizador/enzimas y rendimientos específicos de bioetanol 2G, lignina técnica pura y biogás.
- **Evitación de duplicidades:** No se sobredimensiona la planta mezclando bases contradictorias; el factor de seguridad de diseño estándar (10-15% sobre Q_máx) se aplica sobre los caudales envolventes resultantes de la simulación.
