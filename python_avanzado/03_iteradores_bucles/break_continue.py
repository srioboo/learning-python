nombres = ["Salva", "Pedro", "Carlos"]

for nombre in nombres:
    if nombre == "Pedro":
        break
    print(nombre)

for nombre in nombres:
    if nombre == "Pedro":
        continue # esto hace que se salte el elemento en cuestion
    print(nombre)