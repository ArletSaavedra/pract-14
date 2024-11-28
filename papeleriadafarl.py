print("Hecho por: Dafne Alison Benitez Rojas, Arlet Guadalupe Saaverdra Garcia ")
print("Dada la aplicación básica de un menú (“Papelería”) con la estructura while")

# Base de datos de productos de papelería con 3 características adicionales
papeleria = {
    "101": {"Producto": "Cuaderno", "Marca": "Moleskine", "Tipo": "Rayado", "Color": "Negro", "Tamaño": "A5", "Precio": "$12.99", "Material": "Papel", "Stock": 100, "Fecha de entrada": "2024-11-01"},
    "102": {"Producto": "Bolígrafo", "Marca": "Pilot", "Tipo": "Gel", "Color": "Azul", "Tamaño": "0.7mm", "Precio": "$1.49", "Material": "Plástico", "Stock": 200, "Fecha de entrada": "2024-10-15"},
    "103": {"Producto": "Lápiz", "Marca": "Faber-Castell", "Tipo": "HB", "Color": "Amarillo", "Tamaño": "Largo", "Precio": "$0.99", "Material": "Madera", "Stock": 150, "Fecha de entrada": "2024-11-10"},
    "104": {"Producto": "Resaltador", "Marca": "Sharpie", "Tipo": "Fluorescente", "Color": "Amarillo", "Tamaño": "1.0mm", "Precio": "$2.50", "Material": "Plástico", "Stock": 120, "Fecha de entrada": "2024-11-05"},
    "105": {"Producto": "Regla", "Marca": "Staedtler", "Tipo": "Plástico", "Color": "Transparente", "Tamaño": "30 cm", "Precio": "$3.00", "Material": "Plástico", "Stock": 180, "Fecha de entrada": "2024-11-12"},
    "106": {"Producto": "Tijeras", "Marca": "Fiskars", "Tipo": "Papel", "Color": "Naranja", "Tamaño": "15 cm", "Precio": "$4.99", "Material": "Acero", "Stock": 80, "Fecha de entrada": "2024-09-20"},
    "107": {"Producto": "Carpeta", "Marca": "Oxford", "Tipo": "Vinilo", "Color": "Rojo", "Tamaño": "A4", "Precio": "$5.49", "Material": "Vinilo", "Stock": 140, "Fecha de entrada": "2024-10-30"},
    "108": {"Producto": "Pegamento", "Marca": "UHU", "Tipo": "Líquido", "Color": "Transparente", "Tamaño": "100 ml", "Precio": "$2.99", "Material": "Plástico", "Stock": 220, "Fecha de entrada": "2024-11-01"},
    "109": {"Producto": "Cartulina", "Marca": "Faber-Castell", "Tipo": "Multicolor", "Color": "Mixto", "Tamaño": "A4", "Precio": "$4.00", "Material": "Papel", "Stock": 150, "Fecha de entrada": "2024-11-15"},
    "110": {"Producto": "Borrador", "Marca": "Pelikan", "Tipo": "Goma", "Color": "Blanco", "Tamaño": "Normal", "Precio": "$0.79", "Material": "Goma", "Stock": 500, "Fecha de entrada": "2024-11-20"}
}

# Contraseña inicial
CONTRASEÑA = "1234"

# Validar contraseña con while
while True:
    intento = input("Introduce la contraseña: ")
    if intento == CONTRASEÑA:
        print("Contraseña correcta. Accediendo al sistema...")
        break  # Salir del ciclo while si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtalo nuevamente.")

# Funciones del menú
def mostrar_productos():
    if papeleria:
        print("\nLista de Productos de Papelería:")
        # Encabezado de la tabla
        encabezado = f"{'Producto':<15}{'Código':<10}{'Marca':<15}{'Tipo':<15}{'Color':<10}{'Tamaño':<10}{'Precio':<10}{'Material':<10}{'Stock':<10}{'Fecha de entrada':<15}"
        print(encabezado)
        print("-" * len(encabezado))  # Línea divisoria

        for codigo, detalles in papeleria.items():
            fila =  f"{detalles['Producto']:<15} " \
                    f"{codigo:<10} " \
                    f"{detalles['Marca']:<15} " \
                    f"{detalles['Tipo']:<15} " \
                    f"{detalles['Color']:<10} " \
                    f"{detalles['Tamaño']:<10} " \
                    f"{detalles['Precio']:<10} " \
                    f"{detalles['Material']:<10} " \
                    f"{detalles['Stock']:<10} " \
                    f"{detalles['Fecha de entrada']:<15}"
            print(fila)
    else:
        print("No hay productos en la base de datos.")

def agregar_producto():
    codigo = input("Código (3 dígitos): ")
    if codigo in papeleria:
        print("Este código ya existe.")
    else:
        producto = input("Producto: ")
        marca = input("Marca: ")
        tipo = input("Tipo: ")
        color = input("Color: ")
        tamaño = input("Tamaño: ")
        precio = input("Precio: ")
        material = input("Material: ")
        stock = int(input("Stock: "))
        fecha_entrada = input("Fecha de entrada (YYYY-MM-DD): ")
        papeleria[codigo] = {
            "Producto": producto,
            "Marca": marca,
            "Tipo": tipo,
            "Color": color,
            "Tamaño": tamaño,
            "Precio": precio,
            "Material": material,
            "Stock": stock,
            "Fecha de entrada": fecha_entrada
        }
        print(f"Producto {producto} agregado con éxito.")

def modificar_producto():
    codigo = input("Código del producto a modificar: ")
    if codigo in papeleria:
        producto = input("Nuevo Producto: ")
        marca = input("Nueva Marca: ")
        tipo = input("Nuevo Tipo: ")
        color = input("Nuevo Color: ")
        tamaño = input("Nuevo Tamaño: ")
        precio = input("Nuevo Precio: ")
        material = input("Nuevo Material: ")
        stock = int(input("Nuevo Stock: "))
        fecha_entrada = input("Nueva Fecha de entrada (YYYY-MM-DD): ")
        papeleria[codigo] = {
            "Producto": producto,
            "Marca": marca,
            "Tipo": tipo,
            "Color": color,
            "Tamaño": tamaño,
            "Precio": precio,
            "Material": material,
            "Stock": stock,
            "Fecha de entrada": fecha_entrada
        }
        print(f"Producto {producto} modificado con éxito.")
    else:
        print("Código no encontrado.")

def eliminar_producto():
    codigo = input("Código del producto a eliminar: ")
    if codigo in papeleria:
        eliminado = papeleria.pop(codigo)
        print(f"Producto {eliminado['Producto']} eliminado con éxito.")
    else:
        print("Código no encontrado.")

# Menú principal
while True:
    print("\nMenú de Papelería")
    print("1. Agregar = Insertar = Alta")
    print("2. Consulta = Mostrar")
    print("3. Modificar = Editar")
    print("4. Eliminar = Borrar")
    print("5. Salir del programa")

    opcion = input("Elige una opción (1/2/3/4/5): ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        modificar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")
