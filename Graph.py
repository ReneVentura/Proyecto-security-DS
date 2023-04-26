import pandas as pd
import numpy as np
import string
import random
import matplotlib.pyplot as plt
import zxcvbn   # Biblioteca para medir la fortaleza de las contraseñas

# Leer el archivo CSV
df = pd.read_csv('common_passwords.csv', header=None, names=['contraseña'])

# Limpiar el dataframe de valores nulos o vacíos
df.dropna(inplace=True)

# Función para evaluar la seguridad de las contraseñas y generar una nueva columna para almacenar la fortaleza
def evaluar_fortaleza(password):
    seguridad = zxcvbn.zxcvbn(password)
    return seguridad['score']

df['fortaleza'] = df['contraseña'].apply(evaluar_fortaleza)

# Función para generar recomendaciones de contraseñas seguras
def generar_contraseña_segura():
    longitud = 12  # Longitud de la contraseña a generar
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        if zxcvbn.zxcvbn(contraseña)['score'] >= 3:   # Verificar si la fortaleza de la contraseña generada es >= 3
            return contraseña

# Generar 1000 contraseñas seguras y agregarlas al dataframe
df_seguras = pd.DataFrame({'contraseña': [generar_contraseña_segura() for i in range(1000)]})
df_seguras['fortaleza'] = df_seguras['contraseña'].apply(evaluar_fortaleza)

# Graficar la distribución de las fortalezas de las contraseñas
bins = [0, 1, 2, 3, 4]   # Rangos de fortaleza de 0 a 4
labels = ['Muy débil', 'Débil', 'Mediana', 'Fuerte', 'Muy fuerte']   # Etiquetas de los rangos
plt.hist(df['fortaleza'], bins=bins, label='Contraseñas originales', alpha=0.5)
plt.hist(df_seguras['fortaleza'], bins=bins, label='Contraseñas seguras', alpha=0.5)
plt.legend()
plt.xticks(bins, labels)
plt.xlabel('Fortaleza')
plt.ylabel('Cantidad')
plt.title('Distribución de fortaleza de contraseñas')
plt.show()
