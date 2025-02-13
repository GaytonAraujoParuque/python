numeros = list()
maior = 0
menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite o numero da posicao {c}:')))
    '''if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros'''
maior = max(numeros)
menor = min(numeros)
print(f'O maior numero digitado e {maior}')
print(f'O menor numero digitado e {menor}')