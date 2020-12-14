from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta","Hola soy Nicolas Sepulveda")
    MessageBox.showwarning("Alerta","Hola soy Nicolas Sepulveda")
    MessageBox.showerror("Alerta","Hola soy Nicolas Sepulveda")

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres continuar ejecutando la aplicacion?")
    
    if resultado != "yes":
        MessageBox.showinfo("Adios","Hasta Luego {} ".format(nombre))
        ventana.destroy()

Button(ventana, text="Mostar Alerta!!!", command=sacarAlerta).pack()
Button(ventana, text="Salir", command=lamba:salir("Nicolas Sepulveda")).pack()

ventana.mainloop()