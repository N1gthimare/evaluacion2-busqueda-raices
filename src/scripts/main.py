#Creado por: Manuel Fuentes / Ariel Gallardo

from funciones import Funciones_Evaluar
from biseccion import biseccion
from Newton_Raphson import Newton_Raphson
from Raphson_Modificado import Newton_Raphson_Modificado
from Graficos import graficar_resultados
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from csv_resultados import csv_resultados


Metodos = [
    ("Biseccion", biseccion, ["f", "a", "b", "Nombre"]),
    ("Newton-Raphson", Newton_Raphson, ["f", "a", "Nombre"]),
    ("Newton-Raphson Modificado", Newton_Raphson_Modificado, ["f", "a", "Nombre"]),
    ("Punto Fijo", punto_fijo,["g", "Nombre"]),
    ("Secante", secante,["f", "a", "b", "Nombre"]),
    ("Falsa Posicion", falsa_posicion,["f", "a", "b", "Nombre"])
]


def main():
    Resultados = []

    for caso in Funciones_Evaluar:
        print(f"\n{'=' * 50}")
        print(f"Funcion: {caso['Nombre']}")
        print(f"{'=' * 50}")

        for nombre, metodo, argumentos in Metodos:
            try:
                parametros = [
                    caso[argumento] for argumento in argumentos
                ]

                (
                    raiz,
                    N,
                    errores,
                    aproximaciones,
                    valores_funcion,
                    estado
                ) = metodo(*parametros)

            except Exception as error:
                raiz = None
                N = 0
                errores = []
                aproximaciones = []
                valores_funcion = []
                estado = f"Error durante la ejecución: {error}"

            resultado = {
                "Funcion": caso["Nombre"],
                "Metodo": nombre,
                "Raiz": raiz,
                "Iteraciones": N,
                "Errores": errores,
                "Aproximaciones": aproximaciones,
                "Valores_Funciones": valores_funcion,
                "Estado": estado,
            }

            Resultados.append(resultado)

            print(f"\nMetodo: {nombre}")
            print(f"Raiz aproximada: {raiz}")
            print(f"Iteraciones: {N}")
            print(f"Estado: {estado}")

    funciones = {
        caso["Nombre"]: caso["f"]
        for caso in Funciones_Evaluar
    }

    graficar_resultados(Resultados, funciones)
    csv_resultados(Resultados)


if __name__ == "__main__":
    main()
