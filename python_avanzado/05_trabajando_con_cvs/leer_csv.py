import csv

with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    next(reader) # esto salta la cabecera
    columnas = next(reader)
    print("Columnas", columnas)
    for fila in reader:
        print(fila)
        print(fila[0])

with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila)
        print(fila["nombre"])

