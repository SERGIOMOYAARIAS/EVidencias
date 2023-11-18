# Se hablilita el trabajo con el sistema operativo
import os
# Obtener la ruta de trabajo actual
# (Current Working Directory)
ruta=os.getcwd()
print(ruta)
# Obtiene el valor absoluto de la ruta
ruta_absoluta=os.path.abspath(ruta)
print(ruta_absoluta)