def calcular_area_cuadrado(lado):
    """Calcula el área del un cuadrado al recibir la longitud del lado"""
    area = lado*lado
    return area

lado_cuadrado = [1, 3, 4]
area_cuadrado = []
for lado in lado_cuadrado:
    area = calcular_area_cuadrado(lado)
    area_cuadrado.append(area)