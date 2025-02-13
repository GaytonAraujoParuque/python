from time import *

dic = dict()

dic["nome"] = str(input("Nome:"))

a = int(input("Ano de nascimento:"))
a = 2024 - a
dic["idade"] = a

dic["CTPS"] = int(input("Carteira de trabalho (0 não tem):"))

if dic["CTPS"] != 0:

    dic["contratação"] = int(input("Ano de contratação:"))

    dic["salário"] = float(input("Salário:"))

    c = 2024 - dic["contratação"]
    c = 35 - c
    c += dic["idade"]
    dic["aposentadoria"] = c
    print("-=" * 20)
    

    for k, v in dic.items():
        sleep(1)
        print(f"{k} tem o valor {v}")
        
else:
    print("-=" * 20)
    
    for k,v in dic.items():
        sleep(1)
        print(f"{k} tem o valor {v}")
        

print("-=" * 20)
