"""
01_ventana_y_etiquetas.py
-------------------------
Demuestra los conceptos iniciales de Tkinter:
1. Creación de la ventana principal (root).
2. Configuración de propiedades: título, tamaño (geometry), redimensionamiento y centrado.
3. Uso del widget Label (etiquetas) con personalización de fuentes, colores, bordes y padding.
"""

import tkinter as tk

def main():
    # 1. Crear la instancia de la ventana principal
    root = tk.Tk()
    
    # 2. Configurar el título y el color de fondo de la ventana
    root.title("01 - Ventana Principal y Etiquetas (Labels)")
    root.configure(bg="#F0F4F8")
    
    # 3. Dimensiones y centrado de la ventana en la pantalla
    ancho_ventana = 520
    alto_ventana = 420
    
    # Obtenemos la resolución de la pantalla del usuario
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    
    # Calculamos las coordenadas (x, y) para que aparezca en el centro
    pos_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
    pos_y = int((alto_pantalla / 2) - (alto_ventana / 2))
    
    # Aplicamos geometría en formato: 'Ancho x Alto + X + Y'
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    
    # Permite o restringe si el usuario puede estirar la ventana (ancho, alto)
    root.resizable(True, True)
    root.minsize(400, 300)

    # 4. Creación de diferentes etiquetas (tk.Label)
    
    # Etiqueta de título principal
    lbl_titulo = tk.Label(
        root,
        text="¡Bienvenido a Tkinter!",
        font=("Helvetica", 18, "bold"),
        bg="#F0F4F8",
        fg="#1E3A8A"
    )
    lbl_titulo.pack(pady=(20, 10))

    # Etiqueta de subtítulo explicativo
    lbl_subtitulo = tk.Label(
        root,
        text="Este ejemplo muestra cómo crear una ventana y estilizar etiquetas de texto.",
        font=("Segoe UI", 10),
        bg="#F0F4F8",
        fg="#4B5563"
    )
    lbl_subtitulo.pack(pady=(0, 15))

    # Etiqueta con fondo, texto blanco y padding interno (padx / pady)
    lbl_destacada = tk.Label(
        root,
        text="Etiqueta tipo banner con fondo de color y esquinas destacadas",
        font=("Segoe UI", 11, "bold"),
        bg="#3B82F6",
        fg="#FFFFFF",
        padx=15,
        pady=10
    )
    lbl_destacada.pack(fill="x", padx=30, pady=10)

    # Etiqueta con borde y relieve (relief: solid, ridge, groove, sunken, raised)
    lbl_borde = tk.Label(
        root,
        text="Relieve: 'groove' con borde de 2px",
        font=("Consolas", 10),
        bg="#E2E8F0",
        fg="#334155",
        relief="groove",
        bd=2,
        padx=10,
        pady=8
    )
    lbl_borde.pack(pady=10)

    # Etiqueta multilínea con justificación centrada
    texto_largo = (
        "Las etiquetas pueden contener varias líneas de texto.\n"
        "Configurando 'justify' podemos alinear a la izquierda,\n"
        "al centro o a la derecha."
    )
    lbl_multilinea = tk.Label(
        root,
        text=texto_largo,
        font=("Segoe UI", 9, "italic"),
        bg="#F8FAFC",
        fg="#64748B",
        justify="center",
        relief="solid",
        bd=1,
        padx=15,
        pady=10
    )
    lbl_multilinea.pack(pady=10, padx=30, fill="x")

    # 5. Iniciar el bucle de eventos de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
