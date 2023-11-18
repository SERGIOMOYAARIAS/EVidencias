#SERGIO SMITH MOYA ARIAS
Datos = []

with open("agenda.csv", "r+") as f:
    for linea in f:
        lista = linea.split("|")
        lista[2] = lista[2].replace("\n", "")
        Datos.append(lista)

# Se revisa el contenido de la lista
print(">> Contenido de la nueva lista.\n")
print(Datos)
