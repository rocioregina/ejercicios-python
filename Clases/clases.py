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

def verify_value(num: float):
    #esta funcion verifica que el valor ingresado sea mayor a cero
    try:
        if(num <= 0):
            raise ValueIsZero
    except ValueIsZero:
        print("Numero invalido : {}".format(num), ". Debe ser mayor a cero.")
    else:
        return num

class Circulo:

    def __new__(cls, num: int, *args, **kwargs):
        """
        Testea la funcion que llama al constructor del circulo

        - Intentando instanciar un circulo con radio mayor a cero
        >>> circle1 = Circulo(3)
        >>> print(circle1)
        Radio: 3 m. Area: 28.274333882308138 m2 . Perimetro: 18.84955592153876 m.

        - Intentando instanciar circulos con radio menor o igual a cero
        >>> circle2 = Circulo(-5)
        Numero invalido : -5 . Debe ser mayor a cero.
        >>> circle3 = Circulo(0)
        Numero invalido : 0 . Debe ser mayor a cero.
        """
        if(verify_value(num)):
            return super().__new__(cls, *args, **kwargs)

    def __init__(self, radius: int):
        self.__radio = radius

    def __str__(self):
        """
        Testea el metodo str que es invocado al imprimir el objeto
        >>> circle = Circulo(1)
        >>> print(circle)
        Radio: 1 m. Area: 3.141592653589793 m2 . Perimetro: 6.283185307179586 m.
        """
        return "Radio: " + str(self.__radio) + " m. Area: " + str(self.get_area()) + " m2 . Perimetro: " + str(self.get_perimeter()) + " m."

    def set_radius(self, radius: float):
        """
        Testea el metodo que modifica el radio del circulo:
        >>> circle = Circulo(2)

        - Seteando un radio positivo
        >>> circle.set_radius(3)

        - Seteando un radio negativo
        >>> circle.set_radius(-1)
        Numero invalido : -1 . Debe ser mayor a cero.
        """
        if(verify_value(radius)):
            self.__radio = radius

    def get_area(self):
        """
        Testea el metodo que devuelve el area del circulo:

        - Obteniendo el area de dos circulos creados
        >>> circle1 = Circulo(2)
        >>> circle1.get_area()
        12.566370614359172
        >>> circle2 = Circulo(5)
        >>> circle2.get_area()
        78.53981633974483
        """
        return math.pi * pow(self.__radio, 2)

    def get_perimeter(self):
        """
        Testea el metodo que devuelve el perimetro del circulo:

        - Obteniendo el perimetro de dos circulos creados
        >>> circle1 = Circulo(2)
        >>> circle1.get_perimeter()
        12.566370614359172
        >>> circle2 = Circulo(5)
        >>> circle2.get_perimeter()
        31.41592653589793
        """
        return 2 * math.pi * self.__radio

    def multiply(self, n: float):
        """
        Testea el metodo que multiplica un circulo:

        -Multiplicando por un numero mayor a cero
        >>> circle = Circulo(2)
        >>> circle2 = circle.multiply(3)
        >>> print(circle2)
        Radio: 6 m. Area: 113.09733552923255 m2 . Perimetro: 37.69911184307752 m.

        -Multiplicando por un numero menor a cero
        >>> circle = Circulo(2)
        >>> circle2 = circle.multiply(-1)
        Numero invalido : -1 . Debe ser mayor a cero.
        >>> print(circle2)
        None
        """
        if(verify_value(n)):
            return Circulo(self.__radio * n)

if(__name__ == "__main__"):
    import doctest
    doctest.testmod(verbose=True)
