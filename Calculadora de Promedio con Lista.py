#Calculadora de Promedio con "Lista" de Farid

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    minima = min(notas)
    maxima = max(notas)
    return promedio, minima, maxima

def mostrar_resultado(nombre, notas):
    prom, mn, mx = calcular_promedio(notas)
    print("=" * 40)
    print("     CALCULADORA DE PROMEDIO")
    print("=" * 40)
    print(f"  Alumno       : {nombre}")
    print(f"  Notas        : {notas}")
    print("-" * 40)
    print(f"  Promedio     : {prom:.2f}")
    print(f"  Nota mínima  : {mn}")
    print(f"  Nota máxima  : {mx}")
    print("=" * 40)

# Programa principal
notas_alumno = [15, 18, 12, 20, 16]
mostrar_resultado("Farid", notas_alumno)