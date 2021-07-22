class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo

ancho = int(input('Proporciona el ancho: ')) #3
alto = int(input('Proporciona el alto')) #5
profundo = int(input('Proporciona lo profundo: ')) #6

cubo1 = Cubo(ancho, alto, profundo)
print(f'Volumen cubo: {cubo1.calcular_volumen()}') #90