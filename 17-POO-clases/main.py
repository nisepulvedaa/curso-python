from coche import Coche

coche = Coche("Amarillo","Renault","Clio",150,200,4)
coche1 = Coche("Verde","Seat","Panda",240,200,4)
coche2 = Coche("Azul","Citroen","Xara",100,180,4)
coche3 = Coche("Rojo","Mercedes","Clase A",350,400,4)
"""
print(coche.getInfo())
print(coche1.getInfo())
print(coche2.getInfo())
print(coche3.getInfo())
"""

#Detectar tipado
coche3 = "aleatorio"
if type(coche3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto!!!")    

#Visibilidad   

print(coche.soy_publico)
print(coche.getPrivado())