from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.geometry("300x300")
janela.title("Radiobutton")

valor = StringVar()

lb = Label(janela, text="")
lb.grid(column=1, row=1)

def obter():
    print(f"A opção escolhida é {valor.get()}")
    lb.configure(text=valor.get())
    if valor.get() == "First":
        lb.grid(column=1, row=0)
    elif valor.get() == "Second":
        lb.grid(column=1, row=1)
    else:
        lb.grid(column=1, row=2)

rad1 = Radiobutton(janela, text="First", value="First", var=valor, command=obter)
rad1.grid(column=0, row=0)

rad2= Radiobutton(janela, text="Second", value="Second", var=valor, command=obter)
rad2.grid(column=0, row=1)

rad3 = Radiobutton(janela, text="Third", value="Third", var=valor, command=obter)
rad3.grid(column=0, row=2)



janela.mainloop()

