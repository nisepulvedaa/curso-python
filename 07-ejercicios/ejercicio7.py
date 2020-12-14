"""
Ejercico 7

hacer un programa que muestre todos los numeros impares entre dos numeros que eleja el usuario 
"""

numero1 = int(input("Ingrese su primer numero: "))
numero2 = int(input("Ingrese su Segundo numero: "))

if numero2 < numero1 :
    print("el primer numero no puede ser mayor que el segundo")
else:
    print("Los numeros impares entre {} {} son: ".format(numero1, numero2))
    for indice in range(numero1, numero2+1):
        if indice % 2 != 0:
            print(indice)
