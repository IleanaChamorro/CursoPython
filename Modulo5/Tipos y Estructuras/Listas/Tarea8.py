#Consigna => Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)