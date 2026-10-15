import numpy as np
from validar_FP import comprobar_validez

def falsa_posicion(lista_funciones):
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
            xr = b - (f(b) * (a - b))/(f(a) - f(b))
            if (f(a) * f(xr) < 0):
                b = xr
            else:
                a = xr
            iteraciones += 1
            if abs(f(xr)) < tol or abs(xr - x_anterior) < tol:
                print(f"Se encontro la raiz: {xr} en la iteracion: {iteraciones}")
                resultados.append([f,a,b,xr])
                break
            elif iteraciones == 100:
                print("No se encontro una raiz, iteraciones maximas alcanzadas")
            x_anterior = xr   