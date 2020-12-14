"""
condicional IF
SI se_se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones    

# Operadores de comparación
# == igual
# < menor que
# > mayor que
# <= menor o igual que    
# >= mayor igual o que     


#operadores logicos

and Y
or O
! negacion
not NO
"""

"""
#Ejemplo 1

print("############################# Ejemplo 1 ############ ")

#color = "verde"

color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Correcto mi color favorito es ROJO")
else:
    print("Mi color favorito no es {} ".format(color))   
"""

"""
print("############################# Ejemplo 2 ############ ")    

#year = 2020
year = input("¿En que año Estamos?: ")

if int(year) < 2021:
    print("Estamos antes de 2021 ")
else:
    print("Estamos despues  a 2021")
"""

"""
print("############################# Ejemplo 3 ############ ")    

nombre = "Nicolas Sepulveda"
ciudad = "Santiago"
continente = "America del Sur"
edad = 26
mayoria_edad = 18

if edad >= mayoria_edad:
    print("{} es Mayor de edad!!".format(nombre))

    if continente != "Europa":
        print("{} No es Europeo es de {} de la ciudad de: {} ".format(nombre,continente,ciudad))
    else:
        print("{} es Europeo y de {} ".format(nombre,ciudad))


else:
        print("{} No es Mayor de edad!!".format(nombre))
"""

"""
print("############################# Ejemplo 4 ############ ")   
dia = int(input("Introduce el numero del dia de la semana: "))


if dia == 1:
    print("Es Lunes")
elif dia == 2: print("Es Martes")
elif dia == 3: print("Es Miercoles")
elif dia == 4: print("Es Jueves")    
elif dia == 5: print("Es Viernes")    
elif dia == 6: print("Es Sabado")    
elif dia >  7: print("Debe Ingresar numero menor o igual a 7") 
else: print("Es domingo")   
"""
"""
print("############################# Ejemplo 5 ############ ")   


edad_minima = 18
edad_maxima = 65
edad_real =int(input("Introduce tu edad para validar si tienes edad de trabajar, tu edad es : "))

if edad_real >= 18 and edad_real <= 65:
    print("Esta en edad de trabajar")
else:
     print("No esta en edad de trabajar")   
"""

"""
print("############################# Ejemplo 6 ############ ")   

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print("{} es un pais de habla hispana !!!".format(pais))
else:
     print("{} No es un pais de habla hispana !!!".format(pais))
"""
"""
print("############################# Ejemplo 7 ############ ")   

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
      print("{} No es un pais de habla hispana !!!".format(pais))
else:
       print("{} es un pais de habla hispana !!!".format(pais))
"""
 
print("############################# Ejemplo 8 ############ ")   

pais = "Francia"

if  (pais != "Mexico" and pais != "España" and pais != "Colombia"):
      print("{} No es un pais de habla hispana !!!".format(pais))
else:
       print("{} es un pais de habla hispana !!!".format(pais))      

"""
edad = input("Ingrese su edad: ")

if int(edad) < 18 :
    print("Usted es menor de edad")
else: 
    print("Usted es mayor de edad")
"""    