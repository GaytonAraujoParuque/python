nome = str(input('digite o seu nome completo:'))
print('Analisando seu nome...')
print('>Em letras maiusculas fica:', nome.upper())
print('>Em letras minusculas fica:', nome.lower())
print('>O seu nome contem {} letras'.format(len(nome) - nome.count(' ')))
#print('>seu primeiro nome contem {} letras'.format(nome.find(' ')))
d1 = nome.split()
print('>Seu primeiro nome e {} e ele contem {} letras'.format((d1[0]), len(d1[0])) )