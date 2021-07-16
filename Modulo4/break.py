#La sentencia break nos permite alterar el comportamiento de los bucles while y for. Concretamente, permite terminar con la ejecución del bucle.

#Break en ciclo for
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)

# Salida:
# P
# y
# t
# Se encontró la h

#Break en ciclo while
#La condición while True haría que la sección de código se ejecutara indefinidamente, pero al hacer uso del break, el bucle se romperá cuando x valga cero.
x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")

#4, 3, 2, 1, 0