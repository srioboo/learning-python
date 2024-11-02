def calcular_perimetro(lado_1, lado_2, lado_3, lado_4):
    perimetro = lado_1 + lado_2 + lado_3 + lado_4
    return perimetro

perimetro = calcular_perimetro(1,2,3,4)
print(perimetro)

def calcular_perimetro2(*args):
    print(args)
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro = calcular_perimetro2(1,2,3,4)
print(perimetro)

triangulo = calcular_perimetro2(1,2,3)
print(triangulo)