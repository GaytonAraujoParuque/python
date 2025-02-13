numero = int(input('Digite um numero [999 para parar]:'))
c = s = 0
while numero != 999:
    c += 1
    s += numero
    numero = int(input('Digite um numero [999 para parar]:'))
print(f'Voce digitou {c} numeros e a soma entre eles foi {s}')