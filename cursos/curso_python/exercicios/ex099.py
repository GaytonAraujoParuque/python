def maior(*núm):
    a = max(núm)
    print(f'Os valores digitados foram {núm} e o maior número é {a}')
    

núm = ""
r = ''
while r != 'N':
    núm = int(input('Digite um número:'))

    r = str(input('Quer continuar?[S/N]'))
    if r in 'Nn':
        break
maior(núm)