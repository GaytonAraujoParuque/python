def leiaInt(y):
    while True:
      x = input(y)
      tipo = x.isnumeric()
      if tipo == True:
         return x
         break
      print("\033[31mErro Digite Um Número Inteiro Por Favor!\033[m")

n =leiaInt("Digite um número: ")
print("-=" * 20)
print(f"Você digitou {n}")
print("-=" * 20)


   