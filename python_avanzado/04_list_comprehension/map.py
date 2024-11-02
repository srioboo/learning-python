def calcular_cuadrado(numero):
    return numero**2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)

map_cuadrados = map(calcular_cuadrado, lista_num)
print(list(map_cuadrados))
