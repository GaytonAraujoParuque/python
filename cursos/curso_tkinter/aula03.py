from tkinter import *

#Criando a janela
janela = Tk()

#Difinindo o nome da janela
janela.title("PARUQUE")

#Difinindo o tamanho da janela
janela.geometry("500x250")

#Difinindo a cor ddo background da janela
janela.config(bg="red")

#Criando o label
label = Label (janela, text=("Gayton Araújo Paruque"), font=("Times New Roman",30), bg="Purple", fg="white")

#Posicionando o label
label.grid(column=0, row=0)

#Criando a função que drá um print
def printar():
    print("Olá, mundo! Eu chamo-me Paruque")
    label.configure(text="Olá, mundo")

#Criando um botão
botão = Button(janela, text=("Clique aquí"), bg="yellow", fg="blue", width="20", height="10", command=printar)

#Posicionando o botão
botão.grid(column=1, row=0)

#Criando o loop da janela
janela.mainloop()