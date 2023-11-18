# Importar los módulos para trabajar con pickle y con archivos
import os
import pickle

# Definir la variable Entradas (agrega tu propia definición)
Entradas = [
    ['correo', 'nombre', 'telefono'],
    ['juan@gmail.com', 'Juan', '8123232323'],
    ['maria@gmail.com', 'Maria', '5545454545'],
    ['diana@hotmail.com', 'Diana', '4490909090']
]

# Muestra el contenido del objeto Entradas
print("Contenido de Entradas:")
print(Entradas)

# Muestra el tipo del objeto Entradas
print("\nTipo de Entradas:")
print(type(Entradas))

# Serializa Entradas, usando un archivo pickle llamado
# Entradas.pickle. Recuerda que pickle es formato binario
# por lo que el tipo de contenido debe ser binario, al escribir.
# Utiliza with, open() en modo Write Binary Extended, y dump(), para
# el manejo de pickle con archivos.
with open("Entradas.pickle", "wb+") as f:
    pickle.dump(Entradas, f)

# Recupera el contenido del archivo Entradas.pickle, y asígnalo a una
# lista llamada Recuperado. Recuerda que pickle es formato binario
# por lo que el tipo de contenido debe ser binario, al leer.
# Utiliza with, open() en modo Read Binary, y load(), para
# el manejo de pickle con archivos.
with open("Entradas.pickle", "rb") as f:
    Recuperado = pickle.load(f)

# Compara el objeto Entradas con el objeto Recuperado
# deben ser iguales.
print("\n¿Entradas es igual a Recuperado?")
print(Entradas == Recuperado)
# Importar los módulos para trabajar con pickle y con archivos
import os
import pickle

# Definir la variable Entradas (agrega tu propia definición)
Entradas = [
    ['correo', 'nombre', 'telefono'],
    ['juan@gmail.com', 'Juan', '8123232323'],
    ['maria@gmail.com', 'Maria', '5545454545'],
    ['diana@hotmail.com', 'Diana', '4490909090']
]

