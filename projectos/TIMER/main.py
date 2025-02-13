from tkinter import *
import time

janela = Tk()
janela.title("Timer")
janela.geometry("400x600")
janela.configure(bg="#000000")
janela.resizable(False, False)


cabeçalho = Label(janela, text="Timer", font=("arial", 30, "bold"),  bg="#000000",  fg="#F20B00")
cabeçalho.pack(pady=10)

Label(janela, text="Hora atual:     ", font=("arial",  15,"bold"), bg="papaya whip").place(x=65, y=70)

def clock():
    clock_time = time.strftime("%H:%M:%S %p")
    hora_atual.config(text=clock_time)
    hora_atual.after(1000,clock)

hora_atual = Label(janela, font=("arial", 15,"bold"),  text="", fg="#000",  bg="papaya whip")
hora_atual.place(x=190, y=70)
clock()


#Timer
hrs = StringVar()
Entry(janela, textvariable=hrs, width=2, font=("arial 50")).place(x=30, y=155)
hrs.set("00")
mins = StringVar()
Entry(janela, textvariable=mins, width=2, font=("arial 50")).place(x=150, y=155)
mins.set("00")
sec = StringVar()
Entry(janela, textvariable=sec, width=2, font=("arial 50")).place(x=270, y=155)
sec.set("00")


Label(janela, text="horas", font="arial 12", bg="#000", fg="#fff").place(x=45, y=250)
Label(janela, text="minutos", font="arial 12", bg="#000", fg="#fff").place(x=158, y=250)
Label(janela, text="segundos", font="arial 12", bg="#000", fg="#fff").place(x=272, y=250)

def timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

    while times > -1:
        minuto,  segundo = (times//60,  times % 60)

        hora = 0
        if minuto > 60:
            hora, minuto = (minuto//60,  minuto% 60)

        sec.set(segundo)
        mins.set(minuto)
        hrs.set(hora)

        janela.update()
        time.sleep(1)

        if (times == 0):
            sec.set("00")
            mins.set("00")
            hrs.set("00")

        times -= 1


def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")
    
def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")



botão = Button(janela, text="Start",  bg="#ea3548", bd=0, fg="#fff", width=20,  height=2, font=("arial", 10, "bold"), command=timer)
botão.pack(padx=5, pady=40, side=BOTTOM)

 
bt1 = Button(janela, text="00:02:00", font=("arial", 10,"bold"), command=brush, fg="#fff", bg="gray", overrelief=RIDGE)
bt1.place(x=39, y=300)
bt2 = Button(janela, text="00:15:00", font=("arial", 10,"bold"), command=face, fg="#fff", bg="gray", overrelief=RIDGE)
bt2.place(x=158, y=300)
bt3 = Button(janela, text="00:10:00", font=("arial", 10,"bold"),  command=eggs, fg="#fff", bg="gray", overrelief=RIDGE)
bt3.place(x=275, y=300)



janela.mainloop()
