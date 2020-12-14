"""

Ejercico 8 

¿Cuanto es el x % de z numero ?
20 de 150

"""

numero1 = int(input("Ingrese el porcentaje que desea calcular: "))
numero2 = int(input("Ingrese el numero que sea sacar el porcentaje: "))

if numero1 > 100:
    print("Su porcentaje no puede mayor a  100")
else:
    porcentaje = int((numero1*100)/numero2)
    print("El {} % de {} es: {} ".format(numero1, numero2, porcentaje))    