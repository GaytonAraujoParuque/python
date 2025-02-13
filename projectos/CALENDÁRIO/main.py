from tkinter import *
from tkcalendar import *

janela = Tk()


def select():
    data_selecionada.destroy()
    minhaData = calendário.get_date()
    data_selecionada = Label(janela, text=minhaData)
    data_selecionada.pack(padx=2, pady=2)


calendário = Calendar(janela, setmode="day",  date_pattern='d/m/y')
calendário.pack(padx=15, pady=15)

abrir = Button(janela, text="Select Date", command=select)
abrir.pack(padx=15, pady=15)

janela.title("Calendário")
janela.geometry("300x300")
janela.configure(bg="#3DFFF2")






janela.mainloop()
