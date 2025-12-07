import tkinter as tk
from tkinter import ttk
from gui.afd_tab import AFDTab
from gui.afnd_tab import AFNDTab
from gui.compare_tab import CompareTab

class AutomataApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador visual de AFD y AFND")
        self.geometry("1100x700")

        # Automata almacenados
        self.afd = None
        self.afnd = None

        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        self.tab_afd = AFDTab(self, notebook)
        self.tab_afnd = AFNDTab(self, notebook)
        self.tab_comp = CompareTab(self, notebook)

        notebook.add(self.tab_afd, text="AFD")
        notebook.add(self.tab_afnd, text="AFND")
        notebook.add(self.tab_comp, text="Comparación")
