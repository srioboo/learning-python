nombres = ["Salva", "Pedro", "Carlos"]
apellidos = ["Rio", "Nar", "Re"]

 # combina en sus restectivas posiciones, solo usa la lista de menos elementos
nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo)

# unzip, crea dos listas
nombres_unzip, appellidos_unzip = zip(*nombre_completo)

print(nombres_unzip)
print(appellidos_unzip)

for nombre, appellidos in zip(nombres, apellidos):
    print(nombre, apellidos)