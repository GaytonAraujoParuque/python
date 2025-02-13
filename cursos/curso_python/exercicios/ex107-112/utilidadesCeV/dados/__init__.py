def leiaDinheiro(a):
    while True:
        x = str(input(a).strip())

        tipo = x.isnumeric()
        if tipo == True:
            return int(x)
            break
        
        if "," in x:
            a = x.replace(",", ".")
            return float(a)

        print("\033[31mERRO, preço inválido tente novamente\033[m")
    
