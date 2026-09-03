# Programa para el sistema de reserva de asientos de cine
# Autor: Luis Guillermo Tenorio Rojas

def main():
    # 1. Crear una matriz de 3 filas por 4 columnas (lista de listas)
    # Todos los valores se inicializan en 0 (asiento libre)
    asientos = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    print("SISTEMA DE RESERVA DE ASIENTOS")
    
    # Bucle de validación para asegurar índices correctos
    while True:
        try:
            # Pedir fila y columna al usuario convirtiéndolos a entero
            fila = int(input("Ingrese fila (0 a 2): "))
            columna = int(input("Ingrese columna (0 a 3): "))

            # Validar que los valores ingresados estén dentro del rango permitido
            if 0 <= fila <= 2 and 0 <= columna <= 3:
                # Validar si el asiento ya está reservado
                if asientos[fila][columna] == 1:
                    print("\n[!] El asiento ya está reservado. Intente con otro.\n")
                else:
                    # Marcar el asiento como reservado con el valor 1
                    asientos[fila][columna] = 1
                    print(f"\n[✓] ¡Asiento [{fila}][{columna}] reservado con éxito!\n")
                    break
            else:
                print("\n[!] Error: Fila debe ser de 0 a 2 y Columna de 0 a 3.\n")
        except ValueError:
            print("\n[!] Error: Debe ingresar únicamente números enteros.\n")

    # 2. Mostrar la matriz completa en formato de tabla
    print("Estado de la sala:")
    
    # Bucle externo para recorrer las filas
    for i in range(3):
        # Bucle interno para recorrer las columnas de la fila actual
        for j in range(4):
            # Imprimir valor sin salto de línea y con un espacio de separación
            print(asientos[i][j], end=" ")
        # Salto de línea al terminar de imprimir cada fila
        print()

if __name__ == "__main__":
    main()