import random

columns = 5
rows = 5
sequenceLength = 4

def createMatrix(columns, rows):
    matrix = [[random.randint(1, 5) for x in range(columns)] for y in range(rows)]
    return matrix

def findSequence(matrix, sequence):
    #esta solucion funciona solo cuando la cantidad de filas es la misma que de columnas
    for x in range(len(matrix)):
        y = 0
        while (y < len(matrix[x]) - sequence):
            foundVertical = 1 #cantidad de numeros consecutivos encontrados en la iteracion
            foundHorizontal = 1
            auxIndex = y

            #buscando verticalmente
            while (foundVertical < sequence) and (matrix[x][auxIndex] == matrix[x][auxIndex] - 1):
                auxIndex += 1
                foundVertical += 1
            if(foundVertical == sequence): #si while corta por hallar 4 consecutivos
                return {"initial": [x, y], "final": [x, auxIndex]}

            #buscando horizontalmente
            while (foundHorizontal < sequence) and (matrix[auxIndex][x] == matrix[auxIndex][x] - 1):
                auxIndex += 1
                foundHorizontal += 1
            if(foundVertical == sequence): #si while corta por hallar 4 consecutivos
                return {"initial": [y, x], "final": [auxIndex, x]}
            y += 1
    return -1

newMatrix = createMatrix(columns, rows)
positions = findSequence(newMatrix, sequenceLength)
if(positions != -1):
    print("Posicion inicial y final de la secuencia: ", positions)
else: print("No se encontro una secuencia de numeros consecutivos")
