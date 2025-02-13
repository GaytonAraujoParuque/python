import random
print('=-' * 20)
print('VAMOS JOGAR PAAR OU IMPAR')
print('=-' * 20)
vit = 0
while True:
    valor = int(input('Digite um valor:'))
    opcao = str(input('Par ou Impar [P/I]')).strip().upper()
    print('=-' * 20)
    comp = random.randint(1, 10)
    soma = comp + valor
    if opcao == 'P' and soma % 2 == 0:
        int('-' * 20)
        print(f'Voce jogou {valor} e o computador {comp}')
        print('voce ganhou parabens')
        vit += 1
        print('-' * 20)

    elif opcao == 'I' and soma % 2 != 0:
        print('-' * 20)
        print(f'Voce jogou {valor} e o computador {comp}')
        print('voce ganhou parabens')
        vit += 1
        print('-' * 20)
    else:
        print('Voce perdeu')
        print(f'Voce jogou {valor} e o computador {comp}\nA soma e {soma}')
        print('-=' * 20)
        break
print(f'GAME OVER! Voce venceu {vit} vezes')
