# 1. Crear el arreglo (lista)
numeros = [10, 20, 30, 40, 50]

# 2. Mostrar el valor en la posición 1 (en Python los índices empiezan en 0, por lo que el índice 1 es el valor 20)
print("Valor en la posición 1:", numeros[1])

# 3. Recorrer el arreglo e imprimir todos los elementos
print("\nRecorrido de todo el arreglo:")
for i, numero in enumerate(numeros):
    print(f"Índice {i}: {numero}")