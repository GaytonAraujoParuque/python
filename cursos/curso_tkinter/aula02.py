from tkinter import *

#Criando uma janela
janela = Tk()

#Difinindo o nome da  janela 
janela.title("PARUQUE")

#Difinindo o tamanho da janela
janela.geometry("500x250")

#Difinindo a cor do background da janela
janela.config(bg="red")

#Crindo o label, onde ele ficará, que texto ele tem 
label = Label(janela, text="Gayton Araújo Paruque", font=("Times New Roman", 30), bg="purple", fg="white")

#Posicionando o label
label.grid(column=0, row=0)

#Criando o loop da janela
janela.mainloop()