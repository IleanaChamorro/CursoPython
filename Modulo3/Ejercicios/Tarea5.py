#Consigna - Crear un sistema de calificaciones según se solicita
#El Usuario proporcionará un valor entre 0 y 10
#Si está entre 9 y 10: Imprimir una A, Si está entre 8 y menor a 9: imprimir una B, Si está entre 7 y menor a 8: imprimir una C, Si está entre 6 y menor a 7: imprimir una D, si esta entre 0 y menor a 6: imprimir una F

nota = int(input('Ingresa tu calificacion entre 0 y 10: '))
calificacion = None

if nota <= 0 or nota < 6:
    calificacion = 'F'
elif nota == 6 or nota < 7:
    calificacion = 'D'
elif nota == 7 or nota < 8:
    calificacion = 'C'
elif nota == 8 or nota < 9:
    calificacion = 'B'
elif nota == 9 or nota == 10:
    calificacion = 'A'
else:
    print('Valor desconocido')
print(f'Tu calificación es: {calificacion}')