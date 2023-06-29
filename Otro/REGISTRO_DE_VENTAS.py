'''
REGISTRO DE VENTAS:
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
'''

#   Crear el diccionario con el producto y numero de ventas
ventas = {}
respuesta = 's' 

#  Mensaje con el usuario para comenzar el programa.
print('Bievenido!!: ')

# Registrar ventas producto nuevo o existente
while  True:                                                                #Programa siempre activo
    if respuesta == 's' or respuesta =='S':
        producto = input('Introduzca el nombre del producto:\n')            #Leer los datos del usuario
        uds = int(input('introduzca la cantidad\n'))
        if producto in ventas :                                             #Si el producto esta en ventas, actualizamos la cantidad
            ventas[producto] += uds                                        
        else:                                                               #Si no existe, Creamos un nuevo clave-valor en el dict.
            ventas[producto] = uds
        respuesta = input('Desea seguir registrando productos ? S/N ? ')

# Mostrar el numero total de ventas
    elif respuesta == 'n' or respuesta =='N':
        print('Aqui está tus ventas del dia:')                              #Imprimir el diccionario de ventas ordenado
        for producto, uds in ventas.items():
            print(producto + ":", uds)
        
        total_ventas = sum(ventas.values())
        print(f'El número de ventas totales: es de {total_ventas}')
        break                                                               #Salir del programa

