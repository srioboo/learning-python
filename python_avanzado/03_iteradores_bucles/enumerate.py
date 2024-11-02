"""
enumerate(iterable, start=0)
"""

nombres = ["Salva", "Pedro", "Carlos", "Javier"]
nombres_enumerados = enumerate(nombres)
print(list(nombres_enumerados))

nombres_enumerados = enumerate(nombres, start=5)
print(list(nombres_enumerados))

for indice, elemento in enumerate(nombres):
    print(indice, elemento)

