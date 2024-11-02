import csv
import os

ruta = "csv_vacio.csv"
ruta_absoluta = os.path.join(os.getcwd(), "csv_vacio.csv")
print(ruta_absoluta)

archivo_abierto = open(ruta, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()