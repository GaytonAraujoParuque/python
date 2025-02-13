from utilidadesCeV import moeda,dados

p = dados.leiaDinheiro("Qual é o preço? ")
a = int(input("Qual é a percentagem de aumento? "))
d = int(input("Qual é a percentagem de redução? "))

moeda.resumo(p, a, d)