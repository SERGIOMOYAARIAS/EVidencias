import pickle

# Datos iniciales. Entradas es una lista que contiene listas.
Entradas = [
    ['correo', 'nombre', 'telefono'],
    ['juan@gmail.com', 'Juan', '8123232323'],
    ['maria@gmail.com', 'Maria', '5545454545'],
    ['diana@homail.com', 'Diana', '4490909090']
]

# Grabando el pickle en un archivo
with open("archivo.pickle", "wb+") as f:
    pickle.dump(Entradas, f)

# Leyendo datos de un archivo pickle
with open("archivo.pickle", "rb") as f:
    recuperados = pickle.load(f)

# Imprimiendo los datos recuperados
print(recuperados)

# Comprobando igualdad de objetos
print("\n>> Comprobando igualdad de objetos.\n")
print(Entradas == recuperados)
