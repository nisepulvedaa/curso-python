"""
ejercicio 4

pedir dos numeros al usuarios y hacer todas las operaciones basica de una calculadora
y mostrarla por mandatalla


"""

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

print("{} + {} es igual a {} ".format(numero1, numero2, (numero1+numero2)))
print("{} - {} es igual a {} ".format(numero1, numero2, (numero1-numero2)))
print("{} * {} es igual a {} ".format(numero1, numero2, (numero1*numero2)))
print("{} / {} es igual a {} ".format(numero1, numero2, (numero1/numero2)))