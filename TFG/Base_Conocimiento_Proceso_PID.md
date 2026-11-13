# Base de Conocimiento de Ingeniería del Proceso, Normativa y P&ID (TFG)

Este documento centraliza todas las normas, bases de diseño cinético, balances de materia y especificaciones técnicas para la elaboración, verificación y trazado del Diagrama de Flujo (PFD) y Diagrama de Tuberías e Instrumentación (P&ID) en AutoCAD (`Fatima.dwg`).

---

## 1. Referencias Normativas Obligatorias (Disponibles en el Proyecto)

Las especificaciones de simbología, rotulación y tuberías se rigen estrictamente por las normas oficiales ubicadas en:
- `F:\universidad\3º\EACON\trabajo\010628NXEI100_ES.pdf` $\to$ **UNE-EN ISO 10628-2:2012** (*Diagramas para la industria química y petroquímica. Parte 2: Símbolos gráficos*).
- `F:\universidad\3º\EACON\trabajo\010628NXEI101_ES.pdf` $\to$ **UNE-EN ISO 10628-1:2015** (*Diagramas para la industria química y petroquímica. Parte 1: Especificación de los diagramas de proceso*).
- **ISO 7200 / UNE-EN ISO 7200:2004**: *Documentación técnica de productos. Campos de datos en bloques de títulos y cabeceras de documentos* (Cajetín reglamentario).
- **ANSI / ISA-5.1-2009**: *Instrumentation Symbols and Identification* (Lazos de instrumentación, transmisores, controladores y válvulas de control).
- **IEC 62424**: *Representation of process control engineering requests in P&I diagrams*.

---

## 2. Bases de Diseño de la Biorrefinería y Cinética Química

Datos cinéticos y de operación extraídos de:
- *Romero-García et al. (2022)*: "Ethanol production from olive stones using different process strategies", *Energy*, Elsevier (`F:\universidad\Mi_TFG\Articulos`).
- *Padilla-Rascón et al. (2022)*: "Olive stone biorefinery based on a two-step fractionation", *Renewable Energy* (`F:\universidad\Mi_TFG\Articulos`).
- *Tormos-Belda (2021)*: "Study of biological detoxification of lignocellulose hydrolysate" (`F:\universidad\Mi_TFG\Articulos`).

### 2.1. Reacción 1: Hidrólisis Ácida de Hemicelulosa (`R-01` / `R-101`)
* **Reactivos:** Hueso de aceituna seco triturado ($\approx 1\text{--}2\text{ mm}$), disolución de ácido sulfúrico diluido ($H_2SO_4$).
* **Condiciones:**
  - Temperatura: $T = 128^\circ\text{C}$ (Vapor vivo a $2{,}5\text{ bar}$ en camisa/serpín).
  - Dosis ácida: $10{,}5\text{ g } H_2SO_4 / 100\text{ g}$ hueso seco.
  - Relación Sólido/Líquido: $33\%\text{ p/v}$ ($1\text{ kg hueso} : 3\text{ kg disolución}$).
  - Tiempo de residencia: $t = 60\text{ min}$.
* **Productos generados:**
  - Prehidrolizado líquido: Rico en **Xilosa** ($\approx 70\text{ g/L}$), Glucosa ($\approx 8\text{ g/L}$), Ácido acético ($\approx 15\text{ g/L}$), Furfural ($\approx 1{,}8\text{ g/L}$) e HMF ($\approx 0{,}3\text{ g/L}$).
  - Sólido insoluble (**WIS**): Celulosa ($\approx 48\%$) y Lignina ($\approx 52\%$).

### 2.2. Acondicionamiento Térmico y Separación Sólido-Líquido (`E-04` y `F-01`)
* **Intercambiador `E-04`:** Enfriamiento del slurry desde $128^\circ\text{C}$ hasta $50^\circ\text{C}$ antes de la filtración para evitar descompresión flash violenta y proteger las telas filtrantes.
* **Filtro Prensa / Decanter `F-01`:** Separación de la fase sólida (WIS) de la líquida (Prehidrolizado ácido).
* **Agua de lavado:** Adición de agua en proporción $2:1$ en peso respecto a la torta sólida de WIS para lavar acidez e inhibidores solubles.

### 2.3. Detoxificación del Prehidrolizado Líquido (`A-01` / `D-101`)
* **Misión:** Eliminar furfural y ácido acético para evitar la muerte celular del microorganismo fermentador.
* **Tecnología:** Columnas de carbón activo (AC) o resinas de intercambio iónico (IER).
* **Rendimiento:** Eliminación $>90\%$ de furfural y $>95\%$ de ácido acético.

### 2.4. Neutralización y Cristalización de Subproducto (`TN-01` y `CR-01`)
* Reacción del remanente de ácido sulfúrico con amoníaco anhidro ($NH_3$):
  $$H_2SO_4 + 2\,NH_3 \longrightarrow (NH_4)_2SO_4 \quad (\text{Sulfato de amonio})$$
* Cristalización de sulfato de amonio como fertilizante de alto valor añadido.

### 2.5. Biorreactores de Fermentación
1. **Fermentación de Pentosas (Xilosa) en `BF-01`:**
   - Microorganismo: *Escherichia coli* SL100 (recombinante etanolgénica).
   - Condiciones: $T = 37^\circ\text{C}$, $\text{pH} = 6{,}5\text{--}7{,}0$, $t = 96\text{ h}$.
   - Rendimiento: $\approx 73\%$ del teórico ($\approx 75{,}5\text{ kg etanol / t hueso}$).
2. **Presacarificación y Fermentación Simultánea (PSSF) en `BF-02`:**
   - Enzima: *Cellic CTec2* ($40\text{ FPU/g sustrato}$ seco) + tampón citrato sódico $0{,}05\text{ M}$ ($\text{pH} = 4{,}8$).
   - Presacarificación: $T = 50^\circ\text{C}$, $t = 4\text{ h}$.
   - Fermentación SSF: Enfriamiento a $T = 35^\circ\text{C}$ mediante camisa/intercambiador; inóculo con $1\text{ g/L}$ de *Saccharomyces cerevisiae* "Ethanol Red", $t = 48\text{ h}$.
   - Rendimiento: $\approx 86{,}8\text{ kg etanol / t hueso}$.
* **Rendimiento Total Biorrefinería:** $\mathbf{162{,}3\text{ kg de Bioetanol / tonelada de hueso seco}}$.

### 2.6. Separación de Lignina Pre-Destilación (`CF-01` y `S-01`)
* La suspensión procedente de `BF-02` contiene lignina insoluble.
* Se instala la centrífuga deshidratadora `CF-01` **antes** de la columna de destilación `Z-01`.
* Los sólidos de lignina se deshidratan, se secan en `S-01` y se envían a la caldera de cogeneración `Q-01` para generar el vapor de planta.

### 2.7. Tren de Destilación y Deshidratación (`Z-01`, `E-05`, `A-03A/B`)
* **Columna de rectificación `Z-01`:** Alimentación a plato intermedio, condensador superior `E-01`, acumulador de reflujo `TKR-01` y bomba de reflujo `P-01`.
* **Hervidor de fondo (*Reboiler* `E-05`):** Retorno de vapor a la base de la columna.
* **Tamices moleculares de zeolita `A-03A/B`:** Rotura del azeótropo ($92\text{--}95\% \to 99{,}5\%\text{ p/p}$) para bioetanol carburante anhidro.
* **Línea de vinazas a Digestión Anaerobia `DA-01`:** Fondos de columna sin etanol hacia digestor anaerobio para producir biogás ($CH_4 + CO_2$) para la cogeneración `Q-01`.

---

## 3. Estado de Cajetines y Pestañas en AutoCAD (`Fatima.dwg`)

* **Espacio Papel (*Paper Space* / Layouts):** Contiene el cajetín normalizado ISO 7200 con campos de entidad (`UNIVERSIDAD DE GRANADA`), título de proyecto y autor (`CHRISTIAN PÉREZ HITA`). **Queda protegido sin modificaciones.**
* **Espacio Modelo (*Model Space*):** Contiene los bloques de equipos, tuberías y lazos de instrumentación donde se incorporan las mejoras topológicas.

