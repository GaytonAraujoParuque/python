def ordenar(x):
    x = str(x)
    tamanho = len(x)
    lista=list()
    for c in range(0, tamanho):
        lista.append(x[c])
    lista.sort()
    return lista

print(ordenar(84323))
    