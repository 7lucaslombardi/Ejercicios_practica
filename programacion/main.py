'''
1- Crear una función que muestre por pantalla el número que recibe como parámetro.
2- Crear una función que permita determinar si un número es par o no. La función retorna
“True” en caso afirmativo y “False” en caso contrario. Probar en el programa principal
realizando la invocación o llamada.
3- Especializar la función del punto 1 para que valide el número en un rango determinado
pasado por parámetro “desde”-“hasta”.
4- Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en
sus 4 combinaciones.
restar1(int, int)->int:
restar2()->int:
restar3(int, int):
restar4():
'''

from paquete_ej import *



mostrar_num ()

definir_par_impar (6)
definir_par_impar (7)

print(restar_1 (20,5))
print(restar_2 ())
restar_3 (50,40)
restar_4 ()

'''
5- Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario,
valide el mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una
función llamada realizarDescuento(). Mostrar el resultado por pantalla. Atención: pueden
reutilizarse funciones ya creadas.
'''

numero_1 = int(input("Ingrese un valor: "))
while (numero_1  < 10 or numero_1  > 100):
    print("Valor incorrecto")
    numero_1 = int(input("Ingrese un valor: "))

print(f"El valor con descuento es: {realizar_descuento (numero_1)}")


'''
6- Realizar un programa que: asigne a las variables numero1 y numero2 los valores
solicitados al usuario, valide los mismos entre 10 y 100, asigne a la variable operacion el
valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice la operación de dichos valores
a través de una función. Mostrar el resultado por pantalla
'''

numero_2 = int(input("Ingrese un valor: "))
while (numero_2 < 10 or numero_2 > 100):
    print("Valor incorrecto")
    numero_2= int(input("Ingrese un valor: "))

operacion = input("Ingrese la operacion a realizar 's' -sumar o 'r' -restar: ")
while (operacion != "s" and operacion != "r"):
    operacion = input("Ingrese la operacion a realizar 's' -sumar o 'r' -restar: ")

if operacion == "s":
    print(f"La suma es: {realizar_suma(numero_1,numero_2)}")
else:
    print(f"La resta es: {realizar_resta(numero_1,numero_2)}")