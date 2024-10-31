def calcular_promedio(lista):
    assert len(lista) > 0, "la lista está vacia"
    return sum(lista) / len(lista)

try:
    promedio = calcular_promedio(lista = [1, 2, 3])
    print(promedio)
except:
    print("La funcion no calculo el promedio")

try:
    promedio = calcular_promedio(lista = [])
    print(promedio)
except:
    print("La funcion no calculo el promedio")

try:
    promedio = calcular_promedio(lista = [])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("La funcion no calculo el promedio")
    print(e)