
from tkinter import *
from tkinter import ttk
import posiciona
from numpy import place

cor1 = "#3b3b3b" #preta
cor2 = "#f5f7f5" #branca
cor3 = "#38576B" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

janela = Tk()

'''
janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))'''

janela.title('Calculadora')
janela.geometry("242x313")
janela.config(bg=cor1) #configurar a cor do background.

# criando os frames
frame_tela = Frame(janela, width=300, height=50, bg=cor3) 
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=320)
frame_corpo.grid(row=1, column=0)

receber_valores = ''
aad = ''
valor_texto = StringVar() # vai receber o valor da string passada para o 'textvariable'
# função


def entrar_valores(evento):

    global receber_valores
    receber_valores = receber_valores + str(evento)
    
    # eval('')

    # passando o valor para a tela
    valor_texto.set(receber_valores)


# função para calcular
def calcular():
    global receber_valores
    resultado = eval(receber_valores) # responsável em fazer os cáculos. 
    valor_texto.set(str(resultado))

# função limpar a tela

def limpar_tela():
    global receber_valores
    receber_valores = ""
    valor_texto.set("")


# criando o Label

app_Label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, 
anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor3, fg=cor2)
app_Label.place(x=0, y=0)   #textvariable é uma variável que permite alterar o valor dinamicamente.


# criando os botões
#width=  largura, height = altura

b_1 = Button(frame_corpo, command = limpar_tela, text="C", width=11, height=2, bg=cor4, 
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=121, y=0)

b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=182, y=0)


b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)

b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=61, y=53)

b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=121, y=53)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=182, y=53)


b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)

b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=61, y=106)

b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=121, y=106)

b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=182, y=106)


b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=159)

b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=61, y=159)

b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=121, y=159)

b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=182, y=159)


b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, 
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=212)

b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=121, y=212)

b_18 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2,
font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=182, y=212)

janela.mainloop()
