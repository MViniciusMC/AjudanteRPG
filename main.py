import tkinter as tk
import ttkbootstrap as ttk
import random as rd
from ttkbootstrap import Style
from widgets.hscrollwidget import HScrollableWidget
from widgets.multiscrollwidget import ScrollableWidget
from tkinter import filedialog


def create_card(parent, quant):
    for i in range(0, quant):
        card = ttk.Frame(parent,
                         borderwidth=1, relief='solid', padding=10)
        card.pack(padx=10, pady=10, fill='x', side='left')
        player_index_label = ttk.Label(card, text=f"Player - {i+1}")
        player_index_label.grid(column=0, row=0)
        label_nome = ttk.Label(card, text="Nome")
        label_nome.grid(column=0, row=1)
        card_content_name = ttk.Entry(card)
        card_content_name.grid(column=0, row=2)
        label_vida = ttk.Label(card, text='Atual x Original')
        label_vida.grid(column=0, row=3)
        vida_frame = ttk.Frame(card)
        vida_frame.grid(column=0, row=4)
        vida = [i for i in range(10)]
        card_content_vida_original = ttk.Combobox(
            vida_frame, values=vida, state='readonly', width=5)
        card_content_vida_original.set('PV')
        card_content_vida_original.pack(side='left')
        card_content_vida = ttk.Combobox(
            vida_frame, values=vida, state='readonly', width=5)
        card_content_vida.set('PV')
        card_content_vida.pack(side='left')
        essencia_frame = ttk.Frame(card)
        essencia_frame.grid(column=0, row=5)
        essencia = [i for i in range(24)]
        card_content_essencia = ttk.Combobox(
            essencia_frame, values=essencia, state='readonly', width=5)
        card_content_essencia.set('PE')
        card_content_essencia.pack(side='left')
        card_content_essencia_original = ttk.Combobox(
            essencia_frame, values=essencia, state='readonly', width=5)
        card_content_essencia_original.set('PE')
        card_content_essencia_original.pack(side='left')
        label_aspecto = ttk.Label(card, text="Aspectos e Inventário")
        label_aspecto.grid(column=0, row=6)
        card_content_aspectos = ttk.Text(
            card, wrap=tk.WORD, width=20, height=8)
        card_content_aspectos.grid(column=0, row=7)

        def salvar_player():
            nome = card_content_name.get()
            vida_atual = card_content_vida.get()
            vida_original = card_content_vida_original.get()
            essencia_atual = card_content_essencia.get()
            essencia_original = card_content_essencia_original.get()
            aspectos = card_content_aspectos.get("1.0", tk.END)
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(str(nome+"\n"+vida_atual+"\n"+vida_original+"\n" +
                               essencia_atual+"\n"+essencia_original+"\n"+aspectos))
        botao_salvar_player = ttk.Button(
            card, text=f"Salvar Player {i+1}", command=salvar_player)
        botao_salvar_player.grid(column=0, row=8)

        def carregar_player():
            pass
        botao_carregar_player = ttk.Button(
            card, text='Carregar', command=carregar_player)
        botao_carregar_player.grid(column=0, row=9)


def process_value_dados():
    select1 = dropdown1.get()
    select2 = dropdown2.get()
    if (select1 in dropdown1['values']) and (select2 in dropdown2['values']):
        dados(quantidade=int(select1), marguem=int(select2))
    else:
        pass


def dados(quantidade, marguem):
    lista_dados = []
    for i in range(0, quantidade):
        dado = rd.randint(1, 6)
        if (dado >= marguem):
            lista_dados.append(f'{dado} Sucesso')
        else:
            lista_dados.append(f'{dado} Falha')
    r = f'{lista_dados}'
    r = r.replace("'", ' ')
    r = r[1:-1]
    resultado.configure(text=" Resultado: "+r)


def salvar():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(history.get("1.0", tk.END).strip())


def carregar():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            history.delete("1.0", tk.END)  # Limpa o conteúdo atual do Text
            history.insert(tk.END, content)


root = tk.Tk()
style = Style(theme='solar')
root.title("Text RPG")
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.attributes('-alpha', 0.5)

# Frame configurações
frame = ScrollableWidget(root)
frame.pack(expand=True, fill='both')

# frames
row1 = ttk.Frame(frame.scrollable_frame, borderwidth=10,
                 relief=tk.GROOVE)
frame.add_widget(row1, pady=5)
row2 = ttk.Frame(frame.scrollable_frame, borderwidth=10, relief=tk.GROOVE)
frame.add_widget(row2, pady=5)
row3 = ttk.Frame(frame.scrollable_frame, borderwidth=10,
                 relief=tk.GROOVE, width=120)
frame.add_widget(row3, pady=5)
row4 = ttk.Frame(frame.scrollable_frame)
frame.add_widget(row4, pady=20)
# row 1
label1 = ttk.Label(row1, text="Lançar dados!!!", width=42)
label1.grid(row=0, column=1)
quant_dados = [1, 2, 3]
dropdown1 = ttk.Combobox(row1, values=quant_dados, state='readonly')
dropdown1.set("Quantos dados?")
dropdown1.grid(row=1, column=0, pady=20, padx=20)
quant_marguem = [2, 3, 4, 5, 6]
dropdown2 = ttk.Combobox(row1, values=quant_marguem, state='readonly')
dropdown2.set("Quantos A marguem?")
dropdown2.grid(row=1, column=1, pady=20, padx=20)
botão = ttk.Button(row1, text="Lançar!!!", command=process_value_dados)
botão.grid(row=1, column=3)
resultado = ttk.Label(row1, text='Role os dados')
resultado.grid(row=2, column=0)
# row 2
text_row2 = ttk.Label(row2, text="Players")
text_row2.pack()
player_cards = HScrollableWidget(row2)
player_cards.pack(expand=True, fill='both')
card_frame = ttk.Frame(player_cards.scrollable_frame,
                       borderwidth=10, relief=tk.GROOVE)
player_cards.add_widget(card_frame)
create_card(card_frame, 6)

# variavel texto
name_row3 = ttk.Label(row3, text="História")
name_row3.pack()
history = ttk.Text(row3, width=80, height=20)
history.pack()
space = ttk.Label(row3, text="      ")
space.pack()
botao_salvar = ttk.Button(row3, text="Salvar", command=salvar)
botao_salvar.pack(side='left')
botao_carregar = ttk.Button(row3, text='Carregar', command=carregar)
botao_carregar.pack(side='right')

root.mainloop()
