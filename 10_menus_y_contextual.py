"""
10_menus_y_contextual.py
------------------------
Demuestra la arquitectura completa de menús en aplicaciones de escritorio:
1. Barra de menú superior (tk.Menu con cascade): Archivo, Edición y Ayuda.
2. Separadores visuales y aceleradores de teclado (shortcuts como Ctrl+N, Ctrl+S).
3. Opciones con casillas de verificación (add_checkbutton) dentro de menús.
4. Menú contextual emergente (clic derecho) posicionado dinámicamente con .tk_popup().
"""

import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("10 - Menús de Ventana y Menú Contextual")
    root.geometry("520x420")
    root.configure(bg="#F8FAFC")

    # Etiqueta central de estado
    lbl_accion = tk.Label(
        root,
        text="Explora la barra de menú superior o haz\nCLIC DERECHO en cualquier parte para ver el menú contextual",
        font=("Segoe UI", 12),
        bg="#F8FAFC",
        fg="#334155",
        justify="center"
    )
    lbl_accion.pack(expand=True, fill="both", padx=30, pady=30)

    def registrar_accion(nombre):
        lbl_accion.config(text=f"Última acción ejecutada:\n👉 {nombre}", fg="#2563EB")

    # ==========================================
    # 1. BARRA DE MENÚ SUPERIOR
    # ==========================================
    barra_menu = tk.Menu(root)

    # --- Menú Archivo ---
    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=lambda: registrar_accion("Archivo > Nuevo"))
    menu_archivo.add_command(label="Abrir...", accelerator="Ctrl+O", command=lambda: registrar_accion("Archivo > Abrir"))
    menu_archivo.add_command(label="Guardar", accelerator="Ctrl+S", command=lambda: registrar_accion("Archivo > Guardar"))
    menu_archivo.add_separator()

    # Submenú Exportar
    submenu_exportar = tk.Menu(menu_archivo, tearoff=0)
    submenu_exportar.add_command(label="Exportar a PDF", command=lambda: registrar_accion("Exportado a PDF"))
    submenu_exportar.add_command(label="Exportar a CSV", command=lambda: registrar_accion("Exportado a CSV"))
    menu_archivo.add_cascade(label="Exportar...", menu=submenu_exportar)

    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", accelerator="Alt+F4", command=root.quit)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

    # --- Menú Opciones (con Checkbutton) ---
    menu_opciones = tk.Menu(barra_menu, tearoff=0)
    modo_oscuro = tk.BooleanVar(value=False)

    def cambiar_tema():
        if modo_oscuro.get():
            root.configure(bg="#1E293B")
            lbl_accion.configure(bg="#1E293B", fg="#F8FAFC")
        else:
            root.configure(bg="#F8FAFC")
            lbl_accion.configure(bg="#F8FAFC", fg="#334155")

    menu_opciones.add_checkbutton(label="Modo Oscuro", variable=modo_oscuro, command=cambiar_tema)
    barra_menu.add_cascade(label="Ver", menu=menu_opciones)

    # --- Menú Ayuda ---
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    menu_ayuda.add_command(label="Acerca de...", command=lambda: messagebox.showinfo("Acerca de", "Tutorial de Tkinter en Python"))
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    # Establecer la barra de menú en la ventana principal
    root.config(menu=barra_menu)

    # Atajos de teclado vinculados
    root.bind("<Control-n>", lambda event: registrar_accion("Atajo: Ctrl+N presionado"))
    root.bind("<Control-s>", lambda event: registrar_accion("Atajo: Ctrl+S presionado"))

    # ==========================================
    # 2. MENÚ CONTEXTUAL (Clic Derecho)
    # ==========================================
    menu_contextual = tk.Menu(root, tearoff=0)
    menu_contextual.add_command(label="📋 Copiar", command=lambda: registrar_accion("Menú contextual: Copiar"))
    menu_contextual.add_command(label="✂️ Cortar", command=lambda: registrar_accion("Menú contextual: Cortar"))
    menu_contextual.add_command(label="📌 Pegar", command=lambda: registrar_accion("Menú contextual: Pegar"))
    menu_contextual.add_separator()
    menu_contextual.add_command(label="🔄 Refrescar", command=lambda: registrar_accion("Menú contextual: Refrescar"))

    def mostrar_menu_contextual(event):
        try:
            # Desplegar el menú en las coordenadas absolutas de la pantalla donde ocurrió el clic
            menu_contextual.tk_popup(event.x_root, event.y_root)
        finally:
            menu_contextual.grab_release()

    # En Windows y Linux, clic derecho es <Button-3>
    root.bind("<Button-3>", mostrar_menu_contextual)

    root.mainloop()

if __name__ == "__main__":
    main()
