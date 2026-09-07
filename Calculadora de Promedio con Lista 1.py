# Funcion que recibe una lista de notas
def calcular_promedio(notas):

    # Sumamos todas las notas y las dividimos entre
    # la cantidad de notas que tiene la lista
    promedio = sum(notas) / len(notas)

    # Buscamos la nota mas baja de la lista
    minima = min(notas)

    # Buscamos la nota mas alta de la lista
    maxima = max(notas)

    # Retornamos los tres resultados
    return promedio, minima, maxima


# Funcion encargada de mostrar los resultados
def mostrar_resultado(promedio, minima, maxima):

    # Mostramos un titulo para el reporte
    print("\n--- REPORTE DE NOTAS ---")

    # Mostramos el promedio obtenido
    print("Promedio:", promedio)

    # Mostramos la nota minima
    print("Nota minima:", minima)

    # Mostramos la nota maxima
    print("Nota maxima:", maxima)


# Creamos una lista con las notas del estudiante
notas = [15, 18, 12, 17, 14]

# Llamamos a la funcion para calcular los resultados.
# La funcion devuelve promedio, minima y maxima.
promedio, minima, maxima = calcular_promedio(notas)

# Enviamos los resultados a la funcion que los muestra
mostrar_resultado(promedio, minima, maxima)