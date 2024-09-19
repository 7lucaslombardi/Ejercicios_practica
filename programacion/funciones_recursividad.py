def calcular_factorial_r (n : int) -> int:

    if n > 0:
        resultado = n * calcular_factorial_r (n - 1)
        return resultado
    else:
        return 1
    
print(calcular_factorial_r(4))


def contar_regresivamente (n : int):
    
    if n > 0:
        print(n)
        contar_regresivamente(n- 1)

    else:
        print("cero pa")

contar_regresivamente(10)

# la recursividad si recibe como parametro 0, 
# por defecto funciona hasta 996 veces.

# Fibonacci ejemplo: suma de los dos numeros anteriores en la sucesion

def calcular_fibonacci (n : int) -> int:

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return calcular_fibonacci (n-1) + calcular_fibonacci (n-2)
    
print(calcular_fibonacci(10))  # muestra la posicion de la sucesion de fibonacci
