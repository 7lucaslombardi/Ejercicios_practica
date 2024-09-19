def calcular_exportaciones (valor_exportaciones: float, retenciones: float = 15) -> float:
    '''
    Calcula el valor de las exportaciones con las retenciones
    Como parametros tiene valor_exportaciones y retenciones
    Devuelve un float
    '''

    resultado_exportaciones = valor_exportaciones * (1- (retenciones / 100))
    return resultado_exportaciones

def calcular_nacional (valor_ventas_nacionales: float, iva: float = 21 ) -> float:
    '''
    Calcula el valor de las ventas nacionales con el iva
    Como parametros tiene valor_ventas_nacionales e iva
    Devuelve un float
    '''
    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    return resultado_nacional

def sumar(resultado_exportaciones: float, resultado_nacional: float) -> float:
    '''
    Calcula la suma de los resultados de calcular_importaciones y calcular_nacional
    Como parametros tiene resultado_exportaciones y resultado_nacional
    Devuelve un float
    '''
    resultado_1 = resultado_exportaciones
    resultado_2 = resultado_nacional
    return resultado_1 + resultado_2