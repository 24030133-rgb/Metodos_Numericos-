# Error de Redondeo Binario

## Presentación
El error de redondeo binario ocurre cuando un número decimal 
no puede representarse exactamente en sistema binario, 
generando una pequeña diferencia entre el valor real y el almacenado.

## Fórmula
Error absoluto = |valor_real - valor_aproximado|
Error relativo = |valor_real - valor_aproximado| / |valor_real|

## Algoritmo
1. Tomar un número decimal
2. Convertirlo a representación binaria (float)
3. Reconvertir a decimal
4. Calcular la diferencia entre el valor original y el recuperado

## Ejemplo
0.1 + 0.2 en Python no da exactamente 0.3
debido a la representación binaria de punto flotante

## Caso de prueba
Entrada: 0.1 + 0.2
Esperado: 0.3
Resultado real: 0.30000000000000004

## Ejercicio
Calcular el error de redondeo al representar 
los números 0.1, 0.2 y 0.3 en punto flotante
