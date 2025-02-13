from tkinter import *


#Criando a janela
janela = Tk()
janela.title("Meu app de tarefas")
janela.geometry("500x600")
janela.configure(bg="white")

frame_edição = None

#Criando a função que adiciona as tarefas
def adicionar():
    global frame_edição
    tarefa = entrada.get().strip()
    if tarefa and tarefa != "Escreva a sua terefa aqui":
        if frame_edição is not None:
            atualizar_tarefa(tarefa)
            frame_edição = None
        else:
            adicionar_item_tarefa(tarefa)
            entrada.delete(0, END)
    #else:
        # messagebox.showwarning("Entrada inválida", "Por favor, insira uma tarefa")


def adicionar_item_tarefa(tarefa):
    frame_tarefa = Frame(canva_interior, bg="white", bd=1, relief=SOLID)
    label_tarefa = Label(frame_tarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    label_tarefa.pack(side=LEFT, fill=X, padx=10, pady=5)

    botão_editar= Button(frame_tarefa, text="EDITAR", command=lambda f=frame_tarefa, l=label_tarefa: preparar_edição(f, l), bg="white", relief=FLAT) #image=icon_editar
    botão_editar.pack(side=RIGHT, padx=5)

    botão_deletar= Button(frame_tarefa,text="DELETAR" , command=lambda f=frame_tarefa: deletar_tarefa(f), bg="white", relief=FLAT) #image=icon_deletar
    botão_deletar.pack(side=RIGHT, padx=5)

    frame_tarefa.pack(fill=X, padx=5,  pady=5)

    checkbutton = Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alterar_sublinhado(label))
    checkbutton.pack(side=RIGHT, padx=5)

    canva_interior.update_idletasks()
    canva.config(scrollregion=canva.bbox("all"))

def preparar_edição(frame_tarefa, label_tarefa):
    global frame_edição
    frame_edição = frame_tarefa

    entrada.delete(0, END)
    entrada.insert(0, label_tarefa.cget("text"))

def atualizar_tarefa(nova_tarefa):

    global frame_edição
    for widget in frame_edição.winfo_children():
        if isinstance(widget, Label):
            widget.config(text=nova_tarefa)

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canva_interior.update_idletasks()
    canva.config(scrollregion=canva.bbox("all"))

def alterar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte = fonte_atual.replace(" overstrike", "")
    else:
        nova_fonte = fonte_atual + " overstrike" 
    label.config(font=nova_fonte)


'''
caminho_imagem = "c:\Programacao\PYTHON\PROJETOS\APP_TAREFAS\edit.jpg"
imagem = Image.open(caminho_imagem)
imagem_tk = ImageTk.PhotoImage(imagem)


icon_editar = PhotoImage(image=imagem_tk).subsample(3, 3)
icon_deletar = PhotoImage(file="delete.png").subsample(3, 3)'''


#Colocando um título
título = Label(janela, text="Meu App de Tarefas",  font="Garamond 20 bold", bg="white", fg="black")
título.pack(pady=20)

#Criando um frame
frame = Frame(janela, bg="white",  width=50)
frame.pack(pady=20)

#Adicionando  um campo de entrada
entrada = Entry(frame, bg="gray", font=("Garamond, 14"), relief=FLAT, width=30, text="Olá", fg="black")
entrada.pack(side=LEFT, padx=10)

#Criando botões
botão_adicionar = Button(frame, text="Adicionar Tarefa", bg="green", fg="white", height=1, width=15, font=("roboto", 11), relief=FLAT,command=adicionar)
botão_adicionar.pack(side=LEFT, padx=0)

#Criando um frame para a lista de tarefas com scrolbar
frame_lista = Frame(janela, bg="white")
frame_lista.pack(fill=BOTH, expand=True, padx=10, pady=10)

canva = Canvas(frame_lista, bg="white")
canva.pack(side=LEFT, fill=BOTH,  expand=True)

scrol = Scrollbar(frame_lista, orient="vertical", command=canva.yview)
scrol.pack(side=RIGHT, fill=Y)


#canva.configure(yscrollcommand=scrol.set)
canva_interior = Frame(canva, bg="white")
canva.create_window((0, 0), window=canva_interior, anchor="nw")
canva_interior.bind("<<Configure>>", lambda e: canva.configure(scrollregion=canva.bbox("all")))

janela.mainloop()