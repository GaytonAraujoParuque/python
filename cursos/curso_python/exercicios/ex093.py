from time import *

dic = dict()
lista = list()
def printar():
    print("-=" * 20)

dic["nome"] = str(input("Nome do jogador:"))
par = int(input(f"Quantas partidas {dic['nome']} jogou? "))

for c in range(1, par+1):
    a = int(input(f"Quantos gols na partida{c}? ")) 
    lista.append(a)

total = 0
comp = len(lista)
for c in range(0, comp):
    total += lista[c]

dic["gols"] = lista

dic["total"] = total

printar()
print(dic)
printar()

for k, v in dic.items():
    print(f"O campo {k} tem o valor {v}")

printar()

print(f"O jogador {dic["nome"]} jogou {par} partidas.")

for c in range(0, par):
    print(f"    => Na partida {c+1}, fez {lista[c]} gols")

print(f"foi um total de {total} gols")

printar()
