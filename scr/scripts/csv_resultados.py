import csv


def csv_resultados(funciones, datos):
    ar = open(funciones.get("Nombre"), mode="w", newline="", encoding="utf-8")
    header = ["n", "raíz encontrada", "error"]
    escritor = csv.writer(ar)
    escritor.writerow(header)
    escritor.writerows(datos)