""""
REGISTRO DE PUNTAJES:
Implementa un programa en Python que permita registrar y mantener un seguimiento de los puntajes de un juego. 
El programa debe permitir a los jugadores ingresar sus nombres y puntajes, almacenarlos en un diccionario y proporcionar 
funcionalidades para mostrar el puntaje más alto, el promedio de puntajes y la cantidad total de jugadores.
"""

#defino la funcion registro
def registro_puntajes():
    #defino el diccionario vacio
    puntajes = {}
    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            #solicito ingresar los datos por pantalla
            nombre_jugador = input("Por favor ingrese el nombre del JUGADOR(si ingresa una tarea ya ingresada se actualizarán los datos):\n")
            puntaje_jugador = int(input("Por favor ingrese su PUNTAJE:\n"))
            #agregamos al diccionario puntajes los puntajes de cada jugador
            puntajes[nombre_jugador] = puntaje_jugador
            #se controla los datos ingresados con un try except     
            opcion = input("¿Desea ingresar otra jugador? (s/n): ")
            #con un if verificamos la respuesta ingresada
            if opcion.lower() == 's':
                True
            elif opcion.lower() == 'n':
                #salimos del while
                break
            else:
                print("Nombre de jugador no ingresado. Vuelva a intentarlo.")     
        except ValueError:
            print("Los datos ingresados no son correctos.")            
    #la variable que se devuelve es lista_notas
    return puntajes

#mensaje
print("-----------------------")
print("Bienvenidos al algoritmo de REGISTRO DE PUNTAJES")
print("-----------------------")
print("Este algoritmo sirve para:")
print("1. Ingresar los jugadores y sus puntajes.")
print("2. Mostrar el puntaje mas alto.")
print("3. Mostrar el promedio de puntajes.")
print("4. Mostrar la cantidad total de jugadores.")

#se llama a la funcion y se imprime el registro de tareas.
puntajes = registro_puntajes()
print("-----------------------")
#calculamos el valor mas alto
puntaje_mas_alto = max(puntajes.values())
print("El puntaje más alto es:", puntaje_mas_alto)
#calculamos el promedio y lo redondeamos
promedio_puntajes = sum(puntajes.values()) / len(puntajes)
promedio_puntajes_redondeado = round(promedio_puntajes, 2)
print("El promedio de los puntajes es:", promedio_puntajes_redondeado)
#imprimomos la cantidad de jugadores
print("La cantidad total de jugadores es:", len(puntajes))
