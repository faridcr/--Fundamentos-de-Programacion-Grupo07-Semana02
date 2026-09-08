# Escribe una función calcular_promedio(notas) que reciba una lista de notas y retorne el promedio, la nota
# mínima y la nota máxima. Además crea una función mostrar_resultado(nombre, notas) sin retorno que muestre
# un reporte formateado.



def calcular_promedio(notas):
    lista_notas=[]
    for i in range(notas):
        while True:
            nota=int(input("ingrese su nota :"))
            if 0<= nota <= 20:
                lista_notas.append(nota)
                break
            else:
             print("ingrese una nota valida entre 0 y 20 ")
            
           
    promedio=sum(lista_notas)/len(lista_notas)
    nota_minima=min(lista_notas)
    nota_maxima=max(lista_notas)
    return promedio, nota_minima, nota_maxima


def mostrar_resultado(nombre, promedio, nota_minima, nota_maxima):
    print("el promedio de las notas de", nombre, "es :", promedio)
    print("la nota mas alta de", nombre, "es :", nota_maxima)
    print("la nota mas baja de", nombre, "es :", nota_minima)

notas=int(input("ingrese la canatidad de notas a evaluar : "))
promedio, nota_minima, nota_maxima = calcular_promedio(notas)

nombre=str(input("Ingrese el nombre del estudiante :"))
mostrar_resultado(nombre,promedio,nota_minima,nota_maxima)


