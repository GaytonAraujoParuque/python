print('-' * 20)
print('Sequencia de Fibonacci')
print('-' * 20)
numero = int(input('Quantos termos voce quer mostrar?'))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2}', end=' -> ')
while cont <= numero:
    t3 = t1 + t2
    cont += 1
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('Fim')
