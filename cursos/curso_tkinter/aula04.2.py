from tkinter import *
import time

janela = Tk()
janela.title("PARUQUE")
janela.geometry("250x250")
janela.config(bg="white")

def mudarv():
    janela.config(bg="red")
def mudara():
    janela.config(bg="yellow")
def mudarb():
    janela.config(bg="blue")
def mudarr():
    janela.config(bg="green")

vermelho = Button(janela, text=("vermelho"), bg="red", command=mudarv)
vermelho.pack(side=TOP)

amarelo = Button(janela, text="amarelo", bg="yellow", command=mudara)
amarelo.pack(side=LEFT)

azul = Button(janela, text="azul", bg="blue",command=mudarb)
azul.pack(side=RIGHT)

verde = Button(janela, text="verde", bg="green", command=mudarr)
verde.pack(side=BOTTOM)
'''
cont = 0
while cont < 100000:
    janela.config(bg="red")
    time.sleep(1)
    janela.config(bg="green")
    time.sleep(1)
    janela.config(bg="purple")
    time.sleep(1)
    cont += 1'''


janela.mainloop()