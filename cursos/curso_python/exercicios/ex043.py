print('\033[35m<++>' * 20)
print('ANALISADOR DO INDICE CORPORAL ((> - <))')
print('<++>' * 20)
p = float(input('Digite o seu peso:'))
a = float(input('Digite a sua altura:'))
print('<++>' * 20)
m1 = p / (a * 2)
if m1 < 18.5:
    print('\033[31mABAIXO DO PESO')
elif m1 >= 18.5 and m1 <= 25:
    print('\033[32mPESO IDEAL')
elif m1 > 25 and m1 <= 30:
    print('\033[33mSOBREPESO')
elif m1 > 25 and m1 <= 40:
    print('\033[31mOBESIDADE')
else:
    print('\033[31m0BESIDADE MORBIDA')
print('\033[35m<++>' * 20)

