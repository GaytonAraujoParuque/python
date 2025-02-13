print('\033[34m<==>' * 20)
print('ANALISADOR DE TRIANGULOS [(o) - (o)]  2.0')
print('<==>' * 20)
c1 = float(input('Digite o comprimento da primeira recta:'))
c2 = float(input('Digite o comprimento da segunda recta:'))
c3 = float(input('Digite o comprimento da terceira recta:'))
print('<==>' * 20)
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('\033[32mOS COMPRIMENTOS ACIMA PODEM FORMAR UM TRIANGULO')
    if c1 == c2 == c3:
        print('Formam uma TRIANGULO EQUILATERO')
    elif c1 == c2 != c3 or c1 == c3 != c2 or c1 != c2 == c3:
        print('Formam um TRIANGULO ISOSCELES')
    else:
        print('Formam um TRIANGULO ESCALENO')
else:
    print('\033[31mOS COMPRIMENTOS ACIMA NAO PODEM FORMAR UM TRIANGULO')
print('\033[34m<==>' * 20)
