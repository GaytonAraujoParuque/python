from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c} pessoa:'))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 18:
        print(f'MAIOR DE IDADE {idade} anos')
    else:
        print(f'MENOR DE IDADE {idade} anos')
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo {maior} e/sao maior(es) de idade e {menor} e/sao menor(es) de idade')


