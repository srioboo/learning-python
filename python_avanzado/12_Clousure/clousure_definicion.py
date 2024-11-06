# Scope global
fecha = "01-01-2000"

def funcion_scope_local():
    # scope local
    nombre = "Salva"
    return nombre

def funcion_principal():

    nombre = "Salva"

    def funcion_anidada():
        print(nombre)

    funcion_anidada()

funcion_principal()

"""
Esto es un clousure, dado que cumple los requisitos
1. tiene una funcion anidada
2. la funcion anidada usa una variable exterior a ella
3. la funcion devuelve la función anidada
"""
def saludar():

    mensaje = "Buen día"

    def imprimir_saludo():
        print(mensaje)

    return imprimir_saludo

saludo = saludar()
saludo()