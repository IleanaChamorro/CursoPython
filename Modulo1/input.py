#Función input para procesar la entrada del usuario
resultado = input("Escribe un mensaje: ")
print("valor proporcionado: ", resultado)
print("Fin código")

#Conversion De Entrada de Datos
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

#Solicitar al usuario que escriba la informacion de cierto libro (nombre, id, precio, indicar si el envio es gratuito)
print('Proporcione los siguiente datos del libro: ')
nombre = input("Proporciona el nombre: ")
id = int(input("Proporciona el id: "))
#precio = input("Proporciona el precio: ")
precio = float(input("Proporciona el precio: "))
envio = input("Indica si el envio es gratuito (True/false): ")
  