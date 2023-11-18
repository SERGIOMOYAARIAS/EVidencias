# Abrir el archivo de datos JSON, en modo de solo lectura.
# usa open(), en modo r. Usa el apuntador de archivo f.
#SERGIO SMITH MOYA ARIAS
f = open('agenda.json','r')
# Carga el contenido JSON en una lista. Usa loads() y read().
# Almacena la lectura en una variable llamada Contactos_JSON.
Contactos_JSON=json.loads(f.read())
# Imprime Entradas, Contactos y Contactos JSON.
# Comprueba que son iguales.
print(Entradas)
print(Contactos)
print(Contactos_JSON)