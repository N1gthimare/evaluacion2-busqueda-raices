import numpy as np
from validar_FP import comprobar_validez
from rellenar_csv import crear_csv, escribir_csv


def falsa_posicion(lista_funciones):
    ar = crear_csv(lista_funciones)
    tol = 0.000001
    funciones = comprobar_validez(lista_funciones)
    resultados = []
    
    for elem in funciones:
        iteraciones = 0
        x_anterior = 0
        f = elem[0]
        a = elem[1][0]
        b = elem[1][1]
        while iteraciones < 100:
            res = b - (f(b) * (a - b))/(f(a) - f(b))
            escribir_csv(ar, [a, b, res])
            xr = res
            if (f(a) * f(xr) < 0):
                b = xr
            else:
                a = xr
            iteraciones += 1
            if abs(f(xr)) < tol or abs(xr - x_anterior) < tol:
                resultados.append([iteraciones, xr, (xr - x_anterior)/xr])
                break
            elif iteraciones == 100:
                print("No se encontro una raiz, iteraciones maximas alcanzadas")
                break
            x_anterior = xr   