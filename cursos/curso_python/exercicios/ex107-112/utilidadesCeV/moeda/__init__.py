def aumentar(x, y):
    a = y / 100 * x
    b = a + x
    b = f"R${b:.2f}"
    return b


def diminuir(x, y):
    a = y / 100 * x
    b = x - a
    b = f"R${b:.2f}"
    return b


def dobro(x):
    b = x * 2
    b = f"R${b:.2f}"
    return b


def metade(x):
    b = x / 2
    b = f"R${b:.2f}"
    return b

def moeda(x):
    return f"{x:.2f}"

def resumo(preço, aumento, redução):
    print("-" * 25)
    print("     RESUMO DO VALOR")
    print("-" * 25)

    print(f"Preço analisado: {moeda(preço):>5}")
    print(f"Dobro do preço: {dobro(preço):>9}")
    print(f"Metade do preço: {metade(preço):>4}")
    print(f"{aumento}% de aumento: {aumentar(preço, aumento):>10}")
    print(f"{redução}% de redução: {diminuir(preço, redução):>10}")
    print("-" * 25)

