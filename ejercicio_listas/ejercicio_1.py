'''
1- Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que más gana. No es necesario
ordenar, se puede usar continue y resolver mediante programación estructurada
usando listas.
b) Calcular el promedio de ingresos/hora de todos los respondentes.
c) Buscar cuál es el valor que más se repite. En caso de ser varios, devolverlos todos.
d) Calcular la media geométrica. La media geométrica es la raíz de los productos.
e) Crear una función que permita recorrer las listas en ambos sentidos.
'''

lista = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]







#b
suma_ingresos = 0
for ingreso in lista:
    suma_ingresos += ingreso

total_ingresos = len(lista)

promedio_ingresos = suma_ingresos / total_ingresos
print(f"El promedio de ingresos es:  {promedio_ingresos}")