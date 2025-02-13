#Criando um combobox
from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.geometry("300x300")
janela.title("COMBOBOX")

combo = Combobox(janela, width=20)
combo["values"]=("gayton", "araújo", "paruque", 242)
combo.pack()
#combo.current(0)

lb = Label(janela,text="")
lb.pack()

def printar(eventObject):
    ab = combo.get()
    lb.configure(text=ab)


combo.bind("<<ComboboxSelected>>", printar)

janela.mainloop()




