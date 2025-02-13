print('=-=-' * 20)
print('Gerador de PA')
print('=-=-' * 20)
numero = int(input('Digite o 1 termo:'))
razao = int(input('Digite a razao da PA:'))
print('=-=-' * 20)
termo = numero
cont = 1
while cont <= 10:
    termo += razao
    cont += 1
    print(termo, end=' -> ')
print('Fim')
