# Código para manejar archivos CSV y JSON

import csv
import json

# CSV: Escritura en un archivo CSV
with open('datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Edad'])
    writer.writerow(['Ana', 25])

# JSON: Escritura en un archivo JSON
datos = {"Nombre": "Ana", "Edad": 25}
with open('datos.json', 'w') as file:
    json.dump(datos, file)
