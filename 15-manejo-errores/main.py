#Captura excepciones y manejar errores en codigo
#suceptible a fallos/errores

"""
try:
    nombre = input("¿Cual es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es : " + nombre
    print(nombre_usuario)
except:
    print("Ha Ocurrido un error, mete bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la Iteración!!")        
"""
"""
#Multiples excepciones
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("el cuadrado de {} es: {}".format(str(numero),str(numero*numero)))
except TypeError:
    print("Devbes convertir tus cadenas a enterose")    
except ValueError:
    print("Solo puede ingresar campos numericos vuelva a intentar")   
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)   
 """

#Excepciones personalizadas o lanzar excepcion
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))    

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("el nombre no ésta Completo")
    else:
        print("Bienvenido al master en python {} ".format(nombre))
except ValueError:
    print("Introduce los datos correctamente!!!")       
except Exception as e:
    print("Existe un error: ", e)    