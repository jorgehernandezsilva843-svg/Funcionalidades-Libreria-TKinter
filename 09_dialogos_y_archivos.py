"""
09_dialogos_y_archivos.py
-------------------------
Demuestra la interacción mediante diálogos modales nativos del sistema operativo:
1. messagebox : Mensajes de información, advertencia, error y confirmación (askyesno, askokcancel).
2. filedialog : Selectores de archivos para abrir (askopenfilename), guardar (asksaveasfilename) y directorios (askdirectory).
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def main():
    root = tk.Tk()
    root.title("09 - Cuadros de Diálogo y Manejo de Archivos")
    root.geometry("540x500")
    root.configure(bg="#F8FAFC")
    root.resizable(False, False)

    # Título principal
    tk.Label(
        root,
        text="Diálogos Nativos del Sistema",
        font=("Segoe UI", 15, "bold"),
        bg="#F8FAFC",
        fg="#0F172A"
    ).pack(pady=(15, 10))

    # Etiqueta de resultado
    lbl_resultado = tk.Label(
        root,
        text="Haz clic en cualquier botón para abrir un diálogo modal",
        font=("Segoe UI", 10),
        bg="#E2E8F0",
        fg="#1E293B",
        relief="groove",
        padx=15,
        pady=10,
        wraplength=480
    )
    lbl_resultado.pack(fill="x", padx=30, pady=10)

    # ==========================================
    # SECCIÓN 1: Mensajes y Alertas (messagebox)
    # ==========================================
    frame_msg = tk.LabelFrame(
        root,
        text=" 1. Cuadros de Mensaje (messagebox) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#2563EB",
        padx=10,
        pady=10
    )
    frame_msg.pack(fill="x", padx=30, pady=6)

    def mostrar_info():
        messagebox.showinfo("Información", "Esta es una ventana de información estándar.")
        lbl_resultado.config(text="Se mostró un diálogo de tipo Info", fg="#2563EB")

    def mostrar_warning():
        messagebox.showwarning("Advertencia", "¡Atención! Este es un mensaje de precaución.")
        lbl_resultado.config(text="Se mostró un diálogo de tipo Advertencia", fg="#D97706")

    def mostrar_error():
        messagebox.showerror("Error Crítico", "Ha ocurrido una falla simulada en el proceso.")
        lbl_resultado.config(text="Se mostró un diálogo de tipo Error", fg="#DC2626")

    def mostrar_pregunta():
        respuesta = messagebox.askyesno("Confirmación", "¿Deseas guardar los cambios antes de salir?")
        if respuesta:
            lbl_resultado.config(text="Respuesta del usuario: SÍ (True)", fg="#16A34A")
        else:
            lbl_resultado.config(text="Respuesta del usuario: NO (False)", fg="#DC2626")

    f_sub_msg = tk.Frame(frame_msg, bg="#FFFFFF")
    f_sub_msg.pack(fill="x")
    tk.Button(f_sub_msg, text="ℹ️ Info", command=mostrar_info, width=10, bg="#DBEAFE").pack(side="left", padx=4)
    tk.Button(f_sub_msg, text="⚠️ Aviso", command=mostrar_warning, width=10, bg="#FEF3C7").pack(side="left", padx=4)
    tk.Button(f_sub_msg, text="❌ Error", command=mostrar_error, width=10, bg="#FEE2E2").pack(side="left", padx=4)
    tk.Button(f_sub_msg, text="❓ Pregunta", command=mostrar_pregunta, width=10, bg="#E0E7FF").pack(side="left", padx=4)

    # ==========================================
    # SECCIÓN 2: Selectores de Archivos (filedialog)
    # ==========================================
    frame_files = tk.LabelFrame(
        root,
        text=" 2. Explorador de Archivos (filedialog) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#059669",
        padx=10,
        pady=10
    )
    frame_files.pack(fill="x", padx=30, pady=10)

    def abrir_archivo():
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos Python", "*.py"), ("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            lbl_resultado.config(text=f"📂 Archivo para abrir:\n{ruta}", fg="#059669")
        else:
            lbl_resultado.config(text="Apertura de archivo cancelada.", fg="#64748B")

    def guardar_archivo():
        ruta = filedialog.asksaveasfilename(
            title="Guardar archivo como...",
            defaultextension=".txt",
            filetypes=[("Documento de texto", "*.txt"), ("Archivo Python", "*.py")]
        )
        if ruta:
            lbl_resultado.config(text=f"💾 Archivo destino seleccionado:\n{ruta}", fg="#2563EB")
        else:
            lbl_resultado.config(text="Guardado de archivo cancelado.", fg="#64748B")

    def elegir_carpeta():
        directorio = filedialog.askdirectory(title="Selecciona un directorio")
        if directorio:
            lbl_resultado.config(text=f"📁 Carpeta seleccionada:\n{directorio}", fg="#7C3AED")
        else:
            lbl_resultado.config(text="Selección de carpeta cancelada.", fg="#64748B")

    tk.Button(frame_files, text="📂 Abrir Archivo...", command=abrir_archivo, bg="#D1FAE5", cursor="hand2").pack(fill="x", pady=3)
    tk.Button(frame_files, text="💾 Guardar Como...", command=guardar_archivo, bg="#E0F2FE", cursor="hand2").pack(fill="x", pady=3)
    tk.Button(frame_files, text="📁 Seleccionar Carpeta...", command=elegir_carpeta, bg="#EDE9FE", cursor="hand2").pack(fill="x", pady=3)

    root.mainloop()

if __name__ == "__main__":
    main()
