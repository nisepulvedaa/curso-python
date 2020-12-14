from io import open
import pathlib
import shutil
"""
#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
#print(ruta)
archivo = open(ruta,"a+")

#Escribir 

archivo.write("****Soy un texto metido desde python****\n")


#cerrar archivo

archivo.close()

"""
#Abrir archivo
"""
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
archivo_lectura = open(ruta,"r")
#Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#leer contenido y guardar en lista

lista = archivo_lectura.readlines()
archivo_lectura.close()



for elemento in lista:
    print("" + elemento.upper())

"""
#copiar

"""
ruta_original = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/ficheros_copiado.txt"
ruta_alternativa = "../07-ejercicios/fichero_copiado77.txt"
shutil.copyfile(ruta_original, ruta_alternativa)
  """ 

# Mover
"""
ruta_original = str(pathlib.Path().absolute()) + "/ficheros_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/ficheros_copiado_NUEVO.txt"
shutil.move(ruta_original, ruta_nueva)

"""

import os
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/ficheros_copiado_NUEVO.txt"
os.remove(ruta_nueva)

"""
# comprobar si existe

import os.path

#print(os.path.abspath("./"))

ruta = os.path.abspath("./")+"/ficheros_texto.txt"
print(ruta)
if os.path.isfile(ruta):
    print("El archivo existe")
else:
    print("El archivo no existe")    