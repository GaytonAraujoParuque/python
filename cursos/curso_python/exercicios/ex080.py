lista = list()
for c in range(0, 5):

    dados = int(input('Digite um numero:'))
    if c == 0 or dados > lista[len(lista) - 1]:
        lista.append(dados)
    else:
        pos = 0
        while pos <= len(lista):
            if dados <= lista[pos]:
                lista.insert(pos, dados)
                break
            pos += 1
print('Os valores digitados sao: {}'.format(lista))
