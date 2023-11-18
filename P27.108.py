# Importa la librería para el soporte JSON
import json

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

        # Elimina el salto de línea del último elemento de la lista
        lista_datos[2] = lista_datos[2].replace("\n", "")
        
        # Agrega la lista de datos contenida en lista_datos
        # a la lista Contactos
        Contactos.append(lista_datos)

# Almacena en una variable llamada datos_json, que almacene
# un volcado de datos. Utiliza dumps().
# Proporciona formato con identación a 4 posiciones.
datos_json = json.dumps(Contactos, indent=4)

# Muestra el contenido serializado.
print(datos_json)



# Guarda la serialización en un archivo como agenda.json.
# Utiliza open() en modo Write Extended.
# Usa f como apuntador de archivo.
f = open('agenda.json','w+')
f.write(datos_json)
f.close()
# Este código no genera salidas.
