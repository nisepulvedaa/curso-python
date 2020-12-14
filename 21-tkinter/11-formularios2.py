from tkinter import  *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas",20)
)
#encabezado.pack(anchor=N,side=TOP, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=10,sticky=W)
# Botones check

def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo web "

    if movil.get():
        if web.get():
            texto += "y Desarrollo móvil"
        else:    
             texto += "Desarrolo móvil"   

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
        )    

Label(ventana, text="¿A que te dedicas? ").grid(row=1,column=0)
Label(ventana, text="").grid(row=2,column=0)

web = IntVar()
movil = IntVar()

Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
    ).grid(row=3,column=0,sticky=W)
Checkbutton(
    ventana, 
    text="Desarrollo movile",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=4,column=0,sticky=W)

mostrar = Label(ventana,text="",bg="green")
mostrar.grid(row=5,column=0)

# Botones buttons

def marcar():
    marcado.config(
        text="El valor Seleccionado es:  {}".format(opcion.get())
    )


opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cual es tu genero?").grid(row=6,sticky=W)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=7,sticky=W)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=8,sticky=W)

marcado = Label(ventana)
marcado.grid(row=9,sticky=W)
# Botones Menu

def seleccionadoMenu():
    seleccionado.config(
        text="La opcion Seleccionada es: {} ".format(opcion.get())
    )



opcion = StringVar()
opcion.set("Opcion 1")
Label(ventana, text="Selecciona un Opcion").grid(row=10,column=0,sticky=W)
select = OptionMenu(ventana,opcion,"Opcion 1","Opcion 2","Opcion 3")
select.grid(row=10,column=1,sticky=W)

Button(ventana, text="Ver", command=seleccionadoMenu).grid(row=11,column=1,sticky=W)

seleccionado = Label(ventana)
seleccionado.grid(row=12,sticky=W)

ventana.mainloop()
    