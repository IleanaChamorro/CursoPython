class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Sobrecargar el metodo
    def __add__(self, other):
        return self.nombre + other.nombre
    
    def __sub__(self, otro):
        return self.edad - otro.edad

persona1 = Persona('Juan', 22)
persona2 = Persona('Carlos', 12)
print(persona1 + persona2)#JuanCarlos
print(persona1 - persona2) #10
#obj1 + obj2 
#(es equivalente a obj1.__add__(obj2)