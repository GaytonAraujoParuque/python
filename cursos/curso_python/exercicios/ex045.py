import random
print('\033[36m<<>>' * 20)
print(' ')
print('\033[1mPEDRA\033[36m>','>' * 20,'\033[1;36mPAPEL\033[36m','<' * 20,'\033[1m;36mTESOURA\033[36m')
print(' ')
print('\033[0;36m<<>>' * 20)
print('Vamos jogar...')
v = str(input('Digite SIM ou NAO:')).lower()
if v == 'sim':
    print('Bora la!!! ')
    print('<<>>' * 20)
    a1 = str(input('Digite a sua jogada:')).lower()
    d = 'pedra papel tesoura'
    s = d.split()
    a3 = random.randint(0, 2)
    print('A minha jogada e \033[32m{}\033[36m'.format(s[a3]))
    print('<<>>' * 20)
    if a1 == s[a3]:
        print('Empate')
    elif a1 == 'pedra' and a3 == 1:
        print('Voce perdeu')
    elif a1 == 'pedra' and a3 == 2:
        print('Voce ganhou,parabens!')
    elif a1 == 'papel' and a3 == 0:
        print('Voce ganhou,parabens!')
    elif a1 == 'papel' and a3 == 3:
        print('Voce perdeu')
    elif a1 == 'tesoura' and a3 == 0:
        print('Voce perdeu')
    else:
        print('Voce ganhou,parabens!')
elif v == 'nao':
    print('Okay, ja que tens medo!')
else:
    print('Ha algo de errado com a opcao digitada')

