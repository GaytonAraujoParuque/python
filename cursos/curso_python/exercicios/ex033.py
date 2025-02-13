v1 = int(input('Digite um valor:'))
v2 = int(input('Digite outro valor:'))
v3 = int(input('Digite outro valor'))
if v1 < v2 and v1 < v3:
    print('O menor valor digitado e {}'.format(v1))
if v2 < v1 and v2 <v3:
    print('O menor valor digitado e {}'.format(v2))
if v3 < v1 and v3 < v2:
    print('O menor valor digitado e {}'.format(v3))
if v1 > v2 and v1 > v3:
    print('O maior valor digitado e {}'.format(v1))
if v2 > v1 and v2 > v3:
    print('O maior valor digitado e {}'.format(v2))
if v3 > v1 and v3 > v2:
    print('O maior valor digitado e {}'.format(v3))
if v1 == v2 != v3:
    print('O primeiro e o segundo valor digitado sao iguais')
if v1 == v3 != v2:
    print('O primeiro e o terceiro valor digitado sao iguais')
if v2 == v3 != v1:
    print('O segundo e o terceiro valor sao iguais')
if v1 == v2 == v3:
    print('Todos valores digitados sao iguais')
