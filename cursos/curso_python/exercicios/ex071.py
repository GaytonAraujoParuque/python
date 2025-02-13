print('=' * 25)
print(' ' * 5, 'BANCO PARUQUE')
print('=' * 25)
valor = int(input('Que valor voce quer sacar:'))
total = valor
ced = 100
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        print(f'Total de notas de {ced}: [ {cont} ]')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break


