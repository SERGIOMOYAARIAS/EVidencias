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

