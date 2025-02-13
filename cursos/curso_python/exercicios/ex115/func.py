from time import sleep

def menu_principal():
    print("--" * 40)
    a = "MENU PRINCIPAL"
    print(f"{a:^80}")
    print("--" * 40)

    print("\033[33m1\033[m - \033[34mVer pessoas cadastradas")
    print("\033[33m2\033[m - \033[34mCadastrar  novas pessoas")
    print("\033[33m3\033[m - \033[34mSair do sistema\033[m")

    print("--"  * 40)

lista = []

def cadastrados():
    global lista
    print("--" * 40)
    a = "PESSOAS CADASTRADAS"
    print(f"{a:^80}")
    print("--" * 40)

    for c in lista:
        for k,v  in c.items():
            sleep(1)
            print(f" {k} {v:>20} anos")



def cadastro():
    global lista
    dic = {}

    c = "NOVO CADASTRO"
    print("--" * 40)
    print(f"{c:^80}")
    print("--" * 40)


    while True:
        try:
            nome = str(input("Nome: "))
        
        except:
            print("\033[31mERR)! Digite um nome válido.\033[m")

        else:
            break

    while True:
        try:
            idade = int(input("Idade: "))

        except:
            print("\033[31mERRO! Digite uma idade válida\033[m")

        else:
            print("--" * 40)
            break

    dic[nome] = idade
    print(f"\033[32mNovo registro de {nome} foi adicionado\033[m")
    lista.append(dic)








