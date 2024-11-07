import subprocess

nombre_bash = "bash_ejemplo.sh"
contenido = ""

with open(nombre_bash, mode="rb") as archibo_bash:
    contenido = archibo_bash.read()

print(f"contenido del carchivo: {contenido}")
subprocess.call(contenido, shell=True)
