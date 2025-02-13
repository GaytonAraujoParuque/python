print('Digite uma frase')
frase = str(input('>')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
contador = len(junto)
for letra in range(contador - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase nao e um palindromo')
