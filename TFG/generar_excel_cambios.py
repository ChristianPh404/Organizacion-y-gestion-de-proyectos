import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_engineering_excel():
    wb = openpyxl.Workbook()
    # Eliminar hoja por defecto
    default_sheet = wb.active
    
    # -------------------------------------------------------------
    # ESTILOS GENERALES
    # -------------------------------------------------------------
    font_title = Font(name="Calibri", size=15, bold=True, color="FFFFFF")
    font_subtitle = Font(name="Calibri", size=11, italic=True, color="FFFFFF")
    font_sec = Font(name="Calibri", size=12, bold=True, color="1F497D")
    font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    font_data = Font(name="Calibri", size=10)
    font_bold = Font(name="Calibri", size=10, bold=True)
    font_note = Font(name="Calibri", size=9, italic=True, color="595959")
    
    fill_navy = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    fill_blue_head = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
    fill_steel = PatternFill(start_color="5B9BD5", end_color="5B9BD5", fill_type="solid")
    fill_light_gray = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    fill_accent_green = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
    fill_accent_orange = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")

    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )
    header_border = Border(
        left=Side(style='thin', color='FFFFFF'),
        right=Side(style='thin', color='FFFFFF'),
        top=Side(style='medium', color='1F497D'),
        bottom=Side(style='medium', color='1F497D')
    )

    # =============================================================
    # HOJA 1: RESUMEN DE CAMBIOS CAD (LISTA DE ACCIONES)
    # =============================================================
    ws1 = wb.create_sheet(title="Acciones_AutoCAD_Fatima")
    ws1.views.sheetView[0].showGridLines = True
    
    # Banner
    ws1.merge_cells("A1:F1")
    ws1["A1"] = "PLAN DE ACCIONES Y CAMBIOS TÉCNICOS PARA ACTUALIZAR FATIMA.DWG"
    ws1["A1"].font = font_title
    ws1["A1"].fill = fill_navy
    ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[1].height = 35

    ws1.merge_cells("A2:F2")
    ws1["A2"] = "Biorrefinería de Hueso de Aceituna (Bioetanol y Subproductos) - Revisión según Normativa ISO 10628 / ISA-5.1"
    ws1["A2"].font = font_subtitle
    ws1["A2"].fill = fill_steel
    ws1["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[2].height = 22

    # Encabezados
    headers1 = [
        "ID Acción",
        "Zona / Pestaña del Plano",
        "Equipo Involucrado",
        "Modificación Concreta a Realizar en AutoCAD",
        "Justificación Técnica y Termodinámica",
        "Prioridad de Implementación"
    ]
    
    ws1.append([]) # Fila 3 vacia
    ws1.append(headers1) # Fila 4
    ws1.row_dimensions[4].height = 28
    for col_idx in range(1, 7):
        cell = ws1.cell(row=4, column=col_idx)
        cell.font = font_header
        cell.fill = fill_blue_head
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = header_border

    # Datos
    acciones = [
        (
            "ACC-01",
            "Zona 1 (Pretratamiento)",
            "E-04 (Nuevo Enfriador)",
            "Insertar intercambiador E-04 en la línea de descarga del reactor de hidrólisis ácida R-01 antes de la entrada al filtro prensa F-01.",
            "La hidrólisis opera a 128 ºC y 2.5 bar. Si el slurry entra directamente al filtro F-01 a presión atmosférica se produce flasheo violento de vapor y rotura térmica de telas filtrantes. Se requiere enfriamiento a 50 ºC.",
            "CRÍTICA (Obligatoria)"
        ),
        (
            "ACC-02",
            "Zona 1 (Filtración)",
            "F-01 (Filtro Prensa)",
            "Añadir una línea de agua desmineralizada de lavado (proporción 2:1 en peso respecto a la torta de sólidos WIS).",
            "El sólido insoluble (celulosa + lignina) retiene ácido sulfúrico e inhibidores solubles en los poros. El lavado previo es indispensable para que las enzimas y levaduras no se inactiven en la etapa biológica.",
            "ALTA"
        ),
        (
            "ACC-03",
            "Zona 2 (Detoxificación)",
            "A-01 (Columnas Carbón/Resinas)",
            "Conectar la salida líquida de F-01 directamente a las columnas A-01 antes de realizar la neutralización de pH con amoníaco.",
            "El prehidrolizado contiene furfural (~1.8 g/L) y ácido acético (~15 g/L). La adsorción previa elimina >90% de furfural y >95% de acético. Neutralizar antes provocaría precipitación de sales colmatando el carbón.",
            "ALTA"
        ),
        (
            "ACC-04",
            "Zona 3 (Fermentación)",
            "BF-01 y BF-02",
            "Separar nítidamente las dos líneas de fermentación: línea líquida de xilosa a BF-01 (E. coli, 37 ºC, 96 h) y sólidos WIS a BF-02 (PSSF con S. cerevisiae, 52 h).",
            "E. coli y S. cerevisiae operan con óptimos cinéticos, temperaturas y tiempos de residencia totalmente incompatibles entre sí (96 h frente a 48 h). Deben ser biorreactores independientes.",
            "CRÍTICA (Obligatoria)"
        ),
        (
            "ACC-05",
            "Zona 3 (Biorreactor PSSF)",
            "BF-02 (Intercambiador / Camisa)",
            "Añadir lazo de refrigeración o intercambiador de salto térmico (50 ºC -> 35 ºC) entre la fase de presacarificación y la de fermentación simultánea.",
            "La enzima Cellic CTec2 tiene máxima actividad a 50 ºC, pero la levadura S. cerevisiae Ethanol Red muere si se inocula a 50 ºC. La fermentación debe transcurrir estrictamente a 35 ºC.",
            "CRÍTICA"
        ),
        (
            "ACC-06",
            "Zona 4 (Pre-Destilación)",
            "CF-01 (Decanter Lignina)",
            "Mover la centrífuga / decanter CF-01 para que procese el caldo a la salida del fermentador BF-02, ANTES de que el vino entre a la columna Z-01.",
            "En tu esquema anterior CF-01 aparecía aislado. Si los sólidos insolubles de lignina entran a la columna de destilación atascan los platos y el hervidor. Deben extraerse como torta sólida.",
            "CRÍTICA (Obligatoria)"
        ),
        (
            "ACC-07",
            "Zona 5 (Tren de Destilación)",
            "E-05 (Reboiler / Hervidor)",
            "Dibujar el hervidor de fondos E-05 en la base de la columna Z-01 con línea de retorno de vapor a los fondos.",
            "Toda columna de rectificación necesita suministro continuo de calor en fondos mediante vapor indirecto para generar el vapor ascendente que despoja el bioetanol.",
            "ALTA"
        ),
        (
            "ACC-08",
            "Zona 5 (Deshidratación)",
            "A-03A/B (Tamices Moleculares)",
            "Añadir dos columnas de tamices moleculares de zeolita (tecnología PSA) a la salida del destilado del tanque de reflujo TKR-01.",
            "La destilación simple solo puede concentrar bioetanol hasta el azeótropo (~92.4 - 95% p/p). Para bioetanol carburante la norma EN 15376 exige >99.5% p/p anhidro.",
            "ALTA (Diseño Final)"
        ),
        (
            "ACC-09",
            "Zona 6 (Servicios y Subproductos)",
            "Q-01 y DA-01",
            "Trazar las líneas de valorización: torta de lignina seca desde secador S-01 a caldera Q-01, y vinazas líquidas de fondos de Z-01 al digestor anaerobio DA-01 (biogás).",
            "Cierra el ciclo de la biorrefinería: la planta aprovecha la lignina y el biogás para autoproducir todo el vapor de proceso y electricidad requeridos.",
            "MEDIA"
        )
    ]

    for row_data in acciones:
        ws1.append(row_data)
        r = ws1.max_row
        ws1.row_dimensions[r].height = 42
        for c in range(1, 7):
            cell = ws1.cell(row=r, column=c)
            cell.font = font_data
            cell.border = thin_border
            if c in [1, 2]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif c == 6:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                if "CRÍTICA" in cell.value:
                    cell.fill = fill_accent_orange
                    cell.font = font_bold
                else:
                    cell.fill = fill_accent_green
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # =============================================================
    # HOJA 2: EQUIPOS AUXILIARES Y NUEVAS CONEXIONES DETALLADAS
    # =============================================================
    ws2 = wb.create_sheet(title="Equipos_Auxiliares_Detalle")
    ws2.views.sheetView[0].showGridLines = True

    ws2.merge_cells("A1:G1")
    ws2["A1"] = "ESPECIFICACIÓN DE NUEVOS EQUIPOS AUXILIARES Y CONEXIONES INCORPORADAS"
    ws2["A1"].font = font_title
    ws2["A1"].fill = fill_navy
    ws2["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[1].height = 35

    ws2.merge_cells("A2:G2")
    ws2["A2"] = "Parámetros de Operación, Lazos de Control y Balances Clave de las Unidades de Proceso"
    ws2["A2"].font = font_subtitle
    ws2["A2"].fill = fill_steel
    ws2["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[2].height = 22

    headers2 = [
        "Tag Equipo",
        "Tipo de Equipo",
        "Corriente Entrada (Origen)",
        "Corriente Salida (Destino)",
        "Condiciones de Operación (T, P, Caudal)",
        "Lazo de Control Asociado (ISA-5.1)",
        "Material de Construcción Recomendado"
    ]
    ws2.append([])
    ws2.append(headers2)
    ws2.row_dimensions[4].height = 28
    for col_idx in range(1, 8):
        cell = ws2.cell(row=4, column=col_idx)
        cell.font = font_header
        cell.fill = fill_blue_head
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = header_border

    equipos_detalle = [
        (
            "E-04",
            "Cambiador de Calor Tubo y Carcasa",
            "Descarga slurry de R-01 (128 ºC)",
            "Alimentación a Filtro Prensa F-01 (50 ºC)",
            "T_in = 128 ºC, T_out = 50 ºC, P = 2.5 bar -> 1.2 bar. Fluido servicio: Agua de torre (25 ºC).",
            "TIC-104 en salida de slurry regulando caudal de agua en camisa/carcasa (TCV-104)",
            "Acero inoxidable AISI 316L (resistente a H2SO4 diluido caliente)"
        ),
        (
            "F-01",
            "Filtro Prensa de Membrana",
            "Slurry enfriado de E-04 + Agua de lavado",
            "Torta WIS a BF-02 / Líquido prehidrolizado a P-102",
            "Relación S/L 33% p/v. Lavado con agua a 50 ºC (2 kg agua / kg WIS seco).",
            "PDI-101 (Presión diferencial) para aviso de fin de ciclo y lavado automático",
            "Placas de polipropileno virgen + bastidor en acero carbono recubierto"
        ),
        (
            "A-01",
            "Columna de Adsorción / Intercambio",
            "Prehidrolizado ácido bruto de F-01",
            "Prehidrolizado detoxificado hacia BF-01",
            "T = 40-50 ºC, P = 1.5 bar. Carbón activo granular o resina catiónica Amberlite.",
            "FI-101 y análisis HPLC periódico (monitoreo de saturación de lecho)",
            "Acero inoxidable 316L o fibra de vidrio PRFV con liner químico"
        ),
        (
            "BF-01",
            "Biorreactor CSTR de Pentosas",
            "Xilosa líquida detoxificada + Nutrientes",
            "Vino de pentosas hacia bomba P-201A",
            "T = 37 ºC, pH = 6.5 - 7.0, t = 96 h. Agitación mecánica suave (100 rpm). Microorg: E. coli SL100.",
            "TIC-201 (Control temperatura), pHIC-201 (Dosificación de amoníaco/ácido)",
            "Acero inoxidable AISI 304 / 316L grado sanitario"
        ),
        (
            "BF-02",
            "Biorreactor PSSF (Hexosas)",
            "Sólidos WIS lavados + Enzimas Cellic CTec2",
            "Suspensión fermentada con lignina hacia CF-01",
            "Presacarificación 50 ºC (4 h) -> SSF 35 ºC (48 h). Levadura S. cerevisiae Ethanol Red.",
            "TIC-202 (Enfriamiento programado 50 ºC -> 35 ºC), agitador de alta viscosidad",
            "Acero inoxidable AISI 316L pulido espejo interior (Ra < 0.8 µm)"
        ),
        (
            "CF-01",
            "Centrífuga Decanter Horizontal",
            "Caldo fermentado bruto de BF-02",
            "Líquido clarificado a Z-01 / Torta de lignina a S-01",
            "Fuerza centrífuga 3000 x g. Separación continua de micropartículas de lignina insoluble.",
            "SC-301 (Control de velocidad diferencial del tornillo extractor)",
            "Tambor y tornillo en acero inoxidable dúplex (resistente a erosión y acidez)"
        ),
        (
            "Z-01",
            "Columna de Destilación Rectificadora",
            "Vino clarificado (CF-01 + BF-01)",
            "Cabeza: Etanol azeotrópico 93% p/p / Fondos: Vinazas",
            "P_top = 1.0 atm, T_top = 78.2 ºC, T_bottom = 102 ºC. Platos perforados o empaque estructurado.",
            "PIC-401 (Presión de cabeza), LIC-401 (Nivel de fondos), TIC-401 (Temperatura plato control)",
            "Calderería en AISI 304 / 316 en zona de agotamiento"
        ),
        (
            "E-05",
            "Hervidor de Fondos (Thermosiphon Reboiler)",
            "Líquido de fondos de Z-01",
            "Vapor de recirculación a base de Z-01",
            "T = 105 ºC, fluido térmico: Vapor de baja presión (3 bar de cogeneración Q-01).",
            "TCV-405 regulando admisión de vapor gobernada por TIC de plato sensible en Z-01",
            "Tubos en acero inoxidable 316L, carcasa en acero carbono"
        ),
        (
            "A-03A/B",
            "Tamices Moleculares de Zeolita 3A (PSA)",
            "Vapor azeotrópico de bioetanol (~93% p/p)",
            "Bioetanol anhidro combustible (>99.5% p/p)",
            "Dos lechos cíclicos (adsorción a 3 bar, regeneración por vacío/arrastre).",
            "Secuenciador PLC / DCS con válvulas automáticas temporizadas de cambio de lecho",
            "Recipientes a presión en acero carbono con filtro coalescente previo"
        ),
        (
            "DA-01",
            "Digestor Anaerobio UASB",
            "Vinazas de fondos de Z-01 (enfriadas)",
            "Biogás (CH4 + CO2) a Q-01 / Lodos biofertilizante",
            "Régimen mesófilo (37 ºC), TRH = 15-20 días. Carga orgánica alta (DQO > 40 g/L).",
            "TIC-501, PIC-501 (Presión en campana de gas), medidor de biometano (CH4/CO2)",
            "Hormigón armado con revestimiento epóxico anticorrosión o acero vitrificado"
        ),
        (
            "Q-01",
            "Caldera de Biomasa y Biogás (Cogeneración)",
            "Torta de lignina seca (S-01) + Biogás (DA-01)",
            "Vapor sobrecalentado a turbina y vapor de proceso",
            "Generación de vapor a 25 bar (para turbina) y desahogo a 2.5 bar para hidrólisis y destilación.",
            "BMS (Burner Management System), PIC de vapor, control de combustión O2 en chimenea",
            "Cámara de combustión mixta parrilla vibrante + quemador de gas"
        )
    ]

    for row_data in equipos_detalle:
        ws2.append(row_data)
        r = ws2.max_row
        ws2.row_dimensions[r].height = 42
        for c in range(1, 8):
            cell = ws2.cell(row=r, column=c)
            cell.font = font_data
            cell.border = thin_border
            if c in [1, 2]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = font_bold
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # =============================================================
    # HOJA 3: BASE DE CONOCIMIENTO CINÉTICA Y BALANCES
    # =============================================================
    ws3 = wb.create_sheet(title="Cinetica_Balances_Normativa")
    ws3.views.sheetView[0].showGridLines = True

    ws3.merge_cells("A1:E1")
    ws3["A1"] = "BASE DE CONOCIMIENTO CIENTÍFICA, CINÉTICAS Y NORMAS DEL PROCESO"
    ws3["A1"].font = font_title
    ws3["A1"].fill = fill_navy
    ws3["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws3.row_dimensions[1].height = 35

    ws3.merge_cells("A2:E2")
    ws3["A2"] = "Artículos de Referencia (Romero-García 2022, Padilla-Rascón 2022) y Normas Oficiales de Planos"
    ws3["A2"].font = font_subtitle
    ws3["A2"].fill = fill_steel
    ws3["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws3.row_dimensions[2].height = 22

    headers3 = [
        "Etapa / Aspecto Clave",
        "Referencia Bibliográfica o Norma",
        "Parámetros Cuantitativos de Diseño",
        "Rendimiento o Especificación Técnica",
        "Impacto en el Dibujo de AutoCAD"
    ]
    ws3.append([])
    ws3.append(headers3)
    ws3.row_dimensions[4].height = 28
    for col_idx in range(1, 6):
        cell = ws3.cell(row=4, column=col_idx)
        cell.font = font_header
        cell.fill = fill_blue_head
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = header_border

    bases_datos = [
        (
            "Hidrólisis Ácida de Hemicelulosa",
            "Romero-García et al. (2022) / Padilla-Rascón (2022)",
            "10.5 g H2SO4 / 100 g hueso seco; S/L = 33% p/v; T = 128 ºC; t = 60 min; P = 2.5 bar vapor.",
            "Solubilización >85% de xilana. Generación de ~70 kg xilosa líquida y ~520 kg sólido WIS / t.",
            "R-01 requiere camisa de vapor vivo (2.5 bar), agitador mecánico y válvula de descarga inferior."
        ),
        (
            "Detoxificación del Prehidrolizado",
            "Tormos-Belda (2021) / Romero-García et al. (2022)",
            "Lecho de carbón activo granular (AC) o resinas de intercambio iónico (IER).",
            "Eliminación >90% de furfural y >95% de ácido acético. Azúcares fermentables intactos.",
            "A-01 debe recibir la corriente líquida de F-01 antes de cualquier neutralización con álcali."
        ),
        (
            "Fermentación Pentosas (Xilosa)",
            "Romero-García et al. (2022)",
            "Bacteria E. coli SL100; T = 37 ºC; pH = 6.5-7.0; tiempo t = 96 h.",
            "Rendimiento ~73% sobre azúcares teóricos disueltos: produce ~75.5 kg etanol / t hueso.",
            "BF-01 es un reactor de gran volumen (96 h residencia) con chaqueta de agua a 37 ºC."
        ),
        (
            "Presacarificación y SSF (PSSF)",
            "Romero-García et al. (2022)",
            "Enzima Cellic CTec2 (40 FPU/g sustrato) a 50 ºC (4 h); luego enfriar a 35 ºC con S. cerevisiae (48 h).",
            "Rendimiento de 86.8 kg etanol / t hueso. Concentración final de caldo ~36 g/L etanol.",
            "BF-02 requiere camisa de calefacción/refrigeración y control de temperatura de dos fases."
        ),
        (
            "Destilación y Deshidratación",
            "Manual de Bioetanol / Normativa EN 15376",
            "Columna Z-01 con hervidor E-05 y condensador E-01; tamices moleculares A-03A/B.",
            "Columna alcanza azeótropo (~93% p/p); tamices zeolita 3A alcanzan >99.5% p/p (anhidro).",
            "Z-01 requiere hervidor de fondos, tanque de reflujo y baterías de tamices moleculares."
        ),
        (
            "Normativa de Diagramas de Proceso",
            "UNE-EN ISO 10628-1:2015 y 10628-2:2012 (EACON)",
            "Simbología de equipos, líneas de proceso (línea gruesa) y auxiliares (línea media).",
            "Los recipientes se dibujan en proporciones relativas reales; sentidos de flujo señalizados.",
            "Todos los bloques en AutoCAD deben coincidir con la codificación ISO 10628."
        ),
        (
            "Normativa de Lazos de Instrumentación",
            "ANSI / ISA-5.1-2009 e IEC 62424",
            "Transmisores (TT, PT, LT), Controladores (TIC, PIC, LIC) y Válvulas de control (TCV, FCV).",
            "Lazos cerrados: sensor -> controlador -> válvula con designación de fallo (FC o FO).",
            "Globos de instrumentos de 10-12 mm de diámetro con línea discontinua de señal eléctrica."
        ),
        (
            "Normativa de Cajetines y Carátulas",
            "UNE-EN ISO 7200 / ISO 5457 (EACON)",
            "Campos obligatorios: Entidad legal, Título, Autor, Fecha, Escala (N/S), Nº Plano, Revisión.",
            "Anchura máxima 180 mm en esquina inferior derecha para permitir plegado en A4.",
            "Los cajetines están en el espacio papel (Layouts) y están 100% protegidos sin cambios."
        )
    ]

    for row_data in bases_datos:
        ws3.append(row_data)
        r = ws3.max_row
        ws3.row_dimensions[r].height = 42
        for c in range(1, 6):
            cell = ws3.cell(row=r, column=c)
            cell.font = font_data
            cell.border = thin_border
            if c in [1, 2]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = font_bold
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # -------------------------------------------------------------
    # AJUSTE AUTOMÁTICO DE ANCHURAS DE COLUMNA
    # -------------------------------------------------------------
    col_widths1 = {"A": 12, "B": 24, "C": 26, "D": 45, "E": 45, "F": 22}
    for col_letter, width in col_widths1.items():
        ws1.column_dimensions[col_letter].width = width

    col_widths2 = {"A": 12, "B": 28, "C": 35, "D": 35, "E": 45, "F": 40, "G": 35}
    for col_letter, width in col_widths2.items():
        ws2.column_dimensions[col_letter].width = width

    col_widths3 = {"A": 28, "B": 35, "C": 45, "D": 42, "E": 42}
    for col_letter, width in col_widths3.items():
        ws3.column_dimensions[col_letter].width = width

    # Guardar Excel
    out_xlsx = r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Plan_Modificaciones_AutoCAD_TFG.xlsx"
    wb.save(out_xlsx)
    print("Excel de Ingenieria generado con exito:", out_xlsx)

if __name__ == "__main__":
    create_engineering_excel()

