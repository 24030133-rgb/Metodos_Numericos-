# Método de Falsa Posición (Regula Falsi)

## Presentación
El método de Falsa Posición combina ideas de Bisección 
y la Secante. Usa una línea secante entre dos puntos 
del intervalo para estimar la raíz, convergiendo 
más rápido que Bisección.

## Fórmula
c = b - f(b) * (b - a) / (f(b) - f(a))

Donde:
a = extremo izquierdo del intervalo
b = extremo derecho del intervalo
c = aproximación de la raíz

## Algoritmo
1. Definir intervalo [a, b] donde f(a)*f(b) < 0
2. Calcular c = b - f(b) * (b - a) / (f(b) - f(a))
3. Si f(c) == 0 entonces c es la raíz
4. Si f(a)*f(c) < 0 entonces b = c
5. Si f(b)*f(c) < 0 entonces a = c
6. Repetir hasta que |f(c)| < tolerancia

## Ejemplo
f(x) = x² - 2
Intervalo [1, 2]
Raíz aproximada: 1.4142 (√2)

## Caso de prueba
Entrada: f(x) = x² - 2, a = 1, b = 2, tolerancia = 1e-6
Resultado esperado: 1.4142

## Ejercicio
Encontrar la raíz de f(x) = x³ - x - 2
en el intervalo [1, 2] con tolerancia 1e-6
