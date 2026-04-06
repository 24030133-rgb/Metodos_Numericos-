# Método de la Secante

## Presentación
El método de la Secante es similar a Newton-Raphson pero 
no requiere calcular la derivada. En su lugar usa dos 
aproximaciones iniciales para estimar la pendiente 
de la función y converger a la raíz.

## Fórmula
x(n+1) = x(n) - f(x(n)) * (x(n) - x(n-1)) / (f(x(n)) - f(x(n-1)))

Donde:
x(n)   = aproximación actual
x(n-1) = aproximación anterior
f(x)   = función evaluada

## Algoritmo
1. Definir f(x)
2. Elegir dos aproximaciones iniciales x0 y x1
3. Calcular x2 usando la fórmula de la secante
4. Repetir hasta que |x(n+1) - x(n)| < tolerancia
5. Retornar la raíz aproximada

## Ejemplo
f(x) = x² - 2
x0 = 1.0, x1 = 2.0
Raíz aproximada: 1.4142 (√2)

## Caso de prueba
Entrada: f(x) = x² - 2, x0 = 1.0, x1 = 2.0, tolerancia = 1e-6
Resultado esperado: 1.4142

## Ejercicio
Encontrar la raíz de f(x) = x³ - x - 2
usando x0 = 1.0, x1 = 2.0
y tolerancia de 1e-6
