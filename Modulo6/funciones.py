#Funciones 
#Sintaxis básica
#def nombre_funcion(argumentos):
    #código
    #return retorno

def mi_funcion():
    print('saludos desde función')

mi_funcion()#saludos desde función

#Pasando argumentos de entrada
def mi_funcion2(nombre, apellido):
    print(f'Nombre: {nombre}, Apellido: {apellido}')
mi_funcion2('Juan', 'Perez')
mi_funcion2('Karla', 'Lara')

#Uso return
def sumar(a,b):
    return a + b

resultado = sumar(5 , 3)
print(f'Resultado sumar: {resultado}') #8

#Argumentos de longitud variable
#Si declaramos un argumento con *, esto hará que el argumento que se pase sea empaquetado en una tupla de manera automática y poder iterarls.

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')
#Juan
#Karla
#Maria
#Ernesto
#Laura
#Carlos