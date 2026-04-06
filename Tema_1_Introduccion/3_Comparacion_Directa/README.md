# Comparación Directa con ==

## Presentación
Comparar números de punto flotante con == es un error común 
en programación. Debido al error de redondeo, dos números 
que deberían ser iguales pueden no serlo en memoria.

## Fórmula
En lugar de: a == b
Se debe usar: |a - b| < epsilon
Donde epsilon es una tolerancia pequeña (ej. 1e-9)

## Algoritmo
1. Calcular dos valores que deberían ser iguales
2. Compararlos con ==
3. Observar el resultado incorrecto
4. Aplicar comparación con tolerancia epsilon
5. Verificar el resultado correcto

## Ejemplo
0.1 + 0.2 == 0.3  →  False (incorrecto)
abs(0.1 + 0.2 - 0.3) < 1e-9  →  True (correcto)

## Caso de prueba
Entrada: a = 0.1 + 0.2,  b = 0.3
Comparación ==: False
Comparación con epsilon: True

## Ejercicio
Comparar los resultados de varias operaciones 
flotantes usando == y usando epsilon, 
mostrar cuál es el método correcto
