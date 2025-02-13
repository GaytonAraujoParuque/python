lista = list()
cont = 0
print('=-' * 20)
while True:
    cont += 1
    dados = int(input('Digite o {} numero:'.format(cont)))
    lista.append(dados)
    opcao = str(input('Quer continuar [S/N]:'))
    print('=-' * 20)
    if opcao in 'Nn':
        break
lista.sort(reverse=False)
cont5 = lista.count(5)
print(f'Foram digitados {cont} numero/s')
if 5 not in lista:
    print('O valor 5 nao foi digitado')
if 5 in lista:
    print('O valor 5 foi digitado')
print(f'Voce digitou os seguintes numeros:{lista}')
