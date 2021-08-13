#Ejercicio contador de personas, el cual le asigna un id a cada uno
class Persona: 
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Juan', 28)
persona2 = Persona('Karla', 50)
print(persona1) #Persona [1 Juan 28]
print(persona2) #Persona [2 Karla 50]

print(f'Valor contador personas: {Persona.contador_personas}') #Valor contador personas: 2