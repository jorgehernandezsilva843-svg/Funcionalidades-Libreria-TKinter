"""
15_estilos_y_temas_ttk.py
-------------------------
Demuestra la personalización estética moderna con ttk.Style y temas:
1. Inspección y cambio dinámico entre los temas del sistema (clam, alt, default, classic, etc.).
2. Creación de clases de estilo personalizadas (ej. 'Accent.TButton', 'Card.TFrame').
3. Mapeo de estados visuales interactivos (hover, active, disabled) con style.map().
"""

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("15 - Estilos Modernos y Temas con ttk.Style")
    root.geometry("560x500")
    root.configure(bg="#F1F5F9")
    root.resizable(False, False)

    # 1. Instanciar el gestor de estilos ttk
    style = ttk.Style()
    temas_disponibles = list(style.theme_names())

    # 2. Configuración de estilos personalizados
    # Botón con acento azul moderno
    style.configure(
        "Accent.TButton",
        font=("Segoe UI", 10, "bold"),
        foreground="#FFFFFF",
        background="#2563EB",
        padding=8
    )
    style.map(
        "Accent.TButton",
        background=[("active", "#1D4ED8"), ("disabled", "#94A3B8")]
    )

    # Botón de peligro (rojo)
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
        text="Personalización Visual y Temas ttk",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(15, 10))

    # ==========================================
    # SELECTOR DINÁMICO DE TEMAS
    # ==========================================
    frame_selector = tk.LabelFrame(
        root,
        text=" Cambiar Tema de la Aplicación en Caliente ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#2563EB",
        padx=15,
        pady=10
    )
    frame_selector.pack(fill="x", padx=30, pady=8)

    tk.Label(frame_selector, text="Temas soportados por tu sistema:", bg="#FFFFFF", fg="#475569").pack(anchor="w", pady=(0, 4))

    def cambiar_tema_seleccionado(event=None):
        tema_elegido = combo_temas.get()
        style.theme_use(tema_elegido)
        lbl_tema_actual.config(text=f"Tema activo actualmente: '{tema_elegido}'")

    combo_temas = ttk.Combobox(frame_selector, values=temas_disponibles, state="readonly", font=("Segoe UI", 10))
    combo_temas.set(style.theme_use())  # Tema actual por defecto
    combo_temas.pack(fill="x", pady=5)
    combo_temas.bind("<<ComboboxSelected>>", cambiar_tema_seleccionado)

    lbl_tema_actual = tk.Label(frame_selector, text=f"Tema activo actualmente: '{style.theme_use()}'", font=("Segoe UI", 9, "italic"), bg="#FFFFFF", fg="#059669")
    lbl_tema_actual.pack(anchor="w", pady=(4, 0))

    # ==========================================
    # EXHIBICIÓN DE WIDGETS CON ESTILOS
    # ==========================================
    frame_preview = tk.LabelFrame(
        root,
        text=" Vista Previa de Widgets Bajo el Tema Elegido ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#0F172A",
        padx=15,
        pady=12
    )
    frame_preview.pack(fill="both", expand=True, padx=30, pady=(8, 20))

    ttk.Label(frame_preview, text="Campo de entrada ttk.Entry:").pack(anchor="w", pady=(2, 2))
    entry_demo = ttk.Entry(frame_preview, font=("Segoe UI", 10))
    entry_demo.insert(0, "Texto editable de prueba...")
    entry_demo.pack(fill="x", pady=(0, 10))

    ttk.Label(frame_preview, text="Barra de progreso ttk:").pack(anchor="w", pady=(2, 2))
    pbar = ttk.Progressbar(frame_preview, value=65, maximum=100)
    pbar.pack(fill="x", pady=(0, 12))

    # Botones con diferentes estilos
    f_btns = tk.Frame(frame_preview, bg="#FFFFFF")
    f_btns.pack(fill="x", pady=5)

    btn_normal = ttk.Button(f_btns, text="Botón Estándar")
    btn_normal.pack(side="left", padx=(0, 5), expand=True, fill="x")

    btn_accent = ttk.Button(f_btns, text="Estilo Accent", style="Accent.TButton")
    btn_accent.pack(side="left", padx=5, expand=True, fill="x")

    btn_danger = ttk.Button(f_btns, text="Estilo Peligro", style="Danger.TButton")
    btn_danger.pack(side="left", padx=(5, 0), expand=True, fill="x")

    root.mainloop()

if __name__ == "__main__":
    main()
