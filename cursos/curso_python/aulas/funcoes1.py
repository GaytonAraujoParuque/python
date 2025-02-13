'''
def mensagem(msg):
    print('-------')
    print(msg)
    print('-------')


mensagem('\033[32mGayton\033[m')
mensagem('\033[35mAraujo\033[m')
mensagem('\033[36mParuque\033[m')
'''
'''
def soma(a, b, c):
    s = a + b + c
    print(f'A soma de a={a} com b={b} e c={c} e igual a {s}')


soma(2, 3, 4)
soma(1, 2, 3)
soma(5, 6, 7)
'''
'''
def contador(*num):
    print(f'Recebi os valores {num} no total sao {len(num)}')


contador(1, 2, 3, 4)
contador(1, 2)
'''
'''
def dobra(*valores):
    for c in valores:
        print(f'Valor dado {c}, valor dobrado {c * 2}')


dobra(1, 2, 3, 4)
'''
'''
def dobra(lista):
    print(f'Valores iniciais {lista}')
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(f'Valores dobrados {lista}')

    
sei = []
quant = int(input('Pretende ver o dobro de quantos numeros'))
cont = 0
while cont < quant:
    sei.append(int(input(f'Digite o numero que pretende ver o dobro [{cont + 1}]')))
    cont += 1
dobra(sei)
'''
