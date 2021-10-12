import random

def createMatrix(columns=5, rows=5):
    """
    Testea la funcion que crea una matriz:

    - Creando una matriz randomizada (utilizando seed)
    >>> random.seed(5)
    >>> columns = 5
    >>> rows = 5
    >>> createMatrix(columns, rows)
    [[5, 3, 3, 5, 1], [4, 2, 1, 2, 1], [3, 4, 2, 4, 5], [1, 5, 2, 1, 2], [4, 3, 2, 4, 2]]

    - Accediendo a una posicion de una matriz creada
    >>> random.seed(5)
    >>> matriz = createMatrix(columns, rows)
    >>> matriz[0][4]
    1

    - Accediendo a una posicion inexistente de una matriz creada
    >>> matriz = createMatrix(columns, rows)
    >>> matriz[3][6]
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    """
    matrix = [[random.randint(1, 5) for x in range(columns)] for y in range(rows)]
    return matrix

def findSequence(matrix=[], sequence=4):
    """
    Testea la funcion que halla una secuencia:

    - Buscando una secuencia de 4 en una matriz que no posee ninguna
    >>> columns = 5
    >>> rows = 5
    >>> sequence = 4
    >>> random.seed(5)
    >>> findSequence(createMatrix(columns, rows), sequence)
    -1

    - Buscando una secuencia de 4 en una matriz que posee una horizontal
    >>> matrizPruebaHorizontal = [[5, 3, 1, 5, 1], [4, 2, 2, 2, 1], [3, 4, 3, 4, 5], [1, 5, 4, 1, 2], [4, 3, 2, 4, 2]]
    >>> findSequence(matrizPruebaHorizontal, sequence)
    {'initial': [0, 2], 'final': [3, 2]}

    - Buscando una secuencia de 4 en una matriz que posee una horizontal
    >>> matrizPruebaVertical = [[5, 3, 4, 5, 1], [4, 2, 1, 2, 1], [3, 4, 3, 4, 5], [1, 1, 2, 3, 4], [4, 3, 2, 4, 2]]
    >>> findSequence(matrizPruebaVertical, sequence)
    {'initial': [3, 1], 'final': [3, 4]}
    """
    #esta solucion funciona solo cuando la cantidad de filas es la misma que de columnas
    for x in range(len(matrix)):
        y = 0
        while (y <= len(matrix[x]) - sequence):
            foundVertical = 1 #cantidad de numeros consecutivos encontrados en la iteracion
            foundHorizontal = 1

            #buscando verticalmente
            auxIndex = y
            while (foundVertical < sequence) and (matrix[x][auxIndex] == matrix[x][auxIndex + 1] - 1):
                auxIndex += 1
                foundVertical += 1
            if(foundVertical == sequence): #si while corta por hallar 4 consecutivos
                return {"initial": [x, y], "final": [x, auxIndex]}

            #buscando horizontalmente
            auxIndex = y
            while (foundHorizontal < sequence) and (matrix[auxIndex][x] == matrix[auxIndex + 1][x] - 1):
                auxIndex += 1
                foundHorizontal += 1
            if(foundHorizontal == sequence): #si while corta por hallar 4 consecutivos
                return {"initial": [y, x], "final": [auxIndex, x]}
            y += 1
    return -1

if(__name__ == "__main__"):
    import doctest
    doctest.testmod()
