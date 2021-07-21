#una función recursiva es aquella que está definida en función de sí misma, por lo que se llama repetidamente a sí misma hasta llegar a un punto de salida.
#Cualquier función recursiva tiene dos secciones de código claramente divididas:
# - Por un lado tenemos la sección en la que la función se llama a sí misma.
# Por otro lado, tiene que existir siempre una condición en la que la función retorna sin volver a llamarse. Es muy importante porque de lo contrario, la función se llamaría de manera indefinida.
 
#Ejemplo
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(5)
print(f'El factorial de 5 es {resultado}') #El factorial de 5 es 120