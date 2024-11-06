import time

def medir_tiempo_ejecucion(funcion):

    def wrapper(*arg, **kwargs):
        inicio = time.time()
        funcion(*arg, **kwargs)
        fin = time.time()
        print(f"tiempo total de ejecucion: {fin-inicio}")

    return wrapper

@medir_tiempo_ejecucion
def recorrer_ciclo(rango):
    for i in range(rango):
        print(i)
        time.sleep(1)


recorrer_ciclo(rango=5)