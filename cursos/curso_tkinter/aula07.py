#Usando um checkbutton
from tkinter import *


janela = Tk()
janela.title("CHECKBUTON")
janela.geometry("300x300")

a = IntVar()
lb = Label(janela, text="")
lb.grid(column=1, row=0)

def printar():
    global a
    v = a.get()
    if v == 1:
        lb.config(text="<<Muito bem feito amigo>>")

    else:
        lb.config(text="")

linha = Checkbutton(janela, text="revisar",  var=a, onvalue=1, offvalue=0, command=printar)
linha.grid(column=0, row=0)

janela.mainloop()

