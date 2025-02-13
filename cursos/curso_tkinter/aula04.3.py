from tkinter import *

janela= Tk()
janela.geometry("200x200")

vermelho = Button(janela, text=("vermelho"), bg="red")
vermelho.grid(column=0, row=0)

azul = Button(janela, text=("azul"), bg="blue")
azul.grid(column=1, row=0)

janela.mainloop()