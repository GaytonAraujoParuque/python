soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite {} numero:'.format(c)))
    if n % 2 == 0:
        soma += n
        cont += + 1
print('Voce informou {} nomeros e a soma e {}'.format(cont, soma))
