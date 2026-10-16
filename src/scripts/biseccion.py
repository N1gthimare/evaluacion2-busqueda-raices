import numpy as np

def biseccion(f, a, b, tolerancia=1e-6, iteraciones=50):

    Lista_errores = []
    lista_Xr = []
    lista_Funcion_Xr = []
    if b is None:
        estado = "Falta el extremo b del intervalo"
        return None, 0, Lista_errores, lista_Xr, lista_Funcion_Xr, estado

    if not np.isfinite(a) or not np.isfinite(b) or a >= b:
        estado = "Intervalo no válido"
        return None, 0, Lista_errores, lista_Xr, lista_Funcion_Xr, estado

    fa = f(a)
    fb = f(b)

    if not np.isfinite(fa) or not np.isfinite(fb):
        estado = "Valores de la función no válidos"
        return None, 0, Lista_errores, lista_Xr, lista_Funcion_Xr, estado
    if fa == 0:
        estado = "Convergió"
        return a, 0, Lista_errores, [a], [fa], estado

    if fb == 0:
        estado = "Convergió"
        return b, 0, Lista_errores, [b], [fb], estado
    if fa * fb > 0:
        estado = "No hay cambio de signo en el intervalo"
        return None, 0, Lista_errores, lista_Xr, lista_Funcion_Xr, estado

    Xr_Anterior = None
    estado = "Agotó las iteraciones"

    for N in range(1, iteraciones + 1):

        Xr = (a + b) / 2
        Funcion_Xr = f(Xr)

        if not np.isfinite(Xr) or not np.isfinite(Funcion_Xr):
            estado = "Aproximación o función no válida"
            return None, N - 1, Lista_errores, lista_Xr, lista_Funcion_Xr, estado

        lista_Xr.append(Xr)
        lista_Funcion_Xr.append(Funcion_Xr)
        if abs(Funcion_Xr) < tolerancia:
            estado = "Convergió"
            return Xr, N, Lista_errores, lista_Xr, lista_Funcion_Xr, estado

        # Calcular el error entre aproximaciones consecutivas
        if Xr_Anterior is not None:
            Error = abs(Xr - Xr_Anterior)
            Lista_errores.append(Error)

            if Error < tolerancia:
                estado = "Convergió"
                return Xr, N, Lista_errores, lista_Xr, lista_Funcion_Xr, estado
        if fa * Funcion_Xr > 0:
            a = Xr
            fa = Funcion_Xr
        else:
            b = Xr
            fb = Funcion_Xr

        Xr_Anterior = Xr

    return Xr, N, Lista_errores, lista_Xr, lista_Funcion_Xr, estado
