# Abre el archivo de datos CSV, en modo de solo lectura.
# Usa f como apuntador de archivo. Usa open() en modo r.
#SERGIO SMITH MOYA ARIAS
f=open('agenda.csv','r')
# Lee el contenido del archivo y colócalo en una variable
# llamada contenido. Utiliza read().
contenido=f.read()
# Cierra el archivo. Utiliza close()
f.close()
# Muestra el contenido del archivo, que ya tienes en una variable.
print(contenido)
