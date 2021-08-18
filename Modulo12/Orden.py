from Producto import Producto
class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        #Conversion y asignacion a lista
        self._productos = list(productos)

    def agregar_productos(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        #Variable que almacena el valor total temporal
        total = 0
        #Por cada producto en la lista, se va asignando el valor parcial
        for producto in self._productos:
            total += producto.precio
            #Cuando termina de iterar los productos se almacena el valor final en la variable producto
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, Productos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Remera', 900)
    producto2 = Producto('Jean', 2000)
    print(producto2) #Id Producto: 2, Nombre: Jean, Precio 2000
