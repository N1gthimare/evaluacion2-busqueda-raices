import numpy as np


def extraer_datos(lista_funciones):
    datos = []
    for elem in lista_funciones:
        f = elem.get('f')
        x0 = elem.get('a')
        x1 = elem.get('b')
        datos.append([f,[x0,x1]])
    return datos

def secante(lista_funciones):
    datos = extraer_datos(lista_funciones)
    tol = 0.000001
    resultados = []
    iteraciones = 0
    for lista in datos:
        f = lista[0]
        x0 = lista[1][0]
        x1 =  lista[1][1]
        while iteraciones < 100:
            if (type(x0) != float) or (type(x1) != float): break
            xn = x1 - ((x1 - x0)/(f(x1) - f(x0))) * f(x1)
            iteraciones += 1
            if (xn - x1)/xn <= tol:
                print(f"Raiz {xn} encontrada en la iteracion: {iteraciones}")
                resultados.append([f,xn, x1, x0])
                break
            x0 = x1
            x1 = xn