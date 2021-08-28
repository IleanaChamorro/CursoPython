#Manejo de excepciones
#Try => Este bloque probará que ocurra el error exceptuado
#Except: Manejo del error en esta porcion del codigo
#Else: Si no hay excepción, este bloque se ejecutará
#Finally: El bloque siempre se ejecuta, ya sea que se genere una excepcion o no

#10/0 
#ZeroDivisionError: division by zero, error subclase 'Aritmetic Error'

#Procesar el codigo sin error
try:
    10/0
except Exception as e:
    print(f'Ocurrio un error {e}') #Ocurrio un error division by zero


resultado = None
a = 10
b = 0
try:
    resultado = a / b
except Exception as e:
    print(f'Ocurrio un error: {e}')

print(f'Resultado: {resultado}')#Resultado: None
print('Continuamos...')#Continuamos...

#Otro tipo de excepcion
resultado = None
a = '10'
b = 0
try:
    resultado = a / b
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error: {e}, {type(e)}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecuccion del bloque finally')
    
print(f'Resultado: {resultado}')#TypeError: unsupported operand type(s) for /: 'str' and 'int'
print('Continuamos...')#Continuamos...