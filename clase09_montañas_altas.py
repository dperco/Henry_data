import os

# Crear la carpeta "clase09_montañas_altas"
os.makedirs("clase09_montañas_altas", exist_ok=True)

# Copiar el archivo "clase09_ej3.csv" en la carpeta "clase09_montañas_altas"
os.system("cp clase09_ej3.csv clase09_montañas_altas/")

# Listar el contenido de la carpeta "clase09_montañas_altas"
contenido = os.listdir("clase09_montañas_altas")

print("Contenido de la carpeta 'clase09_montañas_altas':")
for archivo in contenido:
    print(archivo)
