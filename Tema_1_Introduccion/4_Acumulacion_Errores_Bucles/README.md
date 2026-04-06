# Acumulación de Errores en Bucles

## Presentación
Cuando se suma un número de punto flotante muchas veces 
en un bucle, los pequeños errores de redondeo se van 
acumulando hasta generar un error significativo en el resultado final.

## Fórmula
Error acumulado = Resultado_float - Resultado_esperado
Solución: usar Decimal para alta precisión

## Algoritmo
1. Definir un incremento y número de iteraciones
2. Sumar el incremento repetidamente con float
3. Comparar con el valor esperado
4. Observar el error acumulado
5. Repetir usando Decimal para ver la diferencia

## Ejemplo
Sumar 0.1 un millón de veces debería dar 100,000.0
pero float acumula error y da un valor ligeramente diferente

## Caso de prueba
Entrada: incremento = 0.1, iteraciones = 1,000,000
Esperado: 100000.0
Resultado float: 100000.00000001328...
Error: 1.3328e-05

## Ejercicio
Comparar la acumulación de errores usando float vs Decimal
para diferentes números de iteraciones (1000, 10000, 1000000)
y mostrar cómo crece el error
