'''
Ejercicio 7:
Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
productos con impuestos para una determinada empresa:
La respuesta de chatgpt es:
def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
resultado_exportaciones = valor_exportaciones* (1- (retenciones / 100))
resultado_final = resultado_nacional + resultado_exportaciones
return resultado_final
¿Considera que cumple con los objetivos de una función?
Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
documente y denomine correctamente
'''

from paquete_ej import *


print(calcular_exportaciones(1000))
print(calcular_nacional(500))
print(sumar(1000, 500))

'''
Ejercicio 8:
Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
equipo de recursos humanos de la empresa.
En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.
También debe haber una segunda función que calcule la productividad del empleado. 
La misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo.
En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad.
'''

total_salario = calcular_salario(1000)
total_productividad = calcular_productividad(500, 1000)

print(mostrar_datos("lucas" , 22 , total_salario, total_productividad))