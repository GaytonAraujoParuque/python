from datetime import date
ano = int(input('Digite o ano que quer analisar.Digite 0 para analisar o ano atual.'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e BiSSEXTO'.format(ano))
else:
    print('O ano {} nao e BISSEXTO'.format(ano))
