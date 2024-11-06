class AnimalAereo:

    def comer(self):
        print("Animal aéreo comiendo")

    def volar(self):
        print("Volando")

class AnimalTerrestre:

    def comer(self):
        print("Animal terrestre comiendo")

    def caminar(self):
        print("Caminando")

# class Pajaro(AnimalAereo, AnimalTerrestre):
#    pass

class Pajaro(AnimalTerrestre, AnimalAereo):
    pass

pato = Pajaro()
pato.volar()
pato.caminar()
pato.comer() # este método depende de la posicion de las clases
