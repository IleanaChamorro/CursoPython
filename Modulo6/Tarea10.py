#Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.

def sumaNumeros(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumaNumeros(1,2,3,4,5,6,7,8,9,10))