"""
15_estilos_y_temas_ttk.py
-------------------------
Demuestra la personalización estética moderna con ttk.Style y temas:
1. Inspección y cambio dinámico entre los temas del sistema (clam, alt, default, classic, vista, etc.).
2. Creación de clases de estilo personalizadas (ej. 'Accent.TButton', 'Danger.TButton').
3. Vista previa interactiva: cambia de tema y observa cómo se transforman botones, casillas, radios, campos y barras.
"""

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("15 - Estilos Modernos y Selector de Temas con ttk.Style")
    root.geometry("600x560")
    root.configure(bg="#F1F5F9")
    root.resizable(False, False)

    # 1. Instanciar el gestor de estilos ttk
    style = ttk.Style()
    temas_disponibles = list(style.theme_names())

    # 2. Configuración de estilos personalizados
    style.configure(
        "Accent.TButton",
        font=("Segoe UI", 10, "bold"),
        foreground="#FFFFFF",
        background="#2563EB",
        padding=6
    )
    style.map(
        "Accent.TButton",
        background=[("active", "#1D4ED8"), ("disabled", "#94A3B8")]
    )

    style.configure(
        "Danger.TButton",
        font=("Segoe UI", 10),
        foreground="#FFFFFF",
        background="#DC2626",
        padding=6
    )
    style.map(
        "Danger.TButton",
        background=[("active", "#B91C1C")]
    )

    # Título principal
    tk.Label(
        root,
        text="Laboratorio Visual de Estilos y Temas ttk",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(12, 6))

    # ==========================================
    # SELECTOR DINÁMICO DE TEMAS
    # ==========================================
    frame_selector = tk.LabelFrame(
        root,
        text=" 🎨 Cambiar Tema en Caliente ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#2563EB",
        padx=15,
        pady=10
    )
    frame_selector.pack(fill="x", padx=25, pady=6)

    tk.Label(
        frame_selector,
        text="Selecciona un tema para ver cómo cambia la apariencia de todos los controles:",
        bg="#FFFFFF",
        fg="#475569"
    ).pack(anchor="w", pady=(0, 4))

    def cambiar_tema_seleccionado(event=None):
        tema_elegido = combo_temas.get()
        style.theme_use(tema_elegido)
        lbl_tema_actual.config(text=f"Tema activo actualmente: '{tema_elegido}'")
        lbl_feedback.config(text=f"✅ Tema cambiado a '{tema_elegido}'. ¡Compara cómo lucen los botones y bordes!", fg="#16A34A")

    combo_temas = ttk.Combobox(frame_selector, values=temas_disponibles, state="readonly", font=("Segoe UI", 10))
    combo_temas.set(style.theme_use())
    combo_temas.pack(fill="x", pady=5)
    combo_temas.bind("<<ComboboxSelected>>", cambiar_tema_seleccionado)

    lbl_tema_actual = tk.Label(frame_selector, text=f"Tema activo actualmente: '{style.theme_use()}'", font=("Segoe UI", 9, "italic"), bg="#FFFFFF", fg="#059669")
    lbl_tema_actual.pack(anchor="w", pady=(2, 0))

    # ==========================================
    # VISTA PREVIA INTERACTIVA DE CONTROLES
    # ==========================================
    frame_preview = tk.LabelFrame(
        root,
        text=" Vista Previa Interactiva de Widgets ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#0F172A",
        padx=15,
        pady=10
    )
    frame_preview.pack(fill="both", expand=True, padx=25, pady=(6, 12))

    # Entrada de texto
    ttk.Label(frame_preview, text="Campo ttk.Entry:").pack(anchor="w", pady=(2, 2))
    entry_demo = ttk.Entry(frame_preview, font=("Segoe UI", 10))
    entry_demo.insert(0, "Prueba escribir texto aquí...")
    entry_demo.pack(fill="x", pady=(0, 8))

    # Controles de selección (Check y Radio) para ver la diferencia de temas
    f_opciones = tk.Frame(frame_preview, bg="#FFFFFF")
    f_opciones.pack(fill="x", pady=(0, 8))

    chk_val = tk.BooleanVar(value=True)
    ttk.Checkbutton(f_opciones, text="ttk.Checkbutton (casilla)", variable=chk_val).pack(side="left", padx=(0, 15))

    rb_val = tk.StringVar(value="A")
    ttk.Radiobutton(f_opciones, text="Opción 1", value="A", variable=rb_val).pack(side="left", padx=5)
    ttk.Radiobutton(f_opciones, text="Opción 2", value="B", variable=rb_val).pack(side="left", padx=5)

    # Barra de progreso
    ttk.Label(frame_preview, text="Barra de progreso ttk:").pack(anchor="w", pady=(2, 2))
    pbar = ttk.Progressbar(frame_preview, value=50, maximum=100)
    pbar.pack(fill="x", pady=(0, 10))

    # Botones con interacción
    def pulsar_boton(nombre, delta):
        nueva_val = max(0, min(100, pbar["value"] + delta))
        pbar["value"] = nueva_val
        lbl_feedback.config(text=f"Pulsaste '{nombre}' -> Progreso ajustado a {nueva_val}%", fg="#2563EB")

    f_btns = tk.Frame(frame_preview, bg="#FFFFFF")
    f_btns.pack(fill="x", pady=4)

    btn_normal = ttk.Button(f_btns, text="Estándar (+15%)", command=lambda: pulsar_boton("Estándar", 15))
    btn_normal.pack(side="left", padx=(0, 5), expand=True, fill="x")

    btn_accent = ttk.Button(f_btns, text="Accent (+25%)", style="Accent.TButton", command=lambda: pulsar_boton("Accent", 25))
    btn_accent.pack(side="left", padx=5, expand=True, fill="x")

    btn_danger = ttk.Button(f_btns, text="Peligro (-20%)", style="Danger.TButton", command=lambda: pulsar_boton("Peligro", -20))
    btn_danger.pack(side="left", padx=(5, 0), expand=True, fill="x")

    # Feedback inferior
    lbl_feedback = tk.Label(
        frame_preview,
        text="Presiona los botones para interactuar con la barra o cambia el tema arriba",
        font=("Segoe UI", 9, "italic"),
        bg="#F8FAFC",
        fg="#475569",
        pady=6,
        relief="groove"
    )
    lbl_feedback.pack(fill="x", pady=(10, 0))

    root.mainloop()

if __name__ == "__main__":
    main()
