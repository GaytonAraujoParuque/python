pessoas = homens = mulheres  = 0
while True:
    print('-' * 15)
    print('CADASTRE UMA PESSOA')
    print('-' * 15)
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    opcao = ' '
    while opcao != 'S' and opcao != 'N' and opcao != 'SIM' and opcao != 'NAO':
        opcao = str(input('Quer continuar [S/N]:')).upper().strip()
    if opcao == 'N' or opcao == 'NAO':
        break
print(f'O total de pessoas com mais de 18 anos: [ {pessoas} ]')
print(f'O total de homens cadastrados: [ {homens} ]')
print(f'O total de mulheres com menos de 20 anos: [ {mulheres} ]')



