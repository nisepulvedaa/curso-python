"""

Ejercico 10. El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla
cuantos han aprobado y cuantos han suspendido

"""
contador = 0
aprobados = 0
suspendido = 0
numero_alumnos = int(input("¿Cuantos alunos tienes?: "))

while contador != numero_alumnos:
    nota = int(input("Ingrese la nota del alumno {}: ".format(contador+1)))
    if nota >= 5:
        aprobados += 1
    else:
        suspendido += 1    
    contador += 1
print("Alumnos aprobados {} - Alumnos Suspedidos {} ".format(aprobados, suspendido))


