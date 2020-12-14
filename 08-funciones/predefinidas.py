nombre = "Nicolas Sepulveda"

#funciones generales
print(nombre)
print(type(nombre))

#detectar el tipado

comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("la variable no es un numero decimal")

 #Limpiar espacios  


frase = "  mi contenido   "
print(frase)
print(frase.strip())

#Eliminar variables

year = 2022
print(year)
del year

#comprobar variable vacia


texto = "  fff  "
if len(texto) <=0 :
    print("la variable esta vacia")
else:
    print("la variable tieen contenido: ", len(texto))    

#Encontrar caracteres    
frase = "la vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string

nueva_frase = frase.replace("vida", "moto");

print(nueva_frase)


#Mayusculas y minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())