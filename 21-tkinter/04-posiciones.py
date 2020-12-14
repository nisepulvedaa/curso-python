from tkinter import *

ventana = Tk()
#ventana.geometry("550x500")

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
    bg="blue",
    font=("Arial",18 ),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=TOP, anchor=CENTER, fill=X, expand=YES)


texto = Label(ventana,text="Basico 1")
texto.config(
    height=3,
    bg="green",
    font=("Arial",18 ),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X, expand=YES)


texto = Label(ventana,text="Basico 2")
texto.config(
    height=3,
    bg="red",
    font=("Arial",18 ),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X, expand=YES)


texto = Label(ventana,text="Basico 3")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18 ),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)



ventana.mainloop()