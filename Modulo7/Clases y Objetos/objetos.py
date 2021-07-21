
    #init - permite añadir atributos a nuestra clase e inicializarlos
    #self - parametro por default (self-referencia del objeto mismo)
    #def __init__(self):
       # pass
    #def __str__(self):
      #  pass
    #def __repr__(self):
     #   pass

class Persona: 
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28

persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(type(Persona))