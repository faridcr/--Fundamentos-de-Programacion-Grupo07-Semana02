def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    nota_min = min(notas)
    nota_max = max(notas)
    return promedio, nota_min, nota_max


def mostrar_resultado(nombre, notas):
    prom, mn, mx = calcular_promedio(notas)
    print("Reporte de:", nombre)
    print("Notas:", notas)
    print("Promedio:", prom)
    print("Nota mínima:", mn)
    print("Nota máxima:", mx)


# Probamos la función
notas_alumno = [15, 20, 20, 10, 16]
mostrar_resultado("Kevin", notas_alumno)