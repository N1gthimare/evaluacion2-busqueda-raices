import numpy as np

def es_continua(f, a, b):
    puntos = np.linspace(a, b, 100)
    try:
        y = f(puntos)
        if np.any(np.isinf(y)) or np.any(np.isnan(y)):
            return False
        return True
    except Exception:
        return False

def validar(func):
    validas = []
    for elem in func:
        f = elem[0]
        a = elem[1][0]
        b = elem[1][1]
        if (type(a) != float) or (type(b) != float):
            pass
        elif es_continua(f, a, b) and ((f(a) * f(b)) < 0):
            validas.append([f,[a,b]])
    return validas

def comprobar_validez(f, a, b):
    f_validas = validar([f, [a,b]])
    return f_validas