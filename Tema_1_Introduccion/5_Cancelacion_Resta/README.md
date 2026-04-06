# Cancelación por Resta (Loss of Significance)

## Presentación
Ocurre cuando se restan dos números muy cercanos entre sí.
Los dígitos significativos se cancelan y el resultado 
pierde precisión, amplificando el error relativo.

## Fórmula
Si a ≈ b, entonces a - b pierde dígitos significativos.
Solución: reformular la expresión algebraicamente para evitar la resta.

Ejemplo algebraico:
x = (-b + sqrt(b²- 4ac)) / 2a  →  puede cancelarse
x = -2c / (b + sqrt(b²- 4ac))  →  forma estable

## Algoritmo
1. Tomar dos números muy cercanos
2. Restarlos con float
3. Observar la pérdida de dígitos significativos
4. Aplicar reformulación algebraica
5. Comparar resultados

## Ejemplo
a = 1234567890.1234567
b = 1234567890.1234560
a - b debería ser 0.0000007 pero float pierde precisión

## Caso de prueba
Entrada: a = 1234567890.1234567, b = 1234567890.1234560
Resultado float:   puede dar 0.0 o valor incorrecto
Resultado Decimal: 0.0000007 exacto

## Ejercicio
Calcular las raíces de x² - 10000x + 1 = 0
usando la fórmula normal y la fórmula estable,
comparar los errores obtenidos
