"""
main_hub.py
-----------
Lanzador interactivo visual para ejecutar y explorar todos los ejemplos de la suite Tkinter.
Permite iniciar cualquiera de los 15 scripts con un solo clic mediante subprocess.
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

EJEMPLOS = [
    ("01_ventana_y_etiquetas.py", "01. Ventana y Etiquetas", "Creación de ventana principal, propiedades y widgets tk.Label."),
    ("02_botones_y_eventos.py", "02. Botones y Eventos", "Callbacks, lambdas con parámetros, estados y eventos hover con bind."),
    ("03_entradas_texto.py", "03. Entradas de Texto", "Campos Entry, variables StringVar, ocultar claves y tecla Enter."),
    ("04_administradores_layout.py", "04. Gestores de Layout", "Comparativa visual de pack(), grid() y place()."),
    ("05_checks_y_radios.py", "05. Checks y Radios", "Casillas de verificación Checkbutton y botones Radiobutton."),
    ("06_listbox_y_scrollbar.py", "06. Listbox y Scrollbar", "Listas con selección múltiple conectadas a barra de desplazamiento."),
    ("07_combobox_y_spinbox.py", "07. Combobox y Spinbox", "Menús desplegables y selectores numéricos ttk con eventos."),
    ("08_texto_multilinea.py", "08. Texto Multilínea", "Editor de texto Text, formateo con Tags y conteo de palabras."),
    ("09_dialogos_y_archivos.py", "09. Diálogos y Archivos", "Ventanas emergentes messagebox y explorador filedialog."),
    ("10_menus_y_contextual.py", "10. Menús y Clic Derecho", "Barra de menús, atajos de teclado y menú contextual flotante."),
    ("11_canvas_graficos.py", "11. Lienzo Canvas", "Dibujo de figuras vectoriales e interactividad de arrastre."),
    ("12_pestanas_notebook.py", "12. Pestañas Notebook", "Organización por pestañas con ttk.Notebook dinámico."),
    ("13_tablas_treeview.py", "13. Tablas Treeview", "Tablas estructuradas con columnas ordenables al hacer clic."),
    ("14_progreso_y_sliders.py", "14. Progreso y Sliders", "Barras Progressbar determinadas/indeterminadas y Scale."),
    ("15_estilos_y_temas_ttk.py", "15. Estilos y Temas ttk", "Personalización con ttk.Style y cambio de temas en caliente.")
]

def lanzar_script(nombre_archivo, lbl_status):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_script = os.path.join(directorio_actual, nombre_archivo)
    
    if not os.path.exists(ruta_script):
        lbl_status.config(text=f"❌ No se encontró el archivo {nombre_archivo}", fg="#DC2626")
        return

    lbl_status.config(text=f"🚀 Ejecutando {nombre_archivo}...", fg="#2563EB")
    try:
        # Ejecuta el script de manera independiente sin bloquear la ventana principal
        subprocess.Popen([sys.executable, ruta_script])
    except Exception as e:
        lbl_status.config(text=f"❌ Error al iniciar: {e}", fg="#DC2626")

def main():
    root = tk.Tk()
    root.title("Suite de Ejemplos Tkinter - Lanzador Principal")
    root.geometry("720x620")
    root.configure(bg="#0F172A")

    # Encabezado
    frame_header = tk.Frame(root, bg="#0F172A", padx=20, pady=15)
    frame_header.pack(fill="x")

    tk.Label(
        frame_header,
        text="🐍 Guía Práctica de Tkinter en Python",
        font=("Segoe UI", 18, "bold"),
        bg="#0F172A",
        fg="#38BDF8"
    ).pack(anchor="w")

    tk.Label(
        frame_header,
        text="Selecciona cualquier ejemplo para abrirlo en una ventana interactiva independiente:",
        font=("Segoe UI", 10),
        bg="#0F172A",
        fg="#94A3B8"
    ).pack(anchor="w", pady=(4, 0))

    # Marco con Scrollbar para contener la lista de los 15 ejemplos
    frame_canvas = tk.Frame(root, bg="#0F172A")
    frame_canvas.pack(fill="both", expand=True, padx=20, pady=5)

    canvas = tk.Canvas(frame_canvas, bg="#0F172A", highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#0F172A")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def on_canvas_configure(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", on_canvas_configure)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Permitir scroll con la rueda del ratón
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Barra inferior de estado
    lbl_status = tk.Label(
        root,
        text="Listo para ejecutar ejemplos",
        font=("Segoe UI", 9, "italic"),
        bg="#1E293B",
        fg="#38BDF8",
        padx=15,
        pady=8,
        anchor="w"
    )
    lbl_status.pack(fill="x", side="bottom")

    # Construir tarjetas para cada ejemplo
    for archivo, titulo, descripcion in EJEMPLOS:
        card = tk.Frame(scrollable_frame, bg="#1E293B", bd=1, relief="solid")
        card.pack(fill="x", pady=4, padx=5)

        info_frame = tk.Frame(card, bg="#1E293B", padx=10, pady=8)
        info_frame.pack(side="left", fill="both", expand=True)

        tk.Label(
            info_frame,
            text=titulo,
            font=("Segoe UI", 11, "bold"),
            bg="#1E293B",
            fg="#F8FAFC"
        ).pack(anchor="w")

        tk.Label(
            info_frame,
            text=descripcion,
            font=("Segoe UI", 9),
            bg="#1E293B",
            fg="#94A3B8"
        ).pack(anchor="w")

        btn_run = tk.Button(
            card,
            text="▶ Ejecutar",
            font=("Segoe UI", 9, "bold"),
            bg="#0284C7",
            fg="white",
            activebackground="#0369A1",
            activeforeground="white",
            cursor="hand2",
            padx=12,
            pady=4,
            relief="flat",
            command=lambda f=archivo: lanzar_script(f, lbl_status)
        )
        btn_run.pack(side="right", padx=12, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
