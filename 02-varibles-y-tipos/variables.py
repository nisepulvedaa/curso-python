"""
una variable es un contenedor de informacion que dentro guardara un dato, se pueden crear
muchas variables y que cdaa una tenga un dato distinto.

"""

#Crear variables y asignarles un valor
texto = "Máster en Python"
texto2 = "Con Nicolas Sepulveda"
numero = 2020
decimal = 6.7

#Mostrar valor de las varibales
print(texto)
print(texto2)
print(numero)
print(decimal)

print("============================================")

#sustituir valores de variables
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("============================================")


#Concatenación

nombre = "Nicolas"
apellidos = "Sepulveda Alvear"
web = "deinsoluciones.cl"

print(nombre + " " + apellidos + " "+ web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos,web))
print(nombre, apellidos,web)