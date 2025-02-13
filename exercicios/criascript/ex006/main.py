alfabeto = ['a','b', 'c', 'd', 'e',  'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def tirar(x):
    global alfabeto
    lista= list()
    for c in range(0, x):
        lista.append(alfabeto[c])
    return lista

print(tirar(26))