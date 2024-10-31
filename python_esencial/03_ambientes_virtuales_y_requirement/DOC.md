# Ambientes o workspace virtual

1. Virtualenv
2. Venv
3. Anaconda

Para crear un ambiente con virtualenv

```shell
virtualenv nombre_ambiente # esto crea una carpeta nombre_ambiente
```

Para activar el ambiente podemos usar

```shell
source nombre_ambiente/bin/activate

# si el workspace (ambiente) se llama "env"
source env/bin/activate

# para salir del ambiente, usar dentro del ambiente
deactivate
```

Para borrar el ambiente simplemente borrar la carpeta del ambiente creado

## Archivo de requerimientos

Se crea un archivo requirement.txt, aunque se puede nombrar de otra forma de ser necesario

Para instalar las librerías de requerimientos se usa

```shell
pip install -r requirement.txt
```
