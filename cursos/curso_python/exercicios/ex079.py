numeros = list()
opcao = ''
while True:
    print('-=' * 20)
    dados = (int(input('Digite um numero:')))
    print('-=' * 20)
    if dados in numeros:
        print('Valor duplicado! Nao vou adicionar')
        print('-=' * 20)
    else:
        numeros.append(dados)
        print('Valor adicionado com sucesso...')
        print('-=' * 20)
    opcao = str(input('Quer continuar [S/N]:'))
    if opcao in 'Nn':
        break
numeros.sort()
print(f'Voce adicionou os seguintes valores {numeros}')
