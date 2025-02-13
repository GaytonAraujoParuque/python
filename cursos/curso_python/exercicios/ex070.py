total = mais = 0
menos = 0
while True:
    nome = str(input('Nome do produto:'))
    preco = float(input('Preco do produto:'))
    total += preco
    if preco > 1000.00:
        mais += 1
    if preco < menos:
        menos = preco
    opcao = ' '
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar [S/N]:')).upper().strip()
    if opcao == 'N':
        break
print(f'Total da compra: [ {total} ]')
print(f'Total de produtos que custam mais de 1000: [ {mais} ]')
print(f'O produto mais barato e custou: [ {menos} ]')


