import csv


def csv_resultados(funciones, datos):
    ar = open("Resumen_convergencia", mode="w", newline="", encoding="utf-8")
    header = ["Nombre funcion", "Metodo", "n", "raíz encontrada", "error"]
    escritor = csv.writer(ar)
    escritor.writerow(header)
    escritor.writerows(datos)