#Ejercicio Valor dentro del Rango
valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 13

dentroRango = (valor >= valorMinimo ) and (valor <= valorMaximo)

if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
        print(f'el valor {valor} esta fuera de rango')