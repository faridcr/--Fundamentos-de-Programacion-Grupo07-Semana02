
def calculadora_descuento(precio,porcentaje):
    descuento=precio*porcentaje/100
    precio_final=precio-descuento
    return precio_final

precio=float(input("ingrese el precio del producto:"))
porcentaje=float(input("ingrese el porcentaje de descuento :"))

print("El descuento es :", precio*porcentaje/100, "soles")
print("El precio final del producto es : ", calculadora_descuento(precio,porcentaje),"soles")
