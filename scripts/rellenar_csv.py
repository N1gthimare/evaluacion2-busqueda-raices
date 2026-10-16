import csv
from pathlib import Path

esta_carpeta = Path(__file__).resolve().parent
csvs = esta_carpeta.parent / "data"
csvs.mkdir(parents=True, exist_ok=True)


def crear_csv(nombre, nombre_metodo):
    nombre_archivo = nombre+"-"+nombre_metodo+".csv"
    ar = open(csvs / nombre_archivo, mode="w", newline="", encoding="utf-8")
    header = ["x0", "x1", "f(x)"]
    escritor = csv.writer(ar)
    escritor.writerow(header)
    return ar

def escribir_csv(ar, datos):
    escritor = csv.writer(ar)
    escritor.writerow(datos)