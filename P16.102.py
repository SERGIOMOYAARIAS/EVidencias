# Se importa el módulo para trabajar con JSON.
#SERGIO SMITH MOYA ARIAS

import json
# Se crea un objeto de muestra, para serializar.
Original=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
print(">> Tipo del objeto.\n")
print(type(Original))
print("\n>> Contenido del objeto.\n")
print(Original)
print("\n>> Serialización a JSON.\n")
Original_JSON=json.dumps(Original,indent=4)
print(Original_JSON)
print("\n>> Deserialización desde JSON.\n")
Nueva_Lista=json.loads(Original_JSON)
print(Nueva_Lista)
print(type(Nueva_Lista))
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==Nueva_Lista)


# Grabando el JSON en un archivo.
with open("archivo.json","w+") as f:
 json.dump(Original,f,indent=4)
# Leyendo datos de un archivo json
with open("archivo.json","r") as f:
 recuperados=json.load(f)
print(recuperados)
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==recuperados)


import pickle

# Ejemplo de objeto
Original = [1, 'Hola', {'a': 42, 'b': [1, 2, 3]}]

# Serialización a Pickle
print("\n>> Serialización a Pickle.\n")
Original_pickle = pickle.dumps(Original)
print(Original_pickle)

# Deserialización desde Pickle
print("\n>> Deserialización desde Pickle.\n")
Nueva_Lista = pickle.loads(Original_pickle)
print(Nueva_Lista)
print(type(Nueva_Lista))

# Comprobando igualdad de objetos
print("\n>> Comprobando igualdad de objetos.\n")
print(Original == Nueva_Lista)
