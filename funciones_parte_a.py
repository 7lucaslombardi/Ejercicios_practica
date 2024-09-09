#1
def mostrar_num (numero: int=7):
    print(f"El numero es: {numero}")

#2
def definir_par_impar (numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)

#4
def restar_1 (numero_1, numero_2 ) -> int:
    
    diferencia = numero_1 - numero_2
    return diferencia

def restar_2 () -> int:
    numero_1 = 10
    numero_2 = 5
    diferencia = numero_1 - numero_2
    return diferencia

def restar_3 (numero_1 , numero_2):
    
    print(f"El resultado de la resta es {numero_1 - numero_2}")

def restar_4 ():
    numero_3 = 20
    numero_4 = 10
    print(f"El resultado es {numero_3 - numero_4}")

#5
def realizar_descuento (numero_1):
    resultado = numero_1 - (numero_1 * 0.05) 
    return resultado

#6

def realizar_suma (numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado

def realizar_resta (numero_1, numero_2):
    resultado = numero_1 - numero_2
    return resultado