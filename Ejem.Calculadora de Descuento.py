def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

# Pedimos los datos al usuario
precio_original = float(input("Ingrese el precio original: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# Llamamos a la función
precio_final = calcular_descuento(precio_original, porcentaje_descuento)

# Calculamos el ahorro
ahorro = precio_original - precio_final

# Mostramos resultados
print("Precio original:", precio_original)
print("Precio final:", precio_final)
print("Ahorro obtenido:", ahorro)