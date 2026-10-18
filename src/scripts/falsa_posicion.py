from validar_FP import comprobar_validez
from rellenar_csv import crear_csv, escribir_csv


def falsa_posicion(f0, a0, b0, nombre):
    ar = crear_csv(nombre, "falsa_posicion")
    tol = 0.000001
    f, a, b, valida = comprobar_validez(f0, a0, b0)
    lista_x = []
    resultados = []
    errores = []
    iteraciones = 0
    x_anterior = 0
    
    if not valida:
        estado = "La funcion o algun valor entregado no es valido"
        return 0, 0, errores, lista_x, resultados, estado
    
    while iteraciones < 100:
        res = b - (f(b) * (a - b))/(f(a) - f(b))
        iteraciones += 1
        escribir_csv(ar, [a, b, res])

        xr = res
        lista_x.append(res)
        errores.append((xr - x_anterior)/xr)

        if (f(a) * f(xr) < 0):
            b = xr
            resultados.append(f(b))
        else:
            a = xr
            resultados.append(f(a))


        if abs(f(xr)) <= tol or abs((xr - x_anterior) / xr) <= tol:
            estado = "Convergio"
            return xr, iteraciones, errores, lista_x, resultados, estado
        elif iteraciones == 100:
            estado = "Agotó las iteraciones"
            return xr, iteraciones, errores, lista_x, resultados, estado

        x_anterior = xr