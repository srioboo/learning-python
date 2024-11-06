import time

def medir_tiempo_ejecucion(funcion):

    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f"tiempo total de ejecucion: {fin-inicio}")

    return wrapper

@medir_tiempo_ejecucion
def recorrer_ciclo():
    for i in range(5):
        print(i)
        time.sleep(1)


recorrer_ciclo()