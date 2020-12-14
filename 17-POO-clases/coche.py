class Coche:
    #Atributos (propiedades del objeto)
    #caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 50
    plazas = 2

    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"

    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # Metodos, son accioens que hace el objeto (coche) (funciones)


    def getPrivado(self):
        return self.__soy_privado 

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setMarca(self,marca):
            self.marca = marca

    def getMarca(self):
        return self.marca

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

    def getInfo(self):
        info = "---- Información del coche ----"
        info += "\n Color: " +  self.getColor()
        info += "\n Marca: " +  self.getMarca()
        info += "\n Velocidad: " + str(self.getVelocidad())
        info += "\n Modelo: " + self.getModelo()

        return info