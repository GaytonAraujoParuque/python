def contador(inicio, fim, passo):
    print('\033[35m-=\033[m' * 25)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c)

    if inicio > fim:
        valor = inicio
        while valor >= fim:
            inicio -= passo
            print(valor)
            valor -= passo
        
    print('\033[35m-=\033[m' * 25)
    

contador(1, 10, 2)
contador(10, 1, 2)

ini = int(input('Digite o valor do início:'))
fi = int(input('Digite o valor final:'))
pas = int(input('Digite o passo:'))

contador(ini, fi, pas)
