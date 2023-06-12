"""
REGISTRO DE ASISTENCIAS:
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus estudiantes a lo largo del semestre. 
Cada estudiante tiene un nombre y una lista de fechas en las que asistió a clases. Implementa un programa en 
Python que utilice un diccionario para almacenar la información de las asistencias. El programa debe permitir 
registrar la asistencia de los estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de estudiantes 
y las fechas en las que asistieron.
(Pista: puedes comenzar con un diccionario vacío y construir un diccionario de listas)
"""
import datetime

#defino la funcion registro
def asistencias():
    #defino el diccionario vacio
    registro_asistencias = {}
    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            #solicito ingresar los datos por pantalla
            nombre_alumno = input("Por favor ingrese el nombre del Alumno (si es un alumno una tarea ya ingresado se agregaran los datos):\n")
            fecha = input("Por favor ingrese la fecha (DD/MM/AAAA) en las que el alumno asistió a clases:\n")
            fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
            #se controla los datos ingresados con un try except     
            opcion = input("¿Desea ingresar otro alumno? (s/n): ")
            #con un if verificamos la respuesta ingresada
            if opcion.lower() == 's':
                #agregamos al diccionario 
                #si la fecha ya se encontraba ingresada la agregamos a la lista de fechas con un append
                if nombre_alumno in registro_asistencias:
                    registro_asistencias[nombre_alumno].append(fecha)
                #si el alumno no se encontraba ingresado
                else:
                    registro_asistencias[nombre_alumno] = []
                    registro_asistencias[nombre_alumno].append(fecha)
                    True
            elif opcion.lower() == 'n':
                #si la fecha ya se encontraba ingresada la agregamos a la lista de fechas con un append
                if nombre_alumno in registro_asistencias:
                    registro_asistencias[nombre_alumno].append(fecha)
                #si el alumno no se encontraba ingresado
                else:
                    registro_asistencias[nombre_alumno] = []
                    registro_asistencias[nombre_alumno].append(fecha)
                #salimos del while
                break
            else:
                print("Alumno no ingresado. Vuelva a intentarlo.")     
        except ValueError:
            print("Los datos ingresados no son correctos")

    #la variable que se devuelve es lista_notas
    return registro_asistencias

#mensaje
print("-----------------------")
print("Bienvenidos a la ESCUELA DE CONQUER BLOCKS")
print("-----------------------")
print("Este algoritmo sirve para:")
print("1. Registrará las alumnos.")
print("2. Actualizar sus asistencias.")

#se llama a la funcion y se imprime la lista_notas.
registro_asistencias = asistencias()
#con un for recorrecmos todo el diccionario 
#desempaquetamos el diccionario en nombre y fechas
for nombre, fechas in registro_asistencias.items():
    print("------ REGISTRO DE ASISTENCIAS DE {} ------".format(nombre.upper()))
    #ordenamos la lista con las fechas
    fechas.sort()
    #imprimimos las fechas una debajo de la otra
    for _fecha in fechas:
        #formateamos las fechas al formato DD/MM/AAAA
        fechas_formateadas = _fecha.strftime("%d/%m/%Y")
        print(fechas_formateadas)
        #imprimimos la lista ordenada por fecha
    print("-----------")

