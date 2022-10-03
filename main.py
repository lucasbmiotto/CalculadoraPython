from tkinter import *
from tkinter import ttk

# VARIAVEIS COM PELETA DE CORES
branco = "#feffff"
laranja = '#FFAB40'
cinza ="#ECEFF1"
back = "#3b3b3b"

# CONFIGURAÇÃO DA JANELA
janela = Tk()
janela.title('Calculadora')
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


################# Funções ####################

def entrada_valores(event):
	global all_values
	all_values = all_values + str(event)
	value_text.set(all_values)

def calculo():
	global all_values
	result = str(eval(all_values))
	value_text.set(result)
	all_values = ""

def limpar_valores(): 
    global all_values
    all_values = "" 
    value_text.set("")

# ARMAZENAMENTO DOS CALCULOS USADOS
all_values = "" 
value_text = StringVar()

################# Label ####################

app_scream = Label(frame_score,width=16,height=2,textvariable = value_text , padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=branco)
app_scream.place(x=0, y=0)

# BOTÕES
tela = Label(frame_score,width=16,height=2,textvariable = value_text , padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=branco)
tela.place(x=0, y=0)

# NUMERICOS
b0 = Button(frame_quadros, text="0", width=11, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(0))
b0.place(x=0, y=208)
b1 = Button(frame_quadros, text="1", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(1))
b1.place(x=0, y=156)
b2 = Button(frame_quadros, text="2", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(2))
b2.place(x=59, y=156)
b3 = Button(frame_quadros, text="3", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(3))
b3.place(x=118, y=156)
b4 = Button(frame_quadros, text="4", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(4))
b4.place(x=0, y=104)
b5 = Button(frame_quadros, text="5", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(5))
b5.place(x=59, y=104)
b6 = Button(frame_quadros, text="6", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(6))
b6.place(x=118, y=104)
b7 = Button(frame_quadros, text="7", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(7))
b7.place(x=0, y=52)
b8 = Button(frame_quadros, text="8", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(8))
b8.place(x=59, y=52)
b9 = Button(frame_quadros, text="9", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores(9))
b9.place(x=118, y=52)

# OUTROS BOTÕES
bc = Button(frame_quadros, text="C", width=11, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: limpar_valores())
bc.place(x=0, y=0)
bporcentagem = Button(frame_quadros, text="%", width=5, height=2, bg=cinza, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores('%'))
bporcentagem.place(x=118, y=0)
bdiv = Button(frame_quadros, text="/", width=5, height=2, bg=laranja, fg=branco,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores('/'))
bdiv.place(x=177, y=0)
bast = Button(frame_quadros, text="*", width=5, height=2, bg=laranja, fg=branco,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores('*'))
bast.place(x=177, y=52)
bmenos = Button(frame_quadros, text="-", width=5, height=2, bg=laranja, fg=branco,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores('-'))
bmenos.place(x=177, y=104)
bmais = Button(frame_quadros, text="+", width=5, height=2, bg=laranja, fg=branco,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores('+'))
bmais.place(x=177, y=156)
bmult = Button(frame_quadros, text=".", width=5, height=2, bg=laranja, fg=back,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrada_valores('.'))
bmult.place(x=118, y=208)
bigual = Button(frame_quadros, text="=", width=5, height=2, bg=laranja, fg=branco,font=('Ivy 12 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: calculo())
bigual.place(x=177, y=208)

janela.mainloop()