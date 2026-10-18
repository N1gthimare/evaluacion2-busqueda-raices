import csv
from pathlib import Path

esta_carpeta = Path(__file__).resolve().parent
resumen = esta_carpeta.parent / "data"
resumen.mkdir(parents=True, exist_ok=True)


def csv_resultados(datos):
    keys = list(datos[0].keys())
    ar = open(resumen / "Resumen_convergencia.csv", mode="w", newline="", encoding="utf-8")
    header = ["Nombre funcion", "Metodo", "n", "raíz encontrada", "error"]
    escritor = csv.DictWriter(ar, fieldnames=keys, restval="")
    escritor.writeheader()
    escritor.writerows(datos)