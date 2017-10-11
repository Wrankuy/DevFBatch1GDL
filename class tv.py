class Television:
    def __init__(self, marca, definicion, tamanio, curva, precio):
        self.marca= marca
        self.tamanio= tamanio
        self.precio = precio
        self.definicion= definicion
        self.curva= curva

    def marca_tv(self):
       return "{}".format(self.marca)

    def tamanio_tv(self):
         return self.tamanio

    def precio_tv(self):
         return self.precio

    def definicion_tv(self):
        return self.definicion

    def curva_tv(self):
         return self.definicion

    def detalles(self):
        return "    Marca : \t{}\n Tamanio: \t \n Precio: \t{}\n Definicion \t{} \n Curva: \t{}".format(self.marca, self.tamanio, self.precio, self.definicion, self.curva)

tv1 = Television("samsung", "60", 50000, "4k", "Y")
tv2 = Television("LG", "55", 40000, "4k", "N")
tv3 = Television("sony", "70", 60000, "1080p", "N")


#print tv1.marca_tv()
#print Television.precio_tv(tv1)
#print Television.tamanio_tv(tv1)

#print tv2.marca_tv()
#print Television.precio_tv(tv2)
#print Television.tamanio_tv(tv2)


#print tv3.marca_tv()
#print Television.precio_tv(tv3)
#print Television.tamanio_tv(tv3)

print Television.detalles(tv1)
print tv2.detalles()
print Television.detalles(tv3)
