from tkinter import *

#Criando a janela
janela = Tk()

#Definindo o nome da janela
janela.title("PARUQUE")

#Definindo o tamanho da janela
janela.geometry("500x250")

#Definindo a cor do background
janela.config(bg="red")

#Criando o label
label = Label(janela, text="***********", bg="blue")

#Posicionando o label
label.grid(column=0, row=0) 

#Criando a função printar
def printar():
    label.configure(text="Olá, mundo!")

#Criando o botão
botão = Button (janela, text="Clique", command=printar)

#Posicionando o botão
botão.grid(column=0, row=1)

#Criando botões alternativos para testar as funções de posicionamento
a = Button(janela, text="Place")
a.place(x=0, y=50)

b = Button(janela, text="b")




#Criando o loop da janela
janela.mainloop()
