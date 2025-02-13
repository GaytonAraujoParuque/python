from datetime import date
a1 = int(input('Digite o seu ano de nascimento:'))
a2 = date.today().year - a1
if a2 == 18:
    print('Ja e hora de se cadastrar ao servico militar')
elif a2 < 18:
    a3 = 18 - a2
    print('Tera que se alistar daqui a {} anos'.format(a3))
else:
    a4 = a2 - 18
    print('Teria que se alistar a {} anos atras'.format(a4))
ano = int(input('Digite 1 para ver o ano atual:'))
if ano == 1:
    print('Estamos no ano de {}'.format(date.today().year))
