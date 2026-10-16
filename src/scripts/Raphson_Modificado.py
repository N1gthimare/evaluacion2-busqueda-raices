
import numpy as np


def segunda_derivada(f, x, h=1e-5):
    if x - h < 0:
        h = min(h, x / 2)

    if h <= 0:
        return np.nan

    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)


def funcion_derivada(f, x, h=1e-5):
    if x - h >= 0:
        return (f(x + h) - f(x - h)) / (2 * h)

    # Diferencia hacia adelante cerca del límite x = 0
    return (-3 * f(x) + 4 * f(x + h) - f(x + 2*h)) / (2*h)


def Newton_Raphson_Modificado(f, a, tolerancia=1e-6, iteraciones=100):
    lista_Errores = []
    Lista_X = [a]
    X_actual = a
    lista_Funcion = [f(a)]
    estado = "Agotó las iteraciones"

    if not np.isfinite(X_actual) or X_actual < 0 or not np.isfinite(f(X_actual)):
        estado = "Aproximación inicial no válida"
        return X_actual, 0, lista_Errores, Lista_X, lista_Funcion, estado

    for N in range(1, iteraciones + 1):
        valor_funcion = f(X_actual)

        Derivada = funcion_derivada(f, X_actual)
        Derivada_grado2 = segunda_derivada(f, X_actual)

        if not np.isfinite(Derivada) or not np.isfinite(Derivada_grado2):
            estado = "Derivadas no válidas"
            return X_actual, N - 1, lista_Errores, Lista_X, lista_Funcion, estado

        Denominador = Derivada**2 - valor_funcion * Derivada_grado2

        if not np.isfinite(Denominador) or abs(Denominador) < 1e-12:
            estado = "Denominador cercano a cero o no válido"
            return X_actual, N - 1, lista_Errores, Lista_X, lista_Funcion, estado

        x_nuevo = X_actual - (valor_funcion * Derivada) / Denominador

        # No evaluar la función fuera de su dominio real
        if not np.isfinite(x_nuevo) or x_nuevo < 0:
            estado = "La aproximación salió del dominio x >= 0"
            return X_actual, N - 1, lista_Errores, Lista_X, lista_Funcion, estado

        valor_nuevo = f(x_nuevo)

        if not np.isfinite(valor_nuevo):
            estado = "Valor de la función no válido"
            return X_actual, N - 1, lista_Errores, Lista_X, lista_Funcion, estado

        error = abs(x_nuevo - X_actual)

        lista_Errores.append(error)
        Lista_X.append(x_nuevo)
        lista_Funcion.append(valor_nuevo)

        if error < tolerancia or abs(valor_nuevo) < tolerancia:
            estado = "Convergió"
            return x_nuevo, N, lista_Errores, Lista_X, lista_Funcion, estado

        X_actual = x_nuevo

    return X_actual, N, lista_Errores, Lista_X, lista_Funcion, estado
