# Función con retorno: devuelve True si el número es par, False si es impar
def es_par(numero):
    return numero % 2 == 0

# Función sin retorno (void): imprime un mensaje indicando si el número es par o impar
def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es PAR")
    else:
        print(f"El número {numero} es IMPAR")

# Prueba con lista
numeros = [4, 7, 0, -3, 10, 15]
for n in numeros:
    mostrar_paridad(n)
