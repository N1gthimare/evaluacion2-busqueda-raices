import numpy as np
from rellenar_csv import crear_csv, escribir_csv
# Revisar casos de errores

def punto_fijo(g, nombre):
    ar = crear_csv(nombre, "punto fijo")
    tol = 0.000001
    lista_x = []
    resultados = []
    errores = []
    iteraciones = 0
    x_anterior = 1
    xi = 0
    
    while iteraciones < 100:
        if (g == None):
            estado = "No hay funcion g(x) o no es valida"
            return 0, iteraciones, errores, lista_x, resultados, estado
        res = g(x_anterior)

        lista_x.append(xi)
        xi = res
        resultados.append(res)
        errores.append((xi - x_anterior)/xi)
        
        escribir_csv(ar, [x_anterior, xi, res])
        iteraciones += 1

        if abs((xi - x_anterior) / xi) <= tol:
            estado = "Convergio"
            return res, iteraciones, errores, lista_x, resultados, estado
        if iteraciones == 100:
            estado = "Agotó las iteraciones"
            return res, iteraciones, errores, lista_x, resultados, estado
        
        x_anterior = xi
