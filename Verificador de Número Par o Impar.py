def es_par(numero):
    return numero % 2 == 0

def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es PAR")
    else:
        print(f"El número {numero} es IMPAR")

# Programa principal
num = int(input("Ingresa un número: "))
mostrar_paridad(num)