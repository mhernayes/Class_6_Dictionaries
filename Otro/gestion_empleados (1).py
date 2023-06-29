'''Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento.'''

# Crear un diccionario vasio
empleados = {}
continuar = True

while continuar:
   print("1. Aregar empleado.")
   print("2. Actualizar salario de empleados.")
   print("3. Mostrar lista de mepleados.")
   print("4. Calcular promedio salarial por departamento.")
   print("5. Salir.")
   opcion = input("Seleccione una opccion:")

   # Agregar empleado
   if opcion == "1":
      nombre = input("Ingresar el nombre del empleado:")
      salario = float(input("Introdusca el salerio del empleado:"))
      departamento = input("Ingrese el departamento del empleado:")

      empleados[nombre]= {
         "salario": salario,
         "departamento": departamento
      }

      print("Empleado agregado exitosamente!")
      

# Actualisar salrio empleados
   elif opcion == "2":
       nombre = input("Ingresar el nombre del empleado:")
       # comprobar la existencia del empleado en la base de datos
       if nombre in empleados:
          # pedimos nuevo salario
          nuevo_salario = float(input("Introdusca el nuevo salerio del empleado:"))
          # actualisamos nuevo salario en base de datos
          empleados[nombre]["salario"] = nuevo_salario
          print("Salario actualizado exitosamente!")
       # si el empleado no existe en la base de datos   
       else:
          print("Empleado no emcontrado")

# Mostrar lista de mepleados
   
   elif opcion == "3":
      print("lista de empleados: ")
      for nombre ,dato_empleado in empleados.items():
         salario = dato_empleado["salario"]
         departamento = dato_empleado["departamento"]
         print(f"Nombre:{nombre}, Salario:{salario}, Departamento:{departamento}")
      break
         
