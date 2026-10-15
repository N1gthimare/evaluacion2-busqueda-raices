import numpy as np


def punto_fijo(funciones):
    tol = 0.000001
    resultados = []
    for elem in funciones:
        iteraciones = 0
        x_anterior = 0
        xi = 0
        g = elem.get('g')
        while iteraciones < 100:
            xi = g(x_anterior)
            iteraciones += 1
            if ((xi - x_anterior) / xi) <= tol:
                print(f"Raiz encontrada con xi = {xi} y xi-1 = {x_anterior} en la iteracion = {iteraciones}")
                resultados.append([g,x_anterior,xi])
                break
            x_anterior = xi