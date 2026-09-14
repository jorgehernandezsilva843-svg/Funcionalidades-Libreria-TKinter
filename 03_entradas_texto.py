"""
03_entradas_texto.py
--------------------
Demuestra la captura y manipulación de texto con el widget Entry:
1. Creación de campos de texto (tk.Entry).
2. Vinculación con variables de control (tk.StringVar) y métodos .get() y .set().
3. Modo oculto para contraseñas (show="*") con botón para alternar visibilidad.
4. Limpieza de campos (.delete(0, tk.END)) y asignación de foco (.focus_set()).
5. Manejo del evento <Return> (tecla Enter) para procesar el formulario.
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("03 - Entradas de Texto (Entry y StringVar)")
    root.geometry("480x450")
    root.configure(bg="#F8FAFC")
    root.resizable(False, False)

    # Variables de control
    var_usuario = tk.StringVar()
    var_password = tk.StringVar()
    mostrar_clave = tk.BooleanVar(value=False)

    # Título
    lbl_titulo = tk.Label(
        root,
        text="Formulario de Inicio de Sesión",
        font=("Segoe UI", 16, "bold"),
        bg="#F8FAFC",
        fg="#0F172A"
    )
    lbl_titulo.pack(pady=(20, 15))

    # Marco contenedor para los campos
    frame_campos = tk.Frame(root, bg="#F8FAFC")
    frame_campos.pack(padx=40, fill="x")

    # 1. Campo de Usuario
    lbl_usuario = tk.Label(
        frame_campos,
        text="Nombre de Usuario:",
        font=("Segoe UI", 10, "bold"),
        bg="#F8FAFC",
        fg="#334155",
        anchor="w"
    )
    lbl_usuario.pack(fill="x", pady=(5, 2))

    entry_usuario = tk.Entry(
        frame_campos,
        textvariable=var_usuario,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1,
        bg="#FFFFFF"
    )
    entry_usuario.pack(fill="x", ipady=4, pady=(0, 10))
    entry_usuario.focus_set()  # El cursor inicia aquí

    # 2. Campo de Contraseña
    lbl_pass = tk.Label(
        frame_campos,
        text="Contraseña:",
        font=("Segoe UI", 10, "bold"),
        bg="#F8FAFC",
        fg="#334155",
        anchor="w"
    )
    lbl_pass.pack(fill="x", pady=(5, 2))

    frame_pass = tk.Frame(frame_campos, bg="#F8FAFC")
    frame_pass.pack(fill="x", pady=(0, 15))

    entry_pass = tk.Entry(
        frame_pass,
        textvariable=var_password,
        show="•",
        font=("Segoe UI", 11),
        relief="solid",
        bd=1,
        bg="#FFFFFF"
    )
    entry_pass.pack(side="left", fill="x", expand=True, ipady=4)

    # Botón para mostrar / ocultar contraseña
    def alternar_visibilidad():
        if mostrar_clave.get():
            entry_pass.config(show="•")
            btn_ojo.config(text="👁 Mostrar")
            mostrar_clave.set(False)
        else:
            entry_pass.config(show="")
            btn_ojo.config(text="🙈 Ocultar")
            mostrar_clave.set(True)

    btn_ojo = tk.Button(
        frame_pass,
        text="👁 Mostrar",
        font=("Segoe UI", 9),
        bg="#E2E8F0",
        command=alternar_visibilidad,
        cursor="hand2"
    )
    btn_ojo.pack(side="right", padx=(5, 0))

    # Etiqueta de resultado o validación
    lbl_resultado = tk.Label(
        root,
        text="Completa los datos y presiona 'Ingresar' o Enter",
        font=("Segoe UI", 10),
        bg="#E2E8F0",
        fg="#475569",
        pady=8,
        relief="groove"
    )
    lbl_resultado.pack(fill="x", padx=40, pady=10)

    # 3. Procesar formulario
    def procesar_login(event=None):
        usuario = var_usuario.get().strip()
        clave = var_password.get()

        if not usuario or not clave:
            lbl_resultado.config(text="⚠️ Error: Ambos campos son obligatorios.", fg="#DC2626")
            return

        lbl_resultado.config(
            text=f"✅ Bienvenido, {usuario}! Contraseña de {len(clave)} caracteres recibida.",
            fg="#16A34A"
        )

    # 4. Limpiar campos
    def limpiar():
        var_usuario.set("")
        var_password.set("")
        lbl_resultado.config(text="Campos limpiados exitosamente.", fg="#475569")
        entry_usuario.focus_set()

    # Vincular tecla Enter en ambos campos
    entry_usuario.bind("<Return>", procesar_login)
    entry_pass.bind("<Return>", procesar_login)

    # Botones de acción
    frame_botones = tk.Frame(root, bg="#F8FAFC")
    frame_botones.pack(fill="x", padx=40, pady=10)

    btn_limpiar = tk.Button(
        frame_botones,
        text="Limpiar",
        font=("Segoe UI", 10),
        bg="#94A3B8",
        fg="white",
        cursor="hand2",
        command=limpiar
    )
    btn_limpiar.pack(side="left", fill="x", expand=True, padx=(0, 5))

    btn_entrar = tk.Button(
        frame_botones,
        text="Ingresar (Enter)",
        font=("Segoe UI", 10, "bold"),
        bg="#2563EB",
        fg="white",
        cursor="hand2",
        command=procesar_login
    )
    btn_entrar.pack(side="right", fill="x", expand=True, padx=(5, 0))

    root.mainloop()

if __name__ == "__main__":
    main()
