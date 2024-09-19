def calcular_salario(cant_horas_trabajadas: int):
    '''
    Calcula la cantidad de horas trabajadas
    Como parametro tiene cant_horas_trabajadas
    '''
    resultado_salario = (cant_horas_trabajadas * 10) + (cant_horas_trabajadas + (cant_horas_trabajadas * 0.03))
    return resultado_salario

def calcular_productividad (prod_empleado: float, cant_horas_trabajadas: int) -> float:
    '''
    Calcula la productividad 
    Como parametros tiene prod_empleado y cant_horas_trabajadas
    Devuelve un float
    '''
    resultado_productividad = prod_empleado / cant_horas_trabajadas
    return resultado_productividad

def mostrar_datos (resultado_salario : float, resultado_productividad : float, nombre: str, edad: int) -> None:
    '''
    Muestra los datos del empleado
    Como parametros tiene nombre, edad, resultado_salario y resultado_productividad
    '''
    print(nombre)
    print(edad)
    print(resultado_salario)
    print(resultado_productividad)

