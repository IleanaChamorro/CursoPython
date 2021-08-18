class Producto:
    contador_productos = 0
    
    #Metodo inicializador
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio {self._precio}'

    @property
    def precio(self):
        return self._precio
        
    #Solo ejecutar la prueba si es desde este mismo archivo o modulo, de lo contrario no se ejecuta
if __name__ == '__main__':
        producto1 = Producto('Remera', 1000)
        print(producto1)
        #Id Producto: 1, Nombre: Remera, Precio 1000