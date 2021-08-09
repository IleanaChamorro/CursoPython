from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectagulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str_(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'