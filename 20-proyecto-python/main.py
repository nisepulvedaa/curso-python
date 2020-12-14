"""
Proyecto python y mysql

-abrir asistente
-Login o registro
-si elegegimos registro, creare un usuario en la bd
-si elegimos login, identifica al usuario y nos preguntara
-crear nota , mostrar notas, borrarlas

"""

from usuarios import acciones

print("""
acciones disponibles:
- registro
- login
""")

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")
if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
   