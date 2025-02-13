from tkinter import *

janela = Tk()
janela.title("Joguinho")
janela.geometry("300x310")
janela.configure(bg="black")

Label(janela, text="Player 1 : X", font=("times new roman",  15), bg="black").grid(row=0, column=0)
Label(janela, text="_________", font=("times new roman", 15), bg="black").grid(row=0, column=1)
Label(janela, text="Player 2 : O", font=("times new roman", 15),  bg="black").grid(row=0, column=2)

bt1 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt1.grid(column=0, row=1)

bt2 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt2.grid(column=0, row=2)

bt3 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt3.grid(column=0, row=3)


bt4 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt4.grid(column=1, row=1)

bt5 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt5.grid(column=1, row=2)

bt6 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt6.grid(column=1, row=3)


bt7 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt7.grid(column=2, row=1)

bt8 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt8.grid(column=2, row=2)

bt8 = Button(janela, width="10", height="5", overrelief=RIDGE)
bt9 = Button(janela, width="10", height="5")
bt9.grid(column=2, row=3)


janela.mainloop()

