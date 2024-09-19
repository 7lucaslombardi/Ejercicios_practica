# FUNCIONES : se encarga de una tarea especifica
#             sirven para descomponer una tarea en un bloque de codigo
#             permiten que el codigo sea modular, legible y facil de mantener
#             permiten realizar una tarea a la vez y reutilizarla
#             bloque de codigo con una utilidad especifica
#  def (palabra reservada) + nombre de la funcion (verbo) + parametro () (declaracion de la funcion)
# return (palabra reservada)

# Parametros formales : variables locales declaradas en la definicion de la funcion

# Parametros actuales: variables o datos que recibe la funcion al momento de ser invocada

# Parametros por posicion : respetar la posicion de los parametros definidos 

# a los parametros se les puede asignar un determinado tipo (int, float, string)

# Variables locales : son solo las que estan dentro de las funciones, no son accesibles fuera de la funcion

# Variables globales : son las que estan por fuera de las funciones, son accesibles en cualquier parte del codigo
# dentro de la funcion al poner la palabra "global" + variable, determinas que es una variable global y se le puede cambiar el valor

# Cohesion: conexion que asegura que las partes esten bien integradas y funcionen efectivamente juntas

# Acoplamiento: dependencia de las funciones entre si, una funcion depende de otra para funcionar bien

# lo mejor en el codigo es que haya alta cohesion y bajo acoplamiento 



lista_1 = [14, 99, 8, 15, 17, 33, 19, 24, 12, 10]
lista_2 = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_3 = [13, 95, 7, 12, 17, 33, 14, 21, 11, 19]


def calcular_media_geo(lista):

    #"Calcula la enesima raiz del producto de todos los valores de la lista"
    producto = 1
    for numero in lista:
        producto *= numero

    resultado = producto ** (1 / len(lista))
    print(resultado)  # retorno de la funcion

calcular_media_geo(lista_1)
calcular_media_geo(lista_2)
calcular_media_geo(lista_3)


# MODULOS Y PAQUETES
'''
Modularizar : agrupar funciones
Un modulo es un archivo que contiene definiciones de funciones, clases y variables
Tienen la extension .py
Ayudan a organizar y reutilizar codigo

Se crean las funciones en un archivo y en otro archivo (main.py) se importan esas 
funciones para ejecutar el codigo

### funciones.py

MATERIA = "Programacion 1"   # toda variable con mayuscula es una constante

def presentar_materia() -> None:  # None significa que la funcion no devuelve nada
    print(f"Bienvenidos a {MATERIA})

main.py

import funciones   # se importa el nombre del archivo donde se crearon las funciones
                    # el modulo se trae con la palabra reservada import
funciones.presentar_materia()  ###

Un paquete es una forma de organizar los modulos
Todo paquete tiene que tener un archivo __init__.py

Para comunicar dos modulos de un paquete se usa .(nombre del modulos)
Dentro de los paquetes hay modulos, y dentro de los modulos funciones

'''

# Bibliotecas 
# Como instalar y usar modulos de terceros

import pygame