"""
REGISTRO DE VENTAS:
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias de tus productos. 
Cada producto tiene un nombre y una cantidad vendida. Implementa un programa en Python que utilice un diccionario 
para almacenar la información de las ventas. El programa debe permitir registrar las ventas de productos, actualizar la 
cantidad vendida de un producto existente y calcular el total de ventas diarias.
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada producto)
"""
#defino la funcion registro
def registro():
    #defino el diccionario vacio
    productos = {}
    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            #solicito ingresar los datos por pantalla
            nombre_producto = input("Por favor ingrese el nombre del producto:\n")
            cantidad_vendida = int(input("Por favor ingrese el número de ventas del producto ingresado:\n"))
            #se controla los datos ingresados con un try except     
            opcion = input("¿Desea ingresar otro producto? (s/n): ")
            #con un if verificamos la respuesta ingresada
            if opcion.lower() == 's':
                #agregamos al diccionario 
                #si el producto ya se encontraba ingresado le sumamos la cantidad
                if nombre_producto in productos:
                    productos[nombre_producto] += cantidad_vendida
                #si el producto no se encontraba ingresado le agregamos la cantidad
                else:
                    productos[nombre_producto] = cantidad_vendida 
                    True
            elif opcion.lower() == 'n':
                #si el producto ya se encontraba ingresado le sumamos la cantidad
                if nombre_producto in productos:
                    productos[nombre_producto] += cantidad_vendida
                #si el producto no se encontraba ingresado le agregamos la cantidad
                else:
                    productos[nombre_producto] = cantidad_vendida 
                #salimos del while
                break
            else:
                print("Producto no ingresado. Vuelva a intentarlo.")     
        except ValueError:
            print("Los datos ingresados no son correctos") 
         
    #la variable que se devuelve es lista_notas
    return productos

#creamos la funcion total y le pasamos el diccionario con el registro de ventas
def total(registro_ventas):
    #convertimos solos los valores en una lista, le aplicamos la funcion sum y lo guardamos en la variable cantidad_ventas
    cantidad_ventas = sum(list(registro_ventas.values()))
    #devolvemos cantidad_ventas
    return cantidad_ventas

#mensaje
print("-----------------------")
print("Bienvenidos a la TIENDA DE CONQUER BLOCKS")
print("-----------------------")
print("Este algoritmo sirve para:")
print("1. Registrará las ventas.")
print("2. Actualizar la cantidad vendida.")
print("3. Calcular el total de ventas diarias.")

#se llama a la funcion y se imprime la lista_notas.
registro_ventas = registro()
print(registro_ventas)

#se llama a la funcion total, se iguala a la variable cantidad_ventas e imprimimos el resultado por pantalla
cantidad_ventas = total(registro_ventas)
print("La cantidad de ventas totales es:", cantidad_ventas)
