tupla = 'ola', 'bem', 'estava', 'fui', 'como'
for p in tupla:
    print(f'\nNa palavra \033[4m{p}\033[m temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')