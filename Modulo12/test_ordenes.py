from Orden import Orden
from Producto import Producto


producto1 = Producto('Remera', 900)
producto2 = Producto('Jean', 2000)
producto3 = Producto('Camisa', 3000)
producto4 = Producto('Medias', 1000)

#Listas producto
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
#Orden: 1, Productos: Id Producto: 1, Nombre: Remera, Precio 900|Id Producto: 2, Nombre: Jean, Precio 2000|
print(orden1)
print(f'Total orden1: {orden1.calcular_total()}') #Total orden1: 2900