

# DEFINICIÓN DE LA FUNCIÓN
def calcular_total_compra(precio_unitario, cantidad, porcentaje_descuento):
    """
    Calcula el valor total a pagar aplicando un descuento.
    Parámetros:
      - precio_unitario (float): Precio de cada producto.
      - cantidad (int): Cantidad de productos comprados.
      - porcentaje_descuento (float): Descuento en Porcentaje (ej. 10 para 10%).
    Retorno:
      - float: Total final a pagar.
    """
    subtotal = precio_unitario * cantidad
    descuento = subtotal * (porcentaje_descuento / 100)
    total_final = subtotal - descuento
    
    return total_final  # Retorno del valor


# PROGRAMA PRINCIPAL (Llamada a la función y muestra de resultados)
if __name__ == "__main__":
    print("SISTEMA DE CÁLCULO DE COMPRAS")
    
    # Datos de entrada del problema
    precio = 25.50     # Precio unitario en USD
    cant = 4           # Unidades compradas
    desc = 10.0        # 10% de descuento
    
    # LLAMADA A LA FUNCIÓN (Se pasan los parámetros de entrada)
    precio_final = calcular_total_compra(precio, cant, desc)
    
    # MOSTRAR EL RESULTADO EN PANTALLA
    print(f"Precio por unidad: ${precio:.2f}")
    print(f"Cantidad: {cant}")
    print(f"Descuento aplicado: {desc}%")
    print("-" * 35)
    print(f"Total a pagar final: ${precio_final:.2f}")