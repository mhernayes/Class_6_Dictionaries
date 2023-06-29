'''REGISTRO DE PUNTAJES: 
Implementa un programa en Python que permita registrar y mantener un 
seguimiento de los puntajes de un juego. El programa debe permitir a los 
jugadores ingresar sus nombres y puntajes, almacenarlos en un 
diccionario y proporcionar funcionalidades para mostrar el puntaje más 
alto, el promedio de puntajes y la cantidad total de jugadores'''

puntajes={}
continuar="s"
print("---REGISTRO DE PUNTAJES---")
while continuar=="s":
    nombre=input("Ingrese su nombre: ")
    puntaje=int(input("Introduce tu puntaje: "))
    puntajes[nombre]=puntaje
    continuar=input("¿Desea ingresar otro jugador (s/n)?: ")

max_puntaje = max(puntajes.values()) # Obtener el puntaje máximo

promedio_puntaje = round(sum(puntajes.values()) / len(puntajes))  # Obtener el promedio de puntajes

total_jugadores = len(puntajes) # Obtener el total de jugadores

print("El puntaje más alto es:", max_puntaje)
print("El promedio de puntajes es:", promedio_puntaje)
print("La cantidad total de jugadores es:", total_jugadores)


