import sys
import os
sys.path.append(r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\.agents\skills\pfd-generator\scripts")
from pid_lib import PID, LIQ, INK, SUB, RED, GREEN, BLUE
import pymupdf

def build_reactor_section():
    # Lienzo estandar 1400x940
    p = PID(w=1400, h=940)
    
    # Titulo de plano
    p.title(
        main="PLANTA DE BIOETANOL (HUESO DE ACEITUNA) - ÁREA DE REACCIÓN Y DETOXIFICACIÓN",
        subtitle="DIAGRAMA DE FLUJO DE PROCESO (PFD) / BALANCE Y CONTROL CONCEPTUAL (04-PFD-201 Rev A)",
        stamp=True
    )
    
    # 1. REACTOR DE HIDRÓLISIS ÁCIDA R-101 (T = 128 ºC, H2SO4 10.5 g/100g)
    # vessel(x0, y0, x1, y1, r=26, level=None, level_label=None)
    p.vessel(180, 280, 330, 540, r=25, level=470, level_label="NIVEL NLL")
    p.agitator(cx=255, top=280, shaft_bottom=490, tag="AG-101")
    p.equip_tag(cx=255, y=575, tag="R-101", service="REACTOR HIDRÓLISIS ÁCIDA", detail="T = 128 ºC, P = 2.5 bar, t = 60 min")
    
    # 2. SEPARADOR SÓLIDO-LÍQUIDO / FILTRO PRENSA F-101
    p.vessel(450, 360, 550, 500, r=10)
    p.equip_tag(cx=500, y=530, tag="F-101", service="FILTRO PRENSA (WIS / LÍQUIDO)", detail="Separación Sólido-Líquido (33% p/v)")
    
    # 3. COLUMNA DE DETOXIFICACIÓN D-101 (Resina IER / Carbón Activo)
    p.vessel(680, 260, 790, 540, r=20)
    p.equip_tag(cx=735, y=570, tag="D-101", service="COLUMNA DETOXIFICACIÓN", detail="Eliminación Furfural >90%, Acético >95%")
    
    # 4. REACTOR FERMENTADOR PSSF R-201 (Presacarificación y Fermentación Simultánea)
    p.vessel(960, 250, 1140, 560, r=30, level=490, level_label="NIVEL NLL")
    p.agitator(cx=1050, top=250, shaft_bottom=510, tag="AG-201")
    p.equip_tag(cx=1050, y=595, tag="R-201", service="BIORREACTOR PSSF (HEXOSAS/WIS)", detail="Cellic CTec2 + S. cerevisiae (35-50 ºC, 52 h)")

    # 5. BOMBAS CENTRÍFUGAS DE TRASIEGO
    # P-101A (descarga R-101 a F-101)
    p.add(f'<circle cx="370" cy="510" r="18" fill="white" stroke="{INK}" stroke-width="2"/>')
    p.add(f'<path d="M 358,500 L 382,510 L 358,520 Z" fill="{INK}"/>')
    p.txt(x=370, y=542, s="P-101A", size=10, weight="bold")
    
    # P-102A (descarga prehidrolizado a D-101)
    p.add(f'<circle cx="600" cy="460" r="18" fill="white" stroke="{INK}" stroke-width="2"/>')
    p.add(f'<path d="M 588,450 L 612,460 L 588,470 Z" fill="{INK}"/>')
    p.txt(x=600, y=492, s="P-102A", size=10, weight="bold")

    # P-201A (descarga de vino fermentado a destilación)
    p.add(f'<circle cx="1200" cy="520" r="18" fill="white" stroke="{INK}" stroke-width="2"/>')
    p.add(f'<path d="M 1188,510 L 1212,520 L 1188,530 Z" fill="{INK}"/>')
    p.txt(x=1200, y=552, s="P-201A", size=10, weight="bold")

    # LÍNEAS DE PROCESO
    # 1. Alimentación Hueso + H2SO4 a R-101
    p.pipe("M 60,240 L 220,240 L 220,280", arrow=True)
    p.txt(140, 232, "01: HUESO + H2SO4 (33% p/v)", size=10, weight="bold")
    
    p.pipe("M 60,200 L 240,200 L 240,280", arrow=True)
    p.txt(140, 192, "02: VAPOR VIVO 2.5 bar (128 ºC)", size=10, weight="bold")
    
    # 2. Descarga R-101 a Filtro F-101
    p.pipe("M 255,540 L 255,510 L 352,510", arrow=True)
    p.pipe("M 388,510 L 415,510 L 415,420 L 450,420", arrow=True)
    p.txt(415, 410, "03: SLURRY HIDROLIZADO", size=10, weight="bold")

    # 3. Filtro F-101: Separación
    # Salida sólida WIS a R-201 (línea superior sólida)
    p.pipe("M 500,360 L 500,210 L 990,210 L 990,250", arrow=True)
    p.txt(745, 202, "04: SÓLIDO WIS (CELULOSA / LIGNINA)", size=10, weight="bold")
    
    # Salida líquida (Prehidrolizado) a Bomba P-102 y Torre Detox D-101
    p.pipe("M 550,460 L 582,460", arrow=True)
    p.pipe("M 618,460 L 645,460 L 645,340 L 680,340", arrow=True)
    p.txt(662, 330, "05: PREHIDROLIZADO ÁCIDO", size=9.5, weight="bold")

    # 4. Detoxificación D-101 a Fermentación / Almacenamiento
    # Prehidrolizado detoxificado hacia R-201 / Fermentador Pentosas
    p.pipe("M 790,480 L 860,480 L 860,310 L 960,310", arrow=True)
    p.txt(860, 300, "06: LÍQUIDO DETOXIFICADO", size=9.5, weight="bold")
    
    p.pipe("M 860,480 L 860,700 L 1280,700", arrow=True)
    p.txt(1070, 690, "07: A FERMENTADOR DE PENTOSAS (E. coli SL100)", size=10, weight="bold")

    # 5. Adiciones a R-201 (Enzimas Cellic CTec2 + Inóculo levadura)
    p.pipe("M 850,160 L 1050,160 L 1050,250", arrow=True)
    p.txt(950, 150, "08: ENZIMAS CTec2 + TAMPÓN CITRATO", size=10, weight="bold")

    # 6. Salida de producto fermentado de R-201
    p.pipe("M 1050,560 L 1050,520 L 1182,520", arrow=True)
    p.pipe("M 1218,520 L 1280,520", arrow=True)
    p.txt(1250, 510, "09: A DESTILACIÓN (~36 g/L EtOH)", size=10, weight="bold")

    # LAZOS DE CONTROL CONCEPTUAL (ISA-5.1)
    # Lazo de Temperatura en R-101 (TIC-101 regulando válvula de vapor TCV-101)
    p.bubble(cx=120, cy=410, top="TT", bot="101")
    p.bubble(cx=120, cy=340, top="TIC", bot="101")
    p.sig("M 180,410 L 142,410")
    p.sig("M 120,388 L 120,362")
    p.cvalve(cx=150, cy=200, tag="TCV-101", fail="FC")
    p.sig("M 120,318 L 120,200 L 135,200")

    # Lazo de Temperatura en Fermentador R-201 (TIC-201 regulando agua de refrigeración)
    p.bubble(cx=1220, cy=380, top="TT", bot="201")
    p.bubble(cx=1220, cy=300, top="TIC", bot="201")
    p.sig("M 1140,380 L 1198,380")
    p.sig("M 1220,358 L 1220,322")
    p.cvalve(cx=1050, cy=100, tag="TCV-201", fail="FO")
    p.sig("M 1220,278 L 1220,100 L 1065,100")

    # TABLA DE BALANCE CONCEPTUAL DE MATERIA Y RENDIMIENTOS (Romero-García et al., 2022)
    p.add(f'''
    <g transform="translate(60, 680)">
      <rect x="0" y="0" width="760" height="200" fill="#ffffff" stroke="{INK}" stroke-width="1.5" rx="4"/>
      <rect x="0" y="0" width="760" height="28" fill="#e9ecef" stroke="{INK}" stroke-width="1.5"/>
      <text x="15" y="19" font-family="Arial" font-size="12" font-weight="bold" fill="{INK}">TABLA DE CORRIENTES Y BALANCE DE MATERIA DE DISEÑO (Base: 1 000 kg hueso aceituna seco)</text>
      
      <text x="15" y="52" font-family="Arial" font-size="10.5" fill="{INK}"><b>Corriente 01 (Alimentación):</b> 1 000 kg Hueso seco + 3 000 kg H2O + 105 kg H2SO4 (Relación S/L 33% p/v)</text>
      <text x="15" y="74" font-family="Arial" font-size="10.5" fill="{INK}"><b>Corriente 03 (Slurry R-101):</b> Hidrolizado a 128 ºC (Xilosa libre: ~70 kg, Acético: ~15 kg, Furfural: ~1.8 kg)</text>
      <text x="15" y="96" font-family="Arial" font-size="10.5" fill="{INK}"><b>Corriente 04 (Sólido WIS F-101):</b> ~520 kg de sólido insoluble lavado (Celulosa ~48%, Lignina insoluble ~52%)</text>
      <text x="15" y="118" font-family="Arial" font-size="10.5" fill="{INK}"><b>Corriente 06 (Líquido Detox D-101):</b> Furfural &lt;0.1 g/L (&gt;90% eliminación), Acético &lt;0.5 g/L (&gt;95% eliminación)</text>
      <text x="15" y="140" font-family="Arial" font-size="10.5" fill="{INK}"><b>Corriente 08 (Biocatálisis R-201):</b> Cellic CTec2 (40 FPU/g sustrato) + S. cerevisiae Ethanol Red (1 g/L)</text>
      <text x="15" y="162" font-family="Arial" font-size="10.5" font-weight="bold" fill="{BLUE}">Corriente 09 (Caldo a Destilación): 86.8 kg Etanol (de hexosas) + 75.5 kg Etanol (de pentosas) = 162.3 kg Bioetanol / t</text>
    </g>
    ''')

    # Guardar SVG
    out_svg = r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Diagramas\pfd_reaccion_detox.svg"
    out_png = r"F:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Diagramas\pfd_reaccion_detox.png"
    p.save(out_svg)
    print("SVG generado:", out_svg)
    
    # Renderizar a PNG de alta resolución con PyMuPDF
    doc = pymupdf.open(out_svg)
    pix = doc[0].get_pixmap(dpi=150)
    pix.save(out_png)
    print("PNG renderizado con exito:", out_png)

if __name__ == "__main__":
    build_reactor_section()
