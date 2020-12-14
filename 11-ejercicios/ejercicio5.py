"""
Ejercicio 5

Crear una lista con el contenido de esta tabla 
MOSTRAR INFORMACION ORDENADA 
ACCION AVENTURA     DEPORTES
GTA      ASSASINS     FIFA
COD      CASH         PES
PUG      PRICE        MOTOGP

"""

tabla = [
    {
        'categoria': 'ACCION',
        'juegos': ["GTA","Call of Duty", "PUGB"]
    },
     {
        'categoria': 'AVENTURA',
        'juegos': ["Assasins","Crash", "Price"]
    },
     {
        'categoria': 'DEPORTES',
        'juegos': ["Fifa 21","Pes 21", "Moto Gp"]
    }

]

for categoria in tabla:
    print("--------------{}---------------".format(categoria['categoria']))
    for juego in categoria['juegos']:
       print("--------------{}---------------".format(categoria['juegos']))