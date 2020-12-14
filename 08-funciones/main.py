"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesario

def nombreDeMiFuncion(parametros):
    # BLOQUE /CONJUNTO DE INSTRUCCIONES
 nombreDeMiFuncion(mi_parametro)   
"""
"""
#Ejemplo 1

print("#######EJEMPLO 1 #######")

#Definir funcion
def muestraNombre():
   print("Nicolas")
   print("Arnell")
   print("Gustavo")
   print("Juan")
   print("Mauricio")
   print("Andres")
   print("\n")

#Invocar Función
muestraNombre()
#muestraNombre()
#muestraNombre()

# Ejemplo 2
#nombre = "Nicolas Sepulveda"
print("#######EJEMPLO 2 #######")

def mostrarTuNombre(nombre, edad):
    print("Tu nombre es: {} ".format(nombre))
    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Y eres menor de edad")   

#mostrarTuNombre("Nicolas Sepulveda")
#mostrarTuNombre("Juan Baez")
#mostrarTuNombre("Arnell Vazquez")
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)


#Ejemplo 3

print("####Ejemplo 3 #######")

def tabla(numero):
    print("Tabla de multiplicar del número {} ".format(numero))

    for contador in range(1,11):
        operacion = numero * contador
        print("{} x {} = {} ".format(numero,contador,operacion))

tabla(3)        
tabla(7)        
tabla(12)  
print("---------------------------------")


##ejemplo 3.1

for numero_tabla in range(1,11):
    tabla(numero_tabla)



##Ejemplo 4

print("####Ejemplo 4 #######")

# Parametros opcionales

def getEmpleado(nombre, dni = ""):
    print("Empleado")
    print("Nombre {} ".format(nombre))
    if dni != "":
        print("DNI {} ".format(dni))



getEmpleado("Nicolas Sepulveda","18566809-6")    

getEmpleado("Nicolas Sepulveda")    




##Ejemplo 5

print("####Ejemplo 5 #######")

#Ejemplo 5: parametros opcionales y return

def saludame(nombre):
    saludo = "Hola saludos {}".format(nombre)
    return saludo


print(saludame("Nicolas Sepulveda"))

##Ejemplo 6

print("####Ejemplo 6 #######")


def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    cadena = ""

    if basicas != False:

        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
            cadena += "Suma: " + str(suma)
            cadena += "\n"
            cadena += "Resta: " + str(resta)
            cadena += "\n"
            cadena += "Multiplicacion: " + str(multi)
            cadena += "\n"
            cadena += "Division: " + str(division)
            cadena += "\n"
    return cadena

print(calculadora(6,2))
print(calculadora(6,2, True))

##Ejemplo 7

print("####Ejemplo 7 #######")

def getNombre(nombre):
    texto = "El nombre es: {}".format(nombre)
    return texto 

def getApellidos(apellidos):
    texto = "los apellidos son: {}".format(apellidos)
    return texto 

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n"+ getApellidos(apellidos)
    return texto

print(devuelveTodo("Nicolas", "Sepulveda"))

"""

##Ejemplo 8

print("####Ejemplo 8 #######")

dime_el_year = lambda year : "El año es {} ".format(year * 50)

print(dime_el_year(2034))

