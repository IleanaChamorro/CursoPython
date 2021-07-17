#Tupla (tuple) 
#tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables (no pueden ser modificadas una vez declaradas).

#Definir una tupla
frutas = ('Naranja', 'Banana', 'Sandía')

#Saber el largo
print(len(frutas)) # 3

#Acceder a un elemento
print(frutas[0]) #Naranja

#Navegación inversa
print(frutas[-1]) #Sandía

#Acceder a un rango
print(frutas[0:1]) #('Naranja',)

#Recorrer elementos
for fruta in frutas:
    print(fruta, end= '')#NaranjaBananaSandía
#Naranja
#Banana
#Sandía

#Cambiar valor tupla
frutas[0] = 'Pera'
print(frutas) #Si se intenta modificar, tendremos un TypeError

#Cambiar tupla a lista
frutasLista = list(frutas)
#Al ser una lista, sus elementos pueden ser modificados
frutasLista[0] = 'Pera'
#Convertir lista a tupla
frutas = tuple(frutasLista)
print(frutas)
print('\n', frutas)
#eliminar la tupla
del frutas