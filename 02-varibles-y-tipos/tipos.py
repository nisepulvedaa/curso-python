nada = None
cadena = "Hola soy Nicolas Sepulveda"
entero = 99
flotante = 4.2
booleano = True
lista = [10,20,30,40,50,60,70,80,90,100]
listaString = [40,"treinta",30]
tuplaNoCambia = ("master","en","python")
diccionario = {
    "nombre": "Nicolas",
    "apellido": "Robles",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"
#cadena = "Desarrollador Web"
#imprimir variable
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)
#mostrar tipo de datos

print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

#convetir a tipo de dato

texto = "Hola soy un texto"
numerito = str(776)
print(texto + " " + numerito)

print(type(numerito))
numerito = int(776)
print(type(numerito))
numerito = float(776)
print(type(numerito))