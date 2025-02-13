try:    
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    c = a / b
except  ZeroDivisionError:
    print("Não é possível dividir um número por zero")

except (ValueError, TypeError):
    print("Tivemos  problemas com os tipos de dados inseridos")

else:
    print(f"O resultado é {c}")

finally:
    print("Volte sempre")

