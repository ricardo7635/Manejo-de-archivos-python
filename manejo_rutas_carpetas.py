# Código para manejar rutas y crear carpetas
import os
from pathlib import Path

# Crear una carpeta nueva
os.makedirs('nueva_carpeta', exist_ok=True)

# Verificar si un archivo existe usando Pathlib
ruta = Path('nueva_carpeta/archivo.txt')
print(ruta.exists())
