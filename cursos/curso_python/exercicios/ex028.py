print('(0-0):vamos jogar um jogo')
sn = str(input('SIM ou NAO:')).lower()
if sn == 'sim':
    print('Muito bem...')
    print('Eu pensei em um numero inteiro de 0 a 5')
    ad = int(input('Advinhe o numero:'))
    if ad == 1:
        print('Parabens voce ganhou')
    else:
        print('Voce perdeu!!! MAIS SORTE NA PROXIMA')
else:
    print('Parece que tens medo de perder')