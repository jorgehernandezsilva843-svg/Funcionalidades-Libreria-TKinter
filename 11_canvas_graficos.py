"""
11_canvas_graficos.py
---------------------
Demuestra el uso del lienzo gráfico interactivo (tk.Canvas) con MANIPULACIÓN TOTAL:
1. Dibujo de formas vectoriales: rectángulos, círculos, triángulos, estrellas y texto.
2. Interactividad universal: ¡TODAS las figuras se pueden tocar y arrastrar con el mouse!
3. Al hacer clic en cualquier figura, pasa al frente visualmente (tag_raise).
4. Doble clic en cualquier zona vacía crea una nueva forma en esa posición.
"""

import tkinter as tk
import random

def main():
    root = tk.Tk()
    root.title("11 - Lienzo Canvas Interactivo (¡Todas las figuras son manipulables!)")
    root.geometry("700x580")
    root.configure(bg="#F1F5F9")

    tk.Label(
        root,
        text="Lienzo Gráfico: Manipula y Arrastra CUALQUIER Figura",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(12, 4))

    lbl_info = tk.Label(
        root,
        text="🖐️ Haz clic y mantén presionado sobre CUALQUIER figura para moverla por el lienzo",
        font=("Segoe UI", 10, "italic"),
        bg="#F1F5F9",
        fg="#2563EB"
    )
    lbl_info.pack(pady=(0, 6))

    # Lienzo principal
    canvas = tk.Canvas(root, bg="#FFFFFF", bd=2, relief="groove")
    canvas.pack(fill="both", expand=True, padx=20, pady=5)

    # Estado del arrastre
    drag_data = {"x": 0, "y": 0, "item": None}

    def al_hacer_click(event):
        # Detecta qué elemento está debajo del cursor
        items = canvas.find_withtag("current")
        if items:
            item = items[0]
            # Traer la figura al frente para que no quede detrás de otras al arrastrar
            canvas.tag_raise(item)
            drag_data["item"] = item
            drag_data["x"] = event.x
            drag_data["y"] = event.y
            tipo = canvas.type(item)
            lbl_info.config(text=f"Moviendo figura: '{tipo}' (ID: {item})", fg="#16A34A")

    def al_arrastrar(event):
        if drag_data["item"]:
            delta_x = event.x - drag_data["x"]
            delta_y = event.y - drag_data["y"]
            canvas.move(drag_data["item"], delta_x, delta_y)
            drag_data["x"] = event.x
            drag_data["y"] = event.y

    def al_soltar(event):
        drag_data["item"] = None
        lbl_info.config(text="🖐️ Arrastre finalizado. Puedes seleccionar cualquier otra figura.", fg="#2563EB")

    # Vinculamos los eventos de ratón para cualquier elemento arrastrable
    canvas.tag_bind("arrastrable", "<ButtonPress-1>", al_hacer_click)
    canvas.tag_bind("arrastrable", "<B1-Motion>", al_arrastrar)
    canvas.tag_bind("arrastrable", "<ButtonRelease-1>", al_soltar)

    # ==========================================
    # CREACIÓN DE FIGURAS INICIALES (Todas arrastrables)
    # ==========================================
    def dibujar_figuras_iniciales():
        canvas.delete("all")

        # 1. Rectángulo azul
        canvas.create_rectangle(40, 50, 180, 140, fill="#60A5FA", outline="#1D4ED8", width=3, tags="arrastrable")

        # 2. Triángulo amarillo
        canvas.create_polygon([120, 180, 50, 290, 190, 290], fill="#FDE047", outline="#CA8A04", width=3, tags="arrastrable")

        # 3. Óvalo rosa
        canvas.create_oval(240, 60, 390, 160, fill="#F472B6", outline="#BE185D", width=3, tags="arrastrable")

        # 4. Círculo verde con etiqueta
        canvas.create_oval(450, 70, 560, 180, fill="#34D399", outline="#059669", width=3, tags="arrastrable")

        # 5. Estrella / Polígono naranja de 5 puntas
        puntos_estrella = [
            300, 220, 320, 270, 370, 270, 330, 300,
            350, 350, 300, 320, 250, 350, 270, 300,
            230, 270, 280, 270
        ]
        canvas.create_polygon(puntos_estrella, fill="#FB923C", outline="#C2410C", width=2, tags="arrastrable")

        # 6. Tarjeta de texto arrastrable
        canvas.create_rectangle(430, 240, 610, 310, fill="#C7D2FE", outline="#4338CA", width=2, tags="arrastrable")
        canvas.create_text(520, 275, text="¡Incluso este texto\nes arrastrable!", font=("Segoe UI", 10, "bold"), fill="#1E1B4B", tags="arrastrable")

    dibujar_figuras_iniciales()

    # Doble clic para añadir nuevas figuras en la posición del cursor
    COLORES = ["#F87171", "#FB923C", "#FBBF24", "#34D399", "#60A5FA", "#A78BFA", "#F472B6"]

    def al_doble_click(event):
        color = random.choice(COLORES)
        radio = random.randint(25, 45)
        canvas.create_oval(
            event.x - radio, event.y - radio,
            event.x + radio, event.y + radio,
            fill=color, outline="#1E293B", width=2,
            tags="arrastrable"
        )
        lbl_info.config(text=f"✨ Círculo nuevo añadido en ({event.x}, {event.y}). ¡También lo puedes arrastrar!", fg="#7C3AED")

    canvas.bind("<Double-Button-1>", al_doble_click)

    # Barra inferior de acciones
    frame_acciones = tk.Frame(root, bg="#F1F5F9")
    frame_acciones.pack(fill="x", padx=20, pady=8)

    tk.Label(frame_acciones, text="💡 Tip: Haz doble clic en el lienzo para crear nuevas figuras.", font=("Segoe UI", 9), bg="#F1F5F9", fg="#475569").pack(side="left")

    btn_reset = tk.Button(frame_acciones, text="🔄 Restablecer Lienzo", bg="#E2E8F0", command=dibujar_figuras_iniciales, cursor="hand2")
    btn_reset.pack(side="right")

    root.mainloop()

if __name__ == "__main__":
    main()
