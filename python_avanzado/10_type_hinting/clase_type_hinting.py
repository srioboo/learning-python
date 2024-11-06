class Persona:

    def __init__(self, nombre: str, position: int) -> None:
        self.nombre = nombre
        self.posicion = posicion

    def caminar(self, distacia_km: int) -> int:
        self.posicion += distacia_km
        return self.posicion
    
paco = Persona(nombre="Paco", posicion=0)
posicion_paco = paco.caminar(distacia_km=6)