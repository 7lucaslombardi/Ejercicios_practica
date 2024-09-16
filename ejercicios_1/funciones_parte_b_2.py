def calcular_salario(numero_1):
    resultado_salario = (numero_1 * 10) + (numero_1 + (numero_1 * 0.03))
    return resultado_salario

def calcular_productividad (numero_2, numero_1) :
    resultado_productividad = numero_2 / numero_1
    return resultado_productividad

def mostrar_datos (numero_1, numero_2, nombre: str, edad: int):
    print(nombre)
    print(edad)
    resultado_1 = calcular_salario(numero_1)
    resultado_2 = calcular_productividad (numero_2, numero_1)
    return resultado_1 + resultado_2

