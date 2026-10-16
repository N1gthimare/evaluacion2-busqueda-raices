import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def graficar_funciones(funciones, resultados):
    for nombre, f in funciones.items():
        raices = [
            r["Raiz"] for r in resultados
            if r["Funcion"] == nombre
            and r.get("Raiz") is not None
            and r.get("Estado") == "Convergió"
        ]

        if not raices:
            continue

        x = np.linspace(min(raices) - 2, max(raices) + 2, 500)
        y = np.array([f(float(v)) for v in x])

        fig, ax = plt.subplots()
        ax.plot(x, y, label="f(x)")
        ax.axhline(0, color="black", linewidth=0.8)
        ax.scatter(raices, [f(r) for r in raices], color="red", label="Raíz")
        ax.set_title(nombre)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid()
        ax.legend()
        fig.savefig(ASSETS / f"funcion_{nombre}.png", bbox_inches="tight")
        plt.close(fig)


def graficar_errores(resultados):
    for nombre in dict.fromkeys(r["Funcion"] for r in resultados):
        fig, ax = plt.subplots()

        for r in resultados:
            if r["Funcion"] == nombre and r.get("Errores"):
                errores = np.maximum(np.abs(r["Errores"]), 1e-16)
                ax.semilogy(range(1, len(errores) + 1),
                            errores, marker="o", label=r["Metodo"])

        ax.set_title(f"Convergencia: {nombre}")
        ax.set_xlabel("Iteración")
        ax.set_ylabel("Error absoluto")
        ax.grid()
        ax.legend()
        fig.savefig(ASSETS / f"errores_{nombre}.png", bbox_inches="tight")
        plt.close(fig)


def graficar_iteraciones(resultados):
    funciones = list(dict.fromkeys(r["Funcion"] for r in resultados))
    metodos = list(dict.fromkeys(r["Metodo"] for r in resultados))
    x = np.arange(len(funciones))
    ancho = 0.8 / len(metodos)

    fig, ax = plt.subplots()

    for i, metodo in enumerate(metodos):
        valores = [
            next((r["Iteraciones"] for r in resultados
                  if r["Funcion"] == f and r["Metodo"] == metodo), 0)
            for f in funciones
        ]
        ax.bar(x + (i - (len(metodos) - 1) / 2) * ancho,
               valores, ancho, label=metodo)

    ax.set_xticks(x)
    ax.set_xticklabels(funciones, rotation=25, ha="right")
    ax.set_xlabel("Función")
    ax.set_ylabel("Iteraciones")
    ax.set_title("Iteraciones por método y función")
    ax.legend()
    fig.tight_layout()
    fig.savefig(ASSETS / "resumen_iteraciones.png", bbox_inches="tight")
    plt.close(fig)


def graficar_resultados(resultados, funciones=None):
    graficar_errores(resultados)
    graficar_iteraciones(resultados)

    if funciones:
        graficar_funciones(funciones, resultados)
