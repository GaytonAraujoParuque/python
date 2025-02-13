from tkinter import *

janela = Tk()
janela.geometry("300x300")
janela.title("Frame")

frame1 = Frame(janela, width=150, height=150, bg="red")
frame1.grid(column=0, row=0)

frame11 = Frame(janela, width=150, height=150, bg="green")
frame11.grid(column=1, row=0)

frame12 = Frame(janela, width=300, height=150, bg="blue")
frame12.grid(column=0, row=2, columnspan=2)

label = Label(frame1, width=10, height=5, bg="yellow", text="Olá")
label.place(x=0, y=0)

label = Label(frame11, width=10, height=5, bg="yellow", text="Olá")
label.place(x=0, y=0)

label = Label(frame12, width=10, height=5, bg="yellow", text="Olá")
label.place(x=0, y=0)

label = Label(frame12, width=10, height=5, bg="yellow", text="Olá")
label.place(x=150, y=0)

janela.mainloop()