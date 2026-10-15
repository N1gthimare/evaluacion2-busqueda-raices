import numpy as np



def funcion_derivada(f,x,h=1e-5):
  return (f(x + h) - f(x - h)) / (2 * h)

def Newton_Raphson(f, a, tolerancia=1e-6, iteraciones=50):
    lista_Errores=[]
    Lista_X=[a]
    X_actual=a
    x_nuevo=0
    for N in range(1,iteraciones+1):
        Funcion_X=f(X_actual)
        Funcion_derivada=funcion_derivada(f,X_actual)
        if abs(Funcion_derivada) < 1e-12:
            print('Derivada cercana a cero. El método se indefine.')
            return x_actual, N, lista_Errores, Lista_X
        x_nuevo = X_actual - (f(X_actual) / Funcion_derivada)
        Lista_X.append(x_nuevo)


        error = abs(x_nuevo - x_actual)
        lista_Errores.append(error)

        if error < tolerancia or abs(Funcion_X) < tolerancia:
            
            return x_nuevo, N, lista_Errores, Lista_X

        x_actual = x_nuevo

    return x_actual, N, lista_Errores, Lista_X


