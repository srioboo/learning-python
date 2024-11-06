class Persona:
    tipo = "humano"

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento_identidad = None

    def agregar_documento_identidad(self, documento_identidad):
        self.documento_identidad = documento_identidad
        print("Documento guardado")
    
    def ejecutar_accion(self):
        print("Haciendo algo")

class Deportista(Persona):
    
    def __init__(self, nombre, apellido, edad, deporte):
        # Persona.__init__(nombre, apellido, edad) # esto tambien es valido
        super().__init__(nombre, apellido, edad)
        self.deporte = deporte
        
    def ejecutar_accion(self):
        super().ejecutar_accion()
        print(f"Practicando {self.deporte}")

class Ciclista(Deportista):

    def __init__(self, nombre, apellido, edad):
        self.deporte = "ciclismo"
        super().__init__(nombre, apellido, edad, self.deporte)

    def pedalear(self):
        print("Pedaleando")

nairo = Ciclista(nombre="Nairo", apellido="Quintana", edad=33)
nairo.ejecutar_accion()