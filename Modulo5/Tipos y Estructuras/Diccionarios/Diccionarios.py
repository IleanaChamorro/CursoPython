#colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value.

diccionario = {
        'IDE': 'Integrated Development Environment',
        'OOP': 'Object Oriented Programming',
        'DBMS': 'Database Management System'
    }
print(diccionario)
#Otra forma equivalente de crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis
d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])

#También es posible usar el constructor dict() para crear un diccionario.
d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882)


#Conocer el largo
print(len(diccionario))

#Acceder a elementos(key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

#Modificar elementos 
diccionario['IDE'] = 'integrated development enviroment'

#Recorrer los elementos
for termino, valor  in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Comprobar existencia de algún elemento
print('IDE' in diccionario)

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#remover un elemento 
diccionario.po('DBMS')
print(diccionario)

#limpiar
diccionario.clear()

#eliminar el diccionario
del diccionario