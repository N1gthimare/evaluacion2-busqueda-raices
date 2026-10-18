import numpy as np
from rellenar_csv import crear_csv, escribir_csv

def funcion_derivada(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def Newton_Raphson(f, a, nombre, tolerancia=1e-6, iteraciones=100):
    lista_Errores = []
    ar = crear_csv(nombre, "Newton-Raphson")
    Lista_X = [a]
    lista_Funcion = [f(a)]
    X_actual = a

    for N in range(1, iteraciones + 1):
        derivada = funcion_derivada(f, X_actual)

        if not np.isfinite(derivada) or abs(derivada) < 1e-12:
            estado = "Derivada cercana a cero o no válida"
            return X_actual, N - 1, lista_Errores, Lista_X, lista_Funcion, estado

        x_nuevo = X_actual - f(X_actual) / derivada
        

        if not np.isfinite(x_nuevo):
            estado = "Aproximación no válida"
            return X_actual, N - 1, lista_Errores, Lista_X, lista_Funcion, estado

        error = abs(x_nuevo - X_actual)
        valor_funcion = f(x_nuevo)

        Lista_X.append(x_nuevo)
        lista_Funcion.append(valor_funcion)
        lista_Errores.append(error)

        if error < tolerancia or abs(valor_funcion) < tolerancia:
            estado = "Convergió"
            return x_nuevo, N, lista_Errores, Lista_X, lista_Funcion, estado

        X_actual = x_nuevo

    estado = "Agotó las iteraciones"
    return X_actual, iteraciones, lista_Errores, Lista_X, lista_Funcion, estado
