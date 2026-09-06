
def es_par(numero):
    if numero%2==0:
        return True

    else:
        return False
    
def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es PAR")
    else:
        print(f"El número {numero} es IMPAR")
 
 


while True:       
    numero=int(input("Ingrese un número:"))
    
    mostrar_paridad(numero) 
    
    break


       
   

    
