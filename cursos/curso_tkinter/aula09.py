from tkinter import *

janela = Tk()
janela.geometry("300x300")
janela.title("LISTBOX")

caixa = Listbox(janela, width=30, bg="pink")
caixa.grid(column=0, row=0)

lista = ["Python", "CSS/html", "JavaScript", "Gayton Araújo Paruque"]

lb = Label(janela, text="")
lb.grid(column=1, row=0)

def imprimir():
    lb.configure(text=caixa.get(ACTIVE))

def deletar():
    caixa.delete(ANCHOR)
    lb.configure(text="")

for c in lista:
    caixa.insert(END, c)

botão = Button(janela, text="imprimir", command=imprimir)
botão.grid(column=0, row=1)

btdel = Button(janela, text="deletar", command=deletar)
btdel.grid(column=0, row=2)

#delete(início, fim) exclui linhas no intervalo determinado
#delete(ANCHOR) exclui elemento selecionado
#delete(2) exclue o segundo item na posição
#delete(0, END) exclue todos os intens
#delete(0, ANCHOR)




a = caixa.get(ACTIVE) #Obtém o primeiro item da listbox
b = caixa.get(1) #Obtém o itém do index 
c = caixa.get(0,2) #Obtém itens no intervalo entre 1 e 2



janela.mainloop()