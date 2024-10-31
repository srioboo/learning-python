class Mutante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")


paco = Mutante(nombre = "Paco", edad = 20)

paco.cumplir_anios()