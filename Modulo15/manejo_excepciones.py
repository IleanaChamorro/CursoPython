#10/0 
#ZeroDivisionError: division by zero, error subclase 'Aritmetic Error'

#Procesar el codigo sin error
try:
    10/0
except Exception as e:
    print(f'Ocurrio un error {e}') #Ocurrio un error division by zero