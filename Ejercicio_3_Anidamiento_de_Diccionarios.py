"""
22. Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada representa un producto y tiene a su vez las claves "nombre" y "precio" con sus respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada producto.
23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y valor. Imprime el diccionario actualizado.
24.Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de jugadores.
25.Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor. La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario actualizado.
26.Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario "equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado.
"""
#22. Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada representa un producto y 
# tiene a su vez las claves "nombre" y "precio" con sus respectivos valores. 
# Recorre el diccionario e imprime el nombre y precio de cada producto.

#defino el diccionario
productos = {"producto_1": 
             {"nombre": "leche",
              "precio": 100,
              },
            "producto_2":
             {"nombre": "manteca",
              "precio": 50,
              }
            }
#recorreco con el primer for al diccionario productos (para ello tengo que colocar el metodo .items())
for nombre_producto, info_producto in productos.items():
    print(nombre_producto)
    for nombre, precio in info_producto.items():
        print(nombre, ":", precio)
    print("-----")


#23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y valor. Imprime el diccionario actualizado.
#definimos un nuevo item
new_item = {"producto_3": 
             {"nombre": "yogur",
              "precio": 200,
              },
            }
#acutalizamos el diccionario "productos"
productos.update(new_item)

#recorreco con el primer for al diccionario productos (para ello tengo que colocar el metodo .items())
for nombre_producto, info_producto in productos.items():
    print(nombre_producto)
    for nombre, precio in info_producto.items():
        print(nombre, ":", precio)
    print("-----")

#24.Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de jugadores.
equipos = {"Equipo_1": 
             {"nombre": "Boca",
              "jugadores": ["Carlos", "Martin", "Anibal"],
              },
            "Equipo_2":
             {"nombre": "River",
              "jugadores": ["Ricardo", "Andres", "Javier"],
              }
            }
#recorreco con el primer for al diccionario productos (para ello tengo que colocar el metodo .items())
for nombre_equipo, info_equipo in equipos.items():
    print(nombre_equipo)
    for nombre, jugadores in info_equipo.items():
        print(nombre, ":", jugadores)
    print("-----")

#25.Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor. La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario actualizado.
equipos["Equipo 3"] ={"nombre": "Racing", "jugadores": ["Martin", "Silvi", "Leon"]}
print("El diccionario actualizado de equipos es:")
for nombre_equipo, info_equipo in equipos.items():
    print(nombre_equipo)
    for nombre, jugadores in info_equipo.items():
        print(nombre, ":", jugadores)
    print("-----")

#26.Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario "equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado.
print("-----")
print("AGREGAMOS UN NUEVO JUGADOR")
print("-----")
nuevo_jugador_1 = "Enrique"

equipos["Equipo_1"]["jugadores"].append(nuevo_jugador_1)
#recorreco con el primer for al diccionario productos (para ello tengo que colocar el metodo .items())
for nombre_equipo, info_equipo in equipos.items():
    print(nombre_equipo)
    for nombre, jugadores in info_equipo.items():
        print(nombre, ":", jugadores)
    print("-----")

