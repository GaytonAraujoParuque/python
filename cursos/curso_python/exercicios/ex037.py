n = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para a conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
o = int(input('Digite a sua opcao:'))
if o != 1 and o != 2 and o != 3:
    print('Ha algo de errado com o numero digitado')
elif o == 1:
    print('{} convertido para binario e {}'.format(n, bin(n)))
elif o == 2:
    print('{} convertido para octal e {}'.format(n, oct(n)))
elif o == 3:
    print('{} convertido para hexadecimal e {}'.format(n, hex(n)))
