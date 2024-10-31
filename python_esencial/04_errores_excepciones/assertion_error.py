def calcular_promedio(lista):
    assert len(lista) > 0, "la lista está vacia"
    return sum(lista) / len(lista)

promedio = calcular_promedio(lista=[1, 3 , 5])
print(promedio)

promedio = calcular_promedio(lista=[])
print(promedio)