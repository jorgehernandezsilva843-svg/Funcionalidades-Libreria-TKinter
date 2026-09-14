"""
10_menus_y_contextual.py
------------------------
Demuestra la arquitectura completa de menús conectada a ACCIONES REALES:
1. Barra de menú superior (tk.Menu con cascade): Archivo, Ver y Ayuda.
2. Integración real con filedialog: 'Abrir...' abre el explorador de archivos de Windows y carga el contenido en el editor.
3. 'Guardar' permite guardar el texto en tu computadora.
4. Separadores visuales, atajos de teclado (Ctrl+N, Ctrl+O, Ctrl+S) y modo oscuro.
5. Menú contextual emergente (clic derecho) con Copiar, Pegar y Limpiar.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def main():
    root = tk.Tk()
    root.title("10 - Menús de Ventana y Menú Contextual (Conectado a Archivos Reales)")
    root.geometry("600x480")
    root.configure(bg="#F8FAFC")

    # Encabezado explicativo
    frame_top = tk.Frame(root, bg="#F8FAFC", padx=20, pady=10)
    frame_top.pack(fill="x")

    lbl_titulo = tk.Label(
        frame_top,
        text="Mini Bloc de Notas con Barra de Menús",
        font=("Segoe UI", 14, "bold"),
        bg="#F8FAFC",
        fg="#0F172A"
    )
    lbl_titulo.pack(anchor="w")

    lbl_estado = tk.Label(
        frame_top,
        text="Usa 'Archivo > Abrir...' para cargar un archivo real desde tu computadora o haz clic derecho",
        font=("Segoe UI", 9, "italic"),
        bg="#F8FAFC",
        fg="#475569"
    )
    lbl_estado.pack(anchor="w", pady=(2, 0))

    # Editor de texto central
    editor = tk.Text(root, font=("Consolas", 11), wrap="word", padx=10, pady=10, relief="solid", bd=1)
    editor.pack(fill="both", expand=True, padx=20, pady=5)
    editor.insert("1.0", "¡Hola! Este editor está conectado al menú superior.\n\nPuedes probar:\n1. Archivo > Abrir... (o presiona Ctrl+O) para cargar cualquier archivo .txt o .py de tu PC.\n2. Archivo > Guardar (o presiona Ctrl+S) para guardar tus cambios.\n3. Haz CLIC DERECHO aquí adentro para ver el menú contextual de copiar/pegar.")

    # ==========================================
    # FUNCIONES DE ARCHIVO REALES
    # ==========================================
    def nuevo_documento(event=None):
        if editor.get("1.0", "end-1c").strip():
            if messagebox.askyesno("Nuevo Documento", "¿Deseas vaciar el editor para iniciar un nuevo documento?"):
                editor.delete("1.0", tk.END)
                lbl_estado.config(text="Nuevo documento en blanco", fg="#2563EB")
        else:
            editor.delete("1.0", tk.END)

    def abrir_archivo_real(event=None):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo para abrir",
            filetypes=[("Archivos de Texto y Código", "*.txt;*.py;*.md;*.json"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
                    contenido = f.read()
                editor.delete("1.0", tk.END)
                editor.insert("1.0", contenido)
                lbl_estado.config(text=f"📂 Archivo cargado con éxito: {ruta}", fg="#16A34A")
            except Exception as e:
                messagebox.showerror("Error al abrir", f"No se pudo leer el archivo:\n{e}")
        else:
            lbl_estado.config(text="Apertura de archivo cancelada", fg="#64748B")

    def guardar_archivo_real(event=None):
        ruta = filedialog.asksaveasfilename(
            title="Guardar archivo como...",
            defaultextension=".txt",
            filetypes=[("Archivo de Texto", "*.txt"), ("Archivo Python", "*.py"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            try:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(editor.get("1.0", "end-1c"))
                lbl_estado.config(text=f"💾 Guardado correctamente en: {ruta}", fg="#16A34A")
                messagebox.showinfo("Guardado", "El archivo fue guardado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo:\n{e}")

    # ==========================================
    # 1. BARRA DE MENÚ SUPERIOR
    # ==========================================
    barra_menu = tk.Menu(root)

    # --- Menú Archivo ---
    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", command=nuevo_documento)
    menu_archivo.add_command(label="Abrir...", accelerator="Ctrl+O", command=abrir_archivo_real)
    menu_archivo.add_command(label="Guardar Como...", accelerator="Ctrl+S", command=guardar_archivo_real)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", accelerator="Alt+F4", command=root.quit)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

    # --- Menú Ver (con Modo Oscuro) ---
    menu_ver = tk.Menu(barra_menu, tearoff=0)
    modo_oscuro = tk.BooleanVar(value=False)

    def cambiar_tema():
        if modo_oscuro.get():
            root.configure(bg="#0F172A")
            frame_top.configure(bg="#0F172A")
            lbl_titulo.configure(bg="#0F172A", fg="#F8FAFC")
            lbl_estado.configure(bg="#0F172A", fg="#38BDF8")
            editor.configure(bg="#1E293B", fg="#F8FAFC", insertbackground="white")
        else:
            root.configure(bg="#F8FAFC")
            frame_top.configure(bg="#F8FAFC")
            lbl_titulo.configure(bg="#F8FAFC", fg="#0F172A")
            lbl_estado.configure(bg="#F8FAFC", fg="#475569")
            editor.configure(bg="#FFFFFF", fg="#000000", insertbackground="black")

    menu_ver.add_checkbutton(label="Modo Oscuro", variable=modo_oscuro, command=cambiar_tema)
    barra_menu.add_cascade(label="Ver", menu=menu_ver)

    # --- Menú Ayuda ---
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    menu_ayuda.add_command(label="Acerca de...", command=lambda: messagebox.showinfo("Acerca de", "Demostración interactiva de Menús conectada a archivos del sistema en Python."))
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    root.config(menu=barra_menu)

    # Atajos de teclado en la ventana
    root.bind("<Control-n>", nuevo_documento)
    root.bind("<Control-o>", abrir_archivo_real)
    root.bind("<Control-s>", guardar_archivo_real)

    # ==========================================
    # 2. MENÚ CONTEXTUAL (Clic Derecho)
    # ==========================================
    menu_contextual = tk.Menu(root, tearoff=0)
    menu_contextual.add_command(label="📋 Copiar", command=lambda: editor.event_generate("<<Copy>>"))
    menu_contextual.add_command(label="✂️ Cortar", command=lambda: editor.event_generate("<<Cut>>"))
    menu_contextual.add_command(label="📌 Pegar", command=lambda: editor.event_generate("<<Paste>>"))
    menu_contextual.add_separator()
    menu_contextual.add_command(label="🗑️ Limpiar Todo", command=lambda: editor.delete("1.0", tk.END))

    def mostrar_menu_contextual(event):
        try:
            menu_contextual.tk_popup(event.x_root, event.y_root)
        finally:
            menu_contextual.grab_release()

    editor.bind("<Button-3>", mostrar_menu_contextual)

    root.mainloop()

if __name__ == "__main__":
    main()
