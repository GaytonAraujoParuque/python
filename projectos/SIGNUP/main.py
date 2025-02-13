from tkinter import *
from tkinter import messagebox

dicionário = dict()

janela = Tk()
janela.geometry("925x500")
janela.title("Signup")
janela.configure(bg="#fff")
janela.resizable(False, False)

img = PhotoImage(file='login.png')
a = Label(janela, image=img, bg="white")
a.place(x=50, y=80)

def signup():
    global dicionário
    dicionário={}
    nome = usuário.get()
    password = code.get()
    confirmar_password = confirmar.get()

    if password == confirmar_password and nome != "":
        dicionário["nome"]=nome
        dicionário["password"]=password
        messagebox.showinfo("Sign up", f"Sucessfully sign up, welcome {nome}")

    elif password != confirmar_password and nome != "":
        messagebox.showinfo("Sign up", "Both passwords should match")

    elif password == confirmar_password and nome == "":
        messagebox.showinfo("Sign up", "Please, fill the name space")

    elif password=="" and confirmar_password=="" and nome == "":
        messagebox.showinfo("Sign up", "Please, fill the spaces")

    elif password == "":
        messagebox.showinfo("Sign up", "Please, fill the password space")
    print(dicionário)

   







frame = Frame(janela, width=350, height=390, bg="#fff")
frame.place(x=480, y=50)

cabeçalho = Label(frame,  text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light",  23,  "bold"))
cabeçalho.place(x=100, y=5)

#_______________________________________________________________________________________________________________________
def on_enter(e):
    code.delete(0, END)
def on_leave(e):
    if code.get() == "":
        code.insert(0,  "Password")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)

#_______________________________________________________________________________________________________________________
def on_enter(e):
    usuário.delete(0, END)
def on_leave(e):
    if usuário.get() == "":
        usuário.insert(0,  "Nome do usuário")

usuário = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
usuário.place(x=30, y=80)
usuário.insert(0, "Nome do usuário")
usuário.bind("<FocusIn>",on_enter)
usuário.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)


#_______________________________________________________________________________________________________________________
def on_enter(e):
    confirmar.delete(0, END)
def on_leave(e):
    if confirmar.get() == "":
        confirmar.insert(0,  "Confirmar a password")

confirmar = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
confirmar.place(x=30, y=220)
confirmar.insert(0, "Confirmar a password")
confirmar.bind("<FocusIn>",on_enter)
confirmar.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

#_______________________________________________________________________________________________________________________
Button(frame, width=39, pady=7, text="Sign up", bg="#57a1f8", fg="white", bd=0, command=signup).place(x=35, y=280)
label  = Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei  UI Light", 9))
label.place(x=90, y=340)

sign_in = Button(frame,  text="Sign in", width=6,  bd=0, fg="#57a1f8", bg="white", cursor='hand2')
sign_in.place(x=200, y=340)



janela.mainloop()

