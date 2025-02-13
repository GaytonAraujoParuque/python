v = int(input('Digite a velocidade do carro em km/h:'))
if v >= 81:
    m1 = v - 80
    m2 = float(m1 * 7)
    print('[VOCE SERA MULTADO EM {}$]'.format(m2))
else:
    print('Continue assim, voce nao sera multado')
