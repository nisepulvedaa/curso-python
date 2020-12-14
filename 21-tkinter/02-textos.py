from tkinter import *

ventana = Tk()
ventana.geometry("550x500")

texto = Label(ventana,text="Bienvenido a Mi Programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas",30)
)

texto.pack()

texto = Label(ventana,text="Hola, Soy Nicolas Sepulveda")
texto.config(
    height=3,
#    height=400,
    bg="orange",
    font=("Arial",18 ),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack( anchor=SE)

def pruebas(nombre,apellidos,pais):
    return "Hola {} {} veo que eres de {} ".format(nombre, apellidos, pais)


texto = Label(ventana,text=pruebas("Nicolas","Sepulveda","Chile"))
texto.config(
    height=3,
#    height=400,
    bg="green",
    font=("Arial",18 ),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack( anchor=NW)


ventana.mainloop()