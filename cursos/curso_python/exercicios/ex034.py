s = float(input('Digite o salario do funcionario:'))
if s > 1250.00:
    s1 = s * 10 / 100
    s2 = s1 + s
    print('Com o aumento de 10% do salario, o funcionario passa a receber {:.2f}'.format(s2))
else:
    s2 = s * 15 / 100
    s3 = s2 + s
    print('Com o aumento de 15% do salario o funcionario passa a receber {}'.format(s3))