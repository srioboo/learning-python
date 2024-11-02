import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Pedro", "Ri", 26]

datos_lista = [
    ["Paco", "Botero", 24],
    ["Javi", "Otro", 34],
    ["Koji", "Kabuto", 54]
]
datos_dict = [
    {"nombre": "Koji", "apellido": "Kabuto", "edad": 30},
    {"nombre": "Sayaka", "apellido": "Yumi", "edad": 29}
]

with open("datos.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    writer.writerow(columnas)
    writer.writerows(datos_lista)

with open("datos2.csv", "w", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dict)
