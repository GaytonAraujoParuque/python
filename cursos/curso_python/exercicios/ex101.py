def voto(nasc):
    idade = 2024 - nasc
    if idade < 18:
        return f"Com {idade} anos: NÂO VOTA"
    
    elif idade >= 18 and idade < 65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    
    else:
        return f"Com {idade} anos: VOTO OPCIONAL"


nasc = int(input("Qual é o seu ano de nascimento?"))
while True:
    print(voto(nasc))
    resp = str(input("Quer continuar?"))
   
    if resp in "Nn":
        break
