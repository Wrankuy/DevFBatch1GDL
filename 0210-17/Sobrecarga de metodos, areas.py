class figura(object):

    def area(self,area):
        return area
    def area(self):
        raise NotImplementedError("subclass must implement abstract method")


class Circulo(figura):
    def __init__(self, r):

        self.r = r

    def calcular_area(self,r,a):
        r = 5
        a= 3.1415916 * r * r
        return a

class Triangulo(figura):
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b*self.h)/2


class Cuadrado(figura):
    def __init__(self, l):
        self.l= l

    def area(self):

        return self.l*self.l

triangu_1 = Triangulo(5,10)
#print triangu_1.area()

cuadr_1= Cuadrado(6)
print cuadr_1.area()