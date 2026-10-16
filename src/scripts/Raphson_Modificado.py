import numpy as np


def segunda_derivada(f, x, h=1e-5):
  return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)

def funcion_derivada(f,x,h=1e-5):
  return (f(x + h) - f(x - h)) / (2 * h)


def Newton_Raphson_Modificado(f, a, tolerancia=1e-6, iteraciones=100):
    lista_Errores=[]
    Lista_X=[a]
    X_actual=a
    lista_Funcion=[]
    x_nuevo=0
    for N in range(1,iteraciones+1):
        Derivada=funcion_derivada(f,X_actual)
        Derivada_grado2=segunda_derivada(f,X_actual)
        if abs(Derivada) < 1e-12:
            print('Derivada cercana a cero. El método se indefine.')
            return X_actual, N, lista_Errores, Lista_X, lista_Funcion
    
        x_nuevo = X_actual - ((f(X_actual)*Derivada) / ((Derivada**2)-(f(X_actual)*Derivada_grado2)))
        lista_Funcion.append(f(x_nuevo))
        Lista_X.append(x_nuevo)
        error = abs(x_nuevo - X_actual)
        lista_Errores.append(error)

        if error < tolerancia or abs(f(X_actual)) < tolerancia:
            return x_nuevo, N, lista_Errores, Lista_X,lista_Funcion

        X_actual = x_nuevo

    return X_actual, N, lista_Errores, Lista_X,lista_Funcion


    

