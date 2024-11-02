lista_numeros = [1,2,3,4,5,6,7,8]

lista_pares = lambda numero: numero % 2 == 0
print(lista_pares(2))

lista_pares_filter = list(filter(lambda numero: numero % 2 == 0, lista_numeros))
print(lista_pares_filter)


nueva_lista = list(map(lambda numero: numero*10, lista_numeros))
print(nueva_lista)
