numeros = int(input('Digite o 1 numero:')), int(input('Digite o 2 numero:')), int(input('Digite o 3 numero:')),int(input('Digite o 4 numero:'))
print('Voce digitou os seguintes valores:')
print(numeros)
print('O nummero 9 apareceu {} vezes'.format(numeros.count(9)))
ind = numeros.index(3)
ind += 1
print('O numero 3 apareceu na {} posicao'.format(ind))
print(f'Os numeros pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')