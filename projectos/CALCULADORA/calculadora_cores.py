#Importando a toda a informação da biblioteca tkinter
from tkinter import *

janela = Tk() #Criando uma janela
janela.title("PARUQUE") #Dando um nome para a calculadora
janela.geometry("285x473") #Difinindo o tamanho da janela
janela.config(bg="black") #Difinindo a cor de fundo da janela
janela.resizable(False, False)


valores_do_display1 = StringVar() #Criando a variável que vai exibir os valores na primeira tela/display
valores_do_display2 = StringVar() #Criando a variável que vai exibir os resultados na segunda tela/display
todos_valores = "" #Criando a variável que vai guardar todos valores digitados na primeira tela/display
b = ""

def entrada_de_valores(x):
    global todos_valores
    global b
    
    todos_valores += str(x)
    valores_do_display1.set(todos_valores)
    
    try:
        eval(todos_valores)
    except:
        valores_do_display2.set("")
    else:
        valores_do_display2.set(eval(todos_valores))


def calcular():
    try:
        resultado = eval(todos_valores)
    except:
        valores_do_display2.set("ERROR")
    else:
        valores_do_display2.set(resultado)

def limpar_tudo():
    global valores_do_display1
    global valores_do_display2
    global todos_valores
    global b
    b = ""
    todos_valores = ""
    valores_do_display1.set("")
    valores_do_display2.set("")

def deletar():
    global todos_valores
    global b
    todos_valores = todos_valores[:-1]
    b = b[:-1]
    valores_do_display2.set(b)
    valores_do_display1.set(todos_valores)

frame_dos_displays = Frame(janela, width="276", height="100",bg="black")#Criando espaço para as telas que é um frame
frame_dos_displays.place(x=5, y=20)#Posicionando o frame

display1 = Label(frame_dos_displays, textvariable=valores_do_display1,bg="yellow", fg="black", width="37", height="2", font=('ivy 8 bold')) #Criando o primeiro displays(onde os valores aparecerão)
display1.place(x=6, y=5) #Posicionando o primeiro display

display2 = Label(frame_dos_displays, textvariable=valores_do_display2,bg="yellow", width="37", height=2, fg="black", font=("ivy 8 bold")) #Criando o segundo display(onde o resultado irá aparecer)
display2.place(x=6, y=50) #Posicionando o segundo display

frame_dos_botões = Frame(janela, width=290, height=350,bg="black") #Criando um frame para os botões. NB: Um frame é um espaço que ajuda a organizar o espaço da janela,podemos criar vários frames em uma única janela
frame_dos_botões.place(x=0, y=110) #Posicionando o frame

#Criando funções dos botões especiais primários
def mudar_preto():
    frame_dos_displays.config(bg="black")
    janela.config(bg="black")
    frame_dos_botões.config(bg="black")

def mudar_branco():
    frame_dos_displays.config(bg="white")
    janela.config(bg="white")
    frame_dos_botões.config(bg="white")

def mudar_azul():
    frame_dos_displays.config(bg="dark blue")
    janela.config(bg="dark blue")
    frame_dos_botões.config(bg="dark blue")

def mudar_laranja():
    frame_dos_displays.config(bg="orange")
    janela.config(bg="orange")
    frame_dos_botões.config(bg="orange")

def mudar_rosa():
    frame_dos_displays.config(bg="pink")
    janela.config(bg="pink")
    frame_dos_botões.config(bg="pink")

def mudar_vermelho():
    frame_dos_displays.config(bg="red")
    janela.config(bg="red")
    frame_dos_botões.config(bg="red")

#Criando as funções dos botões especiais secundários
def mudar_verde():
    violeta.config(bg="green")
    roxo.config(bg="green")
    cinza.config(bg="green")
    castanho.config(bg="green")
    zero.config(bg="green")
    ponto.config(bg="green")
    três.config(bg="green")
    cinco.config(bg="green")
    sete.config(bg="green")
    nove.config(bg="green")
    par2.config(bg="green")
    par1.config(bg="green")
    um.config(bg="green")
    dois.config(bg="green")
    quatro.config(bg="green")
    seis.config(bg="green")
    oito.config(bg="green")
    limpar.config(bg="green")
    igualidade.config(bg="green")
    adição.config(bg="green")
    subtração.config(bg="green")
    multiplicação.config(bg="green")
    divisão.config(bg="green")
    Del.config(bg="green")
    azul.config(bg="green")
    laranja.config(bg="green")
    vermelho.config(bg="green")
    rosa.config(bg="green")
    branco.config(bg="green")
    preto.config(bg="green")
    display1.config(bg="green")
    display2.config(bg="green")
    verde.config(bg="green")
    amarelo.config(bg="green")

def mudar_amarelo():
    violeta.config(bg="yellow")
    roxo.config(bg="yellow")
    cinza.config(bg="yellow")
    castanho.config(bg="yellow")
    zero.config(bg="yellow")
    ponto.config(bg="yellow")
    três.config(bg="yellow")
    cinco.config(bg="yellow")
    sete.config(bg="yellow")
    nove.config(bg="yellow")
    par2.config(bg="yellow")
    par1.config(bg="yellow")
    um.config(bg="yellow")
    dois.config(bg="yellow")
    quatro.config(bg="yellow")
    seis.config(bg="yellow")
    oito.config(bg="yellow")
    limpar.config(bg="yellow")
    igualidade.config(bg="yellow")
    adição.config(bg="yellow")
    subtração.config(bg="yellow")
    multiplicação.config(bg="yellow")
    divisão.config(bg="yellow")
    Del.config(bg="yellow")
    azul.config(bg="yellow")
    laranja.config(bg="yellow")
    vermelho.config(bg="yellow")
    rosa.config(bg="yellow")
    branco.config(bg="yellow")
    preto.config(bg="yellow")
    verde.config(bg="yellow")
    amarelo.config(bg="yellow")
    display1.config(bg="yellow")
    display2.config(bg="yellow")

def mudar_castanho():
    violeta.config(bg="brown")
    roxo.config(bg="brown")
    cinza.config(bg="brown")
    zero.config(bg="brown")
    ponto.config(bg="brown")
    três.config(bg="brown")
    cinco.config(bg="brown")
    sete.config(bg="brown")
    nove.config(bg="brown")
    par2.config(bg="brown")
    par1.config(bg="brown")
    um.config(bg="brown")
    dois.config(bg="brown")
    quatro.config(bg="brown")
    seis.config(bg="brown")
    oito.config(bg="brown")
    limpar.config(bg="brown")
    igualidade.config(bg="brown")
    adição.config(bg="brown")
    subtração.config(bg="brown")
    multiplicação.config(bg="brown")
    divisão.config(bg="brown")
    Del.config(bg="brown")
    azul.config(bg="brown")
    laranja.config(bg="brown")
    vermelho.config(bg="brown")
    rosa.config(bg="brown")
    branco.config(bg="brown")
    preto.config(bg="brown")
    verde.config(bg="brown")
    amarelo.config(bg="brown")
    castanho.config(bg="brown")
    display1.config(bg="brown")
    display2.config(bg="brown")

def mudar_cinza():
    violeta.config(bg="gray")
    roxo.config(bg="gray")
    zero.config(bg="gray")
    ponto.config(bg="gray")
    três.config(bg="gray")
    cinco.config(bg="gray")
    sete.config(bg="gray")
    nove.config(bg="gray")
    par2.config(bg="gray")
    par1.config(bg="gray")
    um.config(bg="gray")
    dois.config(bg="gray")
    quatro.config(bg="gray")
    seis.config(bg="gray")
    oito.config(bg="gray")
    limpar.config(bg="gray")
    igualidade.config(bg="gray")
    adição.config(bg="gray")
    subtração.config(bg="gray")
    multiplicação.config(bg="gray")
    divisão.config(bg="gray")
    Del.config(bg="gray")
    azul.config(bg="gray")
    laranja.config(bg="gray")
    vermelho.config(bg="gray")
    rosa.config(bg="gray")
    branco.config(bg="gray")
    preto.config(bg="gray")
    verde.config(bg="gray")
    amarelo.config(bg="gray")
    castanho.config(bg="gray")
    cinza.config(bg="gray")
    display1.config(bg="gray")
    display2.config(bg="gray")

def mudar_roxo():
    display1.config(bg="purple")
    display2.config(bg="purple")
    zero.config(bg="purple")
    ponto.config(bg="purple")
    três.config(bg="purple")
    cinco.config(bg="purple")
    sete.config(bg="purple")
    nove.config(bg="purple")
    par2.config(bg="purple")
    par1.config(bg="purple")
    um.config(bg="purple")
    dois.config(bg="purple")
    quatro.config(bg="purple")
    seis.config(bg="purple")
    oito.config(bg="purple")
    limpar.config(bg="purple")
    igualidade.config(bg="purple")
    adição.config(bg="purple")
    subtração.config(bg="purple")
    multiplicação.config(bg="purple")
    divisão.config(bg="purple")
    Del.config(bg="purple")
    azul.config(bg="purple")
    laranja.config(bg="purple")
    vermelho.config(bg="purple")
    rosa.config(bg="purple")
    branco.config(bg="purple")
    preto.config(bg="purple")
    verde.config(bg="purple")
    amarelo.config(bg="purple")
    castanho.config(bg="purple")
    cinza.config(bg="purple")
    roxo.config(bg="purple")
    violeta.config(bg="purple")

def mudar_violeta():
    display1.config(bg="violet")
    display2.config(bg="violet")
    zero.config(bg="violet")
    ponto.config(bg="violet")
    três.config(bg="violet")
    cinco.config(bg="violet")
    sete.config(bg="violet")
    nove.config(bg="violet")
    par2.config(bg="violet")
    par1.config(bg="violet")
    um.config(bg="violet")
    dois.config(bg="violet")
    quatro.config(bg="violet")
    seis.config(bg="violet")
    oito.config(bg="violet")
    limpar.config(bg="violet")
    igualidade.config(bg="violet")
    adição.config(bg="violet")
    subtração.config(bg="violet")
    multiplicação.config(bg="violet")
    divisão.config(bg="violet")
    Del.config(bg="violet")
    azul.config(bg="violet")
    laranja.config(bg="violet")
    vermelho.config(bg="violet")
    rosa.config(bg="violet")
    branco.config(bg="violet")
    preto.config(bg="violet")
    verde.config(bg="violet")
    amarelo.config(bg="violet")
    castanho.config(bg="violet")
    cinza.config(bg="violet")
    roxo.config(bg="violet")
    violeta.config(bg="violet")

#Criando botões especiais primários
preto = Button(frame_dos_botões, text="D", width=4, height=1, command=mudar_preto,bg="yellow", relief=RAISED, overrelief=RIDGE)
branco = Button(frame_dos_botões, text="L", width=4, height=1, command=mudar_branco,bg="yellow", relief=RAISED, overrelief=RIDGE)
rosa = Button(frame_dos_botões, text="P", width=4, height=1, command=mudar_rosa,bg="yellow", overrelief=RIDGE)
vermelho = Button(frame_dos_botões, text="R", width=4, height=1, command=mudar_vermelho,bg="yellow", overrelief=RIDGE)
laranja = Button(frame_dos_botões, text="O", width=4, height=1, command=mudar_laranja,bg="yellow", overrelief=RIDGE)
azul = Button(frame_dos_botões, text="B", width=4, height=1, command=mudar_azul,bg="yellow", overrelief=RIDGE)

#Criando os botões especiais secundários
verde = Button(frame_dos_botões, text="G", width=4, height=1, command=mudar_verde,bg="yellow", overrelief=RIDGE)
amarelo = Button(frame_dos_botões, text="Y", width=4, height=1, command=mudar_amarelo,bg="yellow", overrelief=RIDGE)
castanho = Button(frame_dos_botões, text="Br", width=4, height=1, command=mudar_castanho,bg="yellow", overrelief=RIDGE)
cinza = Button(frame_dos_botões, text="Gra", width=4, height=1, command=mudar_cinza,bg="yellow", overrelief=RIDGE)
roxo = Button(frame_dos_botões, text="P", width=4, height=1, command=mudar_roxo,bg="yellow", overrelief=RIDGE)
violeta = Button(frame_dos_botões, text="V", width=4, height=1, command=mudar_violeta,bg="yellow", overrelief=RIDGE)

#Criando botões
Del = Button(frame_dos_botões, text="DEL", width=10, height=2,bg="yellow", command=deletar, overrelief=RIDGE)
divisão = Button(frame_dos_botões, text="/", width=10, height=2,bg="yellow", command=lambda: entrada_de_valores("/"), overrelief=RIDGE)
multiplicação = Button(frame_dos_botões, text="*", width=10, height=2,bg="yellow",command=lambda: entrada_de_valores("*"), overrelief=RIDGE)
subtração = Button(frame_dos_botões, text="-", width=10, height=2,bg="yellow", command=lambda: entrada_de_valores("-"), overrelief=RIDGE)
adição = Button(frame_dos_botões, text="+", width=10, height=2,bg="yellow", command=lambda: entrada_de_valores("+"), overrelief=RIDGE)
igualidade = Button(frame_dos_botões, text="=", width=10, height=2,bg="yellow", command=calcular, overrelief=RIDGE)

limpar = Button(frame_dos_botões, text="C",bg="yellow", width=10, height=2,command=limpar_tudo, overrelief=RIDGE)
oito  = Button(frame_dos_botões, text="8",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(8), overrelief=RIDGE)
seis = Button(frame_dos_botões, text="6",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(6), overrelief=RIDGE)
quatro = Button(frame_dos_botões, text="4",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(4), overrelief=RIDGE)
dois =  Button(frame_dos_botões, text="2",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(2), overrelief=RIDGE)
um = Button(frame_dos_botões, text="1",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(1), overrelief=RIDGE)

par1 = Button(frame_dos_botões, text="(",bg="yellow", width=4, height=2, command=lambda: entrada_de_valores("("), overrelief=RIDGE)
par2 = Button(frame_dos_botões, text=")",bg="yellow", width=4, height=2, command=lambda: entrada_de_valores(")"), overrelief=RIDGE)
nove = Button(frame_dos_botões, text="9", bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(9), overrelief=RIDGE)
sete = Button(frame_dos_botões, text="7",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(7), overrelief=RIDGE)
cinco = Button(frame_dos_botões, text="5",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(5), overrelief=RIDGE)
três = Button(frame_dos_botões, text="3",bg="yellow", width=10, height=2, command=lambda: entrada_de_valores(3), overrelief=RIDGE)
ponto = Button(frame_dos_botões, text=".",bg="yellow", width=4, height=2, command=lambda: entrada_de_valores("."), overrelief=RIDGE)
zero = Button(frame_dos_botões, text="0",bg="yellow", width=4, height=2, command=lambda: entrada_de_valores(0), overrelief=RIDGE)

#Posicionando os botões
Del.place(x=105, y=60)
divisão.place(x=195, y= 110)
multiplicação.place(x=195, y=160)
subtração.place(x=195, y=210)
adição.place(x=195, y=260)
igualidade.place(x=195, y=310)

limpar.place(x=15, y=60)
oito.place(x=15, y=110)
seis.place(x=15, y=160)
quatro.place(x=15, y=210)
dois.place(x=15, y=260)
um.place(x=15, y=310)

par1.place(x=195, y=60)
par2.place(x=237, y=60)
nove.place(x=105, y=110)
sete.place(x=105, y=160)
cinco.place(x=105, y=210)
três.place(x=105, y=260)
ponto.place(x=148, y=310)
zero.place(x=105, y=310)

#Posicionando os botões especiais primárias 
preto.place(x=237, y=3)
branco.place(x=195, y=3)
azul.place(x=148, y=3)
laranja.place(x=105, y=3)
rosa.place(x=15, y=3)
vermelho.place(x=56, y=3)

#Posicionando os botãos especiais secundários 
verde.place(x=237, y=32)
amarelo.place(x=195, y=32)
castanho.place(x=148, y=32)
cinza.place(x=105, y=32)
roxo.place(x=56, y=32)
violeta.place(x=15, y=32)



janela.mainloop() #Mantendo a janela em um loop