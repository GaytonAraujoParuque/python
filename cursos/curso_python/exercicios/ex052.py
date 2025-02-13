numero = int(input('Digite um numero:'))
numero += 1
total = 0
for c in range(1, numero):
    if numero % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'O numero {numero - 1} foi divsivel {total} vezes no total')
