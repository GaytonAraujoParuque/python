def ficha(nome, gols):
    if nome == "":
        nome = "<desconhecido>"
    if gols == "":
        gols = 0
    return f"O jogador {nome} marcou {gols} gols no campionato"


nome = str(input("Nome do jogador:"))
gols = input("Número de gols:")
print(ficha(nome, gols))
