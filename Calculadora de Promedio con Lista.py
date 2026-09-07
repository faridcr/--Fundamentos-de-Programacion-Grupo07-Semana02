def calcular_promedio(n1, n2, n3, n4, n5):
    promedio = (n1 + n2 + n3 + n4 + n5) / 5
    minima = min(n1, n2, n3, n4, n5)
    maxima = max(n1, n2, n3, n4, n5)
    return promedio, minima, maxima

def mostrar_resultado(nombre, n1, n2, n3, n4, n5):
    prom, mn, mx = calcular_promedio(n1, n2, n3, n4, n5)
    print("=" * 40)
    print("     CALCULADORA DE PROMEDIO")
    print("=" * 40)
    print(f"  Alumno       : {nombre}")
    print(f"  Notas        : {n1}, {n2}, {n3}, {n4}, {n5}")
    print("-" * 40)
    print(f"  Promedio     : {prom:.2f}")
    print(f"  Nota mínima  : {mn}")
    print(f"  Nota máxima  : {mx}")
    print("=" * 40)

# Programa principal
nombre_alumno = "Farid"
nota1 = 15
nota2 = 18
nota3 = 12
nota4 = 20
nota5 = 16

mostrar_resultado(nombre_alumno, nota1, nota2, nota3, nota4, nota5)