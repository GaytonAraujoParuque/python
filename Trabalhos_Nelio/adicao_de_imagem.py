from tkinter import *


root = Tk()
root.geometry("1000x1000")
img = PhotoImage(file="bolsa.png")
label_imagem = Label(root, image=img)
label_imagem.pack()
root.mainloop()

