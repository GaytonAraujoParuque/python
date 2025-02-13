n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
n3 = float(input('Digite a sua terceira nota:'))
m1 = (n1 + n2) / 2
m2 = (m1 + n3) / 2
if m2 < 8:
    print('\033[31mREPROVADO')
elif m2 == 8 or m2 == 9:
    print('\033[33mAPROVADO MAS DEVE MELHORAR')
elif m2 > 20:
    print('Cada nota digitada nao deve ultrapassar 20')
elif m2 > 9 and m2 <= 20:
    print('\033[32mAPROVADO')

