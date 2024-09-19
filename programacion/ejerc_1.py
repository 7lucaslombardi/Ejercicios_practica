'''
Supongamos que está trabajando en desarrollar el programa de carga de una encuesta.
1- Pedir al usuario que ingrese nombre y apellido del encuestado, guardarlo como string.
2- Pedir al usuario que ingrese el salario mensual del encuestado y guardarla como entero.
3- Pedir al usuario que ingrese la cantidad de horas trabajadas en la semana anterior por el
encuestado y guardarlo como entero. Validar que sea un valor entre 0 y 120
4- Calcular el ingreso horario del encuestado (ingreso dividido por horas trabajadas) y
generar una respuesta por pantalla con todos los datos ingresados para verificar que estén
bien cargados.
5- Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que más gana.
b) Calcular el promedio de ingresos/hora de todos los respondentes.
c) Buscar cuál es el valor que más se repite.
d) Calcular la media geométrica
6- Suponiendo que tenemos dos listas en las cuales la posición es la misma en ambas para
cada respondente:
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan”, “Matias”, “Carla”, “Susana”, “Olivia”, “Carlos”, “Daniel”, “Jimena”,
“Mariela”, “Ignacio”]
a) Devolver el nombre del respondiente más jóven y del más grande.
b) Genere dos nuevos listado por sexo y calcule la media etaria para varones y mujeres
c) Utilizando continue, calcule la media etaria para mayores de 40 años
'''



nombre = input("Ingrese nombre y apellido: ")
salario = int(input("Ingrese salario mensual: "))

horas_trabajadas = int(input("Ingrese cant de horas trabajadas: "))
while (horas_trabajadas < 0 or horas_trabajadas > 120):
        print("Incorrecto")
        horas_trabajadas = int(input("Ingrese cant de horas trabajadas: "))

ingreso = salario / horas_trabajadas

mensaje = \
f'''
Nombre: {nombre}
Salario mensual: {salario}
Cant. horas: {horas_trabajadas}
Ingreso: {ingreso}
'''
print(mensaje)

lista = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

#B
suma_ingresos = 0
for ingreso in lista:
    suma_ingresos += ingreso

total_ingresos = len(lista)

promedio_ingresos = suma_ingresos / total_ingresos
print(f"El promedio de ingresos es:  {promedio_ingresos}")

#C
'''valor = lista[0]
max_num_repetido = 0

for num in range(len(lista)):
    valor_actual = lista[num]
    valor_repetido = 0

    for num_1 in range(len(lista)):
        if lista[num_1] == valor_actual:
            valor_repetido += 1

    if valor_repetido > max_num_repetido:
        max_num_repetido = valor_repetido
        valor = valor_actual

print(f"El valor que más se repite es: {valor} 
(se repite {max_num_repetido} veces)")'''

#6
#A

lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]

lista_nombres = ["Juan" , "Matias", "Carla", "Susana", "Olivia", "Carlos", 
                "Daniel", "Jimena", "Mariela", "Ignacio"]

bandera = True

for index in range (len(lista_edad)):
    if bandera == True:
        nombre_max = lista_nombres[index]
        edad_max = lista_edad[index]
        nombre_min = lista_nombres[index]
        edad_min = lista_edad[index]
        bandera = False
    
    else:
        
        if lista_edad[index] > edad_max:
            nombre_max = lista_nombres[index]
            edad_max = lista_nombres[index]

        elif lista_edad[index] < edad_min:
            edad_min = lista_edad[index]
            nombre_min = lista_edad[index]

print(f"La edad minima es {edad_min} y corresponde a {nombre_min}")
print(f"La edad maxima es {edad_max} y corresponde a {nombre_max}")

#C
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]

contador = 0
suma_edades = 0

for edad in lista_edad:
    if lista_edad[edad] > 40:
        continue

    else:
        contador += 1
        suma_edades += lista_edad[edad]

print(suma_edades / contador)


'''7- Dada la siguiente lista:
lista_numeros = [14, 99, 8, 15, 17, 33, 19, 24, 12, 10]
a) Contar cuántos son múltiplos de 5
b) mostrar sólo los números pares'''

lista_numeros = [14, 99, 8, 15, 17, 33, 19, 24, 12, 10]

multiplos_cinco = 0

for numero in lista_numeros:
    if numero % 5 == 0:
        multiplos_cinco += 1
    if numero % 2 == 0:
        











#maximo_1 = ingresos[0]
#for numero in ingresos:
#   if numero > maximo_1:
#      maximo_1 = numero
#maximo_2 = ingresos[0]
#for numero in ingresos:
#   if numero == maximo_1:
#      continue
#   if numero > maximo_2:
#      maximo_2 = numero