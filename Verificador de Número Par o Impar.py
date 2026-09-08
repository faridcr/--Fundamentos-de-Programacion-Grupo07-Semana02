# Verificador de Número Par o Impar de Farid

def es_par(numero):
    return numero % 2 == 0

def mostrar_paridad(numero):
    print("=" * 40)
    print("   VERIFICADOR DE PARIDAD")
    print("=" * 40)
    print(f"  Número ingresado : {numero}")
    print("-" * 40)
    if es_par(numero):
        print(f"  Resultado        : {numero} es PAR")
    else:
        print(f"  Resultado        : {numero} es IMPAR")
    print("=" * 40)

# Programa principal
num = int(input("Ingresa un número: "))
mostrar_paridad(num)