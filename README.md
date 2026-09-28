# 📚 Organización y Gestión de Proyectos

Repositorio de apuntes, informes y casos prácticos para la asignatura de **Organización y Gestión de Proyectos** (4º Grado en Ingeniería Química / Industrial).

---

## 📁 Estructura del Repositorio

- `apuntes.tex`: Archivo principal compilable del libro de apuntes.
- `planta_stevia.tex`: Documento individual del caso práctico de la planta de Stevia.
- `preamble.tex`: Configuración de paquetes, cajas `tcolorbox`, tipografías y márgenes.
- `macros.tex` / `letterfonts.tex`: Comandos y tipografías matemáticas personalizadas.
- `Capitulos/`:
  - `planta_stevia.tex`: Capítulo con el diseño organizativo completo (31 trabajadores), definición detallada de puestos, formación, funciones y organigrama en TikZ.
- `Imagenes/`: Directorio para esquemas, gráficos y figuras.

---

## 🌿 Caso Práctico: Planta Industrial de Producción de Stevia

Diseño de la estructura organizativa de una empresa industrial de 31 trabajadores dedicada a la extracción y purificación de glucósidos de esteviol:

1. **A. Dirección y Gerencia (2 personas):** Director/a General y Director/a de Planta.
2. **B. Departamento de Producción (10 personas):** Jefe de producción, 2 supervisores de turno, 6 operadores de planta y responsable de almacén.
3. **C. Ingeniería y Mantenimiento (4 personas):** Ingeniero/a de procesos, Ingeniero/a de proyectos y 2 técnicos de mantenimiento electromecánico.
4. **D. Calidad e I+D+i (5 personas):** Responsable de calidad alimentaria, 2 técnicos de laboratorio HPLC, Ingeniero/a de I+D y técnico de asuntos regulatorios.
5. **E. Seguridad y Medio Ambiente - HSE (2 personas):** Responsable HSE/PRL y técnico medioambiental.
6. **F. Compras y Aprovisionamiento Agrícola (3 personas):** Responsable de compras, responsable de aprovisionamiento de hoja agrícola y técnico logístico.
7. **G. Administración, RRHH y Comercial (5 personas):** 2 en administración/finanzas, 1 en RRHH y 2 técnicos comerciales B2B.

---

## 🛠️ Compilación en LaTeX

Para compilar el documento completo:
```bash
pdflatex -shell-escape apuntes.tex
# o para compilar el caso suelto:
pdflatex planta_stevia.tex
```