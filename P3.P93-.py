import os

archivo = "colores.txt"

if os.path.exists(archivo):
    os.remove(archivo)
    print("\nEl archivo se eliminó")
else:
    print("\nEl archivo no existe. No se eliminó nada.")