"""
Crear un programa que tenga:

(hecho) - Ventana
(hecho) - Tamaño fijo
(hecho) - No redimensionable
(hecho) - Un menu
(hecho) - Opcion de salir
(hecho) - Diferentes pantallas
(hecho) - Formulario de añadir productos
(hecho) - Guardar datos temporalmente
- Mostrar datos listados en la pantalla home

"""

from tkinter import *
from tkinter import ttk

#Definir Ventana
ventana = Tk()
#ventana.geometry("500x400")
ventana.minsize(500,400)
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0,0)

#Pantallas


def home():
    #Mostar Pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)

      
    products_box.grid(row=2)
    #Listar Productos
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="-----------------").grid()
    """        
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert('',0,text=product[0] ,values=(product[1]))


    #Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
  
    return True

def add():
    #Monta Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=120,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    
    #Monta campos del Formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5,sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5,sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_descripcion_label.grid(row=3, column=0, padx=5, pady=5,sticky=NW)
    add_descripcion_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_descripcion_entry.config(
        width=30,
        height=5,
        font=("Consolas",12),
        padx=15,
        pady=15
    )

    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="black",
        fg="white"
    )

    add_separator.grid(row=4)

    #Ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


    return True

def info():

    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=160,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    #Ocultar otras pantallas
    add_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    home_label.grid_remove()

    return True

def add_product():
       products.append([
         name_data.get(),
         price_data.get(),
         add_descripcion_entry.get("1.0","end-1c")
       ]) 
       name_data.set("")
       price_data.set("")
       add_descripcion_entry.delete("1.0",END)
       #print(products)
       home()
       
     

#variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

#Definir campos de pantalla
home_label = Label(ventana, text="Inicio")
#products_box = Frame(ventana,width=250)
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0,columnspan=2)
products_box.heading("#0",text="Producto",anchor=W)
products_box.heading("#1",text="Precio",anchor=W)

add_label = Label(ventana, text="Añadir Producto")
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Nicolas Sepulveda - 2020 ")

# Campos del formulario

add_frame = Frame(ventana)


add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_descripcion_label = Label(add_frame, text="Descripción: ")
add_descripcion_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)

#Cargar Pantalla de Inicio
home()

#Menu Superior
menu_superior = Menu(ventana)
menu_superior.add_command(labe="Inicio", command=home)
menu_superior.add_command(labe="Añadir", command=add)
menu_superior.add_command(labe="Información", command=info)
menu_superior.add_command(labe="Salir", command=ventana.quit)

#Cargar Menu
ventana.config(menu=menu_superior)

#Cargar Ventana
ventana.mainloop()