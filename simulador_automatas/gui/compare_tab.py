import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox


class CompareTab(ttk.Frame):
    def __init__(self, app, notebook):
        super().__init__(notebook)
        self.app = app
        self._build_ui()

    def _build_ui(self):
        top = ttk.Frame(self)
        top.pack(fill=tk.X, pady=5)

        ttk.Label(top, text="Cadena: ").grid(row=0, column=0)
        self.entry_cadena = ttk.Entry(top, width=40)
        self.entry_cadena.grid(row=0, column=1, padx=5)

        ttk.Button(top, text="Comparar", command=self.comparar).grid(row=0, column=2, padx=5)

        middle = ttk.Frame(self)
        middle.pack(fill=tk.BOTH, expand=True, padx=5)

        frm_afd = ttk.LabelFrame(middle, text="Resultado AFD")
        frm_afd.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.log_afd = scrolledtext.ScrolledText(frm_afd, width=45, height=25, state="disabled")
        self.log_afd.pack(fill=tk.BOTH, expand=True)

        frm_afnd = ttk.LabelFrame(middle, text="Resultado AFND")
        frm_afnd.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.log_afnd = scrolledtext.ScrolledText(frm_afnd, width=45, height=25, state="disabled")
        self.log_afnd.pack(fill=tk.BOTH, expand=True)

    def comparar(self):
        if self.app.afd is None or self.app.afnd is None:
            messagebox.showwarning("Error", "Debe definir primero AFD y AFND.")
            return

        cadena = self.entry_cadena.get()

        res_afd = self.app.afd.simulate_steps(cadena)
        res_afnd = self.app.afnd.simulate_steps(cadena)

        # ---- Log AFD ----
        self.log_afd.configure(state="normal")
        self.log_afd.delete("1.0", tk.END)
        self.log_afd.insert(tk.END, f"Simulación AFD para '{cadena}'\n\n")

        for paso in res_afd["steps"]:
            self.log_afd.insert(tk.END, f"{paso['from']} --{paso['symbol']}--> {paso['to']}\n")

        self.log_afd.insert(
            tk.END,
            "\nResultado: ACEPTADA\n" if res_afd["accepted"] else "\nResultado: NO aceptada\n"
        )
        self.log_afd.configure(state="disabled")

        # ---- Log AFND ----
        self.log_afnd.configure(state="normal")
        self.log_afnd.delete("1.0", tk.END)
        self.log_afnd.insert(tk.END, f"Simulación AFND para '{cadena}'\n\n")

        for paso in res_afnd["steps"]:
            if paso["type"] == "init":
                self.log_afnd.insert(tk.END, f"Inicial: {paso['states']}\n")
            else:
                self.log_afnd.insert(tk.END, f"Paso {paso['step']} '{paso['symbol']}'\n")
                for o, s, d in paso["moves"]:
                    self.log_afnd.insert(tk.END, f"  {o} --{s}--> {d}\n")
                self.log_afnd.insert(tk.END, f"Cierre-ε: {paso['after_epsilon']}\n\n")

        self.log_afnd.insert(
            tk.END,
            "Resultado: ACEPTADA\n" if res_afnd["accepted"] else "Resultado: NO aceptada\n"
        )
        self.log_afnd.configure(state="disabled")
