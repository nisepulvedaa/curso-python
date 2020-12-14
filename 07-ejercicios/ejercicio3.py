
"""
ejercicio 3 escribir un programa que muestre los cuadrados
(numero multiplicado por si mismo) de los 60 primeros numeros naturales.
resolverlo con for y con while
"""

contador = int(0)

print("=============Bucle While")

while contador < 60:
#  print("{}".format(contador))
    contador += 1
    print("el cuadrado de {} es {} ".format(contador, (contador*contador)))

print("==============Bucle For")
for indice in range(1,61):
     print("el cuadrado de {} es {} ".format(indice,(indice*indice)))