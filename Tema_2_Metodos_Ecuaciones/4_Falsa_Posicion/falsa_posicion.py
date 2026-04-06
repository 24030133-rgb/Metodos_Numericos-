# Método de Falsa Posición (Regula Falsi)

def f(x):
    return x**2 - 2

def falsa_posicion(a, b, tolerancia=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("Error: f(a) y f(b) deben tener signos opuestos")
        return None

    print(f"{'Iteración':<12} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12} {'Error':<12}")
    print("-" * 70)

    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        c = round(b - fb * (b - a) / (fb - fa), 4)
        fc = round(f(c), 4)
        error = round(abs(fc), 4)

        print(f"{i+1:<12} {round(a,4):<12} {round(b,4):<12} {c:<12} {fc:<12} {error:<12}")

        if error < tolerancia:
            print(f"\nRaíz encontrada: {c}")
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

    print("No convergió")
    return None

# Caso de prueba
print("=== Falsa Posición: f(x) = x² - 2 ===")
falsa_posicion(a=1.0, b=2.0)

# Ejercicio
print("\n=== Ejercicio: f(x) = x³ - x - 2 ===")
def f(x): return x**3 - x - 2
falsa_posicion(a=1.0, b=2.0)
