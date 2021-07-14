#La estructura de control if ... permite que un programa ejecute unas instrucciones cuando se cumplan una condición.
#La ejecución de esta construcción es la siguiente: La condición se evalúa siempre - Si el resultado es True se ejecuta el bloque de sentencias, Si el resultado es False no se ejecuta el bloque de sentencias

condicion = True

if condicion: 
    print('Condición verdadera') #Devuelve - True
else:
    print('Condición falsa')


condicion = 'hola'

if condicion == True:
    print('Condición verdadera')
elif condicion == False: 
    print('Condicion Falsa')
else: 
    print('Condicion no reconocida')

#Sintaxis simplificada
condicion = True

print('Condición verdadera') if condicion else print('Condición falsa')