#Solicitar al usuario que escriba la informacion de cierto libro (nombre, id, precio, indicar si el envio es gratuito)
print('Proporcione los siguiente datos del libro: ')
nombre = input("Proporciona el nombre: ")
id = int(input("Proporciona el id: "))
#precio = input("Proporciona el precio: ")
precio = float(input("Proporciona el precio: "))
envio = input("Indica si el envio es gratuito (True/false): ")
if envio == "True":
        print("El envio es gratuito")
if envio == "False":
        print("El envio no es gratuito")

print(f'''
    Nombre: {nombre}
    id: {id}
    precio: {precio}
    envio: {envio} 
''')