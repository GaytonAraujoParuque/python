'''from math import factorial
fatorial = int(input('Digite um numero para\ncalcular o seu fatorial:'))
f = factorial(fatorial)
print(f'O fatorial de {fatorial} e {f}')

c = fatorial
print(f'{fatorial}! = ', end='')
while c >= 1:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    c -= 1
print(f, end='')'''


numero = int(input('Digite um numero para\ncalcular o seu fatorial:'))
print(f'{numero}! = ', end='')
c = numero
f = 1

while c > 0:
    print(c, end=' ')
    f *= c
    c -= 1
    print('x' if c > 1 else '=', end=' ')
print(f)
