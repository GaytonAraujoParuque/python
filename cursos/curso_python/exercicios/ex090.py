dicionário = dict()

dicionário["nome"] = str(input("Nome:"))
dicionário["média"] = float(input(f"Média de {dicionário['nome']}:"))

if dicionário["média"] >= 10:
    dicionário["situação"] = "Aprovado"

else:
    dicionário["situação"] = "Reprovado"

print(f"O nome é {dicionário['nome']}")
print(f"A média é {dicionário['média']}")
print(f"A stuação é {dicionário['situação']}")
