import math

class ValueIsZero(Exception):

    def __init__(self, message="El radio debe ser mayor a cero."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class Circulo:

    def __init__(self, radius):
        self.__radio = radius

    def setRadius():
        try:
            radius = int(input("Ingrese un radio: "))
            if (radius <= 0):
                raise ValueIsZero
            else:
                self.__radio = radius
            break
        except ValueIsZero:
            print("El radio debe ser mayor a cero. Ingrese otro valor: ")

    def getArea(self):
        return math.pi * pow(self.__radio, 2)

    def getPerimeter(self):
        return 2 * math.pi * self.__radio

#prueba
radius = int(input("Ingrese un radio para el nuevo circulo: "))
try:
    if(radius <= 0):
        raise ValueIsZero
    else:
        newCircle = Circulo(radius)
        print(newCircle.getArea())
        print(newCircle.getPerimeter())
    break
except ValueIsZero:
    print("El radio debe ser mayor a cero. Ingrese otro valor: ")
