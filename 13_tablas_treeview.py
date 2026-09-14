"""
13_tablas_treeview.py
---------------------
Demuestra la creación y manipulación de tablas estructuradas con ttk.Treeview:
1. Configuración de columnas, encabezados y alineaciones.
2. Inserción de registros tabulares y selección de filas.
3. Ordenamiento interactivo de columnas al hacer clic en el encabezado.
4. Extracción de valores del elemento seleccionado y eliminación de filas.
"""

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("13 - Tablas de Datos Estructurados (ttk.Treeview)")
    root.geometry("680x480")
    root.configure(bg="#F1F5F9")

    tk.Label(
        root,
        text="Gestión de Datos con Tablas (Treeview)",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(12, 5))

    tk.Label(
        root,
        text="💡 Haz clic en cualquier encabezado de columna para ordenar ascendentemente/descendentemente",
        font=("Segoe UI", 9, "italic"),
        bg="#F1F5F9",
        fg="#475569"
    ).pack(pady=(0, 8))

    # Marco contenedor para la tabla y el scrollbar
    frame_tabla = tk.Frame(root, bd=1, relief="solid")
    frame_tabla.pack(fill="both", expand=True, padx=25, pady=5)

    scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
    scroll_y.pack(side="right", fill="y")

    # 1. Definición de columnas
    columnas = ("id", "nombre", "departamento", "salario")
    tree = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",  # Oculta la columna jerárquica inicial '#'
        yscrollcommand=scroll_y.set,
        selectmode="browse"
    )
    scroll_y.config(command=tree.yview)

    # 2. Configurar encabezados y anchos
    encabezados = {
        "id": ("ID", 60, "center"),
        "nombre": ("Nombre y Apellido", 200, "w"),
        "departamento": ("Departamento", 160, "w"),
        "salario": ("Salario (USD)", 120, "e")
    }

    # Función para ordenar columnas interactivamente
    orden_ascendente = {col: True for col in columnas}

    def ordenar_por_columna(col):
        datos = [(tree.set(k, col), k) for k in tree.get_children("")]
        
        # Si es columna de número, convertir a float para ordenar numéricamente
        if col in ("id", "salario"):
            datos.sort(key=lambda t: float(t[0].replace("$", "").replace(",", "")), reverse=not orden_ascendente[col])
        else:
            datos.sort(key=lambda t: t[0].lower(), reverse=not orden_ascendente[col])

        # Reorganizar elementos en la tabla
        for index, (_, item_id) in enumerate(datos):
            tree.move(item_id, "", index)

        # Alternar dirección para el siguiente clic
        orden_ascendente[col] = not orden_ascendente[col]
        simbolo = "▲" if orden_ascendente[col] else "▼"
        tree.heading(col, text=f"{encabezados[col][0]} {simbolo}")

    for col, (texto, ancho, alineacion) in encabezados.items():
        tree.heading(col, text=texto, command=lambda c=col: ordenar_por_columna(c))
        tree.column(col, width=ancho, anchor=alineacion)

    tree.pack(side="left", fill="both", expand=True)

    # 3. Insertar datos iniciales
    empleados = [
        (101, "Guido van Rossum", "Arquitectura Core", "9500"),
        (102, "Margaret Hamilton", "Ingeniería de Vuelo", "9800"),
        (103, "Alan Turing", "Criptografía y Lógica", "9200"),
        (104, "Grace Hopper", "Compiladores", "9600"),
        (105, "Dennis Ritchie", "Sistemas Operativos", "9400"),
        (106, "Linus Torvalds", "Desarrollo del Kernel", "9700"),
        (107, "Ada Lovelace", "Algoritmia", "9900")
    ]
    for emp in empleados:
        tree.insert("", tk.END, values=emp)

    # 4. Panel de información de la fila seleccionada
    frame_detalles = tk.Frame(root, bg="#F1F5F9")
    frame_detalles.pack(fill="x", padx=25, pady=8)

    lbl_seleccion = tk.Label(frame_detalles, text="Selecciona un registro para ver sus detalles", font=("Segoe UI", 10), bg="#E2E8F0", fg="#1E293B", relief="groove", padx=10, pady=6)
    lbl_seleccion.pack(side="left", fill="x", expand=True, padx=(0, 8))

    def al_seleccionar_fila(event):
        seleccion = tree.selection()
        if seleccion:
            item_id = seleccion[0]
            valores = tree.item(item_id, "values")
            lbl_seleccion.config(text=f"Seleccionado: #{valores[0]} {valores[1]} | {valores[2]} | ${valores[3]}")

    tree.bind("<<TreeviewSelect>>", al_seleccionar_fila)

    def eliminar_fila():
        seleccion = tree.selection()
        if seleccion:
            tree.delete(seleccion[0])
            lbl_seleccion.config(text="Registro eliminado de la tabla")

    btn_eliminar = tk.Button(frame_detalles, text="🗑️ Eliminar Fila", bg="#FCA5A5", command=eliminar_fila, cursor="hand2")
    btn_eliminar.pack(side="right")

    root.mainloop()

if __name__ == "__main__":
    main()
