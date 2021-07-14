#Ejercicio - Determina si es mayor de edad
edadAdulto = 18
edadPersona = int(input("Proporciona tu edad: "))

if edadPersona >= edadAdulto:
    print(f'La persona con edad {edad} es un adulto')
else:
    print(f'La persona con edad{edadPersona} es menor de edad')