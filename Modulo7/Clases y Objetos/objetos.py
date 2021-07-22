
    #init - permite añadir atributos a nuestra clase e inicializarlos
    #self - parametro por default (self-referencia del objeto mismo)
    #def __init__(self):
       # pass
    #def __str__(self):
      #  pass
    #def __repr__(self):
     #   pass

class Persona: 
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Juan', 'Perez', 28)
print(f'Objeto Persona1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}')
#Objeto Persona1: Juan, Perez, 28

#Modificar Atributos
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 25 
print(f'Objeto Persona1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}')
#Objeto Persona1: Juan Carlos, Juarez, 25

#Creación de Objetos
persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto Persona2: {persona2.nombre}, {persona2.apellido}, {persona1.edad}')
#Objeto Persona2: Karla, Gomez, 30