from math import sqrt

def equacao(a, b, c):
    delta = b**2 - 4 * a * c
    if delta >= 0:
        x1 = -b + sqrt(delta) / 2 * a
        x2 = -b - sqrt(delta) / 2 * a
        print(f'x1 => {x1}\nx2 => {x2}')
    else:
        print('Delta menor que zero')
equacao(1, 9, -3)