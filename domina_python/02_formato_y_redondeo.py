formateo = "{:.0f}".format(2.4) # formatear 2.4 a texto sin decimales

print(formateo, type(formateo))
print("============")

formateo = "{:.2f}".format(2.8) # formatear 2.8 a texto pasando dos decimales
print(formateo, type(formateo))
print("============")

formateo = "{:.2f}".format(2.888) # formatear 2.867 a texto pasando dos decimales redondeara los decimales a dos
print(formateo, type(formateo))
print("============")

formateo = "{:0>5}".format(2.5) # formatear 2.5 relleando con 0 hasta 5 caracteres
print(formateo, type(formateo))
print("============")

formateo = "{:0<5}".format(2.5) # formatear 2.5 relleando con 0 hasta 5 caracteres a la inversa
print(formateo, type(formateo))
print("============")

formateo = "{:,}".format(1000000)  # agrregar la separacion de millares con coma
print(formateo, type(formateo))
print("============")

formateo = f"{2.5:.2f}" # otra forma de formateo
print(formateo, type(formateo))
print("============")