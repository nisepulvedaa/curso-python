import usuarios.usuario as modelo_usuario
import notas.acciones 

class Acciones:
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema....")
        nombre = input("¿Cual es tu Nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo_usuario.Usuario(nombre,apellidos, email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print("\nPerfecto {} ta has registrado con el email {} ".format(registro[1].nombre, registro[1].email))
        else:
            print("No te ha registrado correctamente!!!!!")

    def login(self):
        print("Vale!! Identificate en el sistema...")

        try:    
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            
            usuario = modelo_usuario.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print("\nBienvenido {} , ta has regitrado en el sistema el {} ".format(login[1],login[5]))
                self.proximasAcciones(login)
            else:
                print("Fallo en el login")
        except Exception as e:
            print(type(e)) 
            #(type(e).__name__)
            print("Login Incorrecto!!! Revisa Tus Credenciales")    

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            print("vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("vamos a mostrar")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a eliminar")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario) 
        elif accion == "salir":
            print("Ok {}, hasta pronto!!! ".format(usuario[1]))
            exit()            


             