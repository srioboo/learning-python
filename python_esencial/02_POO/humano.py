class Humano:
    atributo = 123

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

paco = Humano("Paco", 20)
print(paco.nombre)
print(paco.edad)

print(paco.atributo)