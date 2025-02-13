def area(comprimento, largura):
    multiplicacao = comprimento * largura
    print('-' * 60)
    print(f'\033[32mA area do seu terreno de {comprimento} x {largura} e {multiplicacao} m^2\033[m')
    print('-' * 60)
print('-' * 60)
area(float(input('\033[34mDigite o valor do comprimento [m]:\033[m')), float(input('\033[34mDigite o valor da largura [m]:\033[m')))

