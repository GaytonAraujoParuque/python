print('==' * 21)
print(' ' * 10, '10 TERMOS DE UMA P.A', ' ' * 10)
print('==' * 21)
t1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razao:'))
for c in range(t1, 21, r):
    print(c, end=' -> ')
print('ACABOU')
