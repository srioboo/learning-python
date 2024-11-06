class Persona:
    tipo = "humano"

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento_identidad = None

    def agregar_documento(self, documento_identidad):
        self.documento_identidad = documento_identidad
        print("Documento guardado")

salva = Persona("Salva", "Rio", 23)
print(salva.tipo)
salva.agregar_documento(12334)