"""
05_checks_y_radios.py
---------------------
Demuestra el uso de controles de selección:
1. Checkbutton : Casillas de verificación independientes (selección múltiple).
2. Radiobutton : Botones de opción mutuamente excluyentes (selección única por grupo).
3. Variables asociadas : BooleanVar, IntVar y StringVar para sincronizar estados.
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("05 - Casillas de Verificación y Botones de Opción")
    root.geometry("520x480")
    root.configure(bg="#F8FAFC")
    root.resizable(False, False)

    # Título principal
    tk.Label(
        root,
        text="Configuración de Preferencias",
        font=("Segoe UI", 15, "bold"),
        bg="#F8FAFC",
        fg="#0F172A"
    ).pack(pady=(15, 10))

    # ==========================================
    # SECCIÓN 1: Radiobuttons (Selección Única)
    # ==========================================
    frame_radios = tk.LabelFrame(
        root,
        text=" Nivel de Experiencia en Python (Radiobutton - Selección Única) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#1E3A8A",
        padx=15,
        pady=10
    )
    frame_radios.pack(fill="x", padx=30, pady=5)

    var_nivel = tk.StringVar(value="Intermedio")

    niveles = [("Principiante", "Principiante"), ("Intermedio", "Intermedio"), ("Avanzado", "Avanzado")]

    for texto, valor in niveles:
        rb = tk.Radiobutton(
            frame_radios,
            text=texto,
            variable=var_nivel,
            value=valor,
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            command=lambda: actualizar_resumen()
        )
        rb.pack(anchor="w", pady=2)

    # ==========================================
    # SECCIÓN 2: Checkbuttons (Selección Múltiple)
    # ==========================================
    frame_checks = tk.LabelFrame(
        root,
        text=" Herramientas de Interés (Checkbutton - Selección Múltiple) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#059669",
        padx=15,
        pady=10
    )
    frame_checks.pack(fill="x", padx=30, pady=10)

    var_tk = tk.BooleanVar(value=True)
    var_pandas = tk.BooleanVar(value=False)
    var_flask = tk.BooleanVar(value=False)

    chk1 = tk.Checkbutton(
        frame_checks,
        text="Tkinter / GUI Desktop",
        variable=var_tk,
        font=("Segoe UI", 10),
        bg="#FFFFFF",
        command=lambda: actualizar_resumen()
    )
    chk1.pack(anchor="w", pady=2)

    chk2 = tk.Checkbutton(
        frame_checks,
        text="Pandas & Análisis de Datos",
        variable=var_pandas,
        font=("Segoe UI", 10),
        bg="#FFFFFF",
        command=lambda: actualizar_resumen()
    )
    chk2.pack(anchor="w", pady=2)

    chk3 = tk.Checkbutton(
        frame_checks,
        text="Flask / Desarrollo Web Backend",
        variable=var_flask,
        font=("Segoe UI", 10),
        bg="#FFFFFF",
        command=lambda: actualizar_resumen()
    )
    chk3.pack(anchor="w", pady=2)

    # ==========================================
    # RESUMEN EN TIEMPO REAL
    # ==========================================
    lbl_resumen = tk.Label(
        root,
        text="",
        font=("Segoe UI", 10),
        bg="#E2E8F0",
        fg="#1E293B",
        relief="groove",
        padx=12,
        pady=10,
        justify="left"
    )
    lbl_resumen.pack(fill="x", padx=30, pady=(5, 15))

    def actualizar_resumen():
        nivel = var_nivel.get()
        intereses = []
        if var_tk.get():
            intereses.append("Tkinter")
        if var_pandas.get():
            intereses.append("Pandas")
        if var_flask.get():
            intereses.append("Flask")

        texto_intereses = ", ".join(intereses) if intereses else "Ninguno seleccionado"
        lbl_resumen.config(
            text=f"📌 Nivel seleccionado: {nivel}\n📦 Áreas marcadas: {texto_intereses}"
        )

    # Actualizar texto inicial
    actualizar_resumen()

    root.mainloop()

if __name__ == "__main__":
    main()
