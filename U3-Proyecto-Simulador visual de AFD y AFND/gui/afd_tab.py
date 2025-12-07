import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from automata.dfa import DFA
from utils.helpers import parse_set
from utils.visualizer import draw_automaton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AFDTab(ttk.Frame):
    def __init__(self, app, notebook):
        super().__init__(notebook)
        self.app = app
        self.canvas = None
        self._build_ui()

    def _build_ui(self):
        left = ttk.Frame(self)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        right = ttk.Frame(self)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # -------- Definición del AFD --------
        frm_def = ttk.LabelFrame(left, text="Definición de AFD")
        frm_def.pack(fill=tk.X, pady=5)

        ttk.Label(frm_def, text="Alfabeto (a,b,...)").grid(row=0, column=0, sticky="w")
        self.entry_alpha = ttk.Entry(frm_def, width=30)
        self.entry_alpha.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frm_def, text="Estados (q0,q1,...)").grid(row=1, column=0, sticky="w")
        self.entry_states = ttk.Entry(frm_def, width=30)
        self.entry_states.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frm_def, text="Estado inicial").grid(row=2, column=0, sticky="w")
        self.entry_start = ttk.Entry(frm_def, width=30)
        self.entry_start.grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(frm_def, text="Estados finales").grid(row=3, column=0, sticky="w")
        self.entry_finals = ttk.Entry(frm_def, width=30)
        self.entry_finals.grid(row=3, column=1, padx=5, pady=2)

        ttk.Label(frm_def, text="Transiciones (q0,a,q1)").grid(
            row=4, column=0, columnspan=2, sticky="w"
        )
        self.txt_trans = scrolledtext.ScrolledText(frm_def, width=40, height=8)
        self.txt_trans.grid(row=5, column=0, columnspan=2, pady=3)

        ttk.Button(frm_def, text="Crear / Actualizar AFD",
                   command=self.crear_afd).grid(row=6, column=0, columnspan=2, pady=5)

        # -------- Simulación --------
        frm_sim = ttk.LabelFrame(left, text="Simulación")
        frm_sim.pack(fill=tk.X, pady=5)

        ttk.Label(frm_sim, text="Cadena:").grid(row=0, column=0, sticky="w")
        self.entry_cadena = ttk.Entry(frm_sim, width=30)
        self.entry_cadena.grid(row=0, column=1, padx=5, pady=2)

        ttk.Button(frm_sim, text="Simular AFD",
                   command=self.simular).grid(row=1, column=0, columnspan=2, pady=5)

        ttk.Button(frm_sim, text="Dibujar AFD",
                   command=self.dibujar).grid(row=2, column=0, columnspan=2, pady=5)

        # -------- Log --------
        frm_log = ttk.LabelFrame(right, text="Pasos de simulación")
        frm_log.pack(fill=tk.BOTH, expand=True, pady=5)

        self.txt_log = scrolledtext.ScrolledText(frm_log, width=60, height=15, state="disabled")
        self.txt_log.pack(fill=tk.BOTH, expand=True)

        # -------- Área gráfica --------
        frm_graf = ttk.LabelFrame(right, text="Visualización AFD")
        frm_graf.pack(fill=tk.BOTH, expand=True, pady=5)

        self.frame_graph = ttk.Frame(frm_graf)
        self.frame_graph.pack(fill=tk.BOTH, expand=True)

    # -------- Crear AFD --------
    def crear_afd(self):
        try:
            alphabet = parse_set(self.entry_alpha.get())
            states = parse_set(self.entry_states.get())
            start = self.entry_start.get().strip()
            finals = parse_set(self.entry_finals.get())

            if start not in states:
                messagebox.showerror("Error", "El estado inicial no pertenece al conjunto.")
                return
            if not finals.issubset(states):
                messagebox.showerror("Error", "Estados finales inválidos.")
                return

            transitions = {}
            lines = self.txt_trans.get("1.0", tk.END).strip().splitlines()

            for line in lines:
                if not line.strip():
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    messagebox.showerror("Error", f"Formato inválido: {line}")
                    return
                src, sym, dst = parts

                if src not in states or dst not in states:
                    messagebox.showerror("Error", f"Transición inválida: {line}")
                    return

                transitions[(src, sym)] = dst

            self.app.afd = DFA(states, alphabet, transitions, start, finals)
            messagebox.showinfo("AFD", "AFD creado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

    # -------- Simular --------
    def simular(self):
        if self.app.afd is None:
            messagebox.showwarning("AFD", "Debe crear el AFD primero.")
            return

        cadena = self.entry_cadena.get()
        result = self.app.afd.simulate_steps(cadena)

        self.txt_log.configure(state="normal")
        self.txt_log.delete("1.0", tk.END)

        self.txt_log.insert(tk.END, f"Simulación de '{cadena}' en AFD\n\n")

        for paso in result["steps"]:
            self.txt_log.insert(
                tk.END,
                f"Paso {paso['step']}: {paso['from']} --{paso['symbol']}--> {paso['to']}\n"
            )

        if result["error"]:
            self.txt_log.insert(tk.END, f"\n[Error] {result['error']}\n")
        else:
            self.txt_log.insert(tk.END, f"\nEstado final: {result['final_state']}\n")
            self.txt_log.insert(tk.END,
                                "Resultado: ACEPTADA\n" if result["accepted"]
                                else "Resultado: NO aceptada\n")

        self.txt_log.configure(state="disabled")

    # -------- Dibujar --------
    def dibujar(self):
        if self.app.afd is None:
            messagebox.showwarning("AFD", "Debe crear el AFD primero.")
            return

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        fig = draw_automaton(self.app.afd)

        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
