
while True:
    numero = int(input('Quer ver a tabuada de que valor:'))
    c = soma = 0
    while c < 10:
        c += 1
        multi = numero * c
        print(f'{c} x {numero} = {multi}')
    if numero <= -1:
        break
print('Programa terminado, volte sempre.')