# Tarea Práctica: Definición y uso de funciones en Python

**Estudiante:** Luis Guillermo Tenorio Rojas  
**Fecha de entrega:** 13 de septiembre de 2026  

## Descripción del problema
El objetivo de este proyecto es resolver un caso práctico de la vida real mediante una función modularizada en Python. Se implementó un algoritmo que calcula el costo total a pagar en una tienda en función del precio unitario de un artículo y la cantidad de unidades adquiridas.

## Algoritmo en Pseudocódigo
```text
FUNCION calcularTotal(precio, cantidad)
    total <- precio * cantidad
    RETORNAR total
FIN FUNCION

INICIO
    precio <- 12.50
    cantidad <- 4
    resultado <- calcularTotal(precio, cantidad)
    IMPRIMIR resultado
FIN