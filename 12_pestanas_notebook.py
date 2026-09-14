"""
12_pestanas_notebook.py
-----------------------
Demuestra la organización de interfaces complejas mediante pestañas:
1. Contenedor de pestañas (ttk.Notebook).
2. Adición y configuración de páginas/paneles (frames independientes).
3. Detección de cambio de pestaña mediante el evento <<NotebookTabChanged>>.
4. Creación y cierre dinámico de pestañas.
"""

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("12 - Contenedor con Pestañas (ttk.Notebook)")
    root.geometry("560x440")
    root.configure(bg="#F8FAFC")

    # Título principal
    tk.Label(
        root,
        text="Panel de Control Multipestaña",
        font=("Segoe UI", 15, "bold"),
        bg="#F8FAFC",
        fg="#0F172A"
    ).pack(pady=(12, 6))

    # 1. Crear el widget Notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=20, pady=5)

    # ----------------------------------------------------
    # PESTAÑA 1: Perfil de Usuario
    # ----------------------------------------------------
    tab1 = tk.Frame(notebook, bg="#FFFFFF", padx=20, pady=20)
    notebook.add(tab1, text="👤 Perfil")

    tk.Label(tab1, text="Información Personal", font=("Segoe UI", 12, "bold"), bg="#FFFFFF", fg="#1E3A8A").pack(anchor="w", pady=(0, 10))
    
    tk.Label(tab1, text="Nombre Completo:", bg="#FFFFFF", fg="#475569").pack(anchor="w")
    entry_nombre = tk.Entry(tab1, font=("Segoe UI", 10), relief="solid", bd=1)
    entry_nombre.insert(0, "Ada Lovelace")
    entry_nombre.pack(fill="x", pady=(2, 10), ipady=2)

    tk.Label(tab1, text="Correo Electrónico:", bg="#FFFFFF", fg="#475569").pack(anchor="w")
    entry_email = tk.Entry(tab1, font=("Segoe UI", 10), relief="solid", bd=1)
    entry_email.insert(0, "ada@pioneers.org")
    entry_email.pack(fill="x", pady=(2, 10), ipady=2)

    # ----------------------------------------------------
    # PESTAÑA 2: Ajustes del Sistema
    # ----------------------------------------------------
    tab2 = tk.Frame(notebook, bg="#FFFFFF", padx=20, pady=20)
    notebook.add(tab2, text="⚙️ Configuración")

    tk.Label(tab2, text="Preferencias del Sistema", font=("Segoe UI", 12, "bold"), bg="#FFFFFF", fg="#1E3A8A").pack(anchor="w", pady=(0, 10))

    check_notif = tk.Checkbutton(tab2, text="Recibir notificaciones por correo", bg="#FFFFFF", font=("Segoe UI", 10))
    check_notif.select()
    check_notif.pack(anchor="w", pady=5)

    check_auto = tk.Checkbutton(tab2, text="Actualizaciones automáticas en segundo plano", bg="#FFFFFF", font=("Segoe UI", 10))
    check_auto.pack(anchor="w", pady=5)

    # ----------------------------------------------------
    # PESTAÑA 3: Gestión Dinámica de Pestañas
    # ----------------------------------------------------
    tab3 = tk.Frame(notebook, bg="#FFFFFF", padx=20, pady=20)
    notebook.add(tab3, text="➕ Dinámicas")

    tk.Label(tab3, text="Añadir o Quitar Pestañas Dinámicamente", font=("Segoe UI", 12, "bold"), bg="#FFFFFF", fg="#1E3A8A").pack(anchor="w", pady=(0, 10))

    contador_tabs = {"total": 0}

    def agregar_nueva_pestana():
        contador_tabs["total"] += 1
        num = contador_tabs["total"]
        nueva_tab = tk.Frame(notebook, bg="#F0FDF4", padx=20, pady=20)
        notebook.add(nueva_tab, text=f"Nota #{num}")
        
        tk.Label(nueva_tab, text=f"Contenido de la nota adicional #{num}", font=("Segoe UI", 11, "bold"), bg="#F0FDF4", fg="#166534").pack(pady=10)
        
        btn_cerrar = tk.Button(nueva_tab, text="❌ Cerrar esta pestaña", bg="#FCA5A5", command=lambda t=nueva_tab: notebook.forget(t))
        btn_cerrar.pack(pady=10)
        
        # Enfocar la pestaña recién creada
        notebook.select(nueva_tab)

    tk.Button(tab3, text="➕ Crear Nueva Pestaña Dinámica", font=("Segoe UI", 10, "bold"), bg="#DBEAFE", fg="#1E40AF", command=agregar_nueva_pestana, cursor="hand2").pack(pady=10)

    # Barra de estado inferior que detecta qué pestaña está activa
    lbl_estado = tk.Label(root, text="Pestaña activa: 👤 Perfil", font=("Segoe UI", 9), bg="#E2E8F0", fg="#334155", anchor="w", padx=10, pady=5)
    lbl_estado.pack(fill="x", padx=20, pady=(0, 10))

    def al_cambiar_tab(event):
        indice = notebook.index(notebook.select())
        titulo = notebook.tab(indice, "text")
        lbl_estado.config(text=f"Pestaña activa: {titulo} (Índice: {indice})")

    notebook.bind("<<NotebookTabChanged>>", al_cambiar_tab)

    root.mainloop()

if __name__ == "__main__":
    main()
