def holaMundo(nombre):
    print("Hola bienvenido {} ".format(nombre))



def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    cadena = ""

    if basicas != False:

        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
            cadena += "Suma: " + str(suma)
            cadena += "\n"
            cadena += "Resta: " + str(resta)
            cadena += "\n"
            cadena += "Multiplicacion: " + str(multi)
            cadena += "\n"
            cadena += "Division: " + str(division)
            cadena += "\n"
    return cadena
