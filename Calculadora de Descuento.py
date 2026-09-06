def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

# Programa principal
precio_original = float(input("Ingresa el precio original: "))
porcentaje_descuento = float(input("Ingresa el porcentaje de descuento: "))

precio_final = calcular_descuento(precio_original, porcentaje_descuento)
ahorro = precio_original - precio_final

print('========================')
print(f"Precio final: {precio_final}")
print(f"Ahorro obtenido: {ahorro}")