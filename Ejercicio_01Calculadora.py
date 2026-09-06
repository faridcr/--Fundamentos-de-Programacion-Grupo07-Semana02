def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    return precio - descuento

# Entrada de datos por teclado
precio_original = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))

# Llamada a la función
precio_final = calcular_descuento(precio_original, porcentaje_descuento)

# Cálculo y muestra de resultados
ahorro = precio_original - precio_final

print("\n--- RESUMEN DE COMPRA ---")
print(f"Descuento aplicado: {porcentaje_descuento}%")
print(f"Ahorro total: S/ {ahorro}")
print(f"Precio a pagar: S/ {precio_final}")