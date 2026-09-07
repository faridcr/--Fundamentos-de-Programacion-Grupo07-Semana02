# Ejercicio 3: Calculadora de Promedio con Lista

def calcular_promedio(notas):
    # Retorna tupla (promedio, mínima, máxima)
    return sum(notas)/len(notas), min(notas), max(notas)

def mostrar_resultado(nombre, notas):
    # Función void: imprime reporte formateado
    prom, mn, mx = calcular_promedio(notas)   # desempaquetado
    print(f"=== Reporte de {nombre} ===")
    print(f"Notas: {notas}")
    print(f"Mínima: {mn}")
    print(f"Máxima: {mx}")
    print(f"Promedio: {prom:.2f}")

# Prueba de la función 
notas_Josue = [10, 16, 13, 19, 11]
mostrar_resultado("Josue", notas_Josue)