# listas, son ordenadas
lenguajes = ["python", "java", "goland"]

print(lenguajes)

lista = [1, 2.0, 'python', 1]

print(lista)

print(lista[0])

print(len(lista))

print(lenguajes[2])

# lista inversa
print(lenguajes[-1])
print(lenguajes[-3])

# rango
print(lenguajes[0:2])

# lista anidades
programacion = [lenguajes, "dedicacion", "practiva"]
print(programacion)

print(programacion[0][0])


# listas son mutables
lenguajes[0] = "dart"
print(lenguajes)

# append
lenguajes.append("python")
print(lenguajes)

# extends une dos listas
otros_lenguajes = ["c", "c++"]

lenguajes.extend(otros_lenguajes)
print(lenguajes)

lenguajes.append(otros_lenguajes)
print(lenguajes)

# Tuplas son inmutables
tLenguage = ("python", "c", "c++") # tambien -> tLenguage = "python", "c", "c++"
print(tLenguage)

print(tLenguage[0])

# Diccionarios o hasmap o mapas o json
dlenguajes = {
    "nombre": "python",
    "creador": "Guido"
}

print(dlenguajes)
print(dlenguajes["nombre"])
dlenguajes["anio_lanzamiento"] = 1991
print(dlenguajes)

dlenguajes["caracteristicas"] = ["sencillo", "facil", "genial"]
print(dlenguajes)

print(dlenguajes.items())
print(dlenguajes.keys())
print(dlenguajes.values())

# Set, no se pueden accedier por indices y son unicos
set1 = {1, 2, 3}
print(set1)
set2 = {1, 1, 1}
print(set2)

set3 = {1, 2.0,"texto"}
print(set3)

set3.add(4)
print(set3)

set1.update([4,5,6])
print(set1)

print(len(set1))

set1.discard(2)
print(set1)

set1.remove(3) # si no existe da error
print(set1)

set1.clear() # esto vacia el set
print(set1)