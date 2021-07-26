from encapsulamiento import Persona

print('Creacion Objetos'.center(50, '-'))
#-----------------Creacion Objetos-----------------
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()
#Juan
#Juan Carlos
#Persona: Juan Carlos Lara 30 
#Persona: Karla Gomez 30 

print('Eliminacion objetos'.center(30 , '-'))
#-----Eliminacion objetos------
del persona1 #Persona: Karla Gomez