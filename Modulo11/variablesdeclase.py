#Las variables de clase se asocian directamente con la clase misma y no con los objetos

class miclase:
    #Esta variable se va asociar con la clase misma
    variables_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        #Esta variable de instancia se asocia a cada uno de los objetos
        self.variables_instancia = variable_instancia

print(miclase.variables_clase) #Valor variable clase

#Para acceder a la variable de instancia debe existir un objeto
miClase = miclase('Valor variable instancia')
print(miClase.variables_instancia) #Valor variable instancia
#Acceder a la variable de clase desde el objeto
print(miClase.variables_clase) #Valor variable clase