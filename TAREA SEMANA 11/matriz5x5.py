# 1. Declarar las dimensiones de la matriz
FILAS = 5
COLUMNAS = 5

# Crear la matriz de 5x5 inicializada en 0
matriz = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

print("INGRESE LOS DATOS EN LA MATRIZ (5x5) ")

# 2. Bucles anidados para solicitar y almacenar los 25 valores
for f in range(FILAS):
    for c in range(COLUMNAS):
        matriz[f][c] = int(input(f"Ingrese el valor para la posición [{f}][{c}]: "))

print("\nMATRIZ IMPRESA EN FORMA DE TABLA")

# 3. Bucles anidados para mostrar la matriz en formato de tabla
for f in range(FILAS):
    for c in range(COLUMNAS):
        # end="\t" tabulación para alinear las columnas
        print(matriz[f][c], end="\t")
    print() 