# Se genera una lista vacía llamada Contactos
Contactos = []

# Abrir el archivo de datos CSV, en modo de solo lectura.
# Usa open, en modo r.
with open('agenda.csv', 'r') as f:
    # Elabora un ciclo for, que coloque en una variable llamada
    # linea a cada una de las líneas en el archivo apuntado
    # como f. Recuerda que leer un archivo plano con for equivale
    # a leerlo línea por línea.
    for linea in f:
        # Asigna a una variable llamada lista_datos, el equivalente
        # en lista del contenido de datos, usando como separador
        # el pipe line. Usa split(), con "|" como delimitador.
        lista_datos = linea.split('|')
        print(lista_datos)

        # Elimina el salto de línea del último elemento de la lista
        lista_datos[2] = lista_datos[2].replace("\n", "")
        
        # Agrega la lista de datos contenida en lista_datos
        # a la lista Contactos
        Contactos.append(lista_datos)

# Imprime Contactos y Entradas (si ya está definida), y comprueba que son iguales
if 'Entradas' in locals():
    print("\nEntradas:")
    for e in Entradas:
        print(e)

print("\nContactos:")
for c in Contactos:
    print(c)

# Importa la librería para el soporte JSON
import json

# Se genera una lista vacía llamada Contactos
Contactos = []

# Abrir el archivo de datos CSV, en modo de solo lectura.
# Usa open, en modo r.
with open('agenda.csv', 'r') as f:
    # ... Código para cargar datos en Contactos ...

# Almacena en una variable llamada datos_json, que almacene
# un volcado de datos. Utiliza dumps().
# Proporciona formato con identación a 4 posiciones.
 datos_json = json.dumps(Contactos, indent=4)

# Guarda la serialización en un archivo como agenda.json.
# Utiliza open() en modo Write Extended.
# Usa f como apuntador de archivo.
with open('agenda.json', 'w+') as f:
    f.write(datos_json)

# Lee y muestra el contenido del archivo
with open('agenda.json', 'r') as f_lectura:
    contenido_leido = f_lectura.read()
    print("\nContenido del archivo agenda.json:\n", contenido_leido)



# Abrir el archivo de datos JSON, en modo de solo lectura.
# Usa open(), en modo r. Usa el apuntador de archivo f.
f = open('agenda.json', 'r')

# Carga el contenido JSON en una lista. Usa loads() y read().
# Almacena la lectura en una variable llamada Contactos_JSON.
Contactos_JSON = json.loads(f.read())

# Imprime Entradas, Contactos y Contactos JSON.
# Comprueba que son iguales.
if 'Entradas' in locals():
    print("Entradas:")
    for e in Entradas:
        print(e)

print("\nContactos:")
for c in Contactos:
    print(c)

print("\nContactos_JSON:")
for cj in Contactos_JSON:
    print(cj)


# Importar los módulos para trabajar con pickle y con archivos
import os
import pickle
