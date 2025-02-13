from tkinter import *

janela = Tk()
janela.geometry("450x600")
janela.title("MInha App")
janela.configure(bg="black")

#Adicionando uma tarefa
def adicionar_tarefa():
    tarefa = entrada.get()

    frame_lista = Frame(janela, bg="red", height=10, width=100, relief=SOLID, bd=1)
    frame_lista.pack(fill=X, padx=5, pady=5)
    label_tarefa = Label(frame_lista, text=tarefa, bg="red")
    label_tarefa.pack(side=LEFT)

    botão_deletar = Button(frame_lista, command=lambda: deletar(frame_lista), text="DELETE", bg="red")
    botão_deletar.pack(side=RIGHT)

    feito = Button(frame_lista, bg="red", text="FEITO", command=lambda: certo(label_tarefa, feito, botão_deletar, frame_lista))
    feito.pack(side=RIGHT)
    entrada.delete(0, END)
    
#Deletar uma tarefa
def deletar(x):
    x.destroy()

#mostrar que a tarefa foi concluida
def certo(label_tarefa, feito, botão_deletar, frame_lista):
        cor = label_tarefa.cget("bg")
        #fonte_atual = label_tarefa.cget("font")
        if "red" in cor:
    
            label_tarefa.config(bg="light green")
            feito.config(bg="light green")
            botão_deletar.config(bg="light green")
            frame_lista.config(bg="light green")
            #nova_fonte  = fonte_atual + " overstrike"
    
        else:
             
            label_tarefa.config(bg="red")
            feito.config(bg="red")
            botão_deletar.config(bg="red")
            frame_lista.config(bg="red")
            #nova_fonte = fonte_atual.replace(" overstrike", "")
             
título = Label(janela, text="MINHA APP", font=("times new roman", 20), bg="black", fg="light blue")
título.pack(pady=20)

frame_total = Frame(janela, bg="black", height=10)
frame_total.pack(pady=20)

entrada = Entry(frame_total, width=40, bg="light blue",  text="Escreva a aquí")
entrada.pack(side=LEFT, padx=10)

botão_adicionar = Button(frame_total, text="adicionar", bg="light blue", command=adicionar_tarefa)
botão_adicionar.pack(side=LEFT, padx=10)

rolar = Scrollbar(janela,orient='vertical')#, command=janela.yview)
rolar.pack(side=RIGHT,  fill=Y)


janela.mainloop()