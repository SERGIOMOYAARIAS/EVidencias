import pickle

# Datos iniciales. Entradas es una lista que contiene listas.
Entradas = [
    ['correo', 'nombre', 'telefono'],
    ['juan@gmail.com', 'Juan', '8123232323'],
    ['maria@gmail.com', 'Maria', '5545454545'],
    ['diana@homail.com', 'Diana', '4490909090']
]

# Serialización a Pickle
print("\n>> Serialización a Pickle.\n")
Entradas_pickle = pickle.dumps(Entradas)
print(Entradas_pickle)

# Deserialización desde Pickle
print("\n>> Deserialización desde Pickle.\n")
Nueva_Lista = pickle.loads(Entradas_pickle)
print(Nueva_Lista)
print(type(Nueva_Lista))

# Comprobando igualdad de objetos
print("\n>> Comprobando igualdad de objetos.\n")
print(Entradas == Nueva_Lista)
