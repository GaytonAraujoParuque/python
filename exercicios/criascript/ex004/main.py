def avaliar(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return 'O ano É BISSEXTO 1:)'
    elif ano % 100 == 0 and ano % 400 == 0:
        return 'O ano É BISSEXTO :)'
    else:
        return 'O ano NÃO É BISSEXTO :('


print(avaliar(2023))