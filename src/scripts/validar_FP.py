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

def validar(f, a ,b):
    if (type(a) != float) or (type(b) != float):
        return f, a, b, False
    elif (a < 0) or (b < 0):
        return f, a, b, False
    elif es_continua(f, a, b) and ((f(a) * f(b)) < 0):
        return f, a, b, True
    else:
        return f, a, b, False

def comprobar_validez(f0, a0, b0):
    f, a, b, valido = validar(f0, a0, b0)
    return f, a, b, valido