from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    #Indicar cual es el tipo de dato que estamos imprimiendo al momento de la ejecucion
    print(type(objeto))

empleado = Empleado('Juan', 5000)
imprimir_detalles(Empleado)
print(empleado) 
#Empleado: [Nombre: Juan, Sueldo: 5000]
#<class 'Empleado.Empleado'>
#<class 'type'>

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
#Gerente [Departamento: Sistemas] Empleado: [Nombre: Karla, Sueldo: 6000]
#<class 'Gerente.Gerente'>