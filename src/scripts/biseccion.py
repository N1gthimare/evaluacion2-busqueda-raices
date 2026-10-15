import numpy as np



def biseccion(f, a, b, tolerancia=1e-6, iteraciones=50):
    ##Evaluar si cumple por Teorema de Bolzano
    if f(a)*f(b)>=0:
        print("La funcion no cumple el Teorema de Bolzano al no tener cambio de signo")
        return None

    Lista_errores=[]
    lista_Xr=[]
    lista_Funcion_Xr=[]
    Xr_Anterior=a
    #Uso de las iteraciones
    for N in range(1,iteraciones+1):
        Xr=(a+b)/2
        lista_Xr.append(Xr)
        Funcion_Xr=f(Xr)
        lista_Funcion_Xr.append(Funcion_Xr)

        #Calcular error con la segunda iteracion
        if N>1:
            Error=abs(Xr-Xr_Anterior)
            Lista_errores.append(Error)
            if Error <tolerancia or abs(Funcion_Xr) < tolerancia:
                return Xr,N,Lista_errores,lista_Xr 
        if Funcion_Xr==0:
            return Xr,N,Lista_errores,lista_Xr

        if f(a)*f(Xr)>0:
            a=Xr
        else:
            b=Xr
        lista_Xr.append(Xr)
        
    return Xr,N,Lista_errores,lista_Xr



##solo casos de prueba
Funciones_Evaluar = [
    {
        'Nombre': "Polinomica (Raiz simple)",
        'f': lambda x: x**3 - x - 2,
        'a': 1.0,
        'b': 2.0,
    },
    {
        'Nombre': "Polinomica (Raiz doble)",
        'f': lambda x: (x-2)**2,
        'a': 2.0,
        'b': 3.0,
    },
    {
        'Nombre': "Logaritmica",
        'f': lambda x: np.log(x)+x-4,
        'a': 2.0,
        'b': 3.0,
    },
    {
        'Nombre': "Exponencial",
        'f': lambda x: np.exp(-x)-x,
        'a': 0.0,
        'b': 1.0,
    },
    {
        'Nombre': "Trigonometrica",
        'f': lambda x: np.cos(x) - x,
        'a': 0.0,
        'b': 1.0,
    },
        {
        'Nombre': "Mixta",
        'f': lambda x: np.sqrt(x) - np.cos(x),
        'a': 0.1,
        'b': 1.0,
    },
]

###Caso de prueba evaluados
for caso in Funciones_Evaluar:
    print(f"\n{caso['Nombre']}")

    resultado = biseccion(
        caso['f'],
        caso['a'],
        caso['b']
    )

    if resultado is None:
        print("No se logro obtener una raiz (Revisar).")
    else:
        raiz, N, errores, aproximaciones = resultado

        print(f"Raíz aproximada: {raiz}")
        print(f"Iteraciones: {N}")
        print(f"Cantidad de aproximaciones: {(aproximaciones)}")
        print(f"Cantidad de errores: {(errores)}")