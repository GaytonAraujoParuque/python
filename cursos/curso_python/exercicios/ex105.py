'''
def notas():
    a = int(input("Quantas notas quer digitar?"))
    notas = []
    for c in range(0, a):
        notas.append(float(input(f"Digite a {c + 1} nota:")))
    quantidade = len(notas)
    maior = max(notas)
    menor = min(notas)
    média = 0
    for c in notas:
        média += notas[0]
    média /= len(notas)

    if média < 10:
        situação = "Má"
    elif média >= 10 and média < 15:
        situação = "Razoável"
    else:
        situação = "Muito boa"

    return f"Quantidade de notas digitadas = {quantidade}\nMaior nota = {maior}\nMenor nota = {menor}\nMédia = {média}\nSituação = {situação}"

print(notas())
'''

notas = []
def notasf():
    
    """
    A função recebe vários valores por meio de inputs e todos valores são colocados dentro de um dicionário
    -> Recebe a quanridade de notas
        -> Recebe as notas
    -> Ele adiciona a maior nota
    -> Adiciona a menor nota
    -> Calcula e adiciona a média
    -> Ele pergunta se quer ou não adicionar a situação segundo a média pode ser boa ou má, se a resposta for sim ele adiciona
    -> E no fim ele retorna o dicionário
    """

    dicionário = {}
    dicionário["quantidade"] = int(input("Quantas notas pretende inserir "))

    for c in range(0, dicionário["quantidade"]):
        notas.append(int(input(f"Digite a nota [{c+1}] ")))

    maior = max(notas)
    menor = min(notas)
    dicionário["maior"] = maior
    dicionário["menor"] = menor

    média = 0
    for k, v in enumerate(notas):
        média += int(v)

    média /= len(notas)
    dicionário["média"] = média

    ver = str(input("Pretende ver a situação da turma [S/N]? "))
    if ver in "Ss":
        if dicionário["média"] >= 10:
            dicionário["situação"] = "BOA"
        else:
            dicionário["situação"] = "MÁ"

    return dicionário
    
print(notasf())
help(notasf)