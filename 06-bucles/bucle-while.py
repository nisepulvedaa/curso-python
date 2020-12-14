"""

#BUCLE WHILE

Estructura de control que itera o repite la ejecución de una 
serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condición

while condicion:
    bloque de instrucciones
    actualizacion de contador
"""
"""
contador = 1
while contador <= 100:
    print("Estoy en el Numero {} ".format(contador))
    contador += 1

print("======================")
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador = contador  + 1

print(muestrame)
"""

numero = int(input("Ingrese un numero para Multiplicar: "))
contador = int(1)

while contador <= 10:
    print("{} x {} = {}".format(numero, contador, (numero*contador)))    
    contador = contador + 1
else:
    print("Tabla Terminada.")