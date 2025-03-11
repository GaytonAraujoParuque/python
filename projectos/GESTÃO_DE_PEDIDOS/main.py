from tkinter import *

janela = Tk()
janela.geometry("1000x500")
janela.title("SISTEMA DE GESTÃO DA CONTA")
janela.resizable(False, False)



def Total():
    try: a1 = int(entrada_batatas_fritas.get())
    except: a1 = 0

    try: a2 = int(entrada_hamburguer_simples.get())
    except: a2 = 0

    try: a3 = int(entrada_hamburguer_duplo.get())
    except: a3 = 0

    try: a4 = int(entrada_mini_bolo.get())
    except: a4 = 0

    try: a5 = int(entrada_guisado_de_vaca.get())
    except: a5 = 0

    try: a6 = int(entrada_feijoada.get())
    except: a6 = 0

    try: a7 = int(entrada_fígado.get())
    except: a7 = 0

    #Definindo o preço de cada item por quantidade

    total1 = 100 * a1
    total2 = 80 * a2
    total3 = 150 * a3
    total4 = 150 * a4
    total5 = 200 * a5
    total6 = 180 * a6
    total7 = 200 * a6
    
    

    #entrada_total = Entry(frame_conta, font=("aria", 20, "bold"), textvariable=conta_total, bd=6, width=15, bg="lightgreen")
    #entrada_total.place(x=20, y=100)
    entrada_total = Label(frame_conta, font=("aria", 20, "bold"), textvariable=conta_total, width=15, bg="lightgreen", relief=RAISED)
    entrada_total.place(x=20, y=100)

    custo_total = total1 + total2 + total3 + total4 + total5 + total6 + total7
    conta_string = str("%.2f" %custo_total), "MZN"
    conta_total.set(conta_string)

def Reset():
    entrada_batatas_fritas.delete(0, END)
    entrada_hamburguer_simples.delete(0, END)
    entrada_hamburguer_duplo.delete(0, END)
    entrada_mini_bolo.delete(0, END)
    entrada_guisado_de_vaca.delete(0, END)
    entrada_feijoada.delete(0, END)
    entrada_fígado.delete(0, END)

    global entrada_total
    conta_total.set("")   
    



título = Label(janela, text="GESTÃO DE PEDIDOS", bg="black", fg="white",font=("calibri",  33),  width="300", height="2")
título.pack()

#MENU CARD

frame_menu = Frame(janela, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
frame_menu.place(x=10,  y=118)

Label(frame_menu, text="Cardápio",font=("Gabriola", 40, "bold"), fg="black", bg="lightgreen").place(x=65, y=0)

Label(frame_menu, font=("MV Boli",  15,'bold'), text="Batatas fritas......100", fg="black", bg="lightgreen").place(x=10, y=80)
Label(frame_menu, font=("MV Boli",  15,'bold'), text="Hamburguer simples..80", fg="black", bg="lightgreen").place(x=10, y=110)
Label(frame_menu, font=("MV Boli",  15,'bold'), text="Hamburguer duplo...150", fg="black", bg="lightgreen").place(x=10, y=140)
Label(frame_menu, font=("MV Boli",  15,'bold'), text="Mini bolo............150 ", fg="black", bg="lightgreen").place(x=10, y=170)
Label(frame_menu, font=("MV Boli",  15,'bold'), text="Guisado de vaca......200", fg="black", bg="lightgreen").place(x=10, y=200)
Label(frame_menu, font=("MV Boli",  15,'bold'), text="Feijoada...............180", fg="black", bg="lightgreen").place(x=10, y=230)
Label(frame_menu, font=("MV Boli",  15,'bold'), text="Fígado................200", fg="black", bg="lightgreen").place(x=10, y=260)


#CONTA

frame_conta = Frame(janela, bg="lightyellow", highlightbackground="black",highlightthickness=1, width=300, height=370)
frame_conta.place(x=690,y=118)

label_conta = Label(frame_conta, text="Conta", font=("calibri", 20), bg="lightyellow")
label_conta.place(x=110, y=10)

label_total = Label(frame_conta, font=("aria", 20, "bold"), text="Total", width=16, fg="lightyellow", bg="black")
label_total.place(x=10, y=50)





#Trabalho de entrada
frame_entrada = Frame(janela, width="400", height="370", bd=4,  relief=RAISED)
frame_entrada.place(x=315, y=118)

batatas_fritas = StringVar()
hamburguer_simples = StringVar()
hamburguer_duplo = StringVar()
mini_bolo = StringVar()
guisado_de_vaca = StringVar()
feijoada = StringVar()
fígado = StringVar()
conta_total = StringVar()

#labels
label_batatas_fritas = Label(frame_entrada, font=("aria", 20, "bold"), text="Batatas fritas", width=12, fg="blue4")
label_batatas_fritas.grid(column=0, row=1)

hamburguer_simples = Label(frame_entrada, font=("aria", 20, "bold"), text="Hamburguer simples", width=12, fg="blue4")
hamburguer_simples.grid(column=0, row=2)

hamburguer_duplo= Label(frame_entrada, font=("aria", 20, "bold"), text="Hamburguer duplo", width=12, fg="blue4")
hamburguer_duplo.grid(column=0, row=3)

mini_bolo = Label(frame_entrada, font=("aria", 20, "bold"), text="Mini bolo", width=12, fg="blue4")
mini_bolo.grid(column=0, row=4)

guisado_de_vaca = Label(frame_entrada, font=("aria", 20, "bold"), text="Guisado de vaca", width=12, fg="blue4")
guisado_de_vaca.grid(column=0, row=5)

feijoada = Label(frame_entrada, font=("aria", 20, "bold"), text="Feijoada", width=12, fg="blue4")
feijoada.grid(column=0, row=6)

fígado = Label(frame_entrada, font=("aria", 20, "bold"), text="Fígado", width=12, fg="blue4")
fígado.grid(column=0, row=7)

#Entrada
entrada_batatas_fritas = Entry(frame_entrada, font=("aria", 20, "bold"), textvariable=batatas_fritas, bd=6, width=8, bg="lightpink")
entrada_batatas_fritas.grid(column=1, row=1)

entrada_hamburguer_simples = Entry(frame_entrada, font=("aria", 20, "bold"), textvariable=hamburguer_simples, bd=6, width=8, bg="lightpink")
entrada_hamburguer_simples.grid(column=1, row=2)

entrada_hamburguer_duplo = Entry(frame_entrada, font=("aria", 20, "bold"), textvariable=hamburguer_duplo, bd=6, width=8, bg="lightpink")
entrada_hamburguer_duplo.grid(column=1, row=3)

entrada_mini_bolo = Entry(frame_entrada, font=("aria", 20, "bold"), textvariable=mini_bolo, bd=6, width=8, bg="lightpink")
entrada_mini_bolo.grid(column=1, row=4)

entrada_guisado_de_vaca = Entry(frame_entrada, font=("aria", 20, "bold"), textvariable=guisado_de_vaca, bd=6, width=8, bg="lightpink")
entrada_guisado_de_vaca.grid(column=1, row=5)

entrada_feijoada = Entry(frame_entrada, font=("aria", 20, "bold"), textvariable=feijoada, bd=6, width=8, bg="lightpink")
entrada_feijoada.grid(column=1, row=6)

entrada_fígado = Entry(frame_entrada, font=("aria", 20, "bold"), textvariable=fígado, bd=6, width=8, bg="lightpink")
entrada_fígado.grid(column=1, row=7)


#BOTÕES

botão_reset = Button(frame_entrada, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Reset", command=Reset)
botão_reset.grid(row=8, column=0)

botão_total = Button(frame_entrada, text="Total", bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, command=Total)
botão_total.grid(row=8, column=1)










janela.mainloop()