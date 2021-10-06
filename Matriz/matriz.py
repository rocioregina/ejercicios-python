import random

columns = 5
rows = 5
sequenceLength = 4

def createMatrix(columns, rows):
    matrix = [[random.randint(1, 5) for x in range(columns)] for y in range(rows)]
    return matrix

def findSequence(matrix, sequence):
    for i in range(len(matrix)):
        j = 0
        while (j < len(matrix[i]) - sequence):
            found = 1 #cantidad de numeros consecutivos encontrados en la iteracion
            auxIndex = j #buscando verticalmente, el indice que aumenta sera el de filas
            while (found < sequence) and (matrix[i][auxIndex] == matrix[i][auxIndex] - 1):
                auxIndex += 1
                found += 1
            if(found == sequence): #si while corta por hallar 4 consecutivos
                return {"initial": [i, j], "final": [i, auxIndex]}
            j += 1
    return -1

newMatrix = createMatrix(columns, rows)
positions = findConsecutives(newMatrix, sequenceLength)
