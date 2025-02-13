from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Conversor")
janela.geometry("300x300")
janela.configure(bg="white")
janela.resizable(False, False)

style = ttk.Style(janela)
style.theme_use("clam")

moedas = {"USD":63.89, "EUR":67.16, "BRL":10.53, "GBP":79.64, "ZAR":3.41, "JPY":0.53, "AUD":42.51}

a = 1
def trocar():
    global a 
    saída.delete(0, END)
    moeda = ["USD", "EUR", "BRL", "GBP", "ZAR", "JPY", "AUD"]
    saída.insert(0, moeda[a])
    a += 1
    if a > 6:
        a = 0

def converter():
    tipo = saída.get()
    valor = entrada_principal.get()

    valor_convertido = int(valor) / moedas[tipo]
    moeda_convertida.config(text=str(valor_convertido))


Label(janela, text="Conversor De Moeda", bg="#0A3F03", font=("Open Sans", 15), fg="white", width=27, height=2).place(x=0, y=0)

moeda_convertida = Label(janela, relief="solid", width=19, height=2, text="", bg="white", font=("arial", 9, "bold"))
moeda_convertida.place(x=90, y=55)

Label(janela, text="De", bg="white").place(x=100, y=100)
Label(janela, text="Para", bg="white").place(x=160, y=100)

lb = Label(janela, width=5, text="MZN", bg="#0A3F03", height=1, fg="white")
lb.place(x=90, y=120)
saída = Entry(janela, relief="solid", width=5, bg="#0A3F03", fg="white")
saída.place(x=155, y=120)
saída.insert(0, "USD")


entrada_principal = Entry(janela, width=22, relief=SOLID)
entrada_principal.place(x=90, y=150)


botão_converter = Button(janela, width=18, height=2, bg="#0A3F03", text="Converter", fg="white", command=converter)
botão_converter.place(x=90, y=210)

mudar = Button(janela, text=">", width=1, height=0, bg="#0A3F03", fg="white", command=trocar)
mudar.place(x=209, y=118)

janela.mainloop()