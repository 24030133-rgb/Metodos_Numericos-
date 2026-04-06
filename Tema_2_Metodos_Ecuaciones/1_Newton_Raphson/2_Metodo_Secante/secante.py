# Método de la Secante

def f(x):
    return x**2 - 2

def secante(x0, x1, tolerancia=1e-6, max_iter=100):
    print(f"{'Iteración':<12} {'x':<20} {'f(x)':<20} {'Error':<20}")
    print("-" * 70)

    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            print("Error: división entre cero")
            return None

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)

        print(f"{i+1:<12} {round(x2, 4):<20} {round(f(x2), 4):<20} {round(error, 4):<20}")

        if error < tolerancia:
            print(f"\nRaíz encontrada: {round(x2, 4)}")
            return round(x2, 4)

        x0 = x1
        x1 = x2

    print("No convergió")
    return None

# Caso de prueba
print("=== Secante: f(x) = x² - 2 ===")
secante(x0=1.0, x1=2.0)

# Ejercicio
print("\n=== Ejercicio: f(x) = x³ - x - 2 ===")
def f(x): return x**3 - x - 2
secante(x0=1.0, x1=2.0)
