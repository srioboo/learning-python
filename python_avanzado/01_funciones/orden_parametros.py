# se debe matener el orden de los parametros

def parametros_ordenados(nombre, apellidos, *args, **kwargs):
    pass

# esta está mal dado que los args van antes qeu los kwargs
# def parametros_desordenados(nobre, apelido, **kwargs, *args):
#    pass