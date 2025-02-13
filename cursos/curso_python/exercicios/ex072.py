palavras = ('zero', ' um', 'dois', 'treis', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um numero de 0 a 20:'))
while numero > 20 or numero < 0:
    numero = int(input('Tente novamente.Digite um numero de 0 a 20:'))
print(f'Voce digitou o numero {palavras[numero]}')
print('cara doido')