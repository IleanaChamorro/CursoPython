#Se le solicita al usuario ingresar un valor numerico, dependiendo de tal valor devuelve la etapa de la vida en la cual esta  
edad = int(input('Proporciona tu edad: '))
mensaje = None

if edad <= 0 or edad < 10:
    mensaje = 'La infancia es increible'
elif edad <= 1 or edad < 20:
    mensaje = 'Muchos cambios y mucho estudio'
elif edad >= 20 or edad < 30:
    mensaje = 'Amor y comienza el trabajo'
else:
    mensaje = 'Etapa de vida no reconocida'

print(f'Tu edad es: {edad}, {mensaje}')