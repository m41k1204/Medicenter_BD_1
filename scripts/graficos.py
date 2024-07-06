import pandas as pd
import matplotlib.pyplot as plt

# Datos extraídos de la imagen
data = {
    'Tiempo': [ 171.906, 1820.3, 15724.99, 45.193, 582.65, 6982.16],
    'Tamanho': [ '10k', '100k', '1M', '10k', '100k','1M'],
    'Tipo': [ 'no', 'no','no', 'si', 'si', 'si']
}

# Crear DataFrame
df = pd.DataFrame(data)

# Filtrar datos por laboratorio
df_lab11 = df[df['Tipo'] == 'no']
df_lab11i = df[df['Tipo'] == 'si']

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Graficar datos de lab11 con líneas
plt.plot(df_lab11['Tamanho'], df_lab11['Tiempo'], color='blue', marker='o', linestyle='-', label='datos sin índices')

# Graficar datos de lab11i con líneas
plt.plot(df_lab11i['Tamanho'], df_lab11i['Tiempo'], color='red', marker='o', linestyle='-', label='datos con índices')

# Etiquetas y título
plt.xlabel('Cantidad de datos')
plt.ylabel('Tiempo en [ms]')
plt.title("Comparación de Tiempos entre tablas con datos indexados y no indexados ")
plt.legend()

# Mostrar gráfico
plt.show()
