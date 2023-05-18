import csv
import datetime
import sys

def main():
    # Verificar la cantidad de parámetros
    if len(sys.argv) != 4:
        print("Error: Se esperan exactamente 3 parámetros.")
        return

    # Obtener los parámetros
    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    llovio = sys.argv[3]

    # Obtener la marca de tiempo actual
    marca_tiempo = datetime.datetime.now()

    # Crear una lista con los datos
    datos = [marca_tiempo, temperatura, humedad, llovio]

    # Escribir los datos en el archivo CSV
    with open("clase09_ej2.csv", "a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(datos)

    print("Datos guardados correctamente.")

if __name__ == "__main__":
    main()
