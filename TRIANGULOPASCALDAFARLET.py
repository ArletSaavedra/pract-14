print("DAFNE ALISON BENITEZ ROJAS Y ARLET GUADALUPE SAAVEDRA GARCIA")
def generar_triangulo_pascal(filas):
    # Crear una lista vacía para almacenar el triángulo
    tri_pascal = []

    for n in range(filas):
        # Crear una fila con los valores iniciales (todos son 1)
        fila = [1] * (n + 1)

        # Rellenar la fila con los valores correspondientes a la fórmula
        for i in range(1, n):
            fila[i] = tri_pascal[n - 1][i - 1] + tri_pascal[n - 1][i]

        # Añadir la fila al triángulo
        tri_pascal.append(fila)

    # Imprimir el Triángulo de Pascal
    for fila in tri_pascal:
        print(" ".join(map(str, fila)).center(filas * 2))

# Solicitar al usuario la cantidad de filas
filas = int(input("Introduce el número de filas para el Triángulo de Pascal: "))
generar_triangulo_pascal(filas)
