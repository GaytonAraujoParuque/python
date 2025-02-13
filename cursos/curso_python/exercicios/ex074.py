import random
maior = float('-inf')
menor = float('inf')

print('Os numeros sorteados sao:')
for c in range(1, 6):
    numero = random.randint(1, 10)
    print(numero, end='  ')
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'\nO maior valor e {maior} e o menor valor e {menor}')


