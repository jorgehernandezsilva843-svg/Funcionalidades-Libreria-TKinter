"""
04_administradores_layout.py
----------------------------
Demuestra y permite INTERACTUAR con los 3 gestores de diseño de Tkinter:
1. pack()  : Prueba cambiar la orientación (horizontal vs vertical) y expansión en vivo.
2. grid()  : Prueba alternar la cuadrícula y expansión de columnas (columnspan) en tiempo real.
3. place() : Mueve interactivamente una tarjeta arrastrándola con el mouse o con controles deslizantes X/Y.

REGLA DE ORO DE TKINTER:
Nunca mezcles .pack() y .grid() dentro del mismo contenedor padre (Frame o Tk).
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("04 - Gestores de Diseño Interactivos: pack(), grid() y place()")
    root.geometry("680x640")
    root.configure(bg="#F1F5F9")

    tk.Label(
        root,
        text="Comparativa Interactiva de Layouts en Tkinter",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    ).pack(pady=(10, 4))

    tk.Label(
        root,
        text="💡 ¡Usa los controles dentro de cada sección para ver cómo cambia el diseño en vivo!",
        font=("Segoe UI", 9, "italic"),
        bg="#F1F5F9",
        fg="#475569"
    ).pack(pady=(0, 6))

    # ==========================================
    # SECCIÓN 1: pack() INTERACTIVO
    # ==========================================
    frame_pack_padre = tk.LabelFrame(
        root,
        text=" 1. Administrador pack() (Orientación Dinámica) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#2563EB",
        padx=10,
        pady=8
    )
    frame_pack_padre.pack(fill="x", padx=15, pady=4)

    # Contenedor interno donde se empaquetan los botones
    frame_pack_demo = tk.Frame(frame_pack_padre, bg="#EFF6FF", bd=1, relief="solid", height=70)
    frame_pack_demo.pack(fill="x", expand=True, pady=(0, 6), padx=5)

    btn_p1 = tk.Button(frame_pack_demo, text="Elemento 1", bg="#93C5FD", fg="#1E3A8A")
    btn_p2 = tk.Button(frame_pack_demo, text="Elemento 2", bg="#60A5FA", fg="#1E3A8A")
    btn_p3 = tk.Button(frame_pack_demo, text="Elemento 3", bg="#3B82F6", fg="#FFFFFF")

    lbl_pack_info = tk.Label(frame_pack_padre, text="Modo actual: Horizontal con fill='x'", font=("Consolas", 9), bg="#FFFFFF", fg="#2563EB")
    lbl_pack_info.pack(anchor="w", padx=5)

    def aplicar_pack_horizontal():
        for b in (btn_p1, btn_p2, btn_p3):
            b.pack_forget()
        btn_p1.pack(side="left", padx=5, pady=5)
        btn_p2.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        btn_p3.pack(side="right", padx=5, pady=5)
        lbl_pack_info.config(text="pack(side='left', expand=True) -> Distribución horizontal")

    def aplicar_pack_vertical():
        for b in (btn_p1, btn_p2, btn_p3):
            b.pack_forget()
        btn_p1.pack(side="top", fill="x", padx=5, pady=2)
        btn_p2.pack(side="top", fill="x", padx=5, pady=2)
        btn_p3.pack(side="top", fill="x", padx=5, pady=2)
        lbl_pack_info.config(text="pack(side='top', fill='x') -> Apilados verticalmente")

    aplicar_pack_horizontal()

    frame_pack_ctrls = tk.Frame(frame_pack_padre, bg="#FFFFFF")
    frame_pack_ctrls.pack(fill="x", pady=(4, 0))
    tk.Button(frame_pack_ctrls, text="↔ Modo Horizontal", bg="#DBEAFE", command=aplicar_pack_horizontal, cursor="hand2").pack(side="left", padx=4)
    tk.Button(frame_pack_ctrls, text="↕ Modo Vertical", bg="#DBEAFE", command=aplicar_pack_vertical, cursor="hand2").pack(side="left", padx=4)

    # ==========================================
    # SECCIÓN 2: grid() INTERACTIVO
    # ==========================================
    frame_grid_padre = tk.LabelFrame(
        root,
        text=" 2. Administrador grid() (Cuadrícula y Columnspan) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#059669",
        padx=10,
        pady=8
    )
    frame_grid_padre.pack(fill="x", padx=15, pady=4)

    frame_grid_demo = tk.Frame(frame_grid_padre, bg="#F0FDF4", bd=1, relief="solid")
    frame_grid_demo.pack(fill="x", expand=True, pady=(0, 6), padx=5)

    frame_grid_demo.columnconfigure(0, weight=1)
    frame_grid_demo.columnconfigure(1, weight=1)
    frame_grid_demo.columnconfigure(2, weight=1)

    tk.Label(frame_grid_demo, text="Fila 0, Col 0", bg="#D1FAE5", relief="solid", bd=1).grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    tk.Label(frame_grid_demo, text="Fila 0, Col 1", bg="#A7F3D0", relief="solid", bd=1).grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
    tk.Label(frame_grid_demo, text="Fila 0, Col 2", bg="#6EE7B7", relief="solid", bd=1).grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

    lbl_dinamico = tk.Label(frame_grid_demo, text="Fila 1: Abarca 2 columnas", bg="#059669", fg="white", relief="solid", bd=1)
    lbl_dinamico.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)

    lbl_fijo = tk.Label(frame_grid_demo, text="Fila 1, Col 2", bg="#10B981", fg="white", relief="solid", bd=1)
    lbl_fijo.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

    span_estado = {"ancho": 2}

    def alternar_columnspan():
        if span_estado["ancho"] == 2:
            lbl_dinamico.grid_configure(columnspan=1)
            lbl_dinamico.config(text="Fila 1: Abarca 1 columna")
            span_estado["ancho"] = 1
        else:
            lbl_dinamico.grid_configure(columnspan=2)
            lbl_dinamico.config(text="Fila 1: Abarca 2 columnas")
            span_estado["ancho"] = 2

    tk.Button(frame_grid_padre, text="🔄 Alternar Ancho de Celda (columnspan)", bg="#D1FAE5", command=alternar_columnspan, cursor="hand2").pack(anchor="w", padx=5)

    # ==========================================
    # SECCIÓN 3: place() INTERACTIVO (Arrastre y Sliders)
    # ==========================================
    frame_place_padre = tk.LabelFrame(
        root,
        text=" 3. Administrador place() (¡Arrastra la tarjeta o usa los sliders!) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#D97706",
        padx=10,
        pady=8
    )
    frame_place_padre.pack(fill="both", expand=True, padx=15, pady=(4, 10))

    # Área de coordenadas
    area_place = tk.Frame(frame_place_padre, bg="#FFFBEB", bd=1, relief="solid", height=140)
    area_place.pack(fill="both", expand=True, padx=5, pady=4)
    area_place.pack_propagate(False)

    # Tarjeta arrastrable con place
    tarjeta = tk.Label(
        area_place,
        text="✋ ¡Arrastrame!\nplace(x=30, y=20)",
        bg="#F59E0B",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="raised",
        bd=2,
        cursor="fleur"
    )
    tarjeta.place(x=30, y=20, width=150, height=45)

    coords = {"x": 30, "y": 20, "start_x": 0, "start_y": 0}

    def al_click_tarjeta(event):
        coords["start_x"] = event.x
        coords["start_y"] = event.y

    def al_arrastrar_tarjeta(event):
        delta_x = event.x - coords["start_x"]
        delta_y = event.y - coords["start_y"]
        nuevo_x = max(0, min(area_place.winfo_width() - 150, tarjeta.winfo_x() + delta_x))
        nuevo_y = max(0, min(area_place.winfo_height() - 45, tarjeta.winfo_y() + delta_y))
        tarjeta.place(x=nuevo_x, y=nuevo_y)
        tarjeta.config(text=f"✋ ¡Arrastrame!\nplace(x={nuevo_x}, y={nuevo_y})")
        slider_x.set(nuevo_x)
        slider_y.set(nuevo_y)

    tarjeta.bind("<ButtonPress-1>", al_click_tarjeta)
    tarjeta.bind("<B1-Motion>", al_arrastrar_tarjeta)

    # Sliders para mover con control numérico
    frame_sliders = tk.Frame(frame_place_padre, bg="#FFFFFF")
    frame_sliders.pack(fill="x", pady=2)

    def al_mover_slider(val):
        x = slider_x.get()
        y = slider_y.get()
        tarjeta.place(x=x, y=y)
        tarjeta.config(text=f"✋ ¡Arrastrame!\nplace(x={x}, y={y})")

    tk.Label(frame_sliders, text="Eje X:", bg="#FFFFFF", font=("Segoe UI", 9)).pack(side="left", padx=2)
    slider_x = tk.Scale(frame_sliders, from_=0, to=450, orient="horizontal", command=al_mover_slider, bg="#FFFFFF", highlightthickness=0)
    slider_x.set(30)
    slider_x.pack(side="left", fill="x", expand=True, padx=4)

    tk.Label(frame_sliders, text="Eje Y:", bg="#FFFFFF", font=("Segoe UI", 9)).pack(side="left", padx=2)
    slider_y = tk.Scale(frame_sliders, from_=0, to=90, orient="horizontal", command=al_mover_slider, bg="#FFFFFF", highlightthickness=0)
    slider_y.set(20)
    slider_y.pack(side="left", fill="x", expand=True, padx=4)

    root.mainloop()

if __name__ == "__main__":
    main()
