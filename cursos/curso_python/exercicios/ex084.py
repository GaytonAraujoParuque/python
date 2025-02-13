temp = list()
lista = list()

while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    lista.append(temp[:])
    temp.clear()
    opcao = str(input('Quer continuar [S/N]:'))
    if opcao in 'Nn':
        break
print(f'Ao todo foram cadastradas {len(lista)} pessoas')
maior = max(lista)
menor = min(lista)
for c in lista:
    if c[1] == maior:
        print(f'{c[0]}', end=' ')
print(f'O maior peso digitado foi  {maior}', end=' ')
print(f'\nO menor peso digitado foi {menor}')
