import numpy as np
from rellenar_csv import crear_csv, escribir_csv


def punto_fijo(lista_funciones):
    ar = crear_csv(lista_funciones)
    tol = 0.000001
    resultados = []

    for elem in lista_funciones:
        iteraciones = 0
        x_anterior = 0
        errores = []
        xi = 0
        g = elem.get('g')
        while iteraciones < 100:
            res = g(x_anterior)
            escribir_csv(ar, [x_anterior, xi, res])
            xi = res
            iteraciones += 1
            if ((xi - x_anterior) / xi) <= tol:
                resultados.append([iteraciones, res, (xi - x_anterior) / xi])
                errores.append((xi - x_anterior)/xi)
                break
            errores.append((xi - x_anterior)/xi)
            x_anterior = xi
    return errores