"""
Ejercicio 5. hacer un programa que muestre todos los numeros entre dos numeros que diga el
usuario

"""

numero1 = int(input("ingrese su primer numero: "))
numero2 = int(input("ingrese su segundo numero: "))

if numero1 < numero2:

    print("El rango de numeros entre {} y {} es: ".format(numero1,numero2))
    for indice in range(numero1,numero2+1):
        print(indice)
    
else:
 print("el numero 1 debe ser mayor al numero 2")
