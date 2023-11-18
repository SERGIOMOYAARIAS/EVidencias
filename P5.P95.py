# Abro el archivo en modo Write Extended.
# Si el archivo no existe, lo genera. Si existe, lo remplaza.
# Los contenidos van en secuencia.
#SERGIO SMITH MOYA ARIAS
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 contenidos en secuencia.
f.write("Blanco")
f.write("Negro")
f.write("Naranja")
# Cierro el archivo.
f.close()
# Para saltos de línea, se utiliza \n
# Abro el archivo en modo Write Extended
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 líneas adicionales.
f.write("Rojo\n")
f.write("Amarillo\n")
f.write("Verde\n")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()
f = open(archivo,"a+")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()
# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo el contenido y se lo asigno a la variable
# contenido.
contenido=f.read()
# Muestro el contenido. Debe ser todo el archivo.
print(contenido)
# Cierro el archivo.
f.close()
