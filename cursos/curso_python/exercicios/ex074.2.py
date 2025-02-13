import random
numero = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)

maior = float('-inf')
menor = float('inf')
for n in numero:
    print(n, end=' ')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'\nO maior e {maior} e o menor e {menor}')
print('max =', max(numero))
print('min = ', min(numero))