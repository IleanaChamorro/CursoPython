from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica

figura = FiguraGeometrica() #TypeError: Can't instantiate abstract class FiguraGeometrica with abstract method calcular_area


cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.ancho) #5
print(cuadrado1.alto) #5
print(cuadrado1.color) #rojo
print(cuadrado1.calcular_area()) #25
print(cuadrado1)
#MRO - Method Resolution Order - nos permite saber la jerarquia de clases
#print(Cuadrado.mro()) #[<class 'Cuadrado.Cuadrado'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 


rectangulo1 = Rectangulo(3, 8, 'verde')