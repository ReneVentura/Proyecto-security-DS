import pandas as pd
import bcrypt
import string
import random

# Leer el archivo CSV
data = pd.read_csv('common_passwords.csv')

# Eliminar filas con valores nulos
data.dropna(inplace=True)

# Eliminar filas duplicadas
data.drop_duplicates(inplace=True)

# Preprocesamiento de datos (normalización, codificación, etc.)
...

# Evaluar la seguridad de las contraseñas
for password in data['password']:
    # Realizar el hash de la contraseña utilizando bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Verificar si la contraseña original y la contraseña hash son iguales
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print('La contraseña es segura')
    else:
        print('La contraseña es vulnerable')

# Generar recomendaciones de contraseñas seguras
def generate_password(length):
    # Definir caracteres permitidos
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generar una contraseña aleatoria de longitud dada
    return ''.join(random.choice(characters) for i in range(length))


secure_password = generate_password(12)
print('Contraseña segura generada:', secure_password)
