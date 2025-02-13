"""def somar(a=0, b=0, c=0):
    soma = a + b + c
    print(f'A soma de {a}, {b} e {c} é \033[34m{soma}\033[m')


somar(1, 1)
"""

"""
def função(n2):
    global n1
    n1 = 4
    print(f"n1 dentro vale {n1}")


n1 = 2
função(n1)
print(f"n1 fora vale {n1}")
"""

"""def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma

r1 = somar(1, 2, 3)
r2 = somar(4, 5, 6)
r3 = somar(5, 6, 7)
print(f'As somas foram {r1}, {r2} e {r3}')
"""

"""
from math import sqrt
def raiz(n):
    r = sqrt(n)
    return r
    

n1 = raiz(10)
n2 = raiz(20)
n3 = raiz(30)
print(f"As raizes foram {n1}, {n2}, {n3}")
"""


"""def fatorial(n=1):
    ni = 1
    for c in range(n, 0, -1):
        ni *= c
    return ni

print(fatorial(2))
"""


"""ef par(n=0):
    if n % 2 != 0:
        return False
    else:
        return True
    
r = par(59)
print(r)"""

'''
print(help(input))
print("---" * 40)
print(input.__doc__)'''

def  contador(início,fim,passo):
    """
    -> Faz uma contagem e mostra na tela
    :param início: início da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem 

    Função criada por Gayton Araújo Paruque
    """

    while início <= fim:
        print(início, end="->")
        início += passo
    print("fim")

print(contador(1, 10, 2))

print(help(contador))


