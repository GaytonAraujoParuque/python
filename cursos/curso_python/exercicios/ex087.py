lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
contp = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'digite um numero para [{l}, {c}]:'))
        if lista[l][c] % 2 == 0:
            contp += lista[l][c]

print(f'[{lista[0][0]}] [{lista[0][1]}] [{lista[0][2]}]')
print(f'[{lista[1][0]}] [{lista[1][1]}] [{lista[1][2]}]')
print(f'[{lista[2][0]}] [{lista[2][1]}] [{lista[2][2]}]')

print(f'->A soma de todos valores pares digitados e {contp}')
print(f'->A soma dos valores da terceira coluna e {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'->O maior valor da segunda linha e {max(lista[1])}')

