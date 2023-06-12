"""
ADMINISTRACION DE PROYECTOS:
Eres un gerente de proyectos y necesitas un programa para administrar las tareas y responsabilidades de tu equipo. 
Cada tarea tiene un nombre, una descripción y un responsable asignado. Implementa un programa en Python que utilice un 
diccionario para almacenar la información de las tareas. 
El programa debe permitir agregar nuevas tareas, asignar responsables a las tareas existentes, actualizar 
las descripciones de las tareas y mostrar la lista completa de tareas y responsables.
(Pista: puedes comenzar con un diccionario vacío y construir un diccionario de diccionarios)
"""

#defino la funcion registro
def administracion():
    #defino el diccionario vacio
    tareas = {}
    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            #solicito ingresar los datos por pantalla
            nombre_tarea = input("Por favor ingrese el nombre de la TAREA (si ingresa una tarea ya ingresada se actualizarán los datos):\n")
            nombre_personal = input("Por favor ingrese el nombre del PERSONAL ASGINADO:\n")
            descripcion = input("Por favor ingrese la DESCRIPCION DE LA TAREA:\n")
            #agregamos al diccionario la tarea ingresada 
            tareas[nombre_tarea] = [nombre_personal, descripcion]
            #se controla los datos ingresados con un try except     
            opcion = input("¿Desea ingresar otra tarea? (s/n): ")
            #con un if verificamos la respuesta ingresada
            if opcion.lower() == 's':
                True
            elif opcion.lower() == 'n':
                #salimos del while
                break
            else:
                print("Tarea no ingresada. Vuelva a intentarlo.")     
        except ValueError:
            print("Los datos ingresados no son correctos.")            
    #la variable que se devuelve es lista_notas
    return tareas

#mensaje
print("-----------------------")
print("Bienvenidos al algoritmo de ADMINISTRACION DE PROYECTOS")
print("-----------------------")
print("Este algoritmo sirve para:")
print("1. Registrará las tareas.")
print("2. Asignar responsables.")
print("3. Actualizar la informacion de la tarea.")
print("4. Mostrar la lista completa del responsable y su tarea.")

#se llama a la funcion y se imprime el registro de tareas.
informacion_tarea = administracion()