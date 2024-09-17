import tkinter as tk
from tkinter import ttk


class ScrollableWidget(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Criar o Canvas para a área rolável
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)

        # Barra de rolagem vertical
        self.scrollbar_y = ttk.Scrollbar(
            self, orient='vertical', command=self.canvas.yview)
        self.scrollbar_y.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.canvas.configure(yscrollcommand=self.scrollbar_y.set)

        # Barra de rolagem horizontal
        self.scrollbar_x = ttk.Scrollbar(
            self, orient='horizontal', command=self.canvas.xview)
        self.scrollbar_x.place(relx=0, rely=1, relwidth=1, anchor='sw')
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

        # Frame interno que será rolável
        self.scrollable_frame = tk.Frame(self.canvas)

        # Adiciona o frame interno ao canvas como uma janela
        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw")

        # Atualiza a região de rolagem quando o conteúdo do frame muda
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)

        # Configuração do evento de rolagem com o mouse
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(
            int(-1*(event.delta/120)), "units"))

    def on_frame_configure(self, event):
        """Atualiza a região de rolagem quando o conteúdo do frame muda"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_widget(self, widget, **kwargs):
        """Método auxiliar para adicionar widgets diretamente ao frame rolável"""
        widget.pack(**kwargs)
