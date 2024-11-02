"""
lista = [ epsresion(elemento) for elementoo in objeto_iterable ]
"""

def calcular_cuadrado(numero):
    return numero**2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print("Bucle for", lista_cuadrados)

lista_comprehension = [num**2 for num in lista_num]
print("List comprehension", lista_comprehension)


lista_comprehension_alt = [calcular_cuadrado(num) for num in lista_num]
print("List comprehension alt", lista_comprehension_alt)