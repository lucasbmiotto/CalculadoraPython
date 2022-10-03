# BIBLIOTECAS
from tkinter import *
from tkinter import ttk

# CONFIGURAÇÃO DA JANELA
janela = Tk()
janela.title('CALCULADORA')
janela.geometry('235x318')
janela.configure(bg="#feffff")


style = ttk.Style(janela)
style.theme_use("clam")