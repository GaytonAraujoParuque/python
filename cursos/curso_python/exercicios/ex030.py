n = int(input('Digite um numero inteiro:'))
r = n % 2
if r == 0:
    print('O numero {} e par'.format(n))
else:
    print('O numero {} e impar'.format(n))