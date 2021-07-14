#Ejercicio Practica rango entre 20's y 30's

edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad <30
print(veintes)
treintas = edad >= 30 and edad <40
print(treintas)

if veintes or treintas:
    #print('Dentro de rango (20s) o (30s)')
    if veintes:
        print('Dentro de los 20')
    elif treintas:  
        print('Dentro de los 30')
    else:
        print('Fuera de rango')
else:
    print("No esta dentro de los 20 ni 30")