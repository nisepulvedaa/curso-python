"""
ejecicio 3 programa que comprube si una variable esta vacia
y si esta vacia, rellenarla con texto en minusculas y mostrarlo
en mayuscula
"""

palabra = ""

if len(palabra) == 0:
    palabra = "hola soy un texto"
    palabra = palabra.upper()
    print(palabra)
else:
    print("La variable tiene contenido {} ".format(palabra))    