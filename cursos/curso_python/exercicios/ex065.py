numero = int(input('Digite um numero:'))
c = 1
s = numero
opcao = str(input('Quer contiinuar [S/N]:'))
while opcao in 'Ss':
    numero = int(input('Digite um numero:'))
    opcao = str(input('Quer continuar [S/N]:'))
    maior = menor = numero
    c += 1
    s += numero
    if c == 1:
        maior = menor = numero
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = s / c
print(f'Voce digitou {c} numeros e a media e {media}')
print(f'O maior numero e {maior} e o menor numero e {menor}')
