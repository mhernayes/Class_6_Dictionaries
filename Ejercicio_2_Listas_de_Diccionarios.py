"""
LISTAS DE DICCIONARIOS:
18.Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos valores. Recorre la lista e imprime el nombre y edad de cada estudiante.
19.Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las mismas claves "nombre" y "edad". Imprime la lista actualizada.
20.Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada.
21.Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor. Imprime la lista actualizada.
"""

#18.Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario representa a un estudiante y 
# tiene las claves "nombre" y "edad" con sus respectivos valores. 
# Recorre la lista e imprime el nombre y edad de cada estudiante.
 
estudiantes = [{"Nombre": "Martin", "Edad": 36}, {"Nombre": "Silvina", "Edad": 37}]

#guardamos en la variable info_estudiantes y recorremos con el metodo de compresion de listas
info_estudiantes =  [estudiante["Nombre"] + " - " + str(estudiante["Edad"]) for estudiante in estudiantes]
for info in info_estudiantes:
    print(info)

#19.Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las mismas claves "nombre" y "edad". Imprime la lista actualizada.
#defino en una variable la info del nuevo estudiante
nuevo_usuario = {"Nombre:": "Leon", "Edad:": 6}
#agrego a la lista estudiantes la info del estudiante con el metodo apend
estudiantes.append(nuevo_usuario)
print(estudiantes)

#20.Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada.
estudiantes.pop(1)
print(estudiantes)

#21.Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor. Imprime la lista actualizada.
estudiantes[0].update(Edad = 14)
print(estudiantes)

