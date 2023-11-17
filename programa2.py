#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para
#inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
#Definir dos objetos de la clase Alumno.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def mostrar_estado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")

# Bloque principal

# Crear dos objetos de la clase Alumno
alumno1 = Alumno("Sergio", 6)
alumno2 = Alumno("Rosalva", 3)

# Analizar los datos de cada uno
print("Datos del alumno 1:")
alumno1.imprimir()
alumno1.mostrar_estado()

print("Datos del alumno 2:")
alumno2.imprimir()
alumno2.mostrar_estado()
