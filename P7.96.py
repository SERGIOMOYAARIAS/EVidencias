# Abro el archivo en modo lectura
#SERGIO SMITH MOYA ARIAS
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente la primer línea del archivo.
contenido=f.readline()
# Muestro el contenido
print(contenido)
# Leo siguiente línea
contenido=f.readline()
# Muestro el contenido
print(contenido)
# Cierro el archivo.
f.close()
