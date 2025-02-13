import random
print('_' * 60)
print('(-_-) Vamos jogar um jogo...')
print('Eu vou pensar em um numero de 0 a 10 ')
print('E vais tentar advinhar')
print('_' * 60)

opcao = str(input('SIM ou NAO [S/N]:')).upper()
while opcao != 'SIM' and opcao != 'NAO' and opcao != 'S' and opcao != 'N':
    opcao = str(input('ERRO, SIM ou NAO [S/N]:')).upper()
    if opcao == 'SIM' or opcao == 'NAO' or opcao == 'S' or opcao == 'N':
        break
print('_' * 60)
cont = 1
aleatorio = random.randint(0, 10)
opcao2 = int(input('Digite o numero'))
print('_' * 60)
while opcao2 != aleatorio:
    opcao2 = int(input('Erraste, tente de novo:'))
    cont += 1
    print('_' * 60)

if opcao2 == aleatorio:
    print(f'Parabens acertaste, precisaste de {cont} tentativa(s) para acertar')
