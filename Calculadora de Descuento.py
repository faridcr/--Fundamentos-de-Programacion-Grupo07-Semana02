def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

print("=" * 40)
print("   CALCULADORA DE DESCUENTO")
print("=" * 40)

# Validar precio original
while True:
    precio_original = float(input("Ingresa el precio original (S/): "))
    if precio_original < 0:
        print("Error: el precio no puede ser negativo. Intenta de nuevo.")
    else:
        break

# Validar porcentaje de descuento
while True:
    porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (%): "))
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        print("Error: el porcentaje debe estar entre 0% y 100%. Intenta de nuevo.")
    else:
        break

precio_final = calcular_descuento(precio_original, porcentaje_descuento)
ahorro = precio_original - precio_final

print("-" * 40)
print("           RESUMEN DE COMPRA")
print("-" * 40)
print(f"  Precio original   : S/ {precio_original:.2f}")
print(f"  Descuento aplicado: {porcentaje_descuento:.0f}%")
print(f"  Ahorro obtenido    : S/ {ahorro:.2f}")
print(f"  Precio final       : S/ {precio_final:.2f}")
print("=" * 40)
print("     ¡Gracias por tu compra!")
print("=" * 40)