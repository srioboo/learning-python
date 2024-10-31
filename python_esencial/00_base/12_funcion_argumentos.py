APELLIDO = "Rio"

def perimetro_cuadrado(lado, unidades):
    perimetro = lado * 4
    print(f"Ep perimetro es {perimetro} {unidades}")


perimetro_cuadrado(4, "cm")

perimetro_cuadrado(lado=4, unidades="cm")


def perimetro_cuadrado(lado):
    """Calcular el perimetro del  un cuadrado - esta es la documentación en python"""
    perimetro = lado * 4
    return perimetro

def area_cuadrado(lado):
    """Calcular el area del  un cuadrado
    esta es la documentación en python
    es más larga

    Args:
        lado (int): medida del lado del cuadrado

    Returns:
        perimetro (int): perimetro del cuadrado
    """
    area = lado * lado
    return area

perimetro = perimetro_cuadrado(5)
area = area_cuadrado(5)

print(f"Area: {area}, perimetro: {perimetro}")



def calcular_cuadrado(lado):
    area = lado * lado
    perimetro = lado * 4
    return area, perimetro

area2, perimetro2 = calcular_cuadrado(6)
print(f"Area: {area2}, perimetro: {perimetro2}")

resultado = calcular_cuadrado(6)
print(resultado)
