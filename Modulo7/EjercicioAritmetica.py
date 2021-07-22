class Aritmetica:
    """"
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def division(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)
print(f'Suma: {aritmetica1.sumar()}') #8
print(f'Resta: {aritmetica1.restar()}') #2
print(f'Multiplicacion: {aritmetica1.multiplicar()}') #15
print(f'Division: {aritmetica1.division():.2f}') #1.67