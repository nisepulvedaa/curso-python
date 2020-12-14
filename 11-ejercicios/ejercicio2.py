"""
Ejercicio 2

Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista

pluss usar while y for

"""

coleccion = []

for contador in range(0,120):
    coleccion.append(("elemento-{}".format(contador)))
    print("Mostrando el elemento : {} ".format(contador))

print(coleccion)


coleccion2 = []
indice = 0;
while indice <= 120:
    coleccion2.append(("elemento-{}".format(indice)))
    print("Mostrando el elemento : {} ".format(indice))
    indice += 1

print(coleccion2)     

