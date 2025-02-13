#Importando módulos
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



janela = Tk() #Criando a janela
janela.title("LOGIN") #Definindo o yítulo da janela
janela.configure(bg="white") #Definindo a cor de fundo  da janela
janela.geometry("300x300") #Definindo as dimensões da janela
janela.resizable(True, False) #Desabilitando a opção de redelifinir o tamanho da janela

style = ttk.Style(janela)
style.theme_use("clam")

nome_correto = "Mr.Paruque"
password_correta = "Kronos242"

def login():
    n = nome.get()
    p = password.get()

    if n == "" and p == "":
        messagebox.showwarning("LOGIN", "Por favor digite o nome e a password")
    elif n != nome_correto and p == password_correta:
        messagebox.showerror("LOGIN", "Por favor insira o nome correto")
    elif n == nome_correto and p != password_correta:
        messagebox.showerror("LOGIN", "Por favor insira a password correta")
    elif n == "" and p == password_correta:
        messagebox.showwarning("LOGIN", "Por favor digite o nome")
    elif n == nome_correto and p == "":
        messagebox.showwarning("LOGIN", "Por favor insira a password")
    elif n == nome_correto and p == password_correta:
        messagebox.showinfo("LOGIN", f"Bem vindo de volta {nome_correto}")
    elif n != nome_correto and p != password_correta:
        messagebox.showerror("LOGIN", "Por favor insira nome e password corretos")
    

        



Label(janela, text="LOGIN", fg="black", bg="white", font=("Roboto", 20)).place(x=10, y=10) #Criando o título login e posicionando o mesmo na janela
Frame(janela, bg="#531D95", height=4, width=280).place(x=10, y=50) #Criando a barra sob o título

Label(janela, text="Nome *", fg="black", bg="white", font=("arial", 10)).place(x=10, y=70) #Criando o subtítulo nome
nome = Entry(janela, font=("pacelifico", 10, "bold"), width="39", bd=3, relief="solid") #Criando o local de entrada do nome
nome.place(x=10, y=100) #Posicionando o local de entrada

Label(janela, text="Password *", fg="black", bg="white", font=("arial", 10)).place(x=10, y=150) #Criando o subtítulo nome
password = Entry(janela, font=("pacelifico", 10, "bold"), width="39", bd=3, highlightthickness=1, relief="solid", show="X") #Criando o local de entrada da password
password.place(x=10, y=180) # Posicionando o local de entrada

entrar = Button(janela, text="Entrar", fg="white", bg="#531D95", width=39, height=2, command=login) #Criando um botão para fazer o login
entrar.place(x=10, y=230) #Posicionando o botão




janela.mainloop()