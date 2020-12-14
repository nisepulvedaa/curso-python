"""

Ejercicio 6.mostrar todas las tablas de multiplicar del 1 al 10
mostratando le titulo de la tabla y luego las multiplicaciones del 1 al 10

"""


for indice in range(1,11):
  print("Tabla del {}".format(indice))
  for indice2 in range(1,11):
    print("{} x {} = {}".format(indice, indice2, (indice*indice2)))
    