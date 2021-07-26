# Encapsulamiento - consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.
class Persona:
    def __init__(self, nombre, apellido, edad):
        #Atributo encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #Decorador
    @property #puede ser usado para modificar un método para que sea un atributo o propiedad
    def nombre(self):
         #Metodo get
        return self._nombre

    @nombre.setter
    def nombre(self):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
            return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad 

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} ')

    #Metodo destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

#Solo si esta dentro de main ejecutar el siguiente codigo
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    print(persona1.nombre) #Juan

    persona1._nombre = 'Juan Carlos'
    print(persona1.nombre)  #Juan Carlos

    persona1.apellido = 'Lara'
    persona1.edad = 30
    persona1.mostrar_detalle()#Persona: Juan Carlos Lara 30 

print(__name__) #Nombre del modulo - __main__