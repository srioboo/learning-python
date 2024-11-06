import time

def medir_tiempo_ejecucion(funcion):

    def wrapper(*arg, **kwargs):
        inicio = time.time()
        funcion(*arg, **kwargs)
        fin = time.time()
        print(f"tiempo total de ejecucion: {fin-inicio}")

    return wrapper

def decorador_puntos(funcion):

    def wrapper(*args, **kwargs):
        print("...........")
        funcion(*args, **kwargs)
        print("...........")
    return wrapper

# el orden de los decoradores importa
@decorador_puntos
@medir_tiempo_ejecucion
def recorrer_ciclo(rango):
    for i in range(rango):
        print(i)
        time.sleep(1)


recorrer_ciclo(rango=5)