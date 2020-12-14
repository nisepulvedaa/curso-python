"""
LISTAS(arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
para acceder a esos valores podemos usar un indice númerico.

"""

pelicula = "Batman"

#Definir lista
peliculas = ["Batman","Spiderman","Superman"]
cantantes = list(('2pac','drake','Jennifer Lopez'))
years = list(range(2020,2051))
variada = ["Victor",30,4.4,True, "Texto"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)


#Indices
peliculas[2] = "Avengers"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])
print(peliculas[2:])

#añadir elementos a lista

cantantes.append("Kase 0")
cantantes.append("Natos y waor")

print(cantantes)

#Recorrer lista

print("****************Listado Peliculas********************")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)
print(nueva_pelicula)    

for pelicula in peliculas:
    print(" {}  {} ".format(peliculas.index(pelicula)+1,pelicula))
"""
 # Listas multidimensionales
print("\n**********Lista de contactos**********")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
     [
        'Luis',
        'luis@luis.com'
    ],
     [
        'Salvador',
        'salvador@salvador.com'
    ]

]

for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print("\n")    

#print(contactos[1][1])

