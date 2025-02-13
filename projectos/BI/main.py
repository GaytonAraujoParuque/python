from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from random import randint

janela = Tk()
janela.geometry("800x450")
janela.title("ENTRADA DE DADOS")
janela.resizable(False, False)
janela.configure(bg="white")

style1 = ttk.Style(janela)
style1.theme_use("clam")

caminho_imagem = "emblema.png"
imagem_original = Image.open(caminho_imagem)
largura = 41
altura = 40
emblema = imagem_original.resize((largura, altura))
imagem_tk = ImageTk.PhotoImage(emblema)

caminho_imagem1 = "bandeira.png"
imagem_original1 = Image.open(caminho_imagem1)
largura1 = 70
altura1 = 40
bandeira = imagem_original1.resize((largura1, altura1))
imagem_tk1 = ImageTk.PhotoImage(bandeira)

caminho_imagem2 = "avatar2.jpg"
imagem_original2 = Image.open(caminho_imagem2)
largura2 = 80
altura2 = 100
avatar = imagem_original2.resize((largura2, altura2))
imagem_tk2 = ImageTk.PhotoImage(avatar)

caminho_imagem3 = "avatar.jpg"
imagem_original3 = Image.open(caminho_imagem3)
avatar2 = imagem_original3.resize((80, 100))
imagem_tk3 = ImageTk.PhotoImage(avatar2)



def f1():
    #__________________________________________________________________________________________________________________
    def resetar():
        nome.delete(0, END)
        pai.delete(0, END)
        mãe.delete(0, END)
        naturalidade.delete(0, END)
        distrito.delete(0, END)
        bairro.delete(0, END)
        quarteirão.delete(0, END)
        casa.delete(0, END)
        altura.delete(0, END)
        dia.delete(0, END)
        mês.delete(0, END)
        ano.delete(0, END)
        dia.insert(0, "Dia")
        mês.insert(0, "Mês")
        ano.insert(0, "Ano")

    def Submit():
        entrada_nome = nome.get()
        entrada_pai = pai.get()
        entrada_mãe = mãe.get()

        entrada_naturalidade = naturalidade.get()

        entrada_distrito = distrito.get()
        entrada_quarteirão = quarteirão.get()
        entrada_altura = altura.get()
        entrada_casa = casa.get()
        entrada_bairro = bairro.get()

        entrada_dia = dia.get()
        entrada_mês = mês.get()
        entrada_ano = ano.get()

        sexo = valor.get()
        if entrada_nome == "" or entrada_pai == "" or entrada_mãe == "" or entrada_naturalidade == "" or entrada_distrito == "" or entrada_quarteirão == "" or entrada_altura == "" or entrada_casa == "" or entrada_bairro == "" or entrada_dia == "Dia" or entrada_mês == "Mês" or entrada_ano == "Ano":
            sei_lá = None
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos")
        elif sexo != "M" and sexo != "F":
            messagebox.showwarning("Aviso", "Por favor, indique o seu sexo")
        else:
            tela = Toplevel(janela)
            tela.geometry("430x260")
            tela.resizable(False, False)
            tela.configure(bg="lightgreen")
            tela.title("BILHETE DE IDENTIDADE")
            Label(tela, bg="lightyellow", width=450, height=3).place(x=0, y=0)
            Label(tela, bg="lightyellow", width=450, height=3).place(x=0, y=210)

            Label(tela, image=imagem_tk, bg="lightyellow").place(x=30, y=5)
            Label(tela, image=imagem_tk1, bg="lightyellow").place(x=355, y=5)
            if sexo == "M":
                Label(tela, image=imagem_tk2, bg="green").place(x=10, y=100)
            else:
                Label(tela, image=imagem_tk3, bg="green").place(x=10, y=100)
            
            
            Label(tela, text="REPÚBLICA DE MOÇAMBIQUE", bg="lightyellow", font=("arial", 12, "bold")).place(x=90, y=5)
            Label(tela, text="BILHETE DE IDENTIDADE", bg="lightyellow", font=("arial", 12,"bold")).place(x=110, y=25)
            
            aleatório = randint(1000000000000, 9999999999999)
            aleatório_string = str(aleatório)
            Label(tela, text=f"N*: {aleatório_string}", bg="lightgreen", font=("arial", 8, 'bold')).place(x=100, y=51)
            Label(tela, text="Nome / Name:", bg="lightgreen", font=("arial", 5, "bold")).place(x=100, y=65)
            Label(tela, text=entrada_nome.upper(), bg="lightgreen", font=("arial", 10, "bold")).place(x=100, y=74)

            Label(tela, text="Data de Nascimento /", bg="lightgreen", font=("arial", 5, "bold")).place(x=100, y=94)
            Label(tela, text=f"{str(entrada_dia)}/{str(entrada_mês)}/{str(entrada_ano)}", bg="lightgreen",font=("arial", 7, "bold")).place(x=100, y=114)
            Label(tela, text="Date of Birth:", bg="lightgreen", font=("arial", 5, "bold")).place(x=100, y=104)
            
            Label(tela, text="Naturalidade / Place of Birth:", bg="lightgreen", font=("arial", 5, "bold")).place(x=100, y=127)
            Label(tela, text=entrada_naturalidade.upper(), bg="lightgreen", font=("arial", 7, "bold")).place(x=100, y=136)
            Label(tela, text="Local de Residência  / Address:", bg="lightgreen", font=("arial", 5, "bold")).place(x=100, y=150)
            
            Label(tela, text=f"Q*{entrada_quarteirão} CASA*{entrada_casa}", bg="lightgreen", font=("arial", 7, "bold")).place(x=100, y=160)
            Label(tela, text=entrada_bairro.upper(), bg="lightgreen").place(x=100, y=173)
            Label(tela, text=entrada_distrito.upper(), bg="lightgreen", fg="black").place(x=100, y=188)

            Label(tela, text=f"Altura / Height: {entrada_altura} m", bg="lightgreen", font=("arial", 5, "bold")).place(x=210, y=94)
            
            Label(tela, text=f"Sexo / Sex: {sexo}", bg="lightgreen", font=("arial", 5, "bold")).place(x=210, y=105)
            
            Label(tela, text="Assinatura do Titular/", bg="lightgreen", font=("arial", 5, "bold")).place(x=320, y=185)
            Label(tela, text="Signature:", bg="lightgreen", font=("arial", 5, "bold")).place(x=320, y=195)
            Label(tela, text=entrada_nome, bg="lightyellow", font=("Pacifico",7, "bold")).place(x=320, y=210)




            tela.mainloop()

    #___________________________________________________________________________________________________________________
    frame1 = Frame(janela, width=700, height=300, bg="silver", bd=2, relief="solid")
    frame1.pack(pady=20)
    valor= StringVar()

    Label(frame1, bg="silver", text="Nome", fg="black").place(x=50, y=10)
    nome = Entry(frame1, relief="solid")
    nome.place(x=50, y=50)

    Label(frame1, bg="silver", text="Nome do pai", fg="black").place(x=315, y=10)
    pai = Entry(frame1, relief="solid")
    pai.place(x=295, y=50)

    Label(frame1, bg="silver", text="Nome da mãe", fg="black").place(x=525, y=10)
    mãe = Entry(frame1, relief="solid")
    mãe.place(x=525, y=50)

    Label(frame1, text="Naturalidade", fg="black", bg="silver").place(x=50, y=110)
    naturalidade = Combobox(frame1, width=17)
    naturalidade["values"] = ("MAPUTO", "GAZA", "INHAMBANE", "MANICA", "SOFALA", "TETE", "ZAMBÉZIA", "NAMPULA", "NIASSA", "CABO DELGADO")
    naturalidade.place(x=50, y=155)

    def enter(a):
        if dia.get() == "":
            dia.insert(0, "Dia")
    def leave(a):
        if dia.get() == "Dia":
            dia.delete(0, END)

    def enter1(e):
        if mês.get() == "":
            mês.insert(0, "Mês")
    def leave1(e):
        if mês.get() == "Mês":
            mês.delete(0, END)

    def enter2(e):
        if ano.get() == "":
            ano.insert(0, "Ano")
    def leave2(e):  
        if ano.get() == "Ano":  
            ano.delete(0, END)


    Label(frame1, bg="silver", text="Data de nascimento", fg="black").place(x=525, y=110)
    dia = Entry(frame1, relief="solid", width=5)
    dia.place(x=525, y=155)
    dia.insert(0, "Dia")
    dia.bind("<FocusIn>", leave)
    dia.bind("<FocusOut>", enter)

    mês = Entry(frame1, relief="solid", width=5)
    mês.place(x=570, y=155)
    mês.insert(0, "Mês")
    mês.bind("<FocusIn>", leave1)
    mês.bind("<FocusOut>", enter1)
    
    ano = Entry(frame1, relief="solid", width=5)
    ano.place(x=615, y=155)
    ano.insert(0, "Ano")
    ano.bind("<FocusIn>", leave2)
    ano.bind("<FocusOut>", enter2)
    

    Label(frame1, bg="silver", text="Sexo", fg="black").place(x=345, y=110)
    M = Radiobutton(frame1, value="M", text="M", var=valor, bg="silver")
    M.place(x=295, y=150)
    F = Radiobutton(frame1, value="F", text="F", var=valor, bg="silver")
    F.place(x=385, y=150)

    Label(frame1, bg="silver", text="Distrito", fg="black").place(x=50, y=210)
    distrito = Entry(frame1, relief="solid")
    distrito.place(x=50, y=255)

    Label(frame1, bg="silver", text="Qua", fg="black").place(x=300, y=210)
    quarteirão = Entry(frame1, width=5, relief="solid")
    quarteirão.place(x=295, y=255)
    Label(frame1, bg="silver", text="Altura", fg="black").place(x=340, y=210)
    altura = Entry(frame1, width=5, relief="solid")
    altura.place(x=340, y=255)
    Label(frame1, bg="silver", text="Casa", fg="black").place(x=388, y=210)
    casa = Entry(frame1, width=5, relief=SOLID)
    casa.place(x=385, y=255)

    Label(frame1, bg="silver", text="Bairro", fg="black").place(x=525, y=210)
    bairro = Entry(frame1, relief="solid")
    bairro.place(x=525, y=255)
    #___________________________________________________________________________________________________________________________________

    frame2 = Frame(janela, width=700, height=100, bg="white", bd=1)
    frame2.pack(pady=20)

    reset = Button(frame2, width=40, height=3, text="RESET", bg="silver", relief="solid", command=resetar)
    reset.place(x=0, y=0)
    submit = Button(frame2, width=40, text="SUBMIT", height=3, bg="silver", relief="solid", command=Submit)
    submit.place(x=408, y=0)


f1()
janela.mainloop()