"""
07_combobox_y_spinbox.py
------------------------
Demuestra el uso de selectores desplegables y numéricos avanzados:
1. ttk.Combobox : Menú desplegable con opción de solo lectura y evento <<ComboboxSelected>>.
2. ttk.Spinbox  : Selector de valores continuos o numéricos con flechas de incremento/decremento.
3. Comparación entre widgets clásicos (tk) y widgets temáticos mejorados (ttk).
"""

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("07 - Combobox y Spinbox (Selectores ttk)")
    root.geometry("500x460")
    root.configure(bg="#F8FAFC")
    root.resizable(False, False)

    # Título principal
    tk.Label(
        root,
        text="Selectores Desplegables y Numéricos",
        font=("Segoe UI", 15, "bold"),
        bg="#F8FAFC",
        fg="#0F172A"
    ).pack(pady=(15, 15))

    frame_central = tk.Frame(root, bg="#F8FAFC")
    frame_central.pack(fill="x", padx=40)

    # ==========================================
    # 1. ttk.Combobox (Menú desplegable)
    # ==========================================
    tk.Label(
        frame_central,
        text="Selecciona tu Lenguaje de Programación Favorito:",
        font=("Segoe UI", 10, "bold"),
        bg="#F8FAFC",
        fg="#334155"
    ).pack(anchor="w", pady=(5, 3))

    lenguajes = ["Python", "JavaScript", "C++", "Rust", "Go", "Java", "Kotlin", "TypeScript"]
    combo_lenguaje = ttk.Combobox(
        frame_central,
        values=lenguajes,
        state="readonly",  # Impide que el usuario escriba valores fuera de la lista
        font=("Segoe UI", 10)
    )
    combo_lenguaje.current(0)  # Seleccionar el primer valor por defecto
    combo_lenguaje.pack(fill="x", pady=(0, 15), ipady=2)

    # Evento cuando el usuario cambia la selección del Combobox
    def al_cambiar_lenguaje(event):
        actualizar_pantalla()

    combo_lenguaje.bind("<<ComboboxSelected>>", al_cambiar_lenguaje)

    # ==========================================
    # 2. ttk.Spinbox (Selector de Rango Numérico)
    # ==========================================
    tk.Label(
        frame_central,
        text="Años de experiencia laboral (Rango 0 - 50):",
        font=("Segoe UI", 10, "bold"),
        bg="#F8FAFC",
        fg="#334155"
    ).pack(anchor="w", pady=(5, 3))

    spin_experiencia = ttk.Spinbox(
        frame_central,
        from_=0,
        to=50,
        increment=1,
        wrap=False,
        font=("Segoe UI", 10),
        command=lambda: actualizar_pantalla()
    )
    spin_experiencia.set(2)  # Valor inicial
    spin_experiencia.pack(fill="x", pady=(0, 15), ipady=2)

    # ==========================================
    # 3. ttk.Spinbox con Lista de Textos
    # ==========================================
    tk.Label(
        frame_central,
        text="Horario preferido para programar (Valores discretos):",
        font=("Segoe UI", 10, "bold"),
        bg="#F8FAFC",
        fg="#334155"
    ).pack(anchor="w", pady=(5, 3))

    turnos = ("Mañana (08:00 - 12:00)", "Tarde (13:00 - 18:00)", "Noche (19:00 - 00:00)", "Madrugada (00:00 - 06:00)")
    spin_turnos = ttk.Spinbox(
        frame_central,
        values=turnos,
        wrap=True,  # Al llegar al final vuelve al inicio
        font=("Segoe UI", 10),
        command=lambda: actualizar_pantalla()
    )
    spin_turnos.set(turnos[0])
    spin_turnos.pack(fill="x", pady=(0, 15), ipady=2)

    # ==========================================
    # Resumen interactivo
    # ==========================================
    lbl_resumen = tk.Label(
        root,
        text="",
        font=("Segoe UI", 10),
        bg="#E2E8F0",
        fg="#0F172A",
        relief="groove",
        padx=15,
        pady=12,
        justify="left"
    )
    lbl_resumen.pack(fill="x", padx=40, pady=10)

    def actualizar_pantalla():
        leng = combo_lenguaje.get()
        exp = spin_experiencia.get()
        turno = spin_turnos.get()
        lbl_resumen.config(
            text=f"💻 Lenguaje : {leng}\n"
                 f"📈 Experiencia : {exp} año(s)\n"
                 f"⏰ Horario : {turno}"
        )

    actualizar_pantalla()

    root.mainloop()

if __name__ == "__main__":
    main()
