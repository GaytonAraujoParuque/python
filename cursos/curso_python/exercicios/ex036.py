print('\033[34m<==>' * 20)
print('\033[34mANALISADOR DE EMPRESTIMOS (!0-0!)')
print('\033[34m<==>' * 20)
c1 = float(input('Digite o vaolor da casa:---------------'))
s1 = float(input('Digite o seu salario:------------------'))
a = float(input('Digite por quantos anos pretende pagar:'))
print('<==>' * 20)
p1 = c1 / a
p2 = p1 / 12
p3 = 30 * s1 / 100
if p2 <= p3:
    print('\033[32mO seu emprestimo foi aceite\n Voce devera pagar {:.2f}$ por mes'.format(p2))
else:
    print('\033[31mO SEU EMPRESTOMO FOI NEGADO')
print('\033[34m<==>' * 20)
