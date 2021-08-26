from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    #Contabilizar Objetos 
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        #Incrementar variable de clase 
        Teclado.contador_teclados += 1 
        self._id_teclado = Teclado.contador_teclados
        #Llamada metodo init clase Padre
        super().__init__(marca, tipo_entrada)

        def __str__(self):
            return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'

teclado1 = Teclado('HP', 'USB')
print(teclado1)
teclado2 = Teclado('Gamer', 'Bluetooth')
print(teclado2)