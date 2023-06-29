'''
GESTIÓN DE EMPLEADOS:
Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados.

Cada empleado tiene:
-Nombre
-Salario
-Departamento al que pertenece.

Implementa un programa en Python que permita:
1.agregar nuevos empleados
2.actualizar el salario de un empleado existente
3.mostrar la lista completa de empleados 
4.calcular el promedio salarial por departamento.


VAMOS A TRABAJAR CON UNA BBDD: con la siguiente estructura tipo LISTA

'''


import time
# 1 --- Creo la BBDD tipo LISTA vacía
BBDD = []
# 1.1 Mensaje bienvenida
print('-------- BIENVENIDO --------')

# 2 --- Pregunto por pantalla que desea hacer el usuario:

continuamos = True
opcion = ""

while continuamos:
    print('')
    print('1.Añadir un empleado nuevo..')
    print('2.Modificar un salario...')
    print('3.Mostrar el salario promedio de un departamento...')
    print('4.Mostrar la lista completa...')
    print('5.Salir')
    opcion = input('Por favor elige una de las opciones:')
    
# 2 --- AÑADIR EMPLEADOS
    if opcion == "1":
        # 2.1 Creo una DICCIONARIO vacío para añadir los datos del empleado nuevo
        datos_nuevo_empleado = {}
        print('')
        print('Estás apunto de añadir un empleado nuevo a tu BBDD')
        # 2.2 Pido por pantalla los 3 datos que estoy buscando 
        nombre_empleado = input('Introduce su nombre: ')
        nombre_empleado.lower() # CASE INSENSITIVE
        salario_empleado = input('Introduce su salario: ')
        departamento_empleado = input('Introduce su departamento: ')
        # 2.3 Añado los datos al DICCIONARIO vacío del nuevo usuario en cuestión
        datos_nuevo_empleado = {
            'nombre': nombre_empleado,
            'salario': salario_empleado,
            'departamento': departamento_empleado
        }
        # 2.4 Añado el DICT con los datos a la BBDD
        BBDD.append(datos_nuevo_empleado)
        print('Empleado añadido correctamente')

# 3 --- MODIFICAR EL SALARIO 
    elif opcion == '2':
        print('')
        print('Vas a modificar un salario..')
        empleado_perjudicado = input('¿Cuál es el nombre del empleado perjudicado?')
        #empleado_perjudicado.lower() # CASE INSENSITIVE 
        nuevo_salario = int(input('¿El nuevo salario cuál es?'))
        
        #  3.2 Recorro la BBDD con un FOR y modifico el valor por el nuevo salario
        for empleado in BBDD:

            if BBDD["nombre"] == empleado_perjudicado: #ERROR: TypeError: list indices must be integers or slices, not str ?¿?
                BBDD["salario"] = nuevo_salario
            else:
                print('ERROR')

# 4 --- SALARIO PROMEDIO DEPARTAMENTO
    elif opcion =='3':
        # 4.1 Pregunto por el departamento en cuestion
        departamento = input('¿De cuál departamento quieres saber el salario promedio?')
        # 4.2 Calculo el salario total de todos los empleados de ese departamento
        
        total_salarios = 0
        num_empleados_departamento = 0

        if BBDD['departamento'] == departamento: #ERROR: TypeError: list indices must be integers or slices, not str ?¿?
            total_salarios += BBDD['salario']
            # 4.3 Gracias a este contador calculo el numero de empleados del departamento
            num_empleados_departamento += 1
            print('T.Salario= ', total_salarios)
            print('Numero de empleados: ', num_empleados_departamento)
        
        if num_empleados_departamento > 0:
            salario_promedio = total_salarios / num_empleados_departamento
            print('El salario promedio del departamento es: ', salario_promedio)

        # 4.4 Calculo el promedio: Total Salario / total Empleados
        #for empleado in BBDD:
        
# 5 --- MOSTRAR LISTA COMPLETA
    elif opcion =="4":
        # 5.1 Recorremos la lista y mostramos los empleados
        for i in range(len(BBDD)):
            print(BBDD[i]["nombre"], BBDD[i]["salario"], BBDD[i]["departamento"])
# 6 --- SALIR:
    elif opcion == "5":
        print('Saliendo....')
        continuamos = False
        time.sleep(2)
    
    else:
        print('Error: opción incorrecta')
