lista = []
dic = {}
mulheres = []
idade_acima = []

def  printar():
    print("-=" * 20)

média = 0
quantas = 0
while True:
    dic["nome"] = str(input("Nome:"))
    dic["sexo"] = str(input("Sexo [M/F]:"))
    dic["idade"] = int(input("Idade:"))
    if dic["sexo"] in "Ff":
        mulheres.append(dic["nome"])
    média += dic["idade"]
    quantas += 1
    lista.append(dic.copy())
    resp = str(input("Quer continuar? [S/N]:"))
    if resp in "Nn":
        break

média = média /  quantas

for c in range(0,quantas):
    if lista[c]["idade"] > média:
        idade_acima.append(lista[c])

printar()
print(lista)
printar()
print(f"=> O grupo tem {quantas} pessoas.")
print(f"=> A média de idade é de {média} anos")
print(f"=> AS mulheres cadastradas foram: {mulheres}")
print("=> Lista das pessoas que estão acima da média:")
for c in idade_acima:
    print(f"nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};")

printar()

