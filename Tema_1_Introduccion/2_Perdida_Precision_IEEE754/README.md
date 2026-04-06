# Pérdida de Precisión por Magnitud (IEEE 754)

## Presentación
El estándar IEEE 754 define cómo se representan los números 
de punto flotante en computadoras. Cuando se operan números 
de magnitudes muy diferentes, el número pequeño puede perder 
precisión o incluso desaparecer.

## Fórmula
Un número flotante de 64 bits (double) tiene:
- 1 bit de signo
- 11 bits de exponente
- 52 bits de mantisa

Precisión máxima ≈ 15-17 dígitos decimales

## Algoritmo
1. Tomar dos números de magnitudes muy diferentes
2. Realizar una operación entre ellos
3. Observar cómo el número pequeño pierde dígitos significativos
4. Calcular el error generado

## Ejemplo
1e16 + 1.0 = 1e16 (el 1.0 desaparece)

## Caso de prueba
Entrada: 1e16 + 1.0
Esperado: 10000000000000001.0
Resultado real: 10000000000000000.0

## Ejercicio
Demostrar la pérdida de precisión sumando 
números de diferente magnitud y calcular el error
