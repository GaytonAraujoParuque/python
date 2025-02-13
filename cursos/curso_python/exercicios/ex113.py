def LeiaInt():
    
    while True:
                
        try:
            a = int(input(f"Digite um número inteiro: "))
            
        except Exception as erro:
            print(f"\033[31mERRO: digite um número inteiro válido\033[m {erro.__class__}")

        else:
            print("--" * 40)
            return a
        
def LeiaFloat():

    while True:
        try:
            x = float(input("Digite um número real: "))

        except Exception as erro:
            print(f"\033[31mERRO: digite um número real válido\033[m {erro.__class__}")

        else:
            print("--" * 40)
            
            return x
            
print(f"O número inteiro digitado foi {LeiaInt()} e o número real digitado foi {LeiaFloat()}.")