# Funcion
def funcion(param1, param2):
    return param1 + param2

# Funciones de primerar  clase
def funcion_primera_clase():
    return

variable = funcion_primera_clase
variable()

# funciones anidadas
def funcion_principal():

    nombre = "Ana"

    def funcion_anidada():
        print(nombre)
    
    funcion_anidada()

# funcion de orden superior
def saludar():
    mensaje = "Buen dia"

    def imprimir_saludo():
        print(mensaje)

    return imprimir_saludo