#Criando  um Entry
from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("ENTRY")
janela.geometry("400x400")
janela.config(background="violet")

nome = Label(janela,  text="COMMENT TU T'APPELE?", background="orange").grid(column=0, row=0)
idade = Label(janela,text="QUEL ÂGE TU AS?", background="pink").grid(column=0, row=1)
país = Label(janela, text="QUEL EST TON PAYS?", background="purple").grid(column=0, row=2)

entrada1 = Entry(janela,  width=40)
entrada1.grid(column=1, row=0)
entrada2 = Entry(janela, width=40)
entrada2.grid(column=1, row=1)
entrada3 = Entry(janela, width=40)
entrada3.grid(column=1, row=2)

def testar():
    global entrada1
    global entrada2
    global entrada3
    a = entrada1.get()
    b = entrada2.get()
    c = entrada3.get()

    print(a,b,c)

botão = Button(janela, text="testar", command=testar)
botão.grid(column=1, row=3)

janela.mainloop()