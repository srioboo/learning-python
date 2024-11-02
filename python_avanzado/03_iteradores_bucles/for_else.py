lista_nombres = ["Paco", "Salva", "Emilio", "Sandra"]

for nombre in lista_nombres:
    print(nombre)
else:
    print("Ciclo terminado") # se ejecuta al ternminar todos los elementos y no se rompe el ciclo

for nombre in lista_nombres:
    if nombre == "Salva":
        break
    print(nombre)
else:
    print("Ciclo terminado")