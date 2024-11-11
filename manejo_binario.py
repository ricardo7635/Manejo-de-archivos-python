# Código para manejar archivos binarios (leer, escribir)
with open('imagen.bin', 'wb') as f:
    f.write(b'\x89PNG\r\n\x1a\n')

with open('imagen.bin', 'rb') as f:
    datos = f.read()
print(datos)
