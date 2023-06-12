"""
ANÁLISIS DE VOTACIONES:
Supongamos que tienes los resultados de una elección con los nombres de los candidatos y la cantidad de votos obtenidos por cada uno. 
Implementa un programa en Python que permita registrar los votos, mostrar la lista completa de candidatos y sus votos, 
encontrar al candidato ganador (con más votos) y calcular el porcentaje de votos que obtuvo cada candidato.
"""

#defino la funcion registro
def registro_empleados():
    #defino el diccionario vacio
    info_elecciones = {}
    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            #solicito ingresar los datos por pantalla
            candidato_lista = input("Por favor ingrese el Número de Lista(si ingresa una LISTA ya ingresado se actualizarán los datos):\n")
            candidato_nombre = input("Por favor ingrese el Nombre del Candidato:\n")
            candidato_apellido = input("Por favor ingrese el Apellido:\n")
            candidato_votos = int(input("Por favor ingrese la cantidad Votos:\n"))
            #agregamos al diccionario info_empleado la informacion de cada empleado
            info_elecciones[candidato_lista] = [candidato_nombre, candidato_apellido, candidato_votos]
            #se controla los datos ingresados con un try except     
            opcion = input("¿Desea ingresar otra LISTA? (s/n): ")
            #con un if verificamos la respuesta ingresada
            if opcion.lower() == 's':
                True
            elif opcion.lower() == 'n':
                #salimos del while
                break
            else:
                print("LISTA no ingresada. Vuelva a intentarlo.")     
        except ValueError:
            print("Los datos ingresados no son correctos.")            
    #la variable que se devuelve es lista_notas
    return info_elecciones

#mensaje
print("-----------------------")
print("Bienvenidos al algoritmo de REGISTRO DE VOTOS DE LAS ELECCIONES")
print("-----------------------")
print("Este algoritmo sirve para:")
print("1. Dar de alta una Lista de un Candidato.")
print("2. Actualizar el nombre y apellido.")
print("3. Actualizar la cantidad de votos.")

#se llama a la funcion y se imprime el registro de tareas.
info_elecciones = registro_empleados()

#recorremos todos los salarios de los valores del diccionario y calculamos su maximo
max_votos = max([info[2] for info in info_elecciones.values()])

#recorremos todos los salarios de los valores del diccionario y calculamos su suma
suma_votos = sum([info[2] for info in info_elecciones.values()])

#creamos una lista con todos la info
lista_info_empleados = list(info_elecciones.items())

#recorremos esa lista e imprimimos los resultados
for item in lista_info_empleados:
    print("-----------")
    print("LISTA", item[0])
    print("NOMBRE:", item[1][0])
    print("APELLIDO:", item[1][1])
    print("VOTOS:", item[1][2])
    porcentaje = round((item[1][2] * 100) / suma_votos, 2)
    print("PORCENTAJE:", porcentaje)
    print("-----------")

#imprimomos los datos generales de las elecciones
print("La cantidad de votos más alta es:", max_votos)
print("La cantidad de votos más total es:", suma_votos)
print("La cantidad total de Candidatos es:", len(info_elecciones))