"""
11_canvas_graficos.py
---------------------
Demuestra el uso del lienzo gráfico interactivo (tk.Canvas):
1. Dibujo de formas geométricas vectoriales: líneas, rectángulos, óvalos/círculos, polígonos y texto.
2. Manipulación de propiedades visuales: colores de relleno (fill), contornos (outline) y grosor (width).
3. Interactividad: objeto arrastrable con el ratón (Drag and Drop interactivo usando eventos).
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("11 - Lienzo Gráfico Interactivo (Canvas)")
    root.geometry("640x540")
    root.configure(bg="#F1F5F9")

    tk.Label(
        root,
        text="Lienzo Gráfico (Canvas): Formas Vectoriales e Interactividad",
        font=("Segoe UI", 14, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(12, 5))

    lbl_info = tk.Label(
        root,
        text="💡 Haz clic y arrastra el círculo verde con el ratón para moverlo",
        font=("Segoe UI", 10, "italic"),
        bg="#F1F5F9",
        fg="#475569"
    )
    lbl_info.pack(pady=(0, 8))

    # Crear el Canvas con fondo blanco y borde definido
    canvas = tk.Canvas(root, bg="#FFFFFF", bd=2, relief="groove")
    canvas.pack(fill="both", expand=True, padx=20, pady=5)

    # 1. Dibujar figuras estáticas de muestra
    # Líneas y cuadrícula
    canvas.create_line(20, 30, 200, 30, fill="#94A3B8", width=3, dash=(4, 2))
    canvas.create_text(110, 15, text="Línea punteada", font=("Segoe UI", 9), fill="#64748B")

    # Rectángulo estilizado
    canvas.create_rectangle(30, 60, 190, 150, fill="#DBEAFE", outline="#2563EB", width=2)
    canvas.create_text(110, 105, text="Rectángulo\n(fill + outline)", font=("Segoe UI", 10, "bold"), fill="#1E40AF", justify="center")

    # Polígono (triángulo / diamante)
    puntos_triangulo = [110, 180, 40, 270, 180, 270]
    canvas.create_polygon(puntos_triangulo, fill="#FEF3C7", outline="#D97706", width=2)
    canvas.create_text(110, 240, text="Polígono", font=("Segoe UI", 10), fill="#B45309")

    # Óvalo / Círculo estático
    canvas.create_oval(250, 50, 390, 150, fill="#FCE7F3", outline="#DB2777", width=2)
    canvas.create_text(320, 100, text="Óvalo Elíptico", font=("Segoe UI", 10, "bold"), fill="#9D174D")

    # 2. Objeto interactivo: Círculo Arrastrable
    # create_oval(x1, y1, x2, y2)
    obj_arrastrable = canvas.create_oval(440, 70, 540, 170, fill="#34D399", outline="#059669", width=3, tags="movible")
    texto_arrastrable = canvas.create_text(490, 120, text="¡Arrastra!", font=("Segoe UI", 10, "bold"), fill="#064E3B", tags="movible")

    # Variables de seguimiento de arrastre
    estado_arrastre = {"x": 0, "y": 0}

    def al_iniciar_arrastre(event):
        estado_arrastre["x"] = event.x
        estado_arrastre["y"] = event.y

    def al_mover_objeto(event):
        delta_x = event.x - estado_arrastre["x"]
        delta_y = event.y - estado_arrastre["y"]
        # Mover tanto el círculo como el texto asociado con el tag 'movible'
        canvas.move("movible", delta_x, delta_y)
        estado_arrastre["x"] = event.x
        estado_arrastre["y"] = event.y

    # Asociar eventos directamente al tag "movible"
    canvas.tag_bind("movible", "<ButtonPress-1>", al_iniciar_arrastre)
    canvas.tag_bind("movible", "<B1-Motion>", al_mover_objeto)

    # 3. Dibujo libre al hacer clic en el fondo
    def dibujar_punto(event):
        # Si no se hizo clic en un objeto existente, creamos una pequeña marca
        radio = 6
        canvas.create_oval(
            event.x - radio, event.y - radio,
            event.x + radio, event.y + radio,
            fill="#6366F1", outline=""
        )

    # Doble clic para estampar un punto en el lienzo
    canvas.bind("<Double-Button-1>", dibujar_punto)

    # Barra inferior de acciones
    frame_acciones = tk.Frame(root, bg="#F1F5F9")
    frame_acciones.pack(fill="x", padx=20, pady=8)

    tk.Label(frame_acciones, text="💡 Tip: Haz doble clic en cualquier zona vacía para estampar puntos violetas.", font=("Segoe UI", 9), bg="#F1F5F9", fg="#475569").pack(side="left")

    def reiniciar_lienzo():
        canvas.coords(obj_arrastrable, 440, 70, 540, 170)
        canvas.coords(texto_arrastrable, 490, 120)

    btn_reset = tk.Button(frame_acciones, text="Restablecer Posición", bg="#E2E8F0", command=reiniciar_lienzo, cursor="hand2")
    btn_reset.pack(side="right")

    root.mainloop()

if __name__ == "__main__":
    main()
