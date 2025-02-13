soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
for c in range(1, 5):
    print(f'---- {c} PESSOA ----')
    nome = str(input('NOME:')).capitalize().strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M/F]:')).upper().strip()
    soma_idade += idade
    if c == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

media_idade = soma_idade / 4
print(f'A media de idade do grupo e de {media_idade} anos')
print(f'O homem mais velho tem {idade} e se chama {nome}')









