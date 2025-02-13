def fatorial(a, b):
    c = 1
    while a > 0:
        if b == True:
            print(a, end="")
        c *= a
        a -= 1
        if b == True:
            if a > 0:
                print(f"x", end="")
            else:
                print("=", end="")
    print(c)

fatorial(6, True)