import csv


def crear_csv(funciones):
    ar = open(funciones.get("Nombre"), mode="w", newline="", encoding="utf-8")
    header = ["x0", "x1", "f(x)"]
    escritor = csv.writer(ar)
    escritor.writerow(header)
    return ar

def escribir_csv(ar, datos):
    escritor = csv.writer(ar)
    escritor.writerow(datos)