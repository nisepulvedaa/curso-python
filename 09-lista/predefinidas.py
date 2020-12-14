cantantes = ['2pac','Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1,9,8,4,5,6,7,10,3,2]


#Ordenar
print(numeros)
numeros.sort()
print(numeros)


#Añadir elementos

cantantes.append("Natos y Waros")
cantantes.insert(0,"Davod Bisbal")
print(cantantes)

#Elminar elementos
cantantes.pop(0)
print(cantantes)
cantantes.remove('2pac')
print(cantantes)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista

print('Drake' in cantantes)


# Contar elementos
print(cantantes)
print(len(cantantes))


#cuantas veces aparece un elemento detro de una lista
numeros.append(8)
print(numeros.count(8))

#conseguir indce

print(cantantes.index("Drake"))

#unir listas

cantantes.extend(numeros)
print(cantantes)