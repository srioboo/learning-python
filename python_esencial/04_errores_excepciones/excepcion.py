def validar_x(x):
    if x < 1:
        raise Exception("la variable x debe ser mayor a 1")
    else:
        print("x es mayor a 1")

x = 0.3
validar_x(x)