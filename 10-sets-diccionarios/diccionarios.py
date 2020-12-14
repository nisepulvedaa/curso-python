"""
Diccionario:

Un tipo de datos que almacena un conjuto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.

"""

persona = {
    "nombre": "Nicolas",
    "apellidos": "Sepulveda",
    "web": "deinsoluciones.cl"
}

print(persona["web"])

#Lista con diccionarios

contactos = [
    {
        'nombre': 'Nicolas',
        'email': 'ni.sepulvedaa@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos)

print("\n Listado de contactos: ")
for contacto in contactos:
    print("Nombre del contacto: {} ".format(contacto['nombre']))
    print("Email del contacto: {} ".format(contacto['email']))
    print("----------------------------------------------")