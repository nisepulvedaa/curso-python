"""
Modulos: son funcionaldiaes ya hechas para reutilizar.
en python hay muchos modulos, que los puedes consultar aqui 
https://docs.python.org/3/tutorial/modules.html

podemos conseguir modulos que ya vienen en el lenguaje
modlos en internet y tambien podemos crear nuestro modulos


"""
##Importar modulo propio
import mimodulo
#from mimodulo import holaMundo
mimodulo.holaMundo("Nicolas Sepulveda")
print(mimodulo.calculadora(3,5,True))

#import fechas

import datetime

fecha_completa =  datetime.datetime.now()

print(datetime.date.today())
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%y, %H:%M:%S")
print(fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())


#modulo matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi", float(math.pi))

print("Redondear: ",math.ceil(6.56798))

print("Redondear: ",math.floor(6.56798))

#modulo ramdom
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))