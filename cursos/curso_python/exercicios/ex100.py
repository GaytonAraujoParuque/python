from random import randint
from time import *

lista = []

def sortear():
    for c in range(0,5):
        lista.append(randint(1, 10))


def somaPar():
    som = 0
    global lista
    for c in range(0, 5):
        if lista[c] % 2 == 0:
            som += lista[c]
    return som

sortear()
print("Sorteando 5 valores da  lista: ")
sleep(1)
for c in lista:
    print(c, end=" -> ")
print("Fim")

print(f"Somando os valores pares temos: {somaPar()}")


