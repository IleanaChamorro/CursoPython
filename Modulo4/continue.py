#Termina la ejecución de las sentencias de la iteración actual del bucle actual o la etiqueta y continua la ejecución del bucle con la próxima iteración.
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)
