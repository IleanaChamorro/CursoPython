#Herencia  
# Ejemplo objeto Persona - crear una subclase 'hija' que herede las caracteristicas de clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}'

empleado1 = Empleado('Juan',28,5000)
print(empleado1.nombre) #Juan
print(empleado1.edad) #28
print(empleado1.sueldo)#5000
