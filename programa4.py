#Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los
#atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla
#Triangulo.

class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        print("Lado mayor:", max(self.lado1,self.lado2,self.lado3))

    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")

# Bloque principal

# Obtener los lados del triángulo
lado1 = float(input("Ingrese el valor del primer lado:"))
lado2 = float(input("Ingrese el valor del segundo lado:"))
lado3 = float(input("Ingrese el valor del tercer lado:"))

#creamos un objeto llamado triangulo
triangulo = Triangulo(lado1, lado2, lado3)

#imprimiremos los valores
triangulo.lado_mayor()
triangulo.es_equilatero()