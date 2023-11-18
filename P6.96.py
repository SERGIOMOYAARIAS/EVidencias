# Abro el archivo en modo lectura
#SERGIO SMITH MOYA ARIAS
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente los primeros 5 caracteres del archivo.
contenido=f.read(5)
# Muestro el contenido
print(contenido)
# Leo otros 5 caracteres del archivo.
contenido=f.read(5)
# Muestro el contenido
print(contenido)
# Cierro el archivo.
f.close()
