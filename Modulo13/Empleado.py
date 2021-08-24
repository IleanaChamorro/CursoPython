#Polimorfismo - Multiples formas en tiempo de ejecucion, (Una variable podria ejecutar varios metodos, de distintos objetos dependiendo el objeto al cuál esta apuntando en tiempo de ejecucion) 

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'
        
    def mostrar_detalles(self):
        return self.__str__()