"""
GESTIÓN DE EMPLEADOS:
Imagina que eres el gerente de recursos humanos de una empresa y necesitas gestionar la información de los empleados. 
Cada empleado tiene un nombre, salario y departamento al que pertenece. Implementa un programa en Python que permita 
agregar nuevos empleados, actualizar el salario de un empleado existente, mostrar la lista completa de empleados y 
calcular el promedio salarial por departamento.
"""
#defino la funcion registro
def registro_empleados():
    #defino el diccionario vacio
    info_empleado = {}
    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            #solicito ingresar los datos por pantalla
            legajo_empleado = input("Por favor ingrese el LEGAJO del Empleado(si ingresa una LEGAJO ya ingresado se actualizarán los datos):\n")
            nombre_empleado = input("Por favor ingrese el Nombre:\n")
            apellido_empleado = input("Por favor ingrese su Apellido:\n")
            saladio_empleado = int(input("Por favor ingrese su Salario:\n"))
            departamento_empleado = input("Por favor ingrese su Departamento:\n")
            #agregamos al diccionario info_empleado la informacion de cada empleado
            info_empleado[legajo_empleado] = [nombre_empleado, apellido_empleado, saladio_empleado, departamento_empleado]
            #se controla los datos ingresados con un try except     
            opcion = input("¿Desea ingresar otro LEGAJO? (s/n): ")
            #con un if verificamos la respuesta ingresada
            if opcion.lower() == 's':
                True
            elif opcion.lower() == 'n':
                #salimos del while
                break
            else:
                print("LEGAJO no ingresado. Vuelva a intentarlo.")     
        except ValueError:
            print("Los datos ingresados no son correctos.")            
    #la variable que se devuelve es lista_notas
    return info_empleado

#mensaje
print("-----------------------")
print("Bienvenidos al algoritmo de REGISTRO DE EMPLEADOS DEL DEPARTAMENTO DE CONQUERBLOCKS")
print("-----------------------")
print("Este algoritmo sirve para:")
print("1. Dar de alta un Empleado nomina de RRHH.")
print("2. Actualizar el nombre y apellido.")
print("3. Actualizar el salario.")
print("4. Actualizar su departamento.")

#se llama a la funcion y se imprime el registro de tareas.
info_empleado = registro_empleados()

#recorremos todosl los salarios de los valores del diccionario y calculamos su maximo
max_salario = max([info[2] for info in info_empleado.values()])

#recorremos todosl los salarios de los valores del diccionario y calculamos su suma
suma_salario = sum([info[2] for info in info_empleado.values()])

#calculamos el promedio y lo redondeamos
promedio_salario = suma_salario / len(info_empleado)
promedio_salario_redondeado = round(promedio_salario, 2)

#print("La lista completa de empleados es", info_empleado)
lista_info_empleados = list(info_empleado.items())
for item in lista_info_empleados:
    print("-----------")
    print("LEGAJO", item[0])
    print("NOMBRE:", item[1][0])
    print("APELLIDO:", item[1][1])
    print("SALARIO:", item[1][2])
    print("DEPARTAMENTO:", item[1][3])
    print("-----------")

#imprimomos el salario mas alto, el promedio y la cantidad de empleados
print("El salario más alto es:", max_salario)
print("El salario más promedio:", promedio_salario_redondeado)
print("La cantidad total de Empleados es:", len(info_empleado))

