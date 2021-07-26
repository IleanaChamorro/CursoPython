# Encapsulamiento - consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.
class Persona:
    def __init__(self, nombre, apellido, edad):
        #Atributo encapsulado
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #Decorador
    @property #puede ser usado para modificar un método para que sea un atributo o propiedad
    def nombre(self):
         #Metodo get
        return self._nombre

    @nombre.setter
    def nombre(self):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad} ')

persona1 = Persona('Juan', 'Perez', 28)
print(persona1.nombre) #Juan

persona1._nombre = 'Juan Carlos'
print(persona1.nombre)  #Juan Carlos