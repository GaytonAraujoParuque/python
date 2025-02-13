# Importando modulos
from tkinter import *
from tkinter import ttk 

#Cores
preto = '#3b3b3b'
branco = '#feffff'
azul = '#38576b'
cinzento = '#ECEFF1'
laranja = '#FFAB40'

# Criando uma janela
janela = Tk()
janela.title('Calculadora(._.)')
janela.geometry('235x310') #tamanho da tela
janela.config(bg=preto) #background da tela

#Dividindo da janela em duas partes/frames
frame_tela = Frame(janela, width= 235, height=50, bg=azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 235, height=268)
frame_corpo.grid(row=1, column=0)



valor_texto = StringVar()
todos_valores = ''

#Valores na tela
def entrar_valores(e):
    global todos_valores
    todos_valores = todos_valores + str(e)
    
   
    #Passando valor para tela
    valor_texto.set(todos_valores)


#Logica dos calculos 
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)


#limpar clicando =
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')



#Criando label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 17 bold'), bg=azul, fg=branco)
app_label.place(x=0, y=0)




#Criando botoes
limpar = Button(frame_corpo, command=limpar_tela,text='C', width=11, height=2, bg=cinzento, relief=RAISED, overrelief=RIDGE, font=('Ivy 13 bold'))
limpar.place(x=0, y=0)


porc = Button(frame_corpo, command=lambda: entrar_valores('%') ,text='%', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
porc.place(x=118, y=0)


barra = Button(frame_corpo, command=lambda: entrar_valores('/') ,text='/', width=5, height=2, overrelief=RIDGE, font=('Ivy 13 bold'))
barra.place(x=177, y=0)
barra.config(bg=laranja)


n7 = Button(frame_corpo, command=lambda: entrar_valores('7') ,text='7', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n7.place(x=0, y=52)


n8 = Button(frame_corpo, command=lambda: entrar_valores('8') ,text='8', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n8.place(x=59, y=52)


n9 = Button(frame_corpo, command=lambda: entrar_valores('9') ,text='9', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n9.place(x=118, y=52)


mult = Button(frame_corpo, command=lambda: entrar_valores('*') ,text='*', width=5, height=2, overrelief=RIDGE, font=('Ivy 13 bold'))
mult.place(x=177, y=52)
mult.config(bg=laranja)


n4 = Button(frame_corpo, command=lambda: entrar_valores('4') ,text='4', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n4.place(x=0, y=104)


n5 = Button(frame_corpo, command=lambda: entrar_valores('5') ,text='5', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n5.place(x=59, y=104)


n6 = Button(frame_corpo, command=lambda: entrar_valores('6') ,text='6', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n6.place(x=118, y=104)


sub = Button(frame_corpo, command=lambda: entrar_valores('-') ,text='-', width=5, height=2, overrelief=RIDGE, font=('Ivy 13 bold'))
sub.place(x=177, y=104)
sub.config(bg=laranja)


n1 = Button(frame_corpo, command=lambda: entrar_valores('1') ,text='1', width=5, height=2, bg=cinzento, fg=preto, overrelief=RIDGE, font=('Ivy 13 bold'))
n1.place(x=0, y=156)


n2 = Button(frame_corpo, command=lambda: entrar_valores('2') ,text='2', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n2.place(x=59, y=156)


n3 = Button(frame_corpo, command=lambda: entrar_valores('3') ,text='3', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
n3.place(x=118, y=156)


adi = Button(frame_corpo, command=lambda: entrar_valores('+') ,text='+', width=5, height=2, overrelief=RIDGE, font=('Ivy 13 bold'))
adi.place(x=177, y=156)
adi.config(bg=laranja)


zero = Button(frame_corpo, command=lambda: entrar_valores('0') ,text='0', width=11, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
zero.place(x=0, y=208)


ponto = Button(frame_corpo, command=lambda: entrar_valores('.') ,text='.', width=5, height=2, bg=cinzento, overrelief=RIDGE, font=('Ivy 13 bold'))
ponto.place(x=118, y=208)


igual = Button(frame_corpo, command=calcular,text='=', width=5, height=2, overrelief=RIDGE, font=('Ivy 13 bold'))
igual.place(x=177, y=208)
igual.config(bg=laranja)



janela.mainloop()