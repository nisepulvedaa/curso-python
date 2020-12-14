"""
Ejercicio 4.

Crear un script que tenga 4 variables , una lista, un string y un entero y un booleno
y que imprima un mensaje segun el tipo de dato de cada variables 

"""

mi_lista = ["Hola mundo", 77]
titulo = "mastar en python"
numero = 100 
verdadero = True


def traducirTipo(tipo):
    result = ""
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "String"
    elif tipo == int:
        result = "Int"
    elif tipo == bool:
        result = "Boolean"    
    else:
        result = None  
    return result                  

def verficarTipoDeDato(variable, tipo):
    test = isinstance(variable,tipo)
    result = ""
    if test:
        result += "Este dato es del tipo: {} ".format(traducirTipo(tipo))
    else:
        result = "El tipo de dato no es Correcto"
    return result

print(verficarTipoDeDato(mi_lista,list))        
print(verficarTipoDeDato(titulo,str))      
print(verficarTipoDeDato(numero,int))      
print(verficarTipoDeDato(verdadero,bool))      