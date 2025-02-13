def lista_ord():
    x = str(input('Digite o numero: '))
    lista = list()
    tam = len(x)
    for c in range(0, tam):
        lista.append(int(x[c]))
    lista.sort()
    print(lista)

lista_ord()