"""
Ejercico 1.

hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente
-recorrer la lista y mostrarla
-hacer funcion que recorra lista de nuemeros y devuelva un string
-ordenarla y mostrarla
-mostrar su longitud
-buscar un elemento que el usuario pida por teclado


"""

numeros = [1,4,2,3,7,6,5,8]

#print(numeros)

def monstrarLista(lista):
    resultado = ""
    print("************Recorrer y mostrar*************")   
    for elemento in lista:
        resultado += "Elemento : {} ".format(str(elemento))
        resultado += "\n"
    return resultado   
        
print(monstrarLista(numeros))
#print(numeros)
print("***********Lista Ordenada**************")    
numeros.sort()
print(monstrarLista(numeros))
#print("La longitud de la lista es {} ".format(count(numeros))

print("************Mostar longitud***********+")
print(len(numeros))
try:
    print("************Buscar Elemento***********+")

    busqueda = int(input("Introdusca el numero que desea Buscar "))

    comprobar = isinstance(busqueda , int)

    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introdusca el numero que desea Buscar "))
    else:
        print("Has introducido el: {} ".format(busqueda))   
    print("Buscar en la lista el numero: {} ".format(busqueda))
    search = numeros.index(busqueda)
    print("El numero buscado existe en la lista, es el indice: {} ".format(search))
except:
    print("El número no está en la lista o no tiene el formato correcto vuelva a intertarlo con otro")
