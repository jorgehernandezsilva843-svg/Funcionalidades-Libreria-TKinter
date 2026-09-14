"""
02_botones_y_eventos.py
-----------------------
Demuestra la interacción del usuario mediante botones y eventos:
1. Creación de botones (tk.Button) con estilos personalizados.
2. Manejo de comandos (callbacks simples y con parámetros usando lambda).
3. Habilitar y deshabilitar botones dinámicamente (state="normal" / "disabled").
4. Vinculación de eventos con .bind() (efecto hover al pasar el cursor y clics).
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("02 - Botones y Manejo de Eventos")
    root.geometry("500x480")
    root.configure(bg="#F1F5F9")
    root.resizable(False, False)

    # Estado mutable para contador
    contador = {"valor": 0}

    # Etiqueta para mostrar el resultado de las acciones
    lbl_resultado = tk.Label(
        root,
        text="Haz clic en cualquier botón para ver la interacción",
        font=("Segoe UI", 11, "bold"),
        bg="#E2E8F0",
        fg="#1E293B",
        pady=12,
        relief="groove"
    )
    lbl_resultado.pack(fill="x", padx=30, pady=20)

    # 1. Función de callback simple
    def accion_saludar():
        lbl_resultado.config(text="¡Hola! Has presionado el botón simple 👋", fg="#0284C7")

    btn_saludar = tk.Button(
        root,
        text="1. Saludo Simple (Callback)",
        font=("Segoe UI", 10),
        bg="#0284C7",
        fg="white",
        activebackground="#0369A1",
        activeforeground="white",
        cursor="hand2",
        command=accion_saludar
    )
    btn_saludar.pack(pady=6, padx=30, fill="x")

    # 2. Función con parámetros usando expresión lambda
    def cambiar_contador(paso):
        contador["valor"] += paso
        lbl_resultado.config(
            text=f"Contador actual: {contador['valor']} (cambio de {paso:+d})",
            fg="#16A34A" if contador["valor"] >= 0 else "#DC2626"
        )

    frame_contador = tk.Frame(root, bg="#F1F5F9")
    frame_contador.pack(pady=6)

    btn_restar = tk.Button(
        frame_contador,
        text="➖ Restar 5 (Lambda)",
        font=("Segoe UI", 10),
        bg="#DC2626",
        fg="white",
        cursor="hand2",
        command=lambda: cambiar_contador(-5)
    )
    btn_restar.pack(side="left", padx=5)

    btn_sumar = tk.Button(
        frame_contador,
        text="➕ Sumar 5 (Lambda)",
        font=("Segoe UI", 10),
        bg="#16A34A",
        fg="white",
        cursor="hand2",
        command=lambda: cambiar_contador(5)
    )
    btn_sumar.pack(side="left", padx=5)

    # 3. Habilitar / Deshabilitar botones dinámicamente
    def alternar_estado():
        if btn_objetivo["state"] == "normal":
            btn_objetivo.config(state="disabled", text="Botón Deshabilitado 🔒")
            lbl_resultado.config(text="Se deshabilitó el botón inferior", fg="#D97706")
        else:
            btn_objetivo.config(state="normal", text="Botón Habilitado 🔓")
            lbl_resultado.config(text="Se habilitó el botón inferior", fg="#2563EB")

    btn_toggle = tk.Button(
        root,
        text="3. Alternar Estado del Botón Inferior",
        font=("Segoe UI", 10),
        bg="#475569",
        fg="white",
        cursor="hand2",
        command=alternar_estado
    )
    btn_toggle.pack(pady=6, padx=30, fill="x")

    btn_objetivo = tk.Button(
        root,
        text="Botón Habilitado 🔓",
        font=("Segoe UI", 10),
        bg="#F59E0B",
        fg="white",
        command=lambda: lbl_resultado.config(text="¡Pulsaste el botón condicional!", fg="#B45309")
    )
    btn_objetivo.pack(pady=6, padx=30, fill="x")

    # 4. Vinculación de eventos con .bind() (Efecto Hover dinámico)
    btn_hover = tk.Button(
        root,
        text="4. Pasa el ratón por aquí (Hover con .bind)",
        font=("Segoe UI", 10, "bold"),
        bg="#8B5CF6",
        fg="white",
        cursor="hand2"
    )
    btn_hover.pack(pady=12, padx=30, fill="x")

    def al_entrar(event):
        btn_hover.config(bg="#6D28D9")
        lbl_resultado.config(text="¡Cursor posicionado sobre el botón violeta!", fg="#6D28D9")

    def al_salir(event):
        btn_hover.config(bg="#8B5CF6")
        lbl_resultado.config(text="El cursor salió del botón", fg="#475569")

    # Vinculamos eventos del mouse: <Enter> = cursor entra, <Leave> = cursor sale
    btn_hover.bind("<Enter>", al_entrar)
    btn_hover.bind("<Leave>", al_salir)

    root.mainloop()

if __name__ == "__main__":
    main()
