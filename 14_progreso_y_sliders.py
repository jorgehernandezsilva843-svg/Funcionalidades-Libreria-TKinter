"""
14_progreso_y_sliders.py
------------------------
Demuestra el control de valores continuos y visualización de progreso:
1. ttk.Progressbar : Modo determinado (porcentaje 0-100%) y modo indeterminado (bucle de carga).
2. tk.Scale / ttk.Scale : Controles deslizantes (sliders) para rangos numéricos.
3. Sincronización en tiempo real entre un control deslizante y la barra de progreso.
"""

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("14 - Barras de Progreso y Sliders")
    root.geometry("540x480")
    root.configure(bg="#F8FAFC")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Barras de Progreso y Controles Deslizantes",
        font=("Segoe UI", 15, "bold"),
        bg="#F8FAFC",
        fg="#0F172A"
    ).pack(pady=(15, 12))

    # ==========================================
    # 1. CONTROLES DESLIZANTES (tk.Scale)
    # ==========================================
    frame_slider = tk.LabelFrame(
        root,
        text=" 1. Control Deslizante (tk.Scale) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#2563EB",
        padx=15,
        pady=10
    )
    frame_slider.pack(fill="x", padx=30, pady=8)

    def al_mover_slider(val):
        valor_int = int(float(val))
        barra_determinada["value"] = valor_int
        lbl_porcentaje.config(text=f"{valor_int}%")

    slider = tk.Scale(
        frame_slider,
        from_=0,
        to=100,
        orient="horizontal",
        font=("Segoe UI", 9),
        bg="#FFFFFF",
        highlightthickness=0,
        troughcolor="#E2E8F0",
        command=al_mover_slider
    )
    slider.set(35)
    slider.pack(fill="x", pady=5)

    # ==========================================
    # 2. BARRA DETERMINADA (Sincronizada)
    # ==========================================
    frame_barra_det = tk.LabelFrame(
        root,
        text=" 2. Barra de Progreso Determinada (ttk.Progressbar) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#059669",
        padx=15,
        pady=10
    )
    frame_barra_det.pack(fill="x", padx=30, pady=8)

    barra_determinada = ttk.Progressbar(
        frame_barra_det,
        orient="horizontal",
        mode="determinate",
        maximum=100,
        value=35
    )
    barra_determinada.pack(fill="x", pady=5)

    lbl_porcentaje = tk.Label(frame_barra_det, text="35%", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", fg="#059669")
    lbl_porcentaje.pack()

    # Botones de paso
    f_btns_paso = tk.Frame(frame_barra_det, bg="#FFFFFF")
    f_btns_paso.pack(pady=5)

    def alterar_paso(delta):
        nuevo_val = max(0, min(100, barra_determinada["value"] + delta))
        barra_determinada["value"] = nuevo_val
        slider.set(nuevo_val)
        lbl_porcentaje.config(text=f"{nuevo_val}%")

    tk.Button(f_btns_paso, text="-10%", command=lambda: alterar_paso(-10), bg="#E2E8F0").pack(side="left", padx=4)
    tk.Button(f_btns_paso, text="+10%", command=lambda: alterar_paso(10), bg="#E2E8F0").pack(side="left", padx=4)
    tk.Button(f_btns_paso, text="Completar 100%", command=lambda: alterar_paso(100), bg="#D1FAE5").pack(side="left", padx=4)

    # ==========================================
    # 3. BARRA INDETERMINADA (Bucle de Carga)
    # ==========================================
    frame_barra_indet = tk.LabelFrame(
        root,
        text=" 3. Barra Indeterminada (Simulación de Carga / Spinner) ",
        font=("Segoe UI", 10, "bold"),
        bg="#FFFFFF",
        fg="#D97706",
        padx=15,
        pady=10
    )
    frame_barra_indet.pack(fill="x", padx=30, pady=8)

    barra_indeterminada = ttk.Progressbar(
        frame_barra_indet,
        orient="horizontal",
        mode="indeterminate"
    )
    barra_indeterminada.pack(fill="x", pady=5)

    f_btns_indet = tk.Frame(frame_barra_indet, bg="#FFFFFF")
    f_btns_indet.pack(pady=5)

    def iniciar_carga():
        barra_indeterminada.start(10)  # milisegundos por paso

    def detener_carga():
        barra_indeterminada.stop()

    tk.Button(f_btns_indet, text="▶️ Iniciar Animación", bg="#FEF3C7", command=iniciar_carga, cursor="hand2").pack(side="left", padx=5)
    tk.Button(f_btns_indet, text="⏹️ Detener Animación", bg="#FEE2E2", command=detener_carga, cursor="hand2").pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
