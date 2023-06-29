# 1. Crea un diccionario vacío llamado “mi_diccionario”.
print("\nEjercicio 1")

mi_diccionario = {}
print(type(mi_diccionario))

# 2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor sea tu nombre.
print("\nEjercicio 2")

mi_diccionario = {"nombre": "Nico"}
print(mi_diccionario)

# 3. Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario".
print("\nEjercicio 3")

print(mi_diccionario["nombre"])

# 4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False" en caso contrario.
print("\nEjercicio 4")

print("edad" in mi_diccionario.keys())

# 5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor:
# "nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia favorita.
print("\nEjercicio 5")

estudiante = {"nombre": "Jorge", "edad": "22", "materia": "Matemática"}
print(estudiante)

# 6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad actual de tu amigo.
print("\nEjercicio 6")

print(estudiante["edad"])

# 7. Elimina el par clave-valor con la clave "materia" del diccionario “estudiante".
print("\nEjercicio 7")

del estudiante["materia"]
print(estudiante)

# 8. Imprime todas las claves en el diccionario “estudiante".
print("\nEjercicio 8")

print(estudiante.keys())

# 9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor
# "1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor “5555555555”.
print("\nEjercicio 9")

agenda = {"Juan": "1234567890", "Joana": "9876543210", "Jimena": "5555555555"}
print(agenda)

# 10.Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor "9998887777".
print("\nEjercicio 10")

agenda["Julio"] = "9998887777"
print(agenda)

#11.Imprime el número de entradas (pares clave-valor) en el diccionario “agenda".
print("\nEjercicio 11")

print(len(agenda))

#12.Crea una lista llamada "claves" que contenga todas las claves del diccionario “agenda".
print("\nEjercicio 12")

claves = agenda.keys()
print(claves)

#13.Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y "False" en caso contrario.
print("\nEjercicio 13")

print("Juan" in agenda.keys())

#14.Elimina la entrada con la clave “Jimena”.
print("\nEjercicio 14")

del agenda["Jimena"]
print(agenda)

#15.Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e
# imprime cada par clave-valor en el formato "Nombre: Número”.
print("\nEjercicio 15")

for clave, valor in agenda.items():
    print(f"{clave}: {valor}")

#16.Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el
# diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”.
print("\nEjercicio 16")

print(agenda.get("Juan", "Clave no encontrada"))

#17.Borra todas las entradas del diccionario “agenda”.
print("\nEjercicio 17")

agenda.clear()
print(agenda)
