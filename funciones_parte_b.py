def calcular_exportaciones (valor_exportaciones):
    retenciones = 15
    resultado_exportaciones = valor_exportaciones * (1- (retenciones / 100))
    return resultado_exportaciones

def calcular_nacional (valor_ventas_nacionales):
    iva = 21
    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    return resultado_nacional

def sumar(valor_exportaciones, valor_ventas_nacionales):
    resultado_1 = calcular_exportaciones(valor_exportaciones)
    resultado_2 = calcular_nacional(valor_ventas_nacionales)
    return resultado_1 + resultado_2