v = int(input('Digite a distancia da viagem em km:'))
if v >= 200:
    p = v * 0.45
    print('O preco da passagem sera {:.2f}'.format(p))
else:
    p = v * 0.50
    print('O preco da passagem sera {:.2f}'.format(p))