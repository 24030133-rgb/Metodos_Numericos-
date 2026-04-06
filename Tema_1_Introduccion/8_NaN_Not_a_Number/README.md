# NaN (Not a Number)

## Presentación
NaN es un valor especial del estándar IEEE 754 que representa 
un resultado indefinido o imposible. Aparece cuando se realizan 
operaciones matemáticamente inválidas como raíz de negativo 
o división 0/0.

## Fórmula
Operaciones que generan NaN:
0.0 / 0.0     → NaN
sqrt(-1)      → NaN
inf - inf     → NaN
inf * 0       → NaN

## Algoritmo
1. Realizar una operación matemáticamente inválida
2. Observar el resultado NaN
3. Detectar NaN con math.isnan()
4. Manejar el error apropiadamente

## Ejemplo
import math
math.sqrt(-1) → NaN
float('nan') == float('nan') → False (NaN no es igual a nada)

## Caso de prueba
Entrada: math.sqrt(-1)
Resultado: nan
¿Es NaN? True

## Ejercicio
Generar NaN de tres formas diferentes,
detectarlos con isnan() y proponer
una solución para cada caso
