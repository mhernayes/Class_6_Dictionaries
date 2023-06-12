"""
1. Crea un diccionario vacío llamado “mi_diccionario”.
2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor sea tu nombre.
3. Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario".
4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False" en caso contrario.
5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor: "nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia favorita.
6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad actual de tu amigo.
7. Elimina el par clave-valor con la clave "materia" del diccionario “estudiante".
8. Imprime todas las claves en el diccionario “estudiante".
9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor "1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor “5555555555”.
10.Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor “9998887777".
11.Imprime el número de entradas (pares clave-valor) en el diccionario “agenda".
12.Crea una lista llamada "claves" que contenga todas las claves del diccionario “agenda".
13.Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y "False" en caso contrario.
14.Elimina la entrada con la clave “Jimena”.
15.Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e imprime cada par clave-valor en el formato "Nombre: Número”.
16.Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”.
17.Borra todas las entradas del diccionario “agenda”.

"""
#1. Crea un diccionario vacío llamado “mi_diccionario”.
mi_diccionario = {}
print(type(mi_diccionario))

#2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor sea tu nombre.
mi_diccionario["nombre"] = "Martin"
mi_diccionario["edad"] = "36"

print(mi_diccionario)

#3. Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario".
print(mi_diccionario["nombre"])

#4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False" en caso contrario.
if "edad" in mi_diccionario.keys():
    print("True")
else:
    print("False")

#5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor: "nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia favorita.
estudiantes = {
    "martin": [36, "python"],
    "silvina": [37, "educacion especial"],
    "eduardo": [73, "medicina"],
}
print(estudiantes)

estudiantes_2 = {
    "nombre": "martin",
    "edad": 36,
    "materia": "Python",
}
print("El diccionario estudiantes_2 es:", estudiantes_2)

#6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad actual de tu amigo.
#metodo 1
estudiantes["eduardo"] = [74, "carpinteria"]
print(estudiantes)
#metodo 2
estudiantes.update(eduardo = [78, "cocina"])
print(estudiantes)

#7. Elimina el par clave-valor con la clave "materia" del diccionario “estudiante".
del estudiantes_2["materia"]
print("Eliminamos materia de estudiantes_2:", estudiantes_2)

#otra forma de eliminar es con pop
estudiantes_2.pop("edad")
print("Otra forma de eliminar es con pop:", estudiantes_2)

#8. Imprime todas las claves en el diccionario “estudiante".
print(estudiantes.keys())

#9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor "1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor “5555555555”.
agenda = {"Juan": 1234567890,
          "Joana": 9876543210,
          "Jimena": 5555555555,
}

#10.Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor “9998887777".
agenda["Julio"] = 9998887777
print(agenda)
agenda.setdefault("Martin", 123456788) #otra forma de agregar una clave y un valor al diccionario
print(agenda)

#11.Imprime el número de entradas (pares clave-valor) en el diccionario “agenda".
longitud_agenda = len(agenda)
print("El diccionario agenda, contiene una cantidad de pares clave-valor de:", longitud_agenda)

#12.Crea una lista llamada "claves" que contenga todas las claves del diccionario “agenda".
claves = [agenda.keys()]
print(claves)
print(type(claves))

#13.Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y "False" en caso contrario.
if "Juan" in agenda.keys():
    print("True")
else:
    print("False")

#14.Elimina la entrada con la clave “Jimena”.
agenda_eliminado = agenda.pop("Jimena")
print("La agenda de sin 'Jimena' es:", agenda)
print("El valor eliminada es: ", agenda_eliminado)

#15.Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e imprime cada par clave-valor en el formato "Nombre: Número”.
for nombre, numero in agenda.items():
    print("Nombre:", nombre)
    print("Numero:", numero)
    print("-----")

#16.Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”.
valor_buscado = agenda.get("Juan")
if valor_buscado == None:
    print("Clave no encontrada")
else:
    print(valor_buscado)

#17.Borra todas las entradas del diccionario “agenda”.
agenda = agenda.clear()
if agenda == None:
    print("El diccionario esta vacio")