print('-' * 50)
print('LISTAGEM DE PRECOS')
print('-' * 50)
produtos = 'Lapis', 15.00, 'Borrachas', 20.00, 'Caderno', 50.00, 'Pasta', 1500.00, 'Livro', 700.00
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'{produtos[pos]:.>15}')
