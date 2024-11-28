print("Hecho por arlet guadalupe saavedra garcia")
n = int(input("Ingrese un número mayor que 1: "))

a, b = 0, 1
contador = 1

while contador < n:
    a, b = b, a + b 
    contador+= 1

print(f"El {n}-ésimo número de Fibonacci es: {b}")