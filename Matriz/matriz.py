import random

def create_matrix(columns:int, rows: int):
    """
    Testea la funcion que crea una matriz:

    - Creando una matriz randomizada (utilizando seed)
    >>> random.seed(5)
    >>> columns = 5
    >>> rows = 5
    >>> create_matrix(columns, rows)
    [[5, 3, 3, 5, 1], [4, 2, 1, 2, 1], [3, 4, 2, 4, 5], [1, 5, 2, 1, 2], [4, 3, 2, 4, 2]]

    - Accediendo a una posicion de una matriz creada
    >>> random.seed(5)
    >>> matriz = create_matrix(columns, rows)
    >>> matriz[0][4]
    1

    - Accediendo a una posicion inexistente de una matriz creada
    >>> matriz = create_matrix(columns, rows)
    >>> matriz[3][6]
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    """
    matrix = [[random.randint(1, 5) for x in range(columns)] for y in range(rows)]
    return matrix

def find_sequence(matrix: list, sequence: int):
    """
    Testea la funcion que halla una secuencia:

    - Buscando una secuencia de 4 en una matriz que no posee ninguna
    >>> columns = 5
    >>> rows = 5
    >>> sequence = 4
    >>> random.seed(5)
    >>> find_sequence(create_matrix(columns, rows), sequence)
    -1

    - Buscando una secuencia de 4 en una matriz que posee una horizontal
    >>> matriz_prueba_horizontal = [[5, 3, 1, 5, 1], [4, 2, 2, 2, 1], [3, 4, 3, 4, 5], [1, 5, 4, 1, 2], [4, 3, 2, 4, 2]]
    >>> find_sequence(matriz_prueba_horizontal, sequence)
    {'initial': [0, 2], 'final': [3, 2]}

    - Buscando una secuencia de 4 en una matriz que posee una horizontal
    >>> matriz_prueba_vertical = [[5, 3, 4, 5, 1], [4, 2, 1, 2, 1], [3, 4, 3, 4, 5], [1, 1, 2, 3, 4], [4, 3, 2, 4, 2]]
    >>> find_sequence(matriz_prueba_vertical, sequence)
    {'initial': [3, 1], 'final': [3, 4]}
    """
    #esta solucion funciona solo cuando la cantidad de filas es la misma que de columnas
    for x in range(len(matrix)):
        y = 0
        while (y <= len(matrix[x]) - sequence):
            found_vertical = 1 #cantidad de numeros consecutivos encontrados en la iteracion
            found_horizontal = 1

            #buscando verticalmente
            aux_index = y
            while (found_vertical < sequence) and (matrix[x][aux_index] == matrix[x][aux_index + 1] - 1):
                aux_index += 1
                found_vertical += 1
            if(found_vertical == sequence): #si while corta por hallar 4 consecutivos
                return {"initial": [x, y], "final": [x, aux_index]}

            #buscando horizontalmente
            aux_index = y
            while (found_horizontal < sequence) and (matrix[aux_index][x] == matrix[aux_index + 1][x] - 1):
                aux_index += 1
                found_horizontal += 1
            if(found_horizontal == sequence): #si while corta por hallar 4 consecutivos
                return {"initial": [y, x], "final": [aux_index, x]}
            y += 1
    return -1

if(__name__ == "__main__"):
    import doctest
    doctest.testmod(verbose=True)
