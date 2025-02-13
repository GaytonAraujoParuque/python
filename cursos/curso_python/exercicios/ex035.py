print('\033[34m<==>' * 20)
print('\033[34mSUPER ANALISADOR DE TRIANGULOS (0 - 0)')
print('\033[0;34m<==>' * 20)
c1 = float(input('\033[36mDigite o comprimento da primeira recta:'))
c2 = float(input('Digite o comprimento da segunda recta:'))
c3 = float(input('Digite o comprimento da terceira recta:\033[m'))
print('\033[34m<==>' * 20)
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('\033[32mOs comprimentos acima podem formar um triangulo :)\033[m')
else:
    print('\033[1;31mOs comprimentos acima nao podem formar um triangulo :(\033[m')
print('\033[34m<==>' * 20)
