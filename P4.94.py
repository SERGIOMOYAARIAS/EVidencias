#SERGIO SMITH MOYA ARIAS
import os

archivo = "colores.txt"

with open(archivo, "a+") as f:
    # El archivo se abre automáticamente en el bloque 'with'
    pass  # Puedes realizar operaciones adicionales dentro de este bloque si es necesario

# Verificación de que ya se creó.
if os.path.exists(archivo):
    print("\nEl archivo ya existe")
else:
    print("\nEl archivo no existe")
