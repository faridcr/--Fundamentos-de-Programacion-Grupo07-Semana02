def es_par(numero):
    return numero % 2 == 0
  

def mostrar_paridad(numero):
    if es_par(numero):
      print(numero, "es PAR")
    else:
        print(numero, "es IMPAR")


# Probamos con una lista de números
numeros = [4, 7, 10, 15, 22, 33]

for num in numeros:
    mostrar_paridad(num)