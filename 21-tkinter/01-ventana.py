#Tkinter 
#Modulo para crear interface graficas de usuarios 

from tkinter import * 
import os.path
#Crear la ventana raiz 
ventana = Tk()

class Programa:

    def __init__(self):
        self.tittle = "Master en Python"
        self.icono = "./imagenes/favicon.ico"
        self.icono_alt =  "./21-tkinter/imagenes/favicon.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        

        #titlo de la ventana

        ventana.title(self.tittle)

        #comprobar si exite un archivo

        ruta_icono = os.path.abspath(self.icono)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icono_alt)

        #Mostar texto en el programa

        texto = Label(ventana,text=ruta_icono)
        texto.pack()

        texto = Label(ventana,text="Bienvenido al Master en Python")
        texto.pack()


        #icono de la ventana

        ventana.iconbitmap(ruta_icono)

        #Cambio en el tamañp de la ventana
        ventana.geometry(self.size)


        #Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0) 


        #Arrancar y mostrar la venta hazta que se cierrre 
            ventana.mainloop()
    """
    def addTexto(self,texto):
        texto_2 = Label(ventana,text=texto).pack()
      

    def mostrar(self):
        #Arranca y mostrar la ventana hasta que se cierretk pytho
        ventana.mainloop()      
    """

#instanciaar programa
# 
programa = Programa()
programa.cargar()
#programa.addTexto("Nicolas")
#programa.mostrar()
