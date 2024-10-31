
for letra in "Texto":
    print(letra)


lenguajes = ["python", "java", "golang"]
for elemento in lenguajes:
    print(elemento)


for elemento in lenguajes:
    print(elemento)
    if elemento == "java":
        break

for elemento in lenguajes:
    if elemento == "java":
        continue
    print(elemento)

for element in range(5):
    print(element)

for element in range(5, 15):
    print(element)