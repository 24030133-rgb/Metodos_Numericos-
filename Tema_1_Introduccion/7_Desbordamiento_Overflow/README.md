# Desbordamiento (Overflow) en Punto Flotante

## Presentación
El overflow ocurre cuando un número excede el valor máximo 
representable por un tipo de dato. En Python el resultado 
es `inf` (infinito), lo que puede propagar errores 
en cálculos posteriores.

## Fórmula
Rango máximo float64: ±1.7976931348623157 × 10^308
Si resultado > máximo → inf
Si resultado < mínimo → -inf

## Algoritmo
1. Definir un número muy grande
2. Realizar operaciones que lo hagan crecer
3. Observar cuando se convierte en inf
4. Detectar y manejar el overflow

## Ejemplo
1.8e308 → inf (excede el máximo de float64)
1.8e308 * 2 → inf

## Caso de prueba
Entrada: 1.8e308
Resultado: inf
¿Es infinito? True

## Ejercicio
Encontrar el punto exacto donde ocurre el overflow
multiplicando progresivamente un número grande
y detectar en qué iteración se convierte en inf
