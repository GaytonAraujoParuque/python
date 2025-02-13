from time import *

lista_toda = []
temporal = []
jogador = {}

def printar():
    print("--" * 40)

printar()
cod = 0
while True:
    jogador["cod"] = cod
    jogador["nome"] = str(input("Qual é o nome do jogador? "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    temporal.clear()
    for c  in range(0, partidas):
        temporal.append(int(input(f"Quantos gols na partida {c+1}? ")))
    jogador["gols"] = temporal[:]
    jogador["total"] = sum(jogador["gols"])
    lista_toda.append(jogador.copy())
    cod += 1
    resp = str(input("Quer continuar [S/N]? "))
    printar()
    if resp in "Nn":
        break

printar()

cont=0
for c in lista_toda[0].keys():
    print(f"{c:>15}", end="")
    cont+=15
print()
conta = 0
for k in lista_toda:
    for v in k.values():
        print(f"{str(v):>15}", end="")
        conta += 1
    print()
printar()

while True:
    dados = int(input("Mostrar dados de qual jogador [999 para terminar]? "))
    ler2= len(lista_toda)
    if dados > ler2 or dados <= -1:
        print(f"ERRO! Não existe jogador com cod {dados}")
        dados = int(input("Mostrar dados de qual jogador [999 para terminar]? "))
        
        printar()
    if dados == 999:
        break

    print(f"-- LEVANTAMENTO DO  JOGADOR {lista_toda[dados]["nome"]} --")
    ler = len(lista_toda[dados]["gols"])
    for c  in range(0, ler):
        sleep(1)
        print(f"    No jogo {c} fez {lista_toda[dados]["gols"][c]}")

    printar()
