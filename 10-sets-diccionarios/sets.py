"""
SET es un tipo de dato, para tener una coleccion de valores, 
pero no tiene ni indice ni orden

"""

personas = {
    "Victor",
    "Nicolas",
    "Juan"
}
personas.add("Gustavo")
print(type(personas))
print(personas)
personas.remove("Gustavo")
print(personas)