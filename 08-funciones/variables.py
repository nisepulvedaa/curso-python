"""
Variables locales: se definen dentro de la función y no se pede usar fuera de ella, solo están
disponibles dentro. A no se que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion y estan disponible dentro y fuera de ellas

"""

#Variable Global

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la funcion: ")
    print(frase)

    year = 2021
    print(year)

    global website 
    website = "deinsoluciones.cl"
    print(website)

holaMundo()
print("Fuera de la funcion" + website)

