#Import modulo

import sqlite3

#Conexion

conexion = sqlite3.connect('pruebas.db')


#Crear cursor
cursor = conexion.cursor()

#Crear tabla
"""
#Forma 1
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id integer primary key autoincrement, "+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")
"""

#forma2
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
id integer primary key autoincrement, 
titulo varchar(255), 
descripcion text, 
precio int(255)
);
""")

#guardar cambios

conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer Producto', 'Descripcióm de mi producto', 550 ) ")
conexion.commit()
"""

#Borrar registros
cursor.execute("DELETE from productos")
conexion.commit()
#Insertar muchos registros de golpe

productos = [
    ("Ordenador Portatil", "Buen Pc", 700),
    ("Telefono Movil", "Buen Telefono", 140),
    ("Placa Base", "Buena Placa", 80), 
    ("Tablet 15", "Buena Tablet", 300),

]

cursor.executemany("INSERT INTO productos VALUES (NULL, ?, ? ,?)",productos)
conexion.commit()

#Actualizar datos

cursor.execute("UPDATE productos set precio=678 WHERE precio = 80 ")
conexion.commit()

#Listar datos

cursor.execute("SELECT * FROM productos WHERE precio >= 300 ;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: "+ str(producto[0]))
    print("Titulo: " + producto[1])
    print("Descripción: " + producto[2])
    print("Precio: " + str(producto[3]))
    print("********************************")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

#cerrar conexion

conexion.close()

