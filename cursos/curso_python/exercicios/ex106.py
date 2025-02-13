while True:
    var = str(input("\033[36mDigite a função: "))
    if var == "fim" or var == "Fim":
        break
    print("\033[33m~~" * 60)
    print("\033[35m")
    print(help(var))
    print("\033[31m~~" * 60)
    print("\033[34m~~" * 60)

    

