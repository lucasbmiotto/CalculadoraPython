# BIBLIOTECAS
from tkinter import *
from tkinter import ttk

# VARIAVEIS COM PELETA DE CORES
branco = "#feffff"
laranja = '#FFAB40'
bege ="#ab8918"
cinza ="#ECEFF1"
back = "#3b3b3b"

# CONFIGURAÇÃO DA JANELA
janela = Tk()
janela.title('CALCULADORA')
janela.geometry('235x318')
janela.configure(bg=branco)

style = ttk.Style(janela)
style.theme_use("clam")

# DEFINIÇÃO DOS FRAMES
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_score = Frame(janela, width=300, height=56,bg=branco, pady=0, padx=0, relief="flat",)
frame_score.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340,bg=back, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

# FUNÇÕES DA CALCULADORA
def entrada_valores(event):
    global todos_valores
	todos_valores = todos_valores + str(event)
	texto.set(todos_valores)

def calculo():
    global todos_valores
	resultado = str(eval(todos_valores))
	texto.set(resultado)
	todos_valores = ""

def limpar_valores():
    global todos_valores
    todos_valores = "" 
    texto.set("")

# BOTÕES


janela.mainloop()