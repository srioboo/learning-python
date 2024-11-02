def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["appellido"])

funcion_kwargs(nombre="Paco", appellido="Botero")