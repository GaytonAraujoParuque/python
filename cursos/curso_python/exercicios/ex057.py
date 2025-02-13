genero = str(input('Informe o seu sexo: [M/F]')).upper()
if genero != 'M' and genero != 'F':
    sexo = 0
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados invalidos. Por favor, informe o seu sexo:')).upper()
        if sexo == 'M' or sexo == 'F':
            print(f'Sexo {sexo} registrado com sucesso')

else:
    print(f'Sexo {genero} registrado com sucesso')