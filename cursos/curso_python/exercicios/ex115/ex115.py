import func
from time import sleep

while True:
    func.menu_principal()
    
    while True:
        opção  = int(input("\033[33mSua opção: \033[m")) 
        if opção == 1 or opção == 2 or opção == 3:
            break
        else:
            print("\033[31mERRO! Por favor digite uma opção válida.")

    if opção == 1:
        func.cadastrados()

    elif opção == 2:
        func.cadastro()

    else:
        b = "Saindo do sistema... "
        d = "Até logo"
        print("--" * 40)
        sleep(1)
        print(f"{b:^80}")
        sleep(1)
        print(f"{d:^80}")
        print("--" * 40)
        break
