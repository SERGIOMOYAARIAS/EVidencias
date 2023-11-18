import os

archivo = "colores.txt"

if os.path.exists(archivo):
    print("\nEl archivo ya existe")
else:
    print("\nEl archivo no existe")