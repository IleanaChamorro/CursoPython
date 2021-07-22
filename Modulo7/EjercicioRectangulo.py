class Rectangulo: 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base  * self.altura


base = int(input('Proporciona la base: ')) #10
altura = int(input('Proporciona la altura: ')) # 5

rectangulo1 = Rectangulo(base, altura)
print(f'Area Rectangulo: {rectangulo1.calcular_area()}') #50