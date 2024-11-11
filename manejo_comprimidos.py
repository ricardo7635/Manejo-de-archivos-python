# Código para manejar archivos comprimidos (ZIP)
import zipfile

# Crear un archivo ZIP
with zipfile.ZipFile('archivo.zip', 'w') as zipf:
    zipf.write('archivo.txt')

# Extraer un archivo ZIP
with zipfile.ZipFile('archivo.zip', 'r') as zipf:
    zipf.extractall('carpeta_destino')
