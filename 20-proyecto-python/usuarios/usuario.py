
import datetime
import hashlib
import usuarios.conexiones as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self,nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()

        #Cifrar Contraseña

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0,self]    
        
        return result

    def identificar(self):  
        #consulta para comprobar si existe  
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s "

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql,usuario)
        result = cursor.fetchone()

        return result