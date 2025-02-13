from datetime import date
a1 = int(input('Digite o seu ano de nascimento:'))
a2 = date.today().year - a1
if a2 <= 9:
    print('Atleta MIRIM')
elif a2 > 9 and a2 <= 14:
    print('Atleta INFANTIL')
elif a2 > 14 and a2 <= 19:
    print('Atleta JUNIOR')
elif a2 > 19 and a2 <= 20:
    print('Atleta SENIOR')
else:
    print('Atleta MASTER')
