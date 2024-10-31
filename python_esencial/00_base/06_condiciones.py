# if
a = 3
b = 1

if a < b:
    print("a es menor que")
elif a == b:
    print("a es igual a b")
else:
    print("a es mayor que")

c = True

if c:
    print("c es verdadero")
else:
    print("c es falso")

if type(c) is bool:
    print("c es booleano")
else:
    print("c es de otro tipo")

d = 10
e = 5
f = 1

if d>e and e>f:
    print("las dos condiciones son verdaderas")

if d>e or e>f:
    print("las dos condiciones son verdaderas")