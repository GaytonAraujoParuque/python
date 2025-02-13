print('=--=' * 38)
numero = int(input('Digite o 1 numero:'))
numero2 = int(input('Digite o 2 numero:'))
print('=--=' * 38)
opcao = 0
while opcao != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numero\n[5] sair do programa')
    opcao = int(input('Qual e a sua opcao:'))
    print('=--=' * 38)

    if opcao == 1:
        print(f'A soma entre {numero} e {numero2} e {numero + numero2} ')

    elif opcao == 2:
        print(f'O resultado de {numero} x {numero2} e {numero * numero2}')

    elif opcao == 3:
        if numero == numero2:
            print('Os dois numeros sao iguais')
        elif numero > numero2:
            print(f'O maior numero e {numero}')
        else:
            print(f'O maior numero e {numero2}')

    elif opcao == 4:
        print('Informe os numeros novamente')
        numero = int(input('Digite o 1 numero:'))
        numero2 = int(input('Digite o 2 numero:'))

    elif opcao > 5:
        print('Opcao invalida.')

if opcao == 5:
    print('FIM DO PROGRAMA, volte sempre')



print('=--=' * 38)
