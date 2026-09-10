def calcular_total_compra(precio_unitario: float, cantidad: int) -> float:
    """
    Calcula el total a pagar por la compra de un producto.
    
    Parámetros:
        precio_unitario (float): El costo de una sola unidad del producto.
        cantidad (int): El número de unidades adquiridas.
        
    Retorna:
        float: El monto total a pagar.
    """
    monto_total = precio_unitario * cantidad
    return monto_total


if __name__ == "__main__":
    # Datos de prueba
    precio_producto = 12.50
    cantidad_comprada = 4

    # Llamada a la función
    total_pagar = calcular_total_compra(precio_producto, cantidad_comprada)

    # Impresión del resultado
    print("--- RESUMEN DE COMPRA ---")
    print(f"Precio por unidad: ${precio_producto:.2f}")
    print(f"Cantidad: {cantidad_comprada}")
    print(f"Total a pagar: ${total_pagar:.2f}")