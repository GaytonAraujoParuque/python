from random import randint
from time import sleep
lista = list()
jogos = list()
tot = 0
print('-' * 21)
print('     ELEFANT BET     ')
print('-' * 21)
opcao = int(input('Quantos jogos quer que eu sorteie:'))
print(f'-=-=-= SORTEANDO {opcao} JOGOS =-=-=-')
while tot < opcao:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=-=-=-= > BOA SORTE < =-=-=-=-')
