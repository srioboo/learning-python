import os

def listar_archivos(ruta):
    lista_archivos = os.listdir(ruta)
    return lista_archivos

ruta_absoluta = os.getcwd()
ruta_relativa = "domina_python/"
archivos = listar_archivos(ruta_absoluta)
# archivos = listar_archivos(ruta_relativa)
print(archivos)

