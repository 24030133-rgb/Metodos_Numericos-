# Método de Newton-Raphson

## Presentación
El método de Newton-Raphson es un algoritmo iterativo 
para encontrar raíces de ecuaciones no lineales.
Parte de una aproximación inicial y usa la derivada 
de la función para converger rápidamente a la raíz.

## Fórmula
x(n+1) = x(n) - f(x(n)) / f'(x(n))

Donde:
x(n)   = aproximación actual
f(x)   = función original
f'(x)  = derivada de la función

## Algoritmo
1. Definir f(x) y su derivada f'(x)
2. Elegir una aproximación inicial x0
3. Calcular x1 = x0 - f(x0) / f'(x0)
4. Repetir hasta que |x(n+1) - x(n)| < tolerancia
5. Retornar la raíz aproximada

## Ejemplo
f(x) = x² - 2
f'(x) = 2x
x0 = 1.0
Raíz aproximada: 1.41421356... (√2)

## Caso de prueba
Entrada: f(x) = x² - 2, x0 = 1.0, tolerancia = 1e-6
Resultado esperado: 1.4142135623730951

## Ejercicio
Encontrar la raíz de f(x) = x³ - x - 2
usando Newton-Raphson con x0 = 1.5
y tolerancia de 1e-6
