import notas.nota as modelo_notas

class Acciones:

    def crear(self,usuario):
       print("\nOk {} !!! Vamos a crera una nueva nota.... ".format(usuario[1]))

       titulo = input("Introduce el titulo de tu nota: ")
       descripcion = input("Introduce el Contenido de tu nota: ")

       nota = modelo_notas.Nota(usuario[0], titulo, descripcion)
       guardar = nota.guardar()

       if guardar[0] >= 1:
           print("\nPerfecto has guardado la nota: {} ".format(nota.titulo))
       else:
           print("\nNo se ha guardado la nota, lo siento {} ".format(nota.titulo))    

    def mostrar(self, usuario):
        ("\nVale {}!! Aquí tienes tus notas:  ".format(usuario[1]))    

        nota = modelo_notas.Nota(usuario[0],"","")
        notas = nota.listar()

        #print(notas)
        for nota in notas:
            print("\n*************************************")
            print("Titulo: {} ".format(nota[2]))
            print("Contenido: {} ".format(nota[3]))
            print("*************************************")

    def borrar(self, usuario):
        print("Ok {} !!! Vamos a borrar notas ".format(usuario[1]))

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota  = modelo_notas.Nota(usuario[0],titulo,"")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print("Hemos borrado la nota: {} ".format(nota.titulo))
        else:
            print("No se ha borrado la nota, verifique los datos ingresados")    
        

