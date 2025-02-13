lista_total = list()
lista1 = list()
lista2 = list()
while True:
    dados = int(input('Digite um numero:'))
    if dados % 2 == 0:
        lista2.append(dados)
    else:
        lista1.append(dados)
    lista_total.append(dados)
    opcao = str(input('Quer continuar [S/N]:'))
    if opcao in 'Nn':
        break
print(f'A lista completa e {lista_total}')
print(f'A lista de pares e {lista2[:]}')
print(f'A lista de impares e {lista1[:]}')
