import csv

montañas = {
    'nombre': ['Everest', 'K2', 'Kanchenjunga', 'Lhotse', 'Makalu', 'Cho Oyu', 'Dhaulagiri', 'Manaslu', 'Nanga Parbat', 'Annapurna I'],
    'orden': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'cordillera': ['Himalaya', 'Karakórum', 'Himalaya', 'Himalaya', 'Himalaya', 'Himalaya', 'Himalaya', 'Himalaya', 'Karakórum', 'Himalaya'],
    'pais': ['Nepal', 'Pakistán', 'Nepal', 'Nepal', 'Nepal', 'Nepal', 'Nepal', 'Nepal', 'Pakistán', 'Nepal'],
    'altura': [8849, 8611, 8586, 8516, 8485, 8188, 8167, 8163, 8125, 8091]
}

# Obtener las claves del diccionario
claves = montañas.keys()

# Crear el archivo CSV y escribir los datos
with open("clase09_ej3.csv", "w", newline="") as archivo_csv:
    writer = csv.writer(archivo_csv)
    
    # Escribir la primera fila con los nombres de las claves
    writer.writerow(claves)
    
    # Escribir los valores de cada clave en filas sucesivas
    for i in range(len(montañas['nombre'])):
        fila = [montañas[clave][i] for clave in claves]
        writer.writerow(fila)

print("Archivo creado correctamente.")

import os

# Obtener el tamaño del archivo
tamaño = os.path.getsize("clase09_ej3.csv")

print(f"Tamaño del archivo: {tamaño} bytes")

