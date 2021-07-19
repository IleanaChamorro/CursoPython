# Sets => a estructura de datos usada para almacenar elementos de una manera similar a las listas, pero con ciertas diferencias.
#   -Los elementos de un set son únicos, son desordenados, sus elementos deben ser inmutables

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
#largo
print(len(planetas)) #3
#revisar si un elemento esta presente 
print('Marte' in planetas) #true
#Agregar un elemento
planetas.add('Tierra')
print(planetas) #{'Tierra', 'Marte', 'Venus', 'Jupiter'}
#No se pueden duplicar elementos
planetas.add('Tierra') #{'Jupiter', 'Tierra', 'Marte', 'Venus'}
print(planetas)
#Eliminar elemento
planetas.remove('Tierra')
print(planetas) #{'Jupiter', 'Venus', 'Marte'}

planetas.discard('Jupiter')
print(planetas) #{'Marte', 'Venus'}