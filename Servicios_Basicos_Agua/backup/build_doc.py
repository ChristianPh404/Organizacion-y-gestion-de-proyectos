import os
import re

backup_path = 'grupo5_servicios_basicos_agua_backup_antes_comentar.tex'
with open(backup_path, 'r', encoding='utf-8', errors='replace') as f:
    orig = f.read()

# Fix preamble in orig
orig = re.sub(r'\\addto\\captionsspanish\s*\{[^}]*\}', '', orig)
orig = orig.replace('{\x83\x8dndice General}\n\n}\n', '')
orig = orig.replace('{Índice General}\n\n}\n', '')
orig = orig.replace(r'\nocite{*}', '')

# Ensure pdfpages and pdflscape are loaded
if r'\usepackage{pdfpages}' not in orig:
    orig = orig.replace(r'\usepackage{pdflscape}', '\\usepackage{pdflscape}\n\\usepackage{pdfpages}')

# Find indices
idx_ch1 = orig.find(r'\chapter{Introducci')
idx_ch5 = orig.find(r'\chapter{Normativa Sanitaria')
idx_ch6 = orig.find(r'\chapter{Conclusiones')
idx_bib = orig.find(r'\printbibliography')

preamble = orig[:idx_ch1]
ch1_to_4 = orig[idx_ch1:idx_ch5]
ch6 = orig[idx_ch6:idx_bib]
bib_and_end = orig[idx_bib:]

# Build the complete updated Chapter 5 content with landscape pages and exact citations
new_ch5_content = r'''\chapter{Normativa Sanitaria, Medioambiental y Red de Saneamiento Industrial}

El abastecimiento de agua y la evacuación de efluentes en un complejo de ingeniería química o planta de proceso industrial están sujetos a un régimen regulatorio multidisciplinar y jerárquico. La viabilidad técnica y legal del proyecto depende del cumplimiento sincrónico de la legislación higiénico-sanitaria para agua de consumo y procesos limpios, los reglamentos de seguridad industrial contra riesgos biológicos (\textit{Legionella}), la normativa medioambiental sobre vertidos y protección de masas receptoras (aguas subterráneas y superficiales), el nuevo marco de regeneración y economía circular, y los códigos constructivos y de diseño que rigen las redes de evacuación y saneamiento (\cite{TRLA2001, RDPH1986, RD3_2023, RD487_2022, RD1085_2024, UNE_EN_752, CTE_DB_HS5, UNE_EN_ISO_129_1, ISO_4067_1, ISO_4067_6}).

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[node distance=1.3cm, auto,
    bloque/.style={rectangle, draw=blue!70!black, fill=blue!5, rounded corners=3pt, thick, text width=4.0cm, align=center, minimum height=1.0cm, font=\small},
    norma/.style={rectangle, draw=teal!80!black, fill=teal!10, rounded corners=3pt, dashed, thick, text width=4.2cm, align=center, minimum height=1.0cm, font=\footnotesize},
    linea/.style={draw=gray!80!black, -{Latex[length=2.5mm]}, thick}]
    
    \node [bloque] (origen) {\textbf{Captación \& Red Municipal}\\Abastecimiento industrial};
    \node [norma, right=1.6cm of origen] (n1) {\textbf{RD 3/2023} (Consumo/Proceso)\\Lista positiva de materiales};
    
    \node [bloque, below=0.9cm of origen] (uso) {\textbf{Distribución \& Torres}\\Procesos y refrigeración};
    \node [norma, right=1.6cm of uso] (n2) {\textbf{RD 487/2022} (Legionelosis)\\PPCL / PSL y biocidas};
    
    \node [bloque, below=0.9cm of uso] (red) {\textbf{Red de Saneamiento Interna}\\Redes separativas y arquetas};
    \node [norma, right=1.6cm of red] (n3) {\textbf{CTE DB-HS 5 / UNE-EN 752}\\UNE-EN ISO 129-1 (dibujo)};
    
    \node [bloque, below=0.9cm of red] (vertido) {\textbf{EDARI \& Evacuación Final}\\Colector público o DPH};
    \node [norma, right=1.6cm of vertido] (n4) {\textbf{TRLA / RD 665/2023 / Dir. 2024/3019}\\Canon vertido, VLE y RD 1085/2024};
    
    \path [linea] (origen) -- (uso);
    \path [linea] (uso) -- (red);
    \path [linea] (red) -- (vertido);
    
    \draw [dashed, draw=gray!70, thick] (origen) -- (n1);
    \draw [dashed, draw=gray!70, thick] (uso) -- (n2);
    \draw [dashed, draw=gray!70, thick] (red) -- (n3);
    \draw [dashed, draw=gray!70, thick] (vertido) -- (n4);
\end{tikzpicture}
\caption{Estructura regulatoria integral aplicable al ciclo del agua y saneamiento en plantas químicas e industriales.}
\label{fig:mapa_normativo_integral}
\end{figure}

\section{Marco Jurídico Integrado del Agua en España}

El marco regulatorio hidráulico e higiénico español se estructura en torno a tres pilares coordinados:
\begin{enumerate}
    \item \textbf{Gestión de la Oferta y Calidad de Captación:} Regido por el Texto Refundido de la Ley de Aguas (\cite{TRLA2001}) y su reglamento instrumental, el Reglamento del Dominio Público Hidráulico (\cite{RDPH1986}), recientemente modernizado mediante el \textbf{Real Decreto 665/2023}.
    \item \textbf{Seguridad Sanitaria en Instalaciones Interiores y Usos Especiales:} Articulado por el \textbf{Real Decreto 3/2023} (\cite{RD3_2023}) sobre aguas de consumo y materiales en contacto, junto con el \textbf{Real Decreto 487/2022} (\cite{RD487_2022}) de prevención higiénico-sanitaria de la legionelosis en equipos evaporativos e intercambiadores.
    \item \textbf{Economía Circular, Evacuación de Efluentes y Redes de Saneamiento:} Regido para reutilización por el \textbf{Real Decreto 1085/2024} (\cite{RD1085_2024}), a nivel europeo por la nueva \textbf{Directiva (UE) 2024/3019} (\cite{DirectivaUE_2024_3019}), y a nivel técnico-constructivo y de delineación de planos por el Código Técnico de la Edificación (\cite{CTE_DB_HS5}), la norma europea de alcantarillado industrial \textbf{UNE-EN 752} (\cite{UNE_EN_752}), las directrices vigentes de acotación \textbf{UNE-EN ISO 129-1:2019} (\cite{UNE_EN_ISO_129_1}) (sin que exista una norma única vigente de símbolos de arquetas y pozos, ver sección~\ref{sec:planos_reales}).
\end{enumerate}

\section{Normativa Sanitaria de Calidad del Agua}

\subsection{Real Decreto 3/2023: Criterios Técnico-Sanitarios del Agua de Consumo e Industrial}
El \textbf{Real Decreto 3/2023}, de 10 de enero, transpone la Directiva (UE) 2020/2184, estableciendo un nuevo paradigma de aseguramiento de calidad basado en planes de evaluación del riesgo (\textit{Water Safety Plans}):
\begin{itemize}
    \item \textbf{Lista Positiva de Materiales en Contacto:} El RD 3/2023 impide instalar tuberías, racores, juntas, valvulería o recubrimientos epóxicos que liberen sustancias nocivas o alteren las propiedades organolépticas del agua. En proyectos químicos, las líneas que sirvan como base para preparación de reactivos, calderas de vapor limpio, laboratorios o aseos deben justificar certificados de conformidad sanitaria.
    \item \textbf{Protección contra Retorno y Dispositivos Antirretorno:} El diseño de la red interna de abastecimiento debe impedir físicamente cualquier retorno o sifonamiento de fluidos de proceso hacia la red de distribución general, instalando desconectores hidráulicos de zona de presión reducida no comprobable o comprobable tipo BA (\cite{CTE_DB_HS4}).
    \item \textbf{Valores paramétricos:} El anexo I del RD 3/2023 fija valores para metales (plomo, níquel, cromo, etc.), subproductos de desinfección (trihalometanos $\le 100\,\mu\text{g/L}$) y desinfectante residual en red (cloro libre entre $0.2$ y $1.0\,\text{mg/L}$); las cifras exactas y sus plazos de aplicación deben tomarse del texto consolidado (\cite{RD3_2023}).
\end{itemize}

\subsection{Real Decreto 487/2022: Prevención y Control de la Legionelosis}
En la industria química y de procesos, los sistemas de refrigeración evaporativa (torres de refrigeración, condensadores evaporativos, aeroenfriadores adiabáticos) y los circuitos de agua caliente sanitaria (ACS) constituyen instalaciones de alto riesgo de proliferación y aerosolización de \textit{Legionella pneumophila}:
\begin{itemize}
    \item \textbf{Elección Obligatoria entre PPCL o PSL:} El titular de la instalación industrial debe implantar contractualmente:
    \begin{itemize}
        \item Un \textbf{Plan de Prevención y Control de Legionella (PPCL)}: Basado en requisitos estandarizados de purgas automáticas por conductividad, limpieza/desinfección semestral y dosificación continua de biocidas oxidantes autorizados en el Registro Oficial de Biocidas (ROESB).
        \item Un \textbf{Plan Sanitario de Legionella (PSL)}: Basado en una evaluación formal cuantitativa del riesgo conforme a las directrices de la OMS, obligatorio si se pretenden modular los regímenes analíticos convencionales.
    \end{itemize}
    \item \textbf{Separadores de gotas de alta eficiencia:} Las torres de refrigeración y condensadores evaporativos deben incorporar separadores de gotas que cumplan el caudal máximo de arrastre exigido por la normativa vigente (\cite{RD487_2022}).
    \item \textbf{Acciones correctoras según resultados analíticos:} Para torres y condensadores evaporativos, el RD 487/2022 (anexo VIII) escalona las medidas según la concentración de \textit{Legionella}: por debajo de $100\,\text{UFC/L}$ se mantienen los programas; entre $100$ y $1\,000\,\text{UFC/L}$ se revisan los programas de mantenimiento y tratamiento y se valora limpiar y desinfectar; entre $1\,000$ y $10\,000\,\text{UFC/L}$ la limpieza y desinfección es obligatoria; a partir de $10\,000\,\text{UFC/L}$ se detiene la instalación hasta limpiarla y desinfectarla, con remuestreo posterior (\cite{RD487_2022}).
\end{itemize}

\section{Redes de Saneamiento Industrial y Evacuación de Efluentes}

El diseño de la red de saneamiento en un proyecto de ingeniería química no se limita a un mero desagüe, sino que constituye una infraestructura crítica de seguridad ambiental, contención de fugas y cumplimiento legal (\cite{UNE_EN_752, CTE_DB_HS5}).

\subsection{Topología Separativa Estricta en Plantas Químicas}
A diferencia de los edificios residenciales, una instalación industrial de proceso requiere la segregación física e hidráulica en un mínimo de cuatro subredes independientes:
\begin{enumerate}
    \item \textbf{Red de Fecales o Aguas Negras (R-FEC):} Procedente de vestuarios, comedores y aseos del personal. Se conduce directamente hacia la arqueta sifónica general de acometida al colector municipal, sin mezclarse previamente con efluentes de fabricación.
    \item \textbf{Red de Pluviales Limpias (R-PLU):} Recoge escorrentías de cubiertas de naves y viales perimetrales limpios sin riesgo de derrame químico. Puede conducirse a balsas de laminación o vertido directo a cauce/red municipal sin tratamiento previo intensivo.
    \item \textbf{Red de Pluviales Potencialmente Contaminadas (R-PLC):} Aguas de lluvia caídas sobre zonas de carga/descarga de cisternas, parques de tanques, áreas de proceso exterior y muelles. Obligatoriamente canalizadas hacia un sistema de retención de las primeras lluvias (primeros $15\text{--}20\,\text{mm}$ de precipitación) y enviadas a desarenador y \textbf{separador de hidrocarburos / decantador}.
    \item \textbf{Red de Vertidos Industriales de Proceso (R-IND):} Aguas procedentes de purgas de calderas, rechazos de ósmosis inversa, limpiezas CIP (\textit{Cleaning-in-Place}), condensados contaminados y condensadores barométricos. Estas aguas se canalizan mediante tuberías químicamente resistentes hacia la estación depuradora de aguas residuales industriales (\textbf{EDARI}) para su neutralización, coagulación-floculación y tratamiento biológico/químico antes de su vertido o reutilización.
\end{enumerate}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[node distance=1.1cm, auto,
    unidad/.style={rectangle, draw=blue!80!black, fill=blue!10, rounded corners=2pt, thick, text width=2.9cm, align=center, minimum height=0.9cm, font=\scriptsize},
    colector/.style={rectangle, draw=orange!90!black, fill=orange!15, thick, text width=2.8cm, align=center, minimum height=0.8cm, font=\scriptsize},
    trat/.style={rectangle, draw=purple!80!black, fill=purple!10, rounded corners=3pt, thick, text width=3.0cm, align=center, minimum height=0.9cm, font=\scriptsize},
    destino/.style={rectangle, draw=teal!90!black, fill=teal!20, rounded corners=4pt, line width=1pt, text width=3.2cm, align=center, minimum height=1.0cm, font=\small\bfseries},
    flecha/.style={draw=gray!80!black, -{Latex[length=2.3mm]}, thick}]
    
    % Unidades de origen
    \node [unidad] (cubiertas) {Cubiertas Naves\\(Pluviales limpias)};
    \node [unidad, below=0.6cm of cubiertas] (viales) {Zonas Carga / Viales\\(Pluviales contam.)};
    \node [unidad, below=0.6cm of viales] (edif) {Edificio Servicios\\(Aguas fecales)};
    \node [unidad, below=0.6cm of edif] (proceso) {Reactores / CIP / Purga\\(Vertido industrial)};
    
    % Elementos intermedios
    \node [colector, right=1.2cm of cubiertas] (arc_plu) {Arqueta de Paso\\(R-PLU)};
    \node [trat, right=1.2cm of viales] (sep_hid) {Separador de\\Hidrocarburos (SH)};
    \node [colector, right=1.2cm of edif] (arc_sif) {Arqueta Sifónica\\(R-FEC)};
    \node [trat, right=1.2cm of proceso] (edari) {EDARI Planta\\(Neutraliz. + Fis-Quím)};
    
    % Colector general y pozo de control
    \node [colector, right=1.3cm of sep_hid] (pozo_unif) {Pozo de Registro\\General de Planta};
    \node [trat, right=1.3cm of edari] (pozo_muestras) {Pozo Homologado\\Toma Muestras Oficial};
    
    % Destino final
    \node [destino, right=1.2cm of pozo_unif, yshift=-1.1cm] (emisor) {Colector Municipal o\\Cauce Receptor (DPH)};
    
    % Conexiones
    \path [flecha] (cubiertas) -- (arc_plu);
    \path [flecha] (viales) -- (sep_hid);
    \path [flecha] (edif) -- (arc_sif);
    \path [flecha] (proceso) -- (edari);
    
    \path [flecha] (arc_plu) -| (pozo_unif);
    \path [flecha] (sep_hid) -- (pozo_unif);
    \path [flecha] (arc_sif) -| (pozo_muestras);
    \path [flecha] (edari) -- (pozo_muestras);
    
    \path [flecha] (pozo_unif) -- (emisor);
    \path [flecha] (pozo_muestras) -- (emisor);
\end{tikzpicture}
\caption{Diagrama de bloques de la red separativa de saneamiento y tratamiento previo en un complejo de ingeniería química.}
\label{fig:diagrama_saneamiento_quimico}
\end{figure}

\subsection{Elementos Singulares de la Red de Evacuación}
Conforme a las prescripciones del CTE DB-HS 5 y la UNE-EN 752, toda red industrial debe estructurarse con los siguientes componentes normalizados:
\begin{itemize}
    \item \textbf{Arquetas a Pie de Bajante (APB):} Recogen las aguas verticales de bajantes pluviales o fecales con registro roscado hermético para desobstrucción, evitando uniones directas a $90^\circ$ en cimentación.
    \item \textbf{Arquetas de Paso (AP):} Dispositivos de entronque y cambio de dirección o sección en colectores enterrados. Su fondo debe estar acanalado con una pendiente mínima del $2.0\text{ \%}$ hacia la salida.
    \item \textbf{Arquetas Sifónicas (AS):} Dispositivos con cierre hidráulico permanente (altura de sello de agua $\ge 50\text{--}70\,\text{mm}$) instalados antes de acometer a la red general o municipal para evitar la propagación de gases mefíticos, sulfhídrico ($\text{H}_2\text{S}$) o vapores inflamables hacia el interior de las instalaciones.
    \item \textbf{Separadores de Grasas e Hidrocarburos (SH):} Equipos de retención gravimétrica dotados de filtro coalescente y válvula obturadora automática por flotador calibrado a densidad $0.85\,\text{g/cm}^3$. Según UNE-EN 858, deben retener hidrocarburos residuales por debajo de $5\,\text{mg/L}$ antes de dar salida al efluente.
    \item \textbf{Pozos de Registro (PR):} Elementos visitables instalados en tramos rectos a distancias del orden de $50\,\text{m}$, en quiebros angulares mayores de $45^\circ$, cambios de rasante o saltos de cota hidráulica ($> 0.80\,\text{m}$ con deflector). Cuentan con un diámetro interior mínimo de $\phi 1\,000\,\text{mm}$ y escalerilla de polipropileno reforzado con alma de acero.
    \item \textbf{Pozo Oficial de Control y Toma de Muestras:} Instalado en el límite perimetral de la parcela, previo a la válvula de retención de acometida municipal. Es de diseño homologado por la empresa explotadora del saneamiento o confederación hidrográfica, disponiendo de canaleta Venturi o vertedero Thompson con medidor ultrasónico de caudal y tomamuestras automático refrigerado continuo.
\end{itemize}

\subsection{Criterios Hidráulicos de Dimensionamiento y Materiales}
El trazado y cálculo de colectores en plantas químicas debe satisfacer:
\begin{itemize}
    \item \textbf{Pendiente de Conducciones:} Mínimo del $1.0\text{--}1.5\text{ \%}$ para colectores exteriores enterrados y del $2.0\text{ \%}$ para ramales secundarios interiores.
    \item \textbf{Velocidad de Autolimpieza y Erosión:} El régimen de flujo debe garantizar una velocidad de autolimpieza $v \ge 0.60\text{--}0.80\,\text{m/s}$ a un tercio del caudal nominal para impedir la sedimentación de arenas, y limitar la velocidad máxima a $v \le 3.0\text{--}4.0\,\text{m/s}$ para evitar el desgaste por abrasión.
    \item \textbf{Grado de Llenado:} Los colectores por gravedad no deben calcularse a sección llena continuada, adoptando una relación máxima de calado $y/D \le 0.70\text{--}0.75$ para asegurar la ventilación y renovación de la atmósfera interior del colector.
    \item \textbf{Selección de Materiales de Tubería:}
    \begin{itemize}
        \item \textbf{PVC-U Sanitario (color teja RAL 8023):} De rigidez anular SN4 o SN8 bajo norma UNE-EN 1401 para colectores enterrados generales de pluviales y fecales.
        \item \textbf{Polietileno de Alta Densidad (PEAD) Estructurado / Corrugado:} Excelente resistencia al impacto y asentamientos diferenciales del terreno.
        \item \textbf{Polipropileno (PP) o Acero Inoxidable AISI 316L / PVDF:} Obligatorio en colectores de efluentes de proceso industrial (R-IND) sometidos a temperaturas elevadas ($> 60\,^\circ\text{C}$) o agresividad química por pH ácido o disolventes orgánicos.
    \end{itemize}
\end{itemize}

\subsection{Simbología Normalizada y Representación Gráfica en Planos de Proyecto}
La elaboración de planos de saneamiento debe ajustarse a las normas de dibujo técnico vigentes y a los requisitos constructivos del CTE DB-HS 5 y de la UNE-EN 752 (\cite{CTE_DB_HS5, UNE_EN_752}):
\begin{itemize}
    \item \textbf{Acotación y tolerancias:} La UNE-EN ISO 129-1:2019 regula la indicación de dimensiones y tolerancias y sustituyó a la UNE 1039 (\cite{UNE_EN_ISO_129_1}). No define símbolos de instalaciones.
    \item \textbf{Símbolos de fontanería y saneamiento:} Las partes ISO 4067-1 e ISO 4067-6, históricas, fueron retiradas sin sustitución directa (\cite{ISO_4067_1, ISO_4067_6}). No hay un único conjunto de símbolos vigente para arquetas y pozos: en la práctica cada proyecto fija su propia leyenda, apoyándose p.\,ej. en la serie ISO 14617 (símbolos para esquemas) y en los detalles constructivos del CTE DB-HS 5.
\end{itemize}

Los símbolos y códigos de la Tabla~\ref{tab:simbologia_saneamiento} y de la Figura~\ref{fig:simbolos_graficos_saneamiento} son una convención de representación \textbf{propuesta para este trabajo}, de carácter ilustrativo: no proceden literalmente de ninguna norma y, en un proyecto real, deben definirse en la leyenda del plano.

\begin{table}[htbp]
\centering
\small
\renewcommand{\arraystretch}{1.25}
\begin{tabularx}{\textwidth}{p{2.8cm} c p{4.2cm} X}
\toprule
\textbf{Elemento / Red} & \textbf{Código} & \textbf{Representación propuesta} & \textbf{Función y Criterio Técnico} \\
\midrule
Colector Fecales & \textbf{R-FEC} & Línea de trazos continua marrón/roja & Evacuación aguas de aseos y sanitarios. Pendiente mín. $1.5\text{ \%}$. \\
Colector Pluviales & \textbf{R-PLU} & Línea de raya y punto azul/cian & Escorrentía de cubiertas y viales limpios hacia red exterior. \\
Colector Proceso & \textbf{R-IND} & Línea doble trazo o púrpura continua & Efluentes industriales hacia EDARI. Tubo resistente a corrosión. \\
Arqueta de Paso & \textbf{AP} & Cuadrado con cruz o diagonal interior & Registro y cambio de dirección. Tapa hermética registrable. \\
Arqueta Sifónica & \textbf{AS} & Cuadrado partido con línea curva central & Sello hidráulico ($h \ge 50\,\text{mm}$) contra gases y sulfhídrico. \\
Arqueta a Bajante & \textbf{APB} & Cuadrado con círculo céntrico interior & Recepción de bajante con registro roscado superior. \\
Separador Hidrocarb. & \textbf{SH} & Rectángulo dividido en 2 cámaras & Retención gravimétrica de aceites/grasas con filtro coalescente. \\
Pozo de Registro & \textbf{PR} & Doble círculo concéntrico con centro cruzado & Registro visitable exterior $\phi \ge 1\,000\,\text{mm}$ cada $50\,\text{m}$ o cambios de rasante. \\
Pozo Toma Muestras & \textbf{PTM} & Doble círculo con indicativo `M' interior & Punto oficial de inspección con aforador y tomamuestras refrigerado. \\
Acometida General & \textbf{ACO} & Flecha de conexión saliente hacia red vial & Enlace final con colector público con válvula de retención clapeta. \\
\bottomrule
\end{tabularx}
\caption{Convención de representación y codificación propuesta para planos de saneamiento industrial (ilustrativa, no normalizada).}
\label{tab:simbologia_saneamiento}
\end{table}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.95, every node/.style={transform shape}]
    % Estilo general
    \tikzset{
        simb/.style={draw=black, very thick, fill=white},
        etiq/.style={font=\scriptsize\bfseries, align=center, text=black!85},
        desc/.style={font=\tiny, text=gray!80!black, align=center}
    }
    
    % Fila 1: Redes y conducciones (trazos)
    % R-FEC
    \draw [red!75!black, very thick, dashed] (0, 3.8) -- (2.2, 3.8);
    \node [etiq, above] at (1.1, 3.8) {R-FEC};
    \node [desc, below] at (1.1, 3.7) {Aguas fecales};
    
    % R-PLU
    \draw [cyan!80!black, very thick, dash dot] (3.2, 3.8) -- (5.4, 3.8);
    \node [etiq, above] at (4.3, 3.8) {R-PLU};
    \node [desc, below] at (4.3, 3.7) {Pluviales limpias};
    
    % R-PLC
    \draw [blue!80!black, very thick, loosely dashed] (6.4, 3.8) -- (8.6, 3.8);
    \node [etiq, above] at (7.5, 3.8) {R-PLC};
    \node [desc, below] at (7.5, 3.7) {Pluviales contam.};
    
    % R-IND
    \draw [purple!80!black, very thick, double, double distance=1.2pt] (9.6, 3.8) -- (11.8, 3.8);
    \node [etiq, above] at (10.7, 3.8) {R-IND};
    \node [desc, below] at (10.7, 3.7) {Vertidos proceso};
    
    % Separador horizontal sutil
    \draw [gray!30, thin] (-0.5, 3.0) -- (12.3, 3.0);
    
    % Fila 2: Arquetas y elementos singulares
    % AP: Arqueta de paso
    \begin{scope}[shift={(0.8, 1.6)}]
        \draw [simb] (-0.5, -0.5) rectangle (0.5, 0.5);
        \draw [thick, black!70] (-0.5, -0.5) -- (0.5, 0.5);
        \draw [thick, black!70] (-0.5, 0.5) -- (0.5, -0.5);
        \node [etiq, below=0.6cm] at (0, 0) {AP};
        \node [desc, below=0.9cm] at (0, 0) {Arqueta de paso};
    \end{scope}
    
    % AS: Arqueta sifonica
    \begin{scope}[shift={(3.2, 1.6)}]
        \draw [simb] (-0.5, -0.5) rectangle (0.5, 0.5);
        \draw [thick, black!70] (-0.5, 0) -- (0.5, 0);
        \draw [thick, black!80] (0, 0) arc (180:360:0.25);
        \node [etiq, below=0.6cm] at (0, 0) {AS};
        \node [desc, below=0.9cm] at (0, 0) {Arqueta sifónica};
    \end{scope}
    
    % APB: Arqueta pie bajante
    \begin{scope}[shift={(5.6, 1.6)}]
        \draw [simb] (-0.5, -0.5) rectangle (0.5, 0.5);
        \draw [thick, black!80, fill=gray!20] (0, 0) circle (0.25);
        \fill [black] (0, 0) circle (0.07);
        \node [etiq, below=0.6cm] at (0, 0) {APB};
        \node [desc, below=0.9cm] at (0, 0) {Pie de bajante};
    \end{scope}
    
    % SH: Separador de hidrocarburos
    \begin{scope}[shift={(8.2, 1.6)}]
        \draw [simb] (-0.8, -0.45) rectangle (0.8, 0.45);
        \draw [thick, dashed, black!70] (0, -0.45) -- (0, 0.45);
        \draw [thick, black!80] (-0.4, 0.1) circle (0.12);
        \draw [thick, black!80, fill=black!40] (0.4, -0.1) circle (0.12);
        \node [etiq, below=0.6cm] at (0, 0) {SH};
        \node [desc, below=0.9cm] at (0, 0) {Sep. hidrocarburos};
    \end{scope}
    
    % PR: Pozo de registro
    \begin{scope}[shift={(10.8, 1.6)}]
        \draw [simb] (0, 0) circle (0.55);
        \draw [thick, black!70] (0, 0) circle (0.35);
        \draw [thick, black!60] (-0.25, 0) -- (0.25, 0);
        \draw [thick, black!60] (0, -0.25) -- (0, 0.25);
        \node [etiq, below=0.6cm] at (0, 0) {PR};
        \node [desc, below=0.9cm] at (0, 0) {Pozo de registro};
    \end{scope}
\end{tikzpicture}
\caption{Representación gráfica de la convención propuesta para conducciones, arquetas y pozos de saneamiento (ilustrativa, no normalizada).}
\label{fig:simbolos_graficos_saneamiento}
\end{figure}

\begin{tcolorbox}[colback=teal!5,colframe=teal!60!black,title=\textbf{Ejemplo de Aplicación en Proyecto Real: Planta de Proceso Industrial}]
En los proyectos de ejecución de instalaciones químicas (como en plantas de derivados petroquímicos o anhídrido maleico), los planos de la disciplina de obra civil e hidráulica integran de forma rigurosa esta jerarquía:
\begin{itemize}
    \item \textbf{Plano de Planta General de Saneamiento:} Representa toda la red perimetral de colectores con identificación exhaustiva de cada tramo: diámetro ($\phi$), longitud ($L$), material (PVC-U / PEAD), cota de rasante y cota de solera, pendiente calculada en milésimas ($i$) y número de arqueta o pozo de registro correlativo.
    \item \textbf{Plano de Detalles Constructivos de Redes:} Muestra secciones de arquetas de paso de fábrica o prefabricadas sobre solera de $15\,\text{cm}$, arquetas sifónicas con codo de $90^\circ$ sumergido y tapón roscado de latón, zanjas tipo con cama de arena de río de $10\text{--}15\,\text{cm}$ compactadas al $95\text{ \%}$ Proctor Modificado, y empalme mediante codo a $45^\circ$ en pozo de resalto municipal.
\end{itemize}
A continuación, se insertan en orientación apaisada los planos técnicos reales correspondientes a la planta general y al cuadro de detalles constructivos normalizados.
\end{tcolorbox}

\section{Planos Constructivos de Saneamiento en Proyecto Real}\label{sec:planos_reales}

Se incorporan los planos de saneamiento de un proyecto real de planta de anhídrido maleico (planos fechados en 2014) como ejemplo de organización geométrica y constructiva de una red industrial. Son anteriores a varias de las normas citadas en este capítulo (RD 3/2023, RD 487/2022, RD 665/2023, RD 1085/2024), por lo que no deben tomarse como referencia normativa ni de simbología vigente.

\begin{landscape}
\begin{figure}[p]
\centering
\includegraphics[width=0.95\linewidth,height=0.85\textheight,keepaspectratio]{Doc/Planos/plano_saneamiento_planta_land.png}
\caption{Plano de Planta General de la Red de Saneamiento Industrial: Colectores separativos de fecales, pluviales y vertidos de proceso, arquetas de paso, pozos de registro y acometida municipal.}
\label{fig:plano_general_saneamiento}
\end{figure}
\end{landscape}

\begin{landscape}
\begin{figure}[p]
\centering
\includegraphics[width=0.95\linewidth,height=0.85\textheight,keepaspectratio]{Doc/Planos/plano_saneamiento_detalles_land.png}
\caption{Plano de Detalles Constructivos de Redes de Saneamiento: Secciones de arqueta de paso, arqueta sifónica de cierre hidráulico, bajantes y entronque de acometida al pozo general de registro.}
\label{fig:plano_detalles_saneamiento}
\end{figure}
\end{landscape}

\section{Normativa Medioambiental e Hidráulica de Vertidos}

\subsection{Texto Refundido de la Ley de Aguas (RDL 1/2001 - TRLA) y Canon de Vertido}
El TRLA consagra en sus artículos 100 a 108 el principio de que todo vertido a aguas continentales requiere previa autorización administrativa otorgada por la Confederación Hidrográfica competente:
\begin{itemize}
    \item \textbf{Prohibición Absoluta de Contaminación:} Queda terminantemente prohibido el vertido directo o indirecto de sustancias susceptibles de degradar la calidad del medio hídrico superficial o subterráneo.
    \item \textbf{Cálculo del Canon de Control de Vertidos:} Conforme al art. 113 del TRLA, todo vertido autorizado devenga anualmente este tributo, liquidado según la fórmula oficial:
    \begin{equation}
        \text{Canon} = V \cdot P_{\text{base}} \cdot K_{\text{ind}}
    \end{equation}
    donde $V$ es el volumen anual de vertido, $P_{\text{base}}$ es el precio básico por metro cúbico fijado para vertidos industriales en el RDPH (art.~289) y $K_{\text{ind}}$ es un coeficiente que pondera la naturaleza y grado de contaminación del vertido y la calidad del medio receptor (\cite{TRLA2001, RDPH1986}).
\end{itemize}

\subsection{Reglamento del Dominio Público Hidráulico (RD 849/1986 y RD 665/2023)}
La reforma del RDPH consolidada por el \textbf{Real Decreto 665/2023} ha elevado sensiblemente las exigencias técnicas aplicables a las plantas químicas e industriales:
\begin{itemize}
    \item \textbf{Límites de vertido:} Los valores límite de emisión no son una tabla general del RDPH: se fijan caso por caso en la autorización de vertido del organismo de cuenca, atendiendo a las mejores técnicas disponibles (\cite{CWW_BREF_2016}) y a los objetivos de calidad del medio receptor (\cite{TRLA2001, RDPH1986}).
    \item \textbf{Protección de aguas subterráneas frente a contaminación puntual:} La reforma incorpora valores de referencia para aguas subterráneas y, si se superan, exige un Análisis Cuantitativo de Riesgos (ACR) que determine las medidas correctoras. Para una planta química esto obliga a justificar la contención de derrames y a prever controles piezométricos; el articulado concreto debe consultarse en el texto consolidado del RDPH (\cite{RDPH1986}).
    \item \textbf{Perímetros de protección:} El RDPH regula la delimitación de perímetros de protección de captaciones de agua subterránea destinadas a consumo humano. Si la planta se abastece de un pozo propio para uso industrial, esta obligación no se aplica automáticamente, pero la concesión y la ubicación del pozo deben evaluarse frente a los perímetros existentes en la zona (\cite{RDPH1986}).
\end{itemize}

\subsection{Real Decreto 1085/2024: Reutilización de Aguas Regeneradas}
Aprobado el 22 de octubre de 2024, este reglamento sustituye al RD 1620/2007 y adapta la normativa española al Reglamento (UE) 2020/741 (\cite{RD1085_2024}). Para un proyecto industrial interesa lo siguiente:
\begin{itemize}
    \item \textbf{Calidad según el uso:} El reglamento define clases de calidad y requisitos por uso (incluidos usos industriales como procesos, limpieza y refrigeración); la clase y los parámetros concretos deben tomarse de sus anexos.
    \item \textbf{Refrigeración:} Si el agua regenerada alimenta torres o condensadores evaporativos, se aplica además el RD 487/2022 (\cite{RD487_2022}).
    \item \textbf{Plan de Gestión del Riesgo del Agua Regenerada (PGRAR):} Instrumento de análisis de peligros y puntos de control que acompaña a la solicitud de concesión de agua regenerada.
    \item \textbf{Alcance:} La regeneración no afecta solo a la depuradora: el reglamento regula el suministro y uso del agua regenerada. Queda fuera de su ámbito la recirculación interna de agua dentro de los procesos de una misma industria.
\end{itemize}

\subsection{Directiva (UE) 2024/3019: Tratamiento Cuaternario y Responsabilidad Ampliada (RAP)}
La Directiva (UE) 2024/3019, que refunde el marco europeo de tratamiento de aguas residuales urbanas, introduce dos novedades con efecto indirecto sobre la industria química (por sus vertidos a redes urbanas) (\cite{DirectivaUE_2024_3019}):
\begin{itemize}
    \item \textbf{Tratamiento cuaternario:} Las depuradoras urbanas de mayor tamaño (y otras en zonas sensibles) deben eliminar microcontaminantes (fármacos, tensioactivos, disruptores endocrinos, etc.) mediante procesos como oxidación avanzada o adsorción en carbón activo.
    \item \textbf{Responsabilidad ampliada del productor:} Los productores de sectores identificados como principales fuentes de microcontaminantes (en particular farmacéutico y cosmético) deben sufragar como mínimo el $80\text{ \%}$ del coste adicional del tratamiento cuaternario.
\end{itemize}

\subsection{Huella Hídrica y Ecoeficiencia según Norma UNE-EN ISO 14046}
La norma internacional \textbf{UNE-EN ISO 14046} define los principios de evaluación del ciclo de vida (ACV) aplicados al uso del agua en plantas industriales. En la ingeniería de detalle del proyecto se cuantifican:
\begin{equation}
    \text{HH}_{\text{total}} = \text{HH}_{\text{azul}} + \text{HH}_{\text{verde}} + \text{HH}_{\text{gris}}
\end{equation}
donde la \textbf{Huella Azul} mide el volumen consumido de recursos hídricos de la red o acuífero evaporado o incorporado al producto; la \textbf{Huella Verde} corresponde al agua de lluvia almacenada; y la \textbf{Huella Gris} representa el volumen teórico de agua limpia necesario para asimilar la carga contaminante de los efluentes vertidos hasta alcanzar los estándares de calidad del cauce receptor.

\subsection{Conclusiones Normativas para el Proyecto de Ingeniería}
El cumplimiento integrado de esta arquitectura jurídica y técnica impone en la memoria, pliego y planos del proyecto:
\begin{enumerate}
    \item La justificación técnica formal de la no toxicidad de los materiales en contacto con agua potable (RD 3/2023).
    \item El dimensionamiento higiénico de las torres y balsas de refrigeración según el PPCL exigido por el RD 487/2022.
    \item La segregación y modelado hidráulico estricto de las 4 redes de saneamiento (fecales, pluviales limpias, pluviales contaminadas y vertidos de proceso), reflejando con exactitud la simbología normalizada de arquetas, separadores y pozos (CTE DB-HS 5, UNE-EN 752, UNE-EN ISO 129-1:2019).
    \item La instalación perimetral de un pozo oficial homologado de control y aforo continuo de vertidos para la supervisión ambiental por la administración hidráulica (TRLA / RDPH).
\end{enumerate}
'''

wrapped_ch1_to_4 = '%\n% ==========================================================================\n% CAPITULOS 1 AL 4 COMENTADOS TEMPORALMENTE (PRESERVADOS PARA CONSULTA)\n% ==========================================================================\n\\iffalse\n' + ch1_to_4 + '\n\\fi\n'

wrapped_ch6 = '%\n% ==========================================================================\n% CAPITULO 6 COMENTADO TEMPORALMENTE (PRESERVADO PARA CONSULTA)\n% ==========================================================================\n\\iffalse\n' + ch6 + '\n\\fi\n'

full_doc = preamble + '\n' + wrapped_ch1_to_4 + '\n' + new_ch5_content + '\n\n' + wrapped_ch6 + '\n' + bib_and_end

target_path = 'grupo5_servicios_basicos_agua.tex'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_doc)

print('Updated build_doc.py and wrote grupo5_servicios_basicos_agua.tex successfully.')
