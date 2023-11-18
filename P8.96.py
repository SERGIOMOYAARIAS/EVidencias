# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente los primeros 5 caracteres del arvhivo.
for linea in f:
 print(">", linea)
# Cierro el archivo.
f.close()

f.close()
print(f.closed)