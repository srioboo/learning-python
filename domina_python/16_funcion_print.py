print("Cadena de texto")

variable = 1
print(f"Variable {variable}")

print("elementos", "separados", "por", "comas")

print("elementos", "separados", "por", "comas", sep=".")

print("elementos", "separados", "por", "comas", sep="\n")

print("Primero")
print("Segundo")
print("Primero", end=".")
print("Segundo")

with open("print_ejemplo.txt", "w") as archivo:
    print("hello world!", file=archivo)

import time
print("Inicio", flush=False)
time.sleep(2)
print("Fin")

print("Inicio", end="...", flush=False)
time.sleep(2)
print("Fin")

print("Inicio", end="...", flush=True)
time.sleep(2)
print("Fin")