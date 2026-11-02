import re

path = r'f:\universidad\4º\proyectos\Organizacion y gestion de proyectos\TFG\Estudio_de_Mercado\estudio_mercado2.tex'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. TABLE 2.5
old_t25 = r'''\begin{table}[H]
    \centering
    \caption{Distribución mensual oficial de la aceituna molturada en Córdoba, Granada y Jaén (Campaña 2025/2026) y generación síncrona de hueso total y hoja limpia de almazara en base seca. Fuente primaria de molturación: AICA \autocite{AICA2026}.}
    \adjustbox{max width=0.99\textwidth}{%
        \renewcommand{\arraystretch}{1.2}
        \begin{tabular}{l r r r r c r r}
            \toprule
            \textbf{Mes}       & \textbf{Córdoba (t)} & \textbf{Granada (t)} & \textbf{Jaén (t)} & \textbf{Total Eje (t)} & \textbf{Cuota Mensual} & \textbf{Hueso Gen. (t b.s.)} & \textbf{Hoja Almazara (t b.s.)} \\'''

new_t25 = r'''\begin{table}[H]
    \centering
    \caption{Distribución mensual oficial de la aceituna molturada en Córdoba, Granada y Jaén (Campaña 2025/2026) y generación síncrona de hueso total y hoja limpia de almazara en base seca. Fuente primaria de molturación: AICA \autocite{AICA2026}.}
    \adjustbox{max width=\textwidth}{%
        \renewcommand{\arraystretch}{1.24}
        \setlength{\tabcolsep}{4pt}
        \small
        \begin{tabular}{l r r r r c r r}
            \toprule
            \textbf{Mes}       & \textbf{\shortstack{Córdoba\\(t)}} & \textbf{\shortstack{Granada\\(t)}} & \textbf{\shortstack{Jaén\\(t)}} & \textbf{\shortstack{Total Eje\\(t)}} & \textbf{\shortstack{Cuota\\(\%)}} & \textbf{\shortstack{Hueso Gen.\\(t b.s.)}} & \textbf{\shortstack{Hoja Alm.\\(t b.s.)}} \\'''

# 2. TABLE 2.6
old_t26 = r'''\begin{table}[H]
    \centering
    \caption{Calendario mensual de recepción (acopio), alimentación a reactores (\SI{15.00}{\tonne\text{~b.s.}/\hour}) e inventario de almacenamiento a fin de mes en base seca (t b.s.) para \SI{8000}{\hour/a\text{\~{n}}o} con régimen secuencial de recurso único y paradas en agosto, noviembre y diciembre (Stock inicial enlace fin de septiembre: \num{11500}~t b.s. de hueso).}
    \adjustbox{max width=0.99\textwidth}{%
        \renewcommand{\arraystretch}{1.28}
        \small
        \begin{tabular}{l c | r r r | r r r r | r r r r}
            \toprule
            \multirow{2}{*}{\textbf{Mes}} & \multirow{2}{*}{\textbf{Horas}} & \multicolumn{3}{c|}{\textbf{Acopio Recibido (t b.s.)}} & \multicolumn{4}{c|}{\textbf{Alimentación Consecutiva (t b.s.)}} & \multicolumn{4}{c}{\textbf{Inventario Fin de Mes (t b.s.)}} \\
                                          &                                 & Hueso    & Hoja     & Madera   & Hueso    & Hoja     & Madera   & \textbf{Total}   & Hueso    & Hoja     & Madera   & \textbf{Stock Tot.} \\'''

new_t26 = r'''\begin{table}[H]
    \centering
    \caption{Calendario mensual de recepción (acopio), alimentación a reactores (\SI{15.00}{\tonne\text{~b.s.}/\hour}) e inventario de almacenamiento a fin de mes en base seca (t b.s.) para \SI{8000}{\hour/a\text{\~{n}}o} con régimen secuencial de recurso único y paradas en agosto, noviembre y diciembre (Stock inicial enlace fin de septiembre: \num{11500}~t b.s. de hueso).}
    \adjustbox{max width=\textwidth}{%
        \renewcommand{\arraystretch}{1.22}
        \setlength{\tabcolsep}{2.8pt}
        \footnotesize
        \begin{tabular}{l c | r r r | r r r r | r r r r}
            \toprule
            \multirow{2}{*}{\textbf{Mes}} & \multirow{2}{*}{\textbf{Horas}} & \multicolumn{3}{c|}{\textbf{Acopio (t b.s.)}} & \multicolumn{4}{c|}{\textbf{Alimentación Consecutiva (t b.s.)}} & \multicolumn{4}{c}{\textbf{Inventario Fin de Mes (t b.s.)}} \\
                                          &                                 & Hueso    & Hoja     & Madera   & Hueso    & Hoja     & Madera   & \textbf{Total}   & Hueso    & Hoja     & Madera   & \textbf{Total} \\'''

# 3. TABLE 6.2 (Table 11)
old_t11 = r'''\begin{table}[H]
    \centering
    \caption{Modelos emparejados de Jackson-Black ($Q$ en kt) y Massey-Black ($V$ en M€) en el trienio 2023--2025 con precios oficiales del Reglamento (UE) 2026/2047 \autocite[Considerandos~8 y~11]{DOUE2026} y volúmenes CNA de \textcite[Hoja~\texttt{Balance bioetanol}]{MITECO2026}.}
    \adjustbox{max width=0.99\textwidth}{%
        \renewcommand{\arraystretch}{1.24}
        \begin{tabular}{c c | c c | c c c | c c c}
            \toprule
            \multirow{2}{*}{\textbf{Año}} & \multirow{2}{*}{\textbf{$t$}} & \multicolumn{2}{c|}{\textbf{Jackson-Black (kt)}} & \multicolumn{3}{c|}{\textbf{Massey-Black Serie A (Import.)}} & \multicolumn{3}{c}{\textbf{Massey-Black Serie B (Venta UE)}} \\
                                          &                                & Real $Q_t$ & Pred.\ $\hat{Q}_t$  & Precio (€/t) & Real $V_{A,t}$ & Pred.\ $\hat{V}_{A,t}$ & Precio (€/t) & Real $V_{B,t}$ & Pred.\ $\hat{V}_{B,t}$ \\'''

new_t11 = r'''\begin{table}[H]
    \centering
    \caption{Modelos emparejados de Jackson-Black ($Q$ en kt) y Massey-Black ($V$ en M€) en el trienio 2023--2025 con precios oficiales del Reglamento (UE) 2026/2047 \autocite[Considerandos~8 y~11]{DOUE2026} y volúmenes CNA del MITECO \autocite{MITECO2026}.}
    \adjustbox{max width=\textwidth}{%
        \renewcommand{\arraystretch}{1.24}
        \setlength{\tabcolsep}{3.2pt}
        \small
        \begin{tabular}{c c | c c | c c c | c c c}
            \toprule
            \multirow{2}{*}{\textbf{Año}} & \multirow{2}{*}{\textbf{$t$}} & \multicolumn{2}{c|}{\textbf{Jackson-Black (kt)}} & \multicolumn{3}{c|}{\textbf{Massey-Black A (Import.)}} & \multicolumn{3}{c}{\textbf{Massey-Black B (Venta UE)}} \\
                                          &                                & Real $Q_t$ & \shortstack{Pred.\\$\hat{Q}_t$}  & \shortstack{Precio\\(€/t)} & \shortstack{Real\\$V_{A,t}$} & \shortstack{Pred.\\$\hat{V}_{A,t}$} & \shortstack{Precio\\(€/t)} & \shortstack{Real\\$V_{B,t}$} & \shortstack{Pred.\\$\hat{V}_{B,t}$} \\'''

# 4. TABLE 7.1 (Table 12)
old_t12 = r'''\begin{table}[H]
    \centering
    \caption{Comparativa de flujos anuales en base seca entre los escenarios B-1 a B-5 de \textcite[Tabla~8 y Tabla~13]{Jafari-Gohargan2026} y el escenario seleccionado de proyecto $\text{B-5}^*$ (excluyendo orujo desalperujado B-3).}
    \adjustbox{max width=0.99\textwidth}{%
        \renewcommand{\arraystretch}{1.24}
        \begin{tabular}{l r r r r r r r c}
            \toprule
            \textbf{Escenario}                    & \textbf{Biomasa (t/a)} & \textbf{Etanol (t/a)} & \textbf{Lignina Pura (t/a)} & \textbf{Rich-Lignin (t/a)} & \textbf{$\text{CO}_2$ (t/a)} & \textbf{Biogás ($\text{m}^3$/a)} & \textbf{Fertiliz. (t/a)} & \textbf{$C_{\text{mín}}$ Viable} \\'''

new_t12 = r'''\begin{table}[H]
    \centering
    \caption{Comparativa de flujos anuales en base seca entre los escenarios B-1 a B-5 de \textcite[Tabla~8 y Tabla~13]{Jafari-Gohargan2026} y el escenario seleccionado de proyecto $\text{B-5}^*$ (excluyendo orujo desalperujado B-3).}
    \adjustbox{max width=\textwidth}{%
        \renewcommand{\arraystretch}{1.24}
        \setlength{\tabcolsep}{3.5pt}
        \small
        \begin{tabular}{l r r r r r r r c}
            \toprule
            \textbf{Escenario}                    & \textbf{\shortstack{Biomasa\\(t/a)}} & \textbf{\shortstack{Etanol\\(t/a)}} & \textbf{\shortstack{Lignina P.\\(t/a)}} & \textbf{\shortstack{Rich-Lig.\\(t/a)}} & \textbf{\shortstack{$\text{CO}_2$\\(t/a)}} & \textbf{\shortstack{Biogás\\($\text{m}^3$/a)}} & \textbf{\shortstack{Fertiliz.\\(t/a)}} & \textbf{\shortstack{$C_{\text{mín}}$\\Viable}} \\'''

# 5. TABLE 7.3 (Table 14)
old_t14 = r'''\begin{table}[H]
    \centering
    \caption{Caudales horarios nominales por campaña estacional (alimentación fija de \SI{15000}{\kilo\gram\text{ b.s.}/\hour}) y caudal envolvente máximo ($Q_{\text{máx}}$) para el cálculo y dimensionamiento de los equipos de planta. Deducido de \textcite[Tabla~8]{Jafari-Gohargan2026}.}
    \adjustbox{max width=0.99\textwidth}{%
        \renewcommand{\arraystretch}{1.25}
        \begin{tabular}{l r r r r | r l}
            \toprule
            \textbf{Corriente / Variable de Diseño}     & \textbf{Camp.\ Hueso} & \textbf{Camp.\ Hoja} & \textbf{Camp.\ Madera} & \textbf{Media Anual} & \textbf{Envolvente $Q_{\text{máx}}$} & \textbf{Equipo Crítico Gobernado} \\
            \textit{Duración efectiva en \SI{8000}{\hour/a}} & (\SI{1000.0}{\hour})  & (\SI{2666.7}{\hour}) & (\SI{4333.3}{\hour})   & (\SI{8000.0}{\hour}) & \textit{(Base diseño)}               &                                   \\'''

new_t14 = r'''\begin{table}[H]
    \centering
    \caption{Caudales horarios nominales por campaña estacional (alimentación fija de \SI{15000}{\kilo\gram\text{ b.s.}/\hour}) y caudal envolvente máximo ($Q_{\text{máx}}$) para el cálculo y dimensionamiento de los equipos de planta. Deducido de \textcite[Tabla~8]{Jafari-Gohargan2026}.}
    \adjustbox{max width=\textwidth}{%
        \renewcommand{\arraystretch}{1.24}
        \setlength{\tabcolsep}{3.8pt}
        \small
        \begin{tabular}{l r r r r | r l}
            \toprule
            \textbf{Corriente / Variable de Diseño}     & \textbf{\shortstack{Camp.\\Hueso}} & \textbf{\shortstack{Camp.\\Hoja}} & \textbf{\shortstack{Camp.\\Madera}} & \textbf{\shortstack{Media\\Anual}} & \textbf{\shortstack{Envolvente\\$Q_{\text{máx}}$}} & \textbf{Equipo Crítico Gobernado} \\
            \textit{Duración efectiva en \SI{8000}{\hour/a}} & (\SI{1000}{\hour})  & (\SI{2667}{\hour}) & (\SI{4333}{\hour})   & (\SI{8000}{\hour}) & \textit{(Base diseño)}               &                                   \\'''

for name, old_s, new_s in [('T25', old_t25, new_t25),
                            ('T26', old_t26, new_t26),
                            ('T11', old_t11, new_t11),
                            ('T12', old_t12, new_t12),
                            ('T14', old_t14, new_t14)]:
    if old_s in text:
        text = text.replace(old_s, new_s)
        print(f'{name} replaced successfully!')
    else:
        print(f'{name} NOT matched!')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
