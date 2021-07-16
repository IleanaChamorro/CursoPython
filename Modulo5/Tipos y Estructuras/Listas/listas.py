#Listas - tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas.

#Crear lista
lista = ['Harry', 'Ron', 'Hermione']

#Acceder a elementos usando corchetes y un índice
print(lista[0]) #Harry

#Acceder ultimo elemento usando el índice [-1].
print(lista[-1]) #Hermione

#Modificar elementos lista
lista[2] = 'Draco Malfoy'
print(lista) #['Harry', 'Ron', 'Draco Malfoy']

#Eliminar elementos
del lista[1]
print(lista) #['Harry', 'Draco Malfoy']

#Borrar lista por completo
del lista

#Listas anidadas
lista2 = ['Harry', 'Draco Malfoy' ,['Luna Lovegood', 'Severus Snape', ['Dobby', 'Lord Voldemort']]]
print(lista2[2][0]) #Luna Lovegood

#Modificar multiples valores mediante ":" - indicar a la izquierda el valor de inicio y a la derecha el valor final que no está incluido
lista = ['Harry', 'Ron', 'Hermione']
lista[0:2] = ['Luna Lovegood', 'Severus Snape']
print(lista) #['Luna Lovegood', 'Severus Snape', 'Hermione']

#Iterar Lista
lista = ['Harry', 'Ron', 'Hermione']
for lista in lista: 
    print(lista)
#Harry
#Ron
#Hermione

#Preguntar largo de una lista
lista = ['Harry', 'Ron', 'Hermione']
print(len(lista)) #3

#Agregar un elemento
lista.append('Luna Lovegood')
print(lista) #['Harry', 'Ron', 'Hermione', 'Luna Lovegood']

#Insertar un elemento en un indice especifico
lista = ['Harry', 'Ron', 'Hermione']
lista.insert(1, 'Dobby')
print(lista) #['Harry', 'Dobby', 'Ron', 'Hermione']
#remover un elemento
lista.remove('Dobby')
print(lista) #['Harry', 'Ron', 'Hermione']
#limpiar lista
lista.clear()
print(lista) #[]