numero = 0
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um numero [999 para parar]:'))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Voce digitou {cont} numero/s e a soma entre eles e {soma}')
