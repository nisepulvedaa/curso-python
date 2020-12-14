"""
ejercicio 9 . hacer un programa que pida numeros al usuario
indefinidamente hasta meter el numero 111

"""

numero = int(input("Ingrese un numero: "))
print("Has introducido el: {} ".format(numero))

while numero != 111:
    numero = int(input("Ingrese un numero: "))
    if numero == 111:
        print("Ha ingresado la key para detener el ciclo que era: {}".format(numero))
    else:
         print("Has introducido el: {} ".format(numero))      

