#Un mismo operador puede trabajar de diferentes formas, esto se llama sobrecarga de operadores

#operador +
a = 2
b = 3
print(a + b)#5

a = 'Hola'
b = 'Mundo'
print( a + b) #HolaMundo, en este ejemplo en vez de obtener una suma se obtiene una concatenacion

a = [1, 2, 3]
b = [6 , 7, 8]
print(a + b) #[1, 2, 3, 4, 5, 6, 7, 8] - Se obtiene el valor de ambas listas a una sola

#Todo lo anterior tambien se puede usar en clases usando metodos de sobrecarga
#+ - __add__(self, other)
#- / __sub__(self, other)
#* / __mul__(self, other)
# / , __truediv__(self, other)
# // __floordiv__(self, other)
# % , __mod__(self, other)
# **, __pow__(self, other)

#Metodos de sobrecarga con un solo operando
# -, __neg__(self, other)
# +, __pos__(self, other)
# ~, __invert__(self, other)

