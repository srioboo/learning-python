def calcular_area_cuadrado(lado):
    return lado ** 2

# esta funcion se puede escribir como una lambda

calcular_cuadrado = lambda lado: lado ** 2
print(calcular_cuadrado(2))
print(calcular_cuadrado(5))