''''lista = list()
par = list()
imp = list()

for c in range(1, 8):
    dados = int(input(f'Digite o {c} numero:'))
    if dados % 2 == 0:
        par.append(dados)
    else:
        imp.append(dados)

lista.append(par[:])
lista.append(imp[:])
par.sort()
imp.sort()
print(f'Os valores pares digitados sao {par}')
print(f'Os valores impares digitados sao {imp}')'''

lista = [[], []]
for c in range(0, 7):
    dados = int(input(f'Digite o {c + 1} numero:'))
    if dados % 2 == 0:
        lista[0].insert(c, dados)
    else:
        lista[1].insert(c, dados)
print(f'Os valores pares digitados sao {lista[0]}')
print(f'Os valores impares digitados sao {lista[1]}')
