# Código para manejar archivos de texto (leer, escribir, agregar)
with open('archivo.txt', 'r') as f:
    contenido = f.read()
print(contenido)

with open('archivo.txt', 'w') as f:
    f.write('Texto de ejemplo')

with open('archivo.txt', 'a') as f:
    f.write('\nTexto adicional')
