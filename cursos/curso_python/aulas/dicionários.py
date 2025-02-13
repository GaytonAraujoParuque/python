'''
dados = dict()
dados = {"nome":"gayton"}

dados["idade"] = 16

del dados["idade"]
print(dados)
'''
'''
filmes =  {
"Título":"Star Wars",
"Ano":"1977",
"Diretor":"George Lucas"
}

lista = []
lista.append(filmes)
print(lista[0]["Ano"])
'''

'''
for k, v in filmes.items():
    print(f"{k} é {v}")
'''

'''
print(filmes.items())
print(filmes.values())
print(filmes.keys())
'''


país = dict()
lista = list()

for c in range(0,2):
    país["província"] = str(input("Qual é o nome da província?"))
    país["Sigla"] = str(input("Qual é a sigla?"))
    lista.append(país.copy())

for p in lista:
    for k, v in p.items():
        print(f"{k} = {v}")