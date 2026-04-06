# Conversión Estrecha (Narrowing Primitive Conversion)

## Presentación
Ocurre cuando se convierte un tipo de dato de mayor precisión 
a uno de menor precisión. Al reducir el tamaño del tipo de dato,
se pierden bits y por lo tanto información, generando errores 
o resultados inesperados.

## Fórmula
Pérdida de datos = valor_original - valor_convertido
Rango float:  ±3.4 × 10^38  (7 dígitos de precisión)
Rango double: ±1.7 × 10^308 (15-17 dígitos de precisión)

## Algoritmo
1. Definir un número con alta precisión (double/float)
2. Convertirlo a un tipo de menor precisión (float/int)
3. Observar la pérdida de dígitos
4. Calcular el error generado

## Ejemplo
double → float: 1234567890.123456789 → 1234567936.0
int → byte: 130 → -126 (desbordamiento)

## Caso de prueba
Entrada: 1234567890.123456789 (double)
Convertido a float: valor diferente con menos dígitos
Error: diferencia entre ambos valores

## Ejercicio
Convertir diferentes tipos de datos numéricos
de mayor a menor precisión y calcular
la pérdida de información en cada caso
