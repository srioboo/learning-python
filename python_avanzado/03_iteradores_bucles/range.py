"""
range(inicio, fin, paso)
"""

serie_1 = range(5) # esto inidca solo el fin
print(list(serie_1))

serie_2 = range(5,  10) # inicio y fin
print(list(serie_2))

serie_3 = range(1, 10, 2) # del 1 al 10 de dos en dos
print(list(serie_3))

for elemento in serie_3:
    print(elemento)