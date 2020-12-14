import mysql.connector

#Conexión

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# la conexion ha sido correcta

##print(database)

cursor = database.cursor(buffered=True)

#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
"""
# crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
    
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'OPEL','Astra', 18500)")    

coches = [
    ('Seat','Ibiza',5000),
    ('Renault','Clio',15000),
    ('Citroen','Sazo',2000),
    ('Mercedes','Clase C',35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (NULL, %s,%s,%s)",coches)


cursor.execute("SELECT * FROM vehiculos where precio <= 5000 and marca = 'seat' ")
result = cursor.fetchall()

print("-----------TODOS MIS COCHES----------")
for coche in result:
    print(coche[1],coche[3])



cursor.execute("SELECT * FROM vehiculos ")
result2 = cursor.fetchone()

print("-----------TODOS MIS COCHES----------")

print(result2)


cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes' ")
database.commit()
print(cursor.rowcount,"borrados!!!")


#Actualizar

cursor.execute("UPDATE vehiculos SET modelo='León' where marca='Seat' ")
database.commit()
print(cursor.rowcount,"actualizados!!!")