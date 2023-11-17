#Problema 1:
#Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos
#(funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el
#contenido del mismo.
#Definir dos objetos de la clase Persona.

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print("Nombre:", self.nombre)

# Crearemos dos objetos de la clase Persona para verlo
persona1 = Persona("Carlos")
persona2 = Persona("Alondra")

# Mostraremos el contenido para cada persona
persona1.mostrar_nombre()
persona2.mostrar_nombre()