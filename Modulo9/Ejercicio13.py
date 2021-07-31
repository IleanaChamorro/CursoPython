#Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo

class Vehiculo(color, ruedas):
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", Velocidad (km/hr): " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, tipo):
        super().__init__(color,ruedas, velocidad, tipo)
        self.tipo = tipo

vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)

coche = Coche("Azul", 4, 150)
print(coche)

bicicleta = Bicicleta("Blanca", 2, "Urbana")
print(bicicleta)