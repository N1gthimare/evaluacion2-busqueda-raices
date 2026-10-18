from rellenar_csv import crear_csv, escribir_csv
# Revisar casos de errores

def extraer_datos(lista_funciones):
    datos = []
    for elem in lista_funciones:
        f = elem.get('f')
        a = elem.get('a')
        b = elem.get('b')
        datos.append([f,[a,b]])
    return datos

def secante(f, a, b, nombre):
    ar = crear_csv(nombre, "Secante")
    lista_x = []
    resultados = []
    errores = []
    tol = 0.000001
    iteraciones = 0
    
    while iteraciones < 100:
        if (a == None) or (b == None):
            estado = "Uno de los valores no es valido"
            return 0, iteraciones, errores, lista_x, resultados, estado
        
        res = b - ((b - a)/(f(b) - f(a))) * f(b)
        fx = f(res)
        escribir_csv(ar, [a, b, res])
        xn = res
        iteraciones += 1

        lista_x.append(res)
        resultados.append(fx)
        errores.append((b - a)/b)

        if abs((xn - b)/xn) <= tol or abs(fx) < tol:
            estado = "Convergio"
            return xn, iteraciones, errores, lista_x, resultados, estado
            
        elif iteraciones == 100:
            estado = "Agotó las iteraciones"
            return xn, iteraciones, errores, lista_x, resultados, estado
        
        a = b
        b = xn