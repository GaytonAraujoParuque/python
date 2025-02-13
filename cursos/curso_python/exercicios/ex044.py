print('\033[33m<-->' * 20)
print('ANALISADOR DE PRECOS (0..0)')
print('<-->' * 20)
p = float(input('Digite o valor do produto:'))
print('<-->' * 20)
print('\033[4mCONDICOES DE PAGAMENTO\033[0;33m')
print('[1] A VISTA, DINHEIRO OU CHEQUE')
print('[2] A VISTA NO CARTAO')
print(('[3] EM ATE 2x NO CARTAO'))
print('[4] EM ATE 3x OU MAIS NO CARTAO')
print('<-->' * 20)
c = int(input('Digite o numero da condicao de pagamento:'))
print('<-->' * 20)
if c != 1 and c != 2 and c != 3 and c != 4:
    print('HA ALGO ERRADO COM O NUMERO DIGITADO')
elif c == 1:
    v1 = p * 10 / 100
    v2 = p - v1
    print('O produto custara {:.2f}$'.format(v2))
elif c == 2:
    v1 = p * 5 / 100
    v2 = p - v1
    print('O produto custara {:.2f}'.format(v2))
elif c == 3:
    print('O produto continuara com o seu presso normal')
elif c == 4:
    v1 = p * 20 / 100
    v2 = p + v1
    print('O  produto custara {:.2f}'.format(v2))
print('<-->' * 20)



