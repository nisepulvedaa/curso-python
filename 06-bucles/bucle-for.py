"""
#FOR

for variable in elemento_iterable (lista,rango,etc)
    BLOQUE DE INSTRUCCIONES

"""

"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el {} ".format(contador))
    resultado = resultado + contador
    
print("La suma es: {} ".format(resultado))

"""

#Ejemplo tablas de multiplicar

numero = int(input("Ingrese Un Numero para multiplicar: "))

if numero < 1:
    numero = 1
else:
 print("Tabla de multiplicar del numero {} ".format(numero))

for contador in range(1,11):
    if numero == 45:
        print("No se pueden mostrar numeros prohibidos")
        break
    print("{} x {} = {} ".format(numero, contador,(numero*contador)))
else:
    print("Tabla Finalizada")    


"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el {} ".format(contador))
    resultado = resultado + contador
    
print("La suma es: {} ".format(resultado))
"""