# recorrer todos los elementos de una matriz

matriz = [
    [12, 50, 67],
    [77, 77, 77, 77],
    [534, 96, 56, 66],
    [11, 22, 33, 44]
]

for i in range(len(matriz)):  # cantidad de vueltas segun elementos de la matriz (4)
    for j in range(len(matriz[i])): # cantidad de vuelta dentro de cada elemento madre de la matriz (4)
        print(matriz[i][j], end=" ") # imprime cada elemento de cada posicion con un espacio
    print("")  # se utiliza para dar un salto de linea luego de la vuelta de cada elemento madre de la matriz (4)

# i : representa cada elemento madre de la matriz [] (4)
# j : representa cada elemento dentro de cada elemento madre [[]] (4)

def inicializar_matriz (cant_filas : int, cant_columnas : int) -> list:
    matriz = []
    for _ in range(cant_filas):
        fila = [0] * cant_columnas
        matriz += [fila]
    return matriz

matriz_2x3 = inicializar_matriz(2, 3)
print(matriz_2x3)

def carga_secuencial (matriz : list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input("Ingrese un numero: "))
        return matriz

resultado = carga_secuencial(matriz_2x3)

for i in range(len(resultado)):
    for j in range(len(resultado[i])):
        print(resultado[i][j], " ")
    print("")





def buscar_valor (matriz : list, valor : int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor :
                print (f"El valor esta en la fila {i} y columna {j}")

encontrar_valor = buscar_valor(matriz, 3)
print(encontrar_valor)



