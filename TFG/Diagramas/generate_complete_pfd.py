import sys
import os
sys.path.append(r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\.agents\skills\pfd-generator\scripts")
from pid_lib import PID, INK, BLUE, LIQ, RED, GREEN
import pymupdf

def build_complete_pfd():
    p = PID(w=2000, h=1100)
    
    p.title(
        main="BIORREFINERÍA DE HUESO DE ACEITUNA - PLANTA INTEGRAL DE BIOETANOL Y SUBPRODUCTOS",
        subtitle="DIAGRAMA DE FLUJO DE PROCESO (PFD) CON BALANCES Y EQUIPOS AUXILIARES (ISO 10628 / ISA-5.1)",
        stamp=True
    )
    
    # -------------------------------------------------------------
    # ZONA 1: PRETRATAMIENTO Y DETOXIFICACIÓN (x: 100 a 700)
    # -------------------------------------------------------------
    # R-01: Reactor Hidrólisis Ácida
    p.vessel(140, 260, 280, 500, r=22, level=440, level_label="NLL")
    p.agitator(cx=210, top=260, shaft_bottom=460, tag="AG-01")
    p.equip_tag(cx=210, y=530, tag="R-01", service="REACTOR HIDRÓLISIS ÁCIDA", detail="128 ºC, 2.5 bar, H2SO4 10.5% p/p")
    
    # E-04: Enfriador de Slurry (NUEVO REQUERIDO)
    p.add(f'<circle cx="350" cy="420" r="24" fill="white" stroke="{INK}" stroke-width="2"/>')
    p.add(f'<path d="M 334,420 C 342,408 346,432 354,420 C 360,410 366,420 366,420" fill="none" stroke="{INK}" stroke-width="2"/>')
    p.equip_tag(cx=350, y=470, tag="E-04", service="ENFRIADOR SLURRY", detail="128 ºC -> 50 ºC")
    
    # F-01: Filtro Prensa Sólido-Líquido (WIS / Prehidrolizado)
    p.vessel(440, 360, 530, 480, r=10)
    p.equip_tag(cx=485, y=510, tag="F-01", service="FILTRO PRENSA", detail="Separación WIS / Líquido + Lavado")
    
    # A-01: Columna de Detoxificación Carbón Activo / Resinas
    p.vessel(600, 260, 690, 520, r=18)
    p.equip_tag(cx=645, y=550, tag="A-01", service="COLUMNA DETOXIFICACIÓN", detail="Eliminación Furfural >90%, Acético >95%")

    # TN-01 y CR-01: Neutralización y Cristalizador Sulfato Amonio
    p.vessel(600, 640, 690, 800, r=18)
    p.equip_tag(cx=645, y=830, tag="TN-01", service="TANQUE NEUTRALIZACIÓN", detail="Neutralización con NH3 anhidro")
    p.vessel(750, 660, 840, 800, r=12)
    p.equip_tag(cx=795, y=830, tag="CR-01", service="CRISTALIZADOR", detail="Subproducto: Sulfato de amonio")

    # -------------------------------------------------------------
    # ZONA 2: FERMENTACIÓN PENTOSAS Y HEXOSAS (x: 800 a 1300)
    # -------------------------------------------------------------
    # BF-01: Fermentador Pentosas (E. coli SL100)
    p.vessel(800, 260, 950, 540, r=25, level=480, level_label="NLL")
    p.agitator(cx=875, top=260, shaft_bottom=500, tag="AG-BF01")
    p.equip_tag(cx=875, y=570, tag="BF-01", service="FERMENTADOR PENTOSAS", detail="E. coli SL100 (37 ºC, 96 h, ~75 kg EtOH/t)")

    # BF-02: Biorreactor PSSF Hexosas (Cellic CTec2 + S. cerevisiae)
    p.vessel(1050, 240, 1220, 540, r=28, level=470, level_label="NLL")
    p.agitator(cx=1135, top=240, shaft_bottom=500, tag="AG-BF02")
    p.equip_tag(cx=1135, y=570, tag="BF-02", service="BIORREACTOR PSSF", detail="Cellic CTec2 (50 ºC, 4h) -> S. cerevisiae (35 ºC, 48h)")

    # CF-01: Centrífuga Decanter Lignina Pre-Destilación (NUEVA POSICIÓN REQUERIDA)
    p.vessel(1300, 370, 1390, 480, r=10)
    p.equip_tag(cx=1345, y=510, tag="CF-01", service="DECANTER LIGNINA", detail="Retirada de lignina antes de destilar")

    # -------------------------------------------------------------
    # ZONA 3: TREN DE DESTILACIÓN Y COGENERACIÓN (x: 1450 a 1900)
    # -------------------------------------------------------------
    # Z-01: Columna de Rectificación de Bioetanol
    p.vessel(1480, 180, 1560, 700, r=25)
    p.equip_tag(cx=1520, y=730, tag="Z-01", service="COLUMNA DE DESTILACIÓN", detail="Concentración alcohólica azeotrópica (~93% p/p)")

    # E-01: Condensador superior Z-01
    p.add(f'<circle cx="1640" cy="180" r="22" fill="white" stroke="{INK}" stroke-width="2"/>')
    p.equip_tag(cx=1640, y=145, tag="E-01", service="CONDENSADOR RECTIFICACIÓN")

    # TKR-01: Tanque de Reflujo
    p.vessel(1615, 230, 1665, 300, r=10)
    p.equip_tag(cx=1640, y=325, tag="TKR-01", service="ACUMULADOR REFLUJO")

    # E-05: Hervidor de Fondos Reboiler (NUEVO REQUERIDO)
    p.add(f'<circle cx="1410" cy="660" r="22" fill="white" stroke="{INK}" stroke-width="2"/>')
    p.equip_tag(cx=1410, y=705, tag="E-05", service="REBOILER HERVIDOR")

    # A-03A/B: Tamices Moleculares de Zeolita para Bioetanol Anhidro >99.5% (NUEVO REQUERIDO)
    p.vessel(1740, 220, 1790, 380, r=10)
    p.vessel(1810, 220, 1860, 380, r=10)
    p.equip_tag(cx=1800, y=410, tag="A-03A/B", service="TAMICES MOLECULARES (PSA)", detail="Bioetanol Anhidro Carburante (>99.5% p/p)")

    # DA-01: Digestor Anaerobio (Tratamiento vinazas fondos Z-01)
    p.vessel(1450, 830, 1600, 980, r=25)
    p.equip_tag(cx=1525, y=1010, tag="DA-01", service="DIGESTOR ANAEROBIO", detail="Vinazas -> Biogás (CH4 + CO2) y Biofertilizante")

    # Q-01: Caldera de Cogeneración
    p.vessel(1740, 750, 1880, 940, r=20)
    p.equip_tag(cx=1810, y=970, tag="Q-01", service="CALDERA COGENERACIÓN", detail="Combustión Lignina seca + Biogás -> Vapor proceso")

    # -------------------------------------------------------------
    # TUBERÍAS Y CORRIENTES PRINCIPALES
    # -------------------------------------------------------------
    # C01: Alimentación
    p.pipe("M 50,300 L 140,300", arrow=True)
    p.txt(90, 290, "01: HUESO + H2SO4", size=9, weight="bold")

    # R-01 a E-04
    p.pipe("M 210,500 L 210,520 L 320,520 L 320,420 L 326,420", arrow=True)
    
    # E-04 a F-01
    p.pipe("M 374,420 L 440,420", arrow=True)
    p.txt(405, 410, "03: SLURRY 50ºC", size=8.5, weight="bold")

    # F-01 Sólido WIS a BF-02
    p.pipe("M 485,360 L 485,200 L 1090,200 L 1090,240", arrow=True)
    p.txt(780, 190, "04: SÓLIDO WIS LAVADO (CELULOSA/LIGNINA)", size=9, weight="bold")

    # F-01 Líquido a A-01 Detox
    p.pipe("M 530,440 L 600,440", arrow=True)
    p.txt(565, 430, "05: PREHIDROLIZADO", size=8.5, weight="bold")

    # A-01 Detox hacia BF-01 (Xilosa)
    p.pipe("M 645,260 L 645,220 L 840,220 L 840,260", arrow=True)
    p.txt(740, 210, "06: XILOSA PURIFICADA", size=8.5, weight="bold")

    # BF-01 efluente a destilación
    p.pipe("M 875,540 L 875,600 L 1350,600 L 1350,490 L 1480,490", arrow=True)

    # BF-02 efluente a decanter CF-01
    p.pipe("M 1135,540 L 1135,510 L 1260,510 L 1260,430 L 1300,430", arrow=True)
    p.txt(1220, 420, "08: CALDO PSSF", size=8.5, weight="bold")

    # CF-01 Líquido clarificado a Z-01
    p.pipe("M 1390,430 L 1480,430", arrow=True)
    p.txt(1435, 420, "VINO CLARIFICADO", size=8.5, weight="bold")

    # CF-01 Torta de lignina hacia Cogeneración Q-01
    p.pipe("M 1345,480 L 1345,860 L 1740,860", arrow=True)
    p.txt(1400, 850, "LIGNINA SÓLIDA A Q-01", size=9, weight="bold")

    # Cabeza Z-01 a E-01 y Reflujo TKR-01
    p.pipe("M 1520,180 L 1520,150 L 1640,150 L 1640,158", arrow=True)
    p.pipe("M 1640,202 L 1640,230", arrow=True)
    p.pipe("M 1640,300 L 1640,350 L 1560,350", arrow=True)

    # Destilado de TKR-01 a Tamices Moleculares A-03A/B
    p.pipe("M 1665,270 L 1740,270", arrow=True)
    p.pipe("M 1790,270 L 1810,270", arrow=True)
    p.pipe("M 1860,270 L 1940,270", arrow=True)
    p.txt(1900, 260, "PRODUCTO: BIOETANOL >99.5%", size=9.5, weight="bold")

    # Fondos Z-01 a Hervidor E-05 y retorno
    p.pipe("M 1500,700 L 1500,740 L 1410,740 L 1410,682", arrow=True)
    p.pipe("M 1410,638 L 1410,600 L 1480,600", arrow=True)

    # Vinazas de Z-01 a Digestión Anaerobia DA-01
    p.pipe("M 1520,700 L 1520,830", arrow=True)
    p.txt(1530, 780, "VINAZAS A DA-01", size=8.5, weight="bold")

    # Biogás de DA-01 a Cogeneración Q-01
    p.pipe("M 1600,900 L 1740,900", arrow=True)
    p.txt(1670, 890, "BIOGÁS (CH4)", size=9, weight="bold")

    # Guardar SVG y PNG
    svg_out = r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Diagramas\pfd_planta_completa.svg"
    png_out = r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Diagramas\pfd_planta_completa.png"
    p.save(svg_out)
    print("PFD Completo SVG:", svg_out)
    
    doc = pymupdf.open(svg_out)
    pix = doc[0].get_pixmap(dpi=130)
    pix.save(png_out)
    print("PFD Completo PNG generado con éxito:", png_out)

if __name__ == "__main__":
    build_complete_pfd()

