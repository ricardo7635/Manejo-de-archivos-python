# Código para manejar archivos Excel (lectura y escritura)
import pandas as pd

# Lectura de un archivo Excel
df = pd.read_excel('datos.xlsx')
print(df.head())

# Escritura en un archivo Excel
df = pd.DataFrame({'Nombre': ['Ana'], 'Edad': [25]})
df.to_excel('nuevos_datos.xlsx', index=False)

