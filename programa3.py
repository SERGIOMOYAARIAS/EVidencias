#Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. 
#Imprimir unmensaje si es mayor de edad (edad>=18)
#SERGIO SMITH MOYA ARIAS

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")

# Bloque principal

#datos de la persona
persona1 = Persona("Smith", 19)

#Mostraremos los datos con las siguientes lineas
print("Datos de la persona:")
persona1.mostrar_datos()
persona1.es_mayor_de_edad()