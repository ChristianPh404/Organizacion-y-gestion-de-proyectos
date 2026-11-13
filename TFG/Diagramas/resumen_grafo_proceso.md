# Planta de Bioetanol de Hueso de Aceituna: process knowledge graph summary

Built from `P&IDs` (1 sheets) by pid-to-kg 0.1.0 on 2026-11-11. The graph has 26 nodes and 30 edges; this summary covers equipment-level flow, instruments and control loops. Query `graph.duckdb` or `graph.json` for pipe-segment and valve detail.

| Equipment | Instruments | Valves & fittings | Pipe segments | Control loops | Off-page links |
|---|---|---|---|---|---|
| 7 | 6 | 0 | 9 | 2 | 0 |

## Sheets

| Page | Drawing | Title | Type |
|---|---|---|---|
| 1 | 04-PFD-201 | ÁREA DE REACCIÓN Y DETOXIFICACIÓN | pid |

## Process flow (equipment to equipment)

Each line reads *upstream → downstream*, with the pipe lines and in-line items between them. Pipes, valves and instruments are collapsed; use `kg_query.py path` for the full route.

- **R-101** (Reactor Hidrólisis Ácida CSTR) → **F-101** (Filtro Prensa Separador WIS): lines 03
- **F-101** (Filtro Prensa Separador WIS) → **D-101** (Columna Detoxificación IER/AC): lines 05
- **F-101** (Filtro Prensa Separador WIS) → **R-201** (Biorreactor PSSF Hexosas): lines 04
- **D-101** (Columna Detoxificación IER/AC) → **R-201** (Biorreactor PSSF Hexosas): lines 06

## Equipment

| Tag | Kind | Description | Fed by | Feeds | Status | Sheets |
|---|---|---|---|---|---|---|
| D-101 | column | Columna Detoxificación IER/AC | F-101 | R-201 |  | 04-PFD-201 |
| F-101 | filter | Filtro Prensa Separador WIS | R-101 | D-101, R-201 |  | 04-PFD-201 |
| P-101A | pump | Bomba Slurry Hidrolizado |  |  |  | 04-PFD-201 |
| P-102A | pump | Bomba Prehidrolizado Ácido |  |  |  | 04-PFD-201 |
| P-201A | pump | Bomba Caldo a Destilación |  |  |  | 04-PFD-201 |
| R-101 | reactor | Reactor Hidrólisis Ácida CSTR |  | F-101 |  | 04-PFD-201 |
| R-201 | reactor | Biorreactor PSSF Hexosas | D-101, F-101 |  |  | 04-PFD-201 |

## Instruments

Location is where the instrument senses the process. Pipe locations read `line (upstream item -> downstream item)`.

| Tag | Variable | Function | Mounted | Senses | Loop |
|---|---|---|---|---|---|
| TCV-101 | temperature | final_element | unknown |  | 101 |
| TCV-201 | temperature | final_element | unknown |  | 201 |
| TIC-101 | temperature | controller | unknown |  | 101 |
| TIC-201 | temperature | controller | unknown |  | 201 |
| TT-101 | temperature | transmitter | unknown |  | 101 |
| TT-201 | temperature | transmitter | unknown |  | 201 |

## Control loops

| Loop | Type | Sensor(s) | Controller(s) | Final element(s) | Description |
|---|---|---|---|---|---|
| 101 | control | TT-101 | TIC-101 | TCV-101 | Control loop 101 (temperature). Sensed by TT-101. Controlled by TIC-101 (unknown). Acts on TCV-101. |
| 201 | control | TT-201 | TIC-201 | TCV-201 | Control loop 201 (temperature). Sensed by TT-201. Controlled by TIC-201 (unknown). Acts on TCV-201. |

## Data quality

5 errors, 0 warnings and 0 informational items; see `qa_report.md`. Every node carries `confidence` and the sheet region it was read from (`provenance`). This graph was machine-extracted from drawings and must be verified by a qualified engineer before use in design, operations or safety work.
