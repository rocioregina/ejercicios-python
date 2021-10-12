import math

class CustomError(Exception):
    pass

class ValueIsZero(CustomError):
    #excepcion custom
    def __init__(self, message="Numero invalido"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

def verifyValue(num):
    #esta funcion verifica que el valor ingresado sea mayor a cero
    try:
        if(num <= 0):
            raise ValueIsZero
    except ValueIsZero:
        print("Numero invalido : {}".format(num), ". Debe ser mayor a cero.")
    else:
        return num

class Circulo:

    def __init__(self, radius):
        self.__radio = radius

    def __str__(self):
        #este string se retorna al imprimir el objeto
        return "Radio: " + str(self.__radio) + ". Area: " + str(self.getArea()) + ". Perimetro: " + str(self.getPerimeter())

    def setRadius(self):
        radius = int(input("Ingrese un radio: "))
        if(verifyValue(radius)):
            self.__radio = radius

    def getArea(self):
        return math.pi * pow(self.__radio, 2)

    def getPerimeter(self):
        return 2 * math.pi * self.__radio

    def multiply(self, n):
        if(verifyValue(n)):
            return Circulo(self.__radio * n)
