def criptografar():
    print('=_=-=' * 10)
    x = str(input('\033[31mCriptografar =>\033[m '))
    li = list()
    lista = '********** á+-àb_6âcãdéeè!fêgíhìijóòklmôònao#púùqrstuvwxyz,?B.C/D;E=F:GHIJ\|KLMNO(PQ[R]STU)V&W%XY@ZA'
    lista_completa = list()
    for c in x:
        li.append(lista.index(c))
    print('\033[32m=>> \033[m', end='')
    for b in li:
    
        lista_completa.append(b)
        print(f'\033[35m{b}\033[m', end='')
    print('')
    print('-' * (len(lista_completa) * 2 + 4))


def descriptografar():
    lista = '********** á+-àb_6âcãdéeè!fêgíhìijóòklmôònao#púùqrstuvwxyz,?B.C/D;E=F:GHIJ\|KLMNO(PQ[R]STU)V&W%XY@ZA'
    lista_completa = list()
    x = str(input('\033[31mDescriptografar =>\033[m '))
    lista_des = list()
    tamanho = len(x)
    var = ''
    tam = len(x)
    
    for c in range(0, tamanho - 1, 2):
        c = int(c)
        var = x[c]
        var3 = x[c + 1]
        var5 = str(var) + str(var3)
        lista_completa.append(var5)
        tam -= 2
        c + 1
        
    var2 = ''
    for c in lista_completa:
        var2 += lista[int(c)]
    lista_des.append(var2)
    print(f'\033[32m=>> \033[m\033[35m{lista_des[0]}\033[m')
    print('-' * (len(lista_des[0]) + 4))
    print('=_=-=' * 10)


criptografar()
descriptografar()
