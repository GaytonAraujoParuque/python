expressao = list()
expressao.append(str(input('Digite a expressao:')))
cont1 = expressao.count('(')
cont2 = expressao.count(')')
if cont1 == cont2:
    print(f'A sua expressao e valida :)')
else:
    print(f'A sua expressao nao e valida :(')
