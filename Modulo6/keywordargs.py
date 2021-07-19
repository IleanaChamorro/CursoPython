def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='integrated developement environment') #IDE: integrated developement environment
listarTerminos(DBMS='DataBase Management System') #DBMS: DataBase Management System