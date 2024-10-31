lenguajes = {
    "nombre": "python",
    "autor": "Guido"
}

for key in lenguajes:
    print("key", key)
    print("value", lenguajes[key])


for element in lenguajes.keys():
    print("index", element)

for element in lenguajes.values():
    print("index", element)

for llave, valor in lenguajes.items():
    print("key/value", llave, valor)