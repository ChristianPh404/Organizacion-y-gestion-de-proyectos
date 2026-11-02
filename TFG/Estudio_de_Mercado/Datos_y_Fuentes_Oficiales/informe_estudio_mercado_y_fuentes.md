# AUDITORÍA Y TRAZABILIDAD COMPLETA DEL ESTUDIO DE MERCADO Y CAPACIDAD (CERO ALUCINACIONES)

**Proyecto:** Biorrefinería de Hueso de Aceituna y Poda de Olivo (`estudio_mercado2.tex` / `estudio_mercado2.pdf`)  
**Documento nº 1:** Estudio de Mercado y Capacidad  
**Autor:** Christian Pérez Hita (Grado / Máster en Ingeniería Química — Universidad de Granada)  
**Asignatura:** Organización y Gestión de Proyectos (OGP)  
**Última actualización:** Octubre 2026  

---

> [!NOTE]
> **Estructura para la 1ª Entrega (Estudio de Mercado y Capacidad):**  
> Siguiendo los ejemplos de la asignatura ([OGP_Seminario Estudio de mercado_26-27.pdf](file:///F:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/Documentacion_y_Temario/Temario/OGP_Seminario%20Estudio%20de%20mercado_26-27.pdf) y [estudio de mercado de confiterias.pdf](file:///F:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/Documentacion_y_Temario/Temario/Ejemplos/estudio%20de%20mercado%20de%20confiterias.pdf)), el documento se centra en **Materia Prima**, **Producto**, **Oferta y Competencia** (incluyendo el censo de almazaras de [aceite.xls](file:///F:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/Datos_y_Fuentes_Oficiales/aceite.xls)), **Demanda (CNA)**, **Modelos econométricos (Jackson-Black y Massey-Black)**, **Estudio de Capacidad y Dimensionamiento** y **Esquema de Procesos**.  
> Las secciones de **Macrolocalización y Microlocalización** quedan comentadas en LaTeX y reservadas para la 2ª entrega (*Estudio de Localización*).

---

## 1. ¿Qué significa «Considerando (8), p. 2» en las citas?

En los textos legislativos oficiales de la Unión Europea (publicados en el **DOUE**, Diario Oficial de la Unión Europea, como tu archivo local [L00001-00004.pdf](file:///F:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/Datos_y_Fuentes_Oficiales/L00001-00004.pdf)):

1. **Estructura formal de un Reglamento o Directiva europea:**  
   Todo reglamento de la UE consta de dos partes:
   * **La Exposición de Motivos (Preámbulo):** Comienza con la frase *«Visto el Tratado... Considerando lo siguiente:»*. A continuación vienen párrafos numerados entre paréntesis: **(1), (2), (3)... (8)... (11)...**, que se denominan jurídicamente **Considerandos** (*Recitals* en inglés). En ellos, la Comisión Europea expone los hechos probados, datos del mercado e investigaciones estadísticas que motivan la ley.
   * **La Parte Dispositiva:** Los artículos propiamente dichos (*Artículo 1, Artículo 2...*).
2. **Qué dice exactamente cada «Considerando» citado en tu PDF [L00001-00004.pdf](file:///F:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/Datos_y_Fuentes_Oficiales/L00001-00004.pdf):**
   * **Considerando (5) (pág. 1):** Certifica que las importaciones de etanol en la UE crecieron un **55%** entre 2023 y 2025 (de **621.954 t** a **967.354 t**).
   * **Considerando (8) (pág. 2):** Reporta literalmente que el precio medio de importación en la UE cayó de **1.014 €/t** (en 2023) a **816 €/t** (en 2025). Indica que la importación de EE.UU. cayó de **932 €/t** (en 2024) a **752 €/t** (en 2025), manteniéndose un **16% por debajo del precio de venta de los productores de la UE**.
   * **Considerando (11) (pág. 2):** Certifica que la presión de las importaciones baratas provocó una **caída del 21% en los precios de venta de la industria de la Unión Europea** entre 2023 y 2025.
   * **Cuadro 1 y Nota al pie (7) (pág. 2):** Registra que en 2025 la producción de la UE fue de **4.498.816 t**, el consumo de **4.987.906 t** y la capacidad instalada de **5.319.898 t**.

Por eso, citar **«Considerando (8), p. 2»** es la forma académica y jurídica más precisa de citar una ley europea: cualquier profesor o evaluador que abra [L00001-00004.pdf](file:///F:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/Datos_y_Fuentes_Oficiales/L00001-00004.pdf) en la página 2 va directamente al párrafo `(8)` y encuentra de inmediato los 1.014 €, 816 €, 932 € y 752 €.

---

## 2. Incorporación de los Datos Reales de SABI (`aceite.xls`) en el Estudio de la Oferta

En cumplimiento del temario de OGP (diapositivas 18–20 del *Seminario Estudio de Mercado*), se ha incorporado el análisis censal de tu fichero [aceite.xls](file:///F:/universidad/4º/proyectos/Organizacion%20y%20gestion%20de%20proyectos/TFG/Estudio_de_Mercado/Datos_y_Fuentes_Oficiales/aceite.xls) en el **Capítulo 4 (Análisis de la Oferta y la Competencia)**:

* **Muestra total exportada:** **202 empresas** con unos ingresos de explotación agregados de **851,24 M€**.
* **Distribución territorial:**
  * **Córdoba (21 empresas):** **552,72 M€** (**64,9%** del total de la muestra). Concentra los mayores grupos almazareros, destacando *Sdad. Coop. And. Almazaras de la Subbética* (219,86 M€ en Carcabuey), *Almazara Adamuz S.L.* (112,46 M€), *Almazaras de la Subbética S.L.* (71,65 M€), *Aceites Simón Rosa S.L.* (64,39 M€ en Montoro) y *Almazara de Muela S.L.* (25,74 M€ en Priego).
  * **Ciudad Real (7 empresas):** **102,77 M€** (12,1%), liderada por *Virgen de las Viñas Bodega y Almazara* (95,50 M€).
  * **Jaén (22 empresas):** **72,65 M€** (8,5%), encabezada por *Almazara La Loma S.L.* (29,80 M€ en Canena), *Almazara La Andaluza S.L.* (12,29 M€ en Pozo Alcón), *Almazara Jiménez S.L.* (11,62 M€ en Los Villares) y *Almazara Cruz de Esteban S.L.* (11,38 M€ en Mancha Real).
  * **Granada (9 empresas):** **14,56 M€** (1,7%), liderada por *Almazara de Montillana S. Coop.* (9,42 M€) y *Almazara La Ribera S.L.* (3,05 M€).
  * **Otras provincias (143 empresas):** 108,54 M€ (12,8%).

Esta tabla demuestra cuantitativamente que el eje provincial posee centros de molienda de enorme volumen capaces de suministrar contratos plurianuales de hueso de aceituna sin depender de cientos de pequeños intermediarios.

---

## 3. Estado de Capítulos en `estudio_mercado2.tex` (para la 1ª Entrega)

| Capítulo | Título | Estado en el PDF |
| :--- | :--- | :--- |
| **Capítulo 1** | Introducción, Marco del Proyecto y Metodología | **Activo** (adaptado a *Documento nº 1: Estudio de Mercado y Capacidad*) |
| **Capítulo 2** | Disponibilidad Cuantitativa de Materia Prima: Hueso y Poda | **Activo** (superficies MAPA 2025, molturación AICA 2025/26 e índices de poda CAP 2008) |
| **Capítulo 3** | Estudio de Materias Primas, Productos y Marco Regulatorio | **Activo** (composición química, especificaciones EN 15376 y normativas RED III / RD 611/2026) |
| **Capítulo 4** | Análisis de la Oferta y la Competencia | **Activo** (plantas 1G de Vertex MITECO, informe MIEA 2026 **+ Censo SABI `aceite.xls`**) |
| **Capítulo 5** | Análisis de la Demanda y Consumo Nacional Aparente | **Activo** (serie histórica física MITECO 2017–2025 y mercado comunitario DOUE) |
| **Capítulo 6** | Estimación de Demanda, Ventas y Precios (Modelos OGP) | **Activo** (Jackson-Black 2017–2025 y modelos emparejados 2023–2025 con precios auditados DOUE) |
| **Capítulo 7** | Estudio de Capacidad y Dimensionamiento de la Planta Industrial | **Activo** (Escenarios B-1 a B-5, umbral $C_{\min} = \SI{30000}{t/año}$, escala \SI{45000}{t/año}, consumos de reactivos y facturación) |
| *(Localización)* | *Prospección Comarcal SABI, Matriz de Ponderación y Brown-Gibson* | **Comentado con `%`** (reservado para la 2ª entrega *Documento nº 2: Localización*) |
| **Capítulo 8** | Esquema General de Procesos e Integración | **Activo** (Diagrama de bloques TikZ y síntesis de equipos de ingeniería) |
| **Capítulo 9** | Conclusiones del Estudio de Mercado | **Activo** (5 conclusiones cuantitativas alineadas con la entrega de mercado y capacidad) |
