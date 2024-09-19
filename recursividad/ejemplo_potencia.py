def calcular_potencia (base : int , exponente : int) -> int:

    if exponente == 1:
        return base
    
    else:
        return base * calcular_potencia (base , exponente - 1)
    
print(calcular_potencia(4 , 3))

# se resuelve como 4**2 * 4**1 / 16 * 4 = 64