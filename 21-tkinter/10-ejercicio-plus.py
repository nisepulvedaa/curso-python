"""

CALCULADORA:

-Dos campos de texxto
-4 botones para las operaciones
-Mostrar el resultado en una alerta

"""
from tkinter import *
from tkinter import messagebox  as MessageBox

class Calculadora:

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas


    def convertirFloar(self,numero):
        try:
            result = float(numero)
        except:
            result = 0
            MessageBox.showerror("Error","Solo puede ingresar Datos numeros intente nuevamente")
        return result    

    def sumar(self):
        self.resultado.set(self.convertirFloar(self.numero1.get()) + self.convertirFloar(self.numero2.get()))
        self.mostrarResultado()

        

    def restar(self):
        self.resultado.set(self.convertirFloar(self.numero1.get()) - self.convertirFloar(self.numero2.get()))
        self.mostrarResultado()
    

    def multiplicar(self):
        self.resultado.set(self.convertirFloar(self.numero1.get()) * self.convertirFloar(self.numero2.get()))
        self.mostrarResultado()


    def dividir(self):
        self.resultado.set(self.convertirFloar(self.numero1.get()) / self.convertirFloar(self.numero2.get()))
        self.mostrarResultado()


    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", "El resultado de la operacion es {} ".format(self.resultado.get()))
        self.numero1.set("")
        self.numero2.set("")




ventana = Tk()
ventana.title("Ejercicio Calculadora - Maser en python")
ventana.geometry("400x250")
ventana.resizable(0,0) 


calculadora = Calculadora(MessageBox)


marco = Frame(ventana, width=250, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco,textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco,textvariable=calculadora.numero2,justify="center").pack()


Label(marco, text="").pack()
Button(marco, text="Sumar",command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar",command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar",command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir",command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()