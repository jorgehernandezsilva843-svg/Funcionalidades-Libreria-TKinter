"""
08_texto_multilinea.py
----------------------
Demuestra el uso avanzado del widget de edición multilínea (tk.Text):
1. Inserción y extracción de contenido utilizando índices (formato 'linea.columna', ej: '1.0').
2. Aplicación de etiquetas de estilo (tags) para resaltar partes de texto con colores y fuentes.
3. Ajuste de línea (wrap='word') y vinculación con Scrollbar.
4. Conteo dinámico de palabras y caracteres en tiempo real.
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("08 - Editor y Texto Multilínea (Text Widget y Tags)")
    root.geometry("600x520")
    root.configure(bg="#F1F5F9")

    # Título
    tk.Label(
        root,
        text="Editor de Texto con Formato por Tags",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(12, 6))

    # Barra de herramientas superior
    frame_toolbar = tk.Frame(root, bg="#E2E8F0", bd=1, relief="solid")
    frame_toolbar.pack(fill="x", padx=25, pady=(0, 8))

    # Marco para Text + Scrollbar
    frame_editor = tk.Frame(root, bd=1, relief="solid")
    frame_editor.pack(fill="both", expand=True, padx=25, pady=4)

    scrollbar = tk.Scrollbar(frame_editor)
    scrollbar.pack(side="right", fill="y")

    # Widget Text principal
    editor = tk.Text(
        frame_editor,
        wrap="word",
        font=("Consolas", 11),
        yscrollcommand=scrollbar.set,
        padx=10,
        pady=10,
        undo=True  # Permite Ctrl+Z
    )
    editor.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=editor.yview)

    # 1. Configurar Tags (Estilos reutilizables)
    editor.tag_configure("titulo", font=("Segoe UI", 14, "bold"), foreground="#1E3A8A")
    editor.tag_configure("resaltado", background="#FEF08A", foreground="#854D0E", font=("Consolas", 11, "bold"))
    editor.tag_configure("alerta", foreground="#DC2626", font=("Consolas", 11, "bold"))
    editor.tag_configure("subrayado", underline=True, foreground="#2563EB")

    # 2. Insertar texto inicial con formato
    editor.insert(tk.END, "Bienvenido al Widget Text de Tkinter\n\n", "titulo")
    editor.insert(tk.END, "A diferencia de un Entry común, el widget Text soporta ")
    editor.insert(tk.END, "múltiples estilos", "resaltado")
    editor.insert(tk.END, " en el mismo documento.\n\nPuedes marcar ")
    editor.insert(tk.END, "palabras de advertencia", "alerta")
    editor.insert(tk.END, " o crear enlaces como ")
    editor.insert(tk.END, "www.python.org", "subrayado")
    editor.insert(tk.END, ".\n\nEscribe cualquier texto aquí abajo para probar el contador de palabras en tiempo real...\n")

    # 3. Acciones de la barra de herramientas
    def aplicar_resaltado():
        try:
            inicio = editor.index(tk.SEL_FIRST)
            fin = editor.index(tk.SEL_LAST)
            editor.tag_add("resaltado", inicio, fin)
        except tk.TclError:
            pass  # No hay selección activa

    def limpiar_formato():
        try:
            inicio = editor.index(tk.SEL_FIRST)
            fin = editor.index(tk.SEL_LAST)
            for tag in ("titulo", "resaltado", "alerta", "subrayado"):
                editor.tag_remove(tag, inicio, fin)
        except tk.TclError:
            pass

    btn_tag_resaltar = tk.Button(frame_toolbar, text="🖍️ Resaltar Selección", bg="#FEF08A", command=aplicar_resaltado, cursor="hand2")
    btn_tag_resaltar.pack(side="left", padx=4, pady=4)

    btn_tag_quitar = tk.Button(frame_toolbar, text="Quitar Formato", bg="#F8FAFC", command=limpiar_formato, cursor="hand2")
    btn_tag_quitar.pack(side="left", padx=4, pady=4)

    btn_borrar_todo = tk.Button(frame_toolbar, text="🗑️ Limpiar Todo", bg="#FCA5A5", command=lambda: editor.delete("1.0", tk.END), cursor="hand2")
    btn_borrar_todo.pack(side="right", padx=4, pady=4)

    # 4. Barra inferior de estadísticas
    lbl_stats = tk.Label(
        root,
        text="Caracteres: 0 | Palabras: 0 | Líneas: 0",
        font=("Segoe UI", 9),
        bg="#E2E8F0",
        fg="#334155",
        anchor="w",
        padx=10,
        pady=5
    )
    lbl_stats.pack(fill="x", padx=25, pady=(4, 12))

    def actualizar_estadisticas(event=None):
        contenido = editor.get("1.0", "end-1c")  # "end-1c" omite el salto de línea final invisible
        num_caracteres = len(contenido)
        num_palabras = len(contenido.split()) if contenido.strip() else 0
        num_lineas = int(editor.index("end-1c").split(".")[0])
        lbl_stats.config(text=f"Caracteres: {num_caracteres} | Palabras: {num_palabras} | Líneas: {num_lineas}")

    # Escuchar cada pulsación de tecla para refrescar estadísticas
    editor.bind("<KeyRelease>", actualizar_estadisticas)
    actualizar_estadisticas()

    root.mainloop()

if __name__ == "__main__":
    main()
