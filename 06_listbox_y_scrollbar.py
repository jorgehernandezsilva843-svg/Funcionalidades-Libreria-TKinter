"""
06_listbox_y_scrollbar.py
-------------------------
Demuestra la visualización y gestión de colecciones con Listbox y Scrollbar:
1. Creación de una lista de elementos (tk.Listbox) con modo de selección múltiple (selectmode=tk.EXTENDED).
2. Vinculación bidireccional con una barra de desplazamiento (tk.Scrollbar).
3. Operaciones dinámicas: agregar elementos, eliminar seleccionados y vaciar la lista.
4. Lectura de selecciones con .curselection() y .get().
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("06 - Listas de Elementos (Listbox) y Scrollbar")
    root.geometry("540x520")
    root.configure(bg="#F1F5F9")
    root.resizable(False, False)

    # Título
    tk.Label(
        root,
        text="Gestor de Tareas y Elementos",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(15, 10))

    # Marco contenedor de entrada para agregar ítems
    frame_agregar = tk.Frame(root, bg="#F1F5F9")
    frame_agregar.pack(fill="x", padx=30, pady=5)

    entry_nuevo = tk.Entry(frame_agregar, font=("Segoe UI", 11), relief="solid", bd=1)
    entry_nuevo.pack(side="left", fill="x", expand=True, ipady=3, padx=(0, 8))

    def agregar_item(event=None):
        texto = entry_nuevo.get().strip()
        if texto:
            listbox.insert(tk.END, texto)
            entry_nuevo.delete(0, tk.END)
            lbl_estado.config(text=f"Agregado: '{texto}'", fg="#16A34A")

    entry_nuevo.bind("<Return>", agregar_item)

    btn_agregar = tk.Button(
        frame_agregar,
        text="➕ Agregar",
        font=("Segoe UI", 10, "bold"),
        bg="#2563EB",
        fg="white",
        cursor="hand2",
        command=agregar_item
    )
    btn_agregar.pack(side="right")

    # Marco contenedor para la Listbox y el Scrollbar
    frame_lista = tk.Frame(root, bg="#FFFFFF", bd=1, relief="solid")
    frame_lista.pack(fill="both", expand=True, padx=30, pady=10)

    # 1. Crear el Scrollbar
    scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    # 2. Crear la Listbox con selección múltiple
    listbox = tk.Listbox(
        frame_lista,
        selectmode=tk.EXTENDED,
        yscrollcommand=scrollbar.set,
        font=("Consolas", 10),
        selectbackground="#3B82F6",
        selectforeground="white",
        bd=0,
        highlightthickness=0
    )
    listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    # 3. Conectar el Scrollbar a la Listbox
    scrollbar.config(command=listbox.yview)

    # Poblar con datos iniciales
    items_iniciales = [
        "Aprender sintaxis básica de Python",
        "Comprender la jerarquía de widgets en Tkinter",
        "Diseñar formularios con Entry y Labels",
        "Organizar elementos con grid() y pack()",
        "Conectar eventos con comandos y lambdas",
        "Manejar diálogos y mensajes de alerta",
        "Crear barras de menú y menús contextuales",
        "Explorar widgets avanzados ttk (Treeview, Notebook)",
        "Compilar interfaces y crear ejecutables .exe",
        "Subir proyecto final a GitHub"
    ]
    for item in items_iniciales:
        listbox.insert(tk.END, item)

    # Botones de control
    frame_acciones = tk.Frame(root, bg="#F1F5F9")
    frame_acciones.pack(fill="x", padx=30, pady=5)

    def eliminar_seleccionados():
        seleccion = listbox.curselection()
        if not seleccion:
            lbl_estado.config(text="⚠️ Selecciona al menos un elemento para eliminar", fg="#DC2626")
            return
        # Se elimina en orden inverso para no alterar los índices de los elementos restantes
        for indice in reversed(seleccion):
            listbox.delete(indice)
        lbl_estado.config(text="Elementos seleccionados eliminados", fg="#D97706")

    def ver_seleccion():
        seleccion = listbox.curselection()
        if not seleccion:
            lbl_estado.config(text="No hay elementos seleccionados", fg="#64748B")
            return
        textos = [listbox.get(i) for i in seleccion]
        lbl_estado.config(text=f"Seleccionado(s): {', '.join(textos)}", fg="#2563EB")

    btn_ver = tk.Button(frame_acciones, text="Ver Selección", bg="#E2E8F0", command=ver_seleccion, cursor="hand2")
    btn_ver.pack(side="left", padx=(0, 5))

    btn_eliminar = tk.Button(frame_acciones, text="🗑️ Eliminar Seleccionado(s)", bg="#FCA5A5", command=eliminar_seleccionados, cursor="hand2")
    btn_eliminar.pack(side="left", padx=5)

    btn_vaciar = tk.Button(frame_acciones, text="Vaciar Todo", bg="#E2E8F0", command=lambda: listbox.delete(0, tk.END), cursor="hand2")
    btn_vaciar.pack(side="right")

    # Etiqueta informativa de estado
    lbl_estado = tk.Label(
        root,
        text="Puedes seleccionar varios ítems manteniendo presionada la tecla Ctrl o Shift",
        font=("Segoe UI", 9, "italic"),
        bg="#E2E8F0",
        fg="#475569",
        pady=8
    )
    lbl_estado.pack(fill="x", padx=30, pady=(5, 15))

    root.mainloop()

if __name__ == "__main__":
    main()
