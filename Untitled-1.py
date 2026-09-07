# Ejercicio 2: Verificar si un numero es par o impar

# Esta funcion recibe un numero y verifica si es par.
# Si el resto de dividir entre 2 es 0, devuelve True.
def es_par(numero):
    return numero % 2 == 0


# Esta funcion muestra en pantalla si el numero es par o impar.
# No utiliza return, solamente imprime un mensaje.
def mostrar_paridad(numero):
    
    # Llamamos a la funcion es_par() para comprobar el numero.
    if es_par(numero):
        print(f"El numero {numero} es PAR")
    else:
        print(f"El numero {numero} es IMPAR")


# Lista de numeros que vamos a verificar.
numeros = [10, 7, 4, 9, 12, 15]


# Recorremos cada numero de la lista.
# En cada vuelta llamamos a mostrar_paridad().
for numero in numeros:
    mostrar_paridad(numero)
