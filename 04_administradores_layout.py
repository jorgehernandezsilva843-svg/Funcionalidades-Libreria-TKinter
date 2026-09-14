"""
04_administradores_layout.py
----------------------------
Demuestra y compara los 3 administradores de diseño (Geometry Managers) en Tkinter:
1. pack()  : Posicionamiento secuencial (arriba, abajo, izquierda, derecha) con fill y expand.
2. grid()  : Posicionamiento en cuadrícula (filas y columnas) con rowspan, columnspan y sticky.
3. place() : Posicionamiento absoluto y relativo por coordenadas (x, y, relx, rely).

REGLA DE ORO DE TKINTER:
Nunca mezcles .pack() y .grid() dentro del mismo contenedor padre (Frame o Tk),
ya que causará un bloqueo en la interfaz al competir por el tamaño.
"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("04 - Gestores de Diseño: pack(), grid() y place()")
    root.geometry("640x520")
    root.configure(bg="#F1F5F9")

    # Título principal
    lbl_encabezado = tk.Label(
        root,
        text="Comparativa de Layouts en Tkinter",
        font=("Segoe UI", 15, "bold"),
        bg="#F1F5F9",
        fg="#0F172A"
    )
    lbl_encabezado.pack(pady=(12, 5))

    # ==========================================
    # SECCIÓN 1: pack()
    # ==========================================
    frame_pack = tk.LabelFrame(
        root,
        text=" 1. Administrador pack() (Secuencial) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#2563EB",
        padx=10,
        pady=8
    )
    frame_pack.pack(fill="x", padx=15, pady=6)

    # Elementos apilados y distribuidos con pack
    btn_p1 = tk.Button(frame_pack, text="pack(side='left', padx=5)", bg="#DBEAFE", fg="#1E40AF")
    btn_p1.pack(side="left", padx=5)

    btn_p2 = tk.Button(frame_pack, text="pack(side='left', fill='x', expand=True)", bg="#93C5FD", fg="#1E3A8A")
    btn_p2.pack(side="left", fill="x", expand=True, padx=5)

    btn_p3 = tk.Button(frame_pack, text="pack(side='right', padx=5)", bg="#BFDBFE", fg="#1E40AF")
    btn_p3.pack(side="right", padx=5)

    # ==========================================
    # SECCIÓN 2: grid()
    # ==========================================
    frame_grid = tk.LabelFrame(
        root,
        text=" 2. Administrador grid() (Cuadrícula / Tabular) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#059669",
        padx=10,
        pady=8
    )
    frame_grid.pack(fill="x", padx=15, pady=6)

    # Configuración de pesos para que las columnas crezcan equitativamente
    frame_grid.columnconfigure(0, weight=1)
    frame_grid.columnconfigure(1, weight=1)
    frame_grid.columnconfigure(2, weight=1)

    tk.Label(frame_grid, text="Fila 0, Col 0", bg="#D1FAE5", relief="solid", bd=1).grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
    tk.Label(frame_grid, text="Fila 0, Col 1", bg="#A7F3D0", relief="solid", bd=1).grid(row=0, column=1, sticky="nsew", padx=3, pady=3)
    tk.Label(frame_grid, text="Fila 0, Col 2", bg="#6EE7B7", relief="solid", bd=1).grid(row=0, column=2, sticky="nsew", padx=3, pady=3)

    # Elemento que abarca 2 columnas (columnspan=2)
    tk.Label(frame_grid, text="Fila 1 (columnspan=2, sticky='nsew')", bg="#34D399", fg="white", relief="solid", bd=1).grid(
        row=1, column=0, columnspan=2, sticky="nsew", padx=3, pady=3
    )
    tk.Label(frame_grid, text="Fila 1, Col 2", bg="#10B981", fg="white", relief="solid", bd=1).grid(
        row=1, column=2, sticky="nsew", padx=3, pady=3
    )

    # ==========================================
    # SECCIÓN 3: place()
    # ==========================================
    frame_place = tk.LabelFrame(
        root,
        text=" 3. Administrador place() (Coordenadas Absolutas / Relativas) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#D97706",
        height=160
    )
    frame_place.pack(fill="both", expand=True, padx=15, pady=(6, 12))

    # place permite posicionar por coordenadas exactas o porcentajes relativos
    lbl_pos_abs = tk.Label(frame_place, text="place(x=15, y=20)", bg="#FEF3C7", fg="#92400E", bd=1, relief="solid")
    lbl_pos_abs.place(x=15, y=20, width=140, height=30)

    lbl_pos_rel = tk.Label(
        frame_place,
        text="place(relx=0.5, rely=0.5, anchor='center')\n[Centro Relativo]",
        bg="#FDE68A",
        fg="#78350F",
        bd=1,
        relief="solid"
    )
    lbl_pos_rel.place(relx=0.5, rely=0.55, anchor="center")

    lbl_pos_esq = tk.Label(frame_place, text="place(relx=0.98, rely=0.85, anchor='se')", bg="#FCD34D", fg="#78350F", bd=1, relief="solid")
    lbl_pos_esq.place(relx=0.98, rely=0.9, anchor="se")

    root.mainloop()

if __name__ == "__main__":
    main()
