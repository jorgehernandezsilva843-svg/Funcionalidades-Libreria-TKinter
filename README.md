# 🐍 Guía Práctica y Referencia de Tkinter en Python

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![GUI Toolkit](https://img.shields.io/badge/GUI-Tkinter-brightgreen)
![Status](https://img.shields.io/badge/Status-Completo%20y%20Educativo-success)
![License](https://img.shields.io/badge/Licencia-MIT-orange)

Bienvenido a este repositorio diseñado como un **manual práctico, modular y progresivo de la biblioteca `tkinter` en Python**. 

Contiene **15 scripts independientes**, cada uno enfocado en una funcionalidad específica del desarrollo de interfaces gráficas de escritorio, más un **lanzador interactivo central** (`main_hub.py`) para probar todos los módulos con un solo clic.

---

## 📋 Tabla de Contenido

- [Requisitos Previos](#-requisitos-previos)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Lanzador Rápido (`main_hub.py`)](#-lanzador-rápido-main_hubpy)
- [Explicación Detallada de los 15 Archivos](#-explicación-detallada-de-los-15-archivos)
  - [01. Ventana Principal y Etiquetas](#01_ventana_y_etiquetaspy)
  - [02. Botones y Manejo de Eventos](#02_botones_y_eventospy)
  - [03. Entradas de Texto y Variables](#03_entradas_textopy)
  - [04. Gestores de Posicionamiento (Layouts)](#04_administradores_layoutpy)
  - [05. Casillas y Botones de Opción](#05_checks_y_radiospy)
  - [06. Listas de Elementos y Scrollbar](#06_listbox_y_scrollbarpy)
  - [07. Menús Desplegables y Selectores Numéricos](#07_combobox_y_spinboxpy)
  - [08. Editor de Texto Multilínea](#08_texto_multilineapy)
  - [09. Diálogos Modales y Manejo de Archivos](#09_dialogos_y_archivospy)
  - [10. Barra de Menú y Menú Contextual](#10_menus_y_contextualpy)
  - [11. Lienzo Gráfico Vectorial (Canvas)](#11_canvas_graficospy)
  - [12. Pestañas de Navegación (Notebook)](#12_pestanas_notebookpy)
  - [13. Tablas Estructuradas (Treeview)](#13_tablas_treeviewpy)
  - [14. Barras de Progreso y Sliders](#14_progreso_y_sliderspy)
  - [15. Temas y Estilos Modernos (ttk.Style)](#15_estilos_y_temas_ttkpy)
- [Cómo Subir este Proyecto a GitHub](#-cómo-subir-este-proyecto-a-github)
- [Licencia](#-licencia)

---

## 💻 Requisitos Previos

`tkinter` viene incluido de forma nativa con la mayoría de instalaciones de Python en Windows, macOS y Linux.

Para verificar que dispones de Python y Tkinter, abre tu terminal y ejecuta:

```powershell
# En Windows (usando el lanzador de Python):
py -c "import tkinter; print('Tkinter versión:', tkinter.TkVersion)"

# O en Linux / macOS:
python3 -c "import tkinter; print('Tkinter versión:', tkinter.TkVersion)"
```

Si muestra una versión como `8.6`, ¡todo está listo!

---

## 📁 Estructura del Repositorio

```text
Libreria TKinter/
│
├── .gitignore                    # Exclusión de archivos generados y temporales
├── README.md                     # Documentación completa y guía de uso
├── main_hub.py                   # Panel interactivo visual para ejecutar cualquier script
│
├── 01_ventana_y_etiquetas.py     # Ventana básica, dimensiones y etiquetas (tk.Label)
├── 02_botones_y_eventos.py       # Botones, callbacks, funciones lambda y eventos .bind()
├── 03_entradas_texto.py          # Cajas de texto Entry, StringVar y modo contraseña
├── 04_administradores_layout.py  # Comparativa visual de pack(), grid() y place()
├── 05_checks_y_radios.py         # Casillas Checkbutton y opciones Radiobutton
├── 06_listbox_y_scrollbar.py     # Listbox con selección múltiple y scroll vertical
├── 07_combobox_y_spinbox.py      # ttk.Combobox desplegable y ttk.Spinbox numérico
├── 08_texto_multilinea.py        # Widget Text con etiquetas de estilo (tags) y contador
├── 09_dialogos_y_archivos.py     # messagebox (alertas) y filedialog (archivos/carpetas)
├── 10_menus_y_contextual.py      # Barra de menú superior, atajos y clic derecho
├── 11_canvas_graficos.py         # Dibujo vectorial y arrastre interactivo (Drag & Drop)
├── 12_pestanas_notebook.py       # Navegación multipestaña con ttk.Notebook
├── 13_tablas_treeview.py         # Tablas estructuradas con columnas ordenables
├── 14_progreso_y_sliders.py      # ttk.Progressbar y controles tk.Scale
└── 15_estilos_y_temas_ttk.py     # Personalización avanzada y selector de temas ttk
```

---

## 🚀 Lanzador Rápido (`main_hub.py`)

Para explorar todos los ejemplos de forma cómoda sin tener que escribir comandos repetidos en la consola, ejecuta el lanzador:

```powershell
py main_hub.py
```

Se abrirá una ventana que lista cada ejemplo con su descripción y un botón **"▶ Ejecutar"** para abrirlo en su propia ventana sin bloquear el lanzador.

---

## 🔍 Explicación Detallada de los 15 Archivos

### `01_ventana_y_etiquetas.py`
- **Objetivo**: Conocer el ciclo de vida fundamental de una aplicación Tkinter.
- **Conceptos clave**:
  - `tk.Tk()`: Instanciación de la ventana raíz.
  - `geometry("Ancho x Alto + X + Y")`: Dimensionar y centrar la ventana en la pantalla calculando las coordenadas mediante `winfo_screenwidth()` y `winfo_screenheight()`.
  - `resizable(bool, bool)` y `minsize()`: Control del redimensionamiento.
  - `tk.Label()`: Creación de etiquetas de texto personalizando `font`, `bg` (fondo), `fg` (color de letra), `relief` (bordes: groove, solid) y `justify`.
  - `root.mainloop()`: Inicio del bucle que escucha los eventos del sistema operativo.
- **Ejecución**: `py 01_ventana_y_etiquetas.py`

---

### `02_botones_y_eventos.py`
- **Objetivo**: Manejar la interactividad mediante pulsaciones y eventos de puntero.
- **Conceptos clave**:
  - `tk.Button()`: Creación de botones interactivos con `activebackground` y `cursor="hand2"`.
  - `command=callback`: Ejecución de funciones estándar al hacer clic.
  - `command=lambda: fn(param)`: Envío dinámico de argumentos mediante funciones anónimas.
  - Estados dinámicos: Habilitar o deshabilitar botones con `state="normal"` o `state="disabled"`.
  - Vinculación con `.bind("<Enter>", ...)` y `.bind("<Leave>", ...)`: Efecto hover (cambio de color al entrar y salir el cursor).
- **Ejecución**: `py 02_botones_y_eventos.py`

---

### `03_entradas_texto.py`
- **Objetivo**: Capturar datos del usuario y vincularlos con variables de Tkinter.
- **Conceptos clave**:
  - `tk.Entry()`: Campo para entrada de texto de una sola línea.
  - `tk.StringVar()`: Variable de control reactiva con métodos `.get()` y `.set()`.
  - `show="•"`: Enmascaramiento de caracteres para campos de contraseña sensible.
  - `entry.focus_set()`: Colocación programática del foco/cursor en un campo.
  - `entry.bind("<Return>", ...)`: Disparar el envío del formulario al presionar la tecla **Enter**.
- **Ejecución**: `py 03_entradas_texto.py`

---

### `04_administradores_layout.py`
- **Objetivo**: Dominar y comparar los 3 gestores de geometría de Tkinter.
- **Conceptos clave**:
  - `pack()`: Posicionamiento en bloques secuenciales (`side="top"|"left"|"right"|"bottom"`, `fill="x"|"y"|"both"`, `expand=True`).
  - `grid()`: Posicionamiento en cuadrícula tabular con filas (`row`), columnas (`column`), expansión (`columnspan`, `rowspan`) y anclaje elástico (`sticky="nsew"`).
  - `place()`: Posicionamiento milimétrico absoluto (`x`, `y`) o porcentual relativo (`relx`, `rely`, `anchor="center"`).
  - **Regla de oro**: Explicación de por qué nunca se deben mezclar `pack()` y `grid()` en el mismo contenedor padre.
- **Ejecución**: `py 04_administradores_layout.py`

---

### `05_checks_y_radios.py`
- **Objetivo**: Implementar controles de selección múltiple y excluyente.
- **Conceptos clave**:
  - `tk.Checkbutton()`: Casillas de verificación independientes vinculadas a variables `tk.BooleanVar()`.
  - `tk.Radiobutton()`: Grupos de botones donde solo uno puede estar activo a la vez, vinculados a una misma `tk.StringVar()`.
  - Actualización en tiempo real: Actualizar resúmenes de selecciones al momento de cambiar cualquier opción.
- **Ejecución**: `py 05_checks_y_radios.py`

---

### `06_listbox_y_scrollbar.py`
- **Objetivo**: Gestionar colecciones de elementos y listas desplazables.
- **Conceptos clave**:
  - `tk.Listbox()`: Lista con modo de selección extendida (`selectmode=tk.EXTENDED`).
  - `tk.Scrollbar()`: Barra de desplazamiento vertical sincronizada bidireccionalmente con `yscrollcommand` y `yview`.
  - Operaciones CRUD: `insert(tk.END, item)`, `delete(indice)` y vaciado completo.
  - `.curselection()`: Lectura de las tuplas de índices seleccionados por el usuario.
- **Ejecución**: `py 06_listbox_y_scrollbar.py`

---

### `07_combobox_y_spinbox.py`
- **Objetivo**: Ofrecer selecciones desplegables modernas y selectores de rangos.
- **Conceptos clave**:
  - `ttk.Combobox`: Desplegable con modo de solo lectura (`state="readonly"`) para evitar entradas no válidas.
  - Evento virtual `<<ComboboxSelected>>`: Detección instantánea del cambio de selección.
  - `ttk.Spinbox`: Selector de números continuos (`from_`, `to`, `increment`) o valores discretos en bucle (`wrap=True`).
- **Ejecución**: `py 07_combobox_y_spinbox.py`

---

### `08_texto_multilinea.py`
- **Objetivo**: Crear editores o visores de texto enriquecido de varias líneas.
- **Conceptos clave**:
  - `tk.Text()`: Área de texto multilínea con ajuste de palabras (`wrap="word"`).
  - Sistema de coordenadas e índices de Tkinter: formato `"linea.columna"` (ej. `"1.0"` para el inicio y `tk.END` para el final).
  - Etiquetas de formato (`tags`): Aplicación de negrita, colores de fondo y subrayado a fragmentos seleccionados.
  - Conteo dinámico de palabras, caracteres y líneas al escuchar el evento `<KeyRelease>`.
- **Ejecución**: `py 08_texto_multilinea.py`

---

### `09_dialogos_y_archivos.py`
- **Objetivo**: Mostrar alertas emergentes nativas y permitir la selección de archivos del sistema.
- **Conceptos clave**:
  - `tkinter.messagebox`: Mensajes de `showinfo`, `showwarning`, `showerror` y diálogos de confirmación booleana `askyesno`.
  - `tkinter.filedialog`: 
    - `askopenfilename()`: Ventana del explorador para abrir archivos con filtros por extensión (`*.py`, `*.txt`).
    - `asksaveasfilename()`: Selector para guardar archivos con extensión por defecto.
    - `askdirectory()`: Selector de carpetas del sistema.
- **Ejecución**: `py 09_dialogos_y_archivos.py`

---

### `10_menus_y_contextual.py`
- **Objetivo**: Construir barras de menú tradicionales y menús contextuales.
- **Conceptos clave**:
  - `tk.Menu(root)`: Creación de la barra superior configurada mediante `root.config(menu=barra)`.
  - Cascadas y submenús: Jerarquías (`add_cascade`), separadores (`add_separator`) y comandos.
  - Aceleradores de teclado: Mostrar atajos (ej. `Ctrl+N`, `Ctrl+S`) y asociarlos con `.bind("<Control-n>", ...)`.
  - Menú contextual: Despliegue con clic derecho (`<Button-3>`) usando el método `.tk_popup(event.x_root, event.y_root)`.
- **Ejecución**: `py 10_menus_y_contextual.py`

---

### `11_canvas_graficos.py`
- **Objetivo**: Dibujar gráficos vectoriales en 2D e interactuar con ellos mediante el ratón.
- **Conceptos clave**:
  - `tk.Canvas()`: Creación de un lienzo de dibujo.
  - Primitivas gráficas: `create_line()`, `create_rectangle()`, `create_oval()`, `create_polygon()` y `create_text()`.
  - Atributos visuales: `fill` (relleno), `outline` (borde exterior), `width` y punteado `dash`.
  - **Drag and Drop interactivo**: Vinculación de eventos de arrastre (`<ButtonPress-1>` y `<B1-Motion>`) con `canvas.move()` para mover objetos libremente.
- **Ejecución**: `py 11_canvas_graficos.py`

---

### `12_pestanas_notebook.py`
- **Objetivo**: Estructurar aplicaciones complejas en múltiples pantallas o paneles usando pestañas.
- **Conceptos clave**:
  - `ttk.Notebook`: Contenedor principal de pestañas.
  - `notebook.add(frame, text="Pestaña")`: Incorporación de vistas independientes dentro de cada pestaña.
  - Evento `<<NotebookTabChanged>>`: Detección en tiempo real de qué pestaña se encuentra activa.
  - Manejo dinámico: Creación y eliminación de pestañas en tiempo de ejecución con `notebook.forget()`.
- **Ejecución**: `py 12_pestanas_notebook.py`

---

### `13_tablas_treeview.py`
- **Objetivo**: Presentar conjuntos de datos en tablas con filas y columnas ordenables.
- **Conceptos clave**:
  - `ttk.Treeview`: Tabla con definición de identificadores de columna (`columns`) y encabezados (`show="headings"`).
  - Personalización de columnas: Asignación de anchos (`width`) y alineaciones (`anchor="center"|"w"|"e"`).
  - **Ordenamiento dinámico**: Función interactiva que ordena ascendente o descendentemente las filas numéricas o alfabéticas al hacer clic en el encabezado.
  - Selección de registros: Detección del evento `<<TreeviewSelect>>` para leer valores de la fila activa.
- **Ejecución**: `py 13_tablas_treeview.py`

---

### `14_progreso_y_sliders.py`
- **Objetivo**: Visualizar procesos de carga y permitir la selección de valores continuos.
- **Conceptos clave**:
  - `ttk.Progressbar`:
    - **Modo Determinado**: Representa un porcentaje exacto de 0 a 100%.
    - **Modo Indeterminado**: Bucle de animación continuo para cargas de duración desconocida (`.start()` y `.stop()`).
  - `tk.Scale`: Control deslizante horizontal sincronizado bidireccionalmente con la barra de progreso.
- **Ejecución**: `py 14_progreso_y_sliders.py`

---

### `15_estilos_y_temas_ttk.py`
- **Objetivo**: Modernizar la estética de las aplicaciones mediante el motor de estilos de `ttk`.
- **Conceptos clave**:
  - `ttk.Style()`: Motor central de estilos para widgets temáticos.
  - Exploración y cambio de temas en caliente: Uso de `style.theme_names()` y `style.theme_use()` (`clam`, `alt`, `default`, `classic`, etc.).
  - Clases de estilo personalizadas: Configuración con `style.configure("Accent.TButton", ...)` para crear botones con estilos visuales únicos.
  - Mapeo dinámico de estados: `style.map()` para definir variaciones de color cuando el botón está activo o deshabilitado.
- **Ejecución**: `py 15_estilos_y_temas_ttk.py`

---

## 🌐 Cómo Subir este Proyecto a GitHub

Sigue estos sencillos pasos para vincular esta carpeta con un repositorio en tu cuenta de GitHub:

### Paso 1: Crear un nuevo repositorio en GitHub
1. Ve a [github.com](https://github.com) e inicia sesión con tu cuenta.
2. Haz clic en el botón verde **"New"** (Nuevo Repositorio).
3. Asigna un nombre a tu repositorio (por ejemplo: `tkinter-tutorial-python`).
4. Déjalo como **Público** (o Privado, según tu preferencia).
5. **IMPORTANTE**: No marques las casillas de "Add a README file" ni "Add .gitignore", ya que este proyecto ya los incluye.
6. Haz clic en **"Create repository"**.

### Paso 2: Conectar y subir desde tu terminal
Abre la terminal en la carpeta de este proyecto y ejecuta los siguientes comandos:

```powershell
# Clonar este repositorio en cualquier máquina:
git clone https://github.com/jorgehernandezsilva843-svg/Funcionalidades-Libreria-TKinter.git

# O para subir nuevos cambios tras editar:
git add .
git commit -m "nuevos cambios"
git push
```

¡Listo! Todos los scripts, el lanzador interactivo y este manual `README.md` estarán publicados en tu perfil de GitHub.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Eres libre de usar, modificar y distribuir estos ejemplos con propósitos educativos o comerciales.
