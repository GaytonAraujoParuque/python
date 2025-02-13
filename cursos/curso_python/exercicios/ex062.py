print('Gerador de PA')
print('-=' * 20)
termo = int(input('Primeiro termo:'))
razao = int(input('Razao da PA'))
numero = termo
c = 0
print(termo, end=' ')
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        numero += razao
        c += 1
        print(numero, end=' ')
    mais = int(input('Quantos termos mais voce quer mostrar:'))
print(f'Progressao finalizada com {total} termos mostrados')
