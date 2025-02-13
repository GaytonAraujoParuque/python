ficha = list()
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota1:'))
    nota2 = float(input('Nota2:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar [S/N]:'))
    if opcao in 'Nn':
        break
print('No  nome        media')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i}  {a[0]}        {a[2]}')
while True:
    opc = int(input('Mostrar notas de que aluno (999 interrompe):'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} sao {ficha[opc][1]}')
