from random import randint
from time import *
from operator import itemgetter

ranking =  {}

def printar():
    print("--" * 40)

printar()

print("Valores sorteados:")
dicionário = dict()
for c in range(0, 4):
    dicionário[f"jogador{c+1}"] = randint(1, 6)
    sleep(1)
    print(f"O jogador{c+1} tirou {dicionário[f"jogador{c+1}"]}")

ranking = sorted(dicionário.items(),key=itemgetter(1))

printar()
print(dicionário)
print(ranking)
printar()

print("    == RANKING DOS JOGADORES ==")
cont = 0
for c in ranking:
    cont += 1
    sleep(1)
    print(f"      {cont} lugar: {c[0]} com {c[1]}")
    
        
printar()
