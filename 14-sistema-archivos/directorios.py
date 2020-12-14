import os
import shutil
#crear carpeta

if not  os.path.isdir("./mi_carpeta"):
    print("carpeta creada")   
    os.mkdir("./mi_carpeta")
else:
    print("ya existe el directorio")    

 #eliminar
    
#os.rmdir("./mi_carpeta")


#Copiar
"""
ruta_original =  "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"
shutil.copytree(ruta_original, ruta_nueva)
"""

##os.rmdir("./mi_carpeta_COPIADA")

print("Contenido de mi carpeta: ")
contenido = os.listdir("./")
#print(contenido)
for fichero in contenido:
    print("Fichero: {} ".format(fichero))