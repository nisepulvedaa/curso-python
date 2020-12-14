#Programacion orianta a objetos(Poo o OOP)

#definir una clase (molde para crear mas objetos de ese tipo)
#(coche) con caracteristicas similares

class Coche:
    #Atributos (propiedades del objeto)
    #caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 50
    plazas = 2

    # Metodos, son accioens que hace el objeto (coche) (funciones)

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# fin definicion clase
#    


#crear objeto


coche = Coche()
coche.setColor("amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getColor(), coche.getModelo())
print("Velocidad actual: {}".format(coche.getVelocidad()))

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
print("Velocidad actual: {}".format(coche.getVelocidad()))
coche.frenar()
print("Velocidad actual: {}".format(coche.getVelocidad()))

#crear mas objetos

print("Objetoo!!! 2")

coche2 = Coche()
coche2.setColor("Verde")
coche2.setColor("Gallardo")

print(coche2.marca, coche2.getColor(), coche2.getModelo())
print("Velocidad actual: {}".format(coche2.getVelocidad()))