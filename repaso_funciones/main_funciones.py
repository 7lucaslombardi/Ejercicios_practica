'''
Repaso funciones
1- Elabore un módulo que contenga 3 funciones:
a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.
c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.
3- generar paquete.
4- subir a github.
Recursividad
1- Calcular mediante recursividad la potencia de un número, mediante una función que
recibe un número base de tipo entero y un exponente de tipo entero. Utilizar parámetros
opcionales para definir que si la función no recibe ningún parámetro devolverá 2 al
cuadrado.
2- Resolver mediante recursividad el problema de las torres de Hanoi
https://www.youtube.com/watch?v=vrXue8Lq1Ow
No utilizar listas, la función solo debe devolver un print con los movimientos.
'''


from geometria import *


print(calcular_area_circulo(3.14, 10))
print(calcular_area_cuadrado(5))
print(calcular_area_triangulo())


print(calcular_perimetro_circulo(10))
print(calcular_perimetro_cuadrado(5))
print(calcular_perimetro_triangulo(3, 5, 7))






