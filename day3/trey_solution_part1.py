'''
def detectSymbols(row_index, col_index, matrix):
    for r in range(row_index - 1, row_index + 1):
        if r > 0 and r < len(matrix):
            for c in range (col_index - 1, col_index + 1):
                if c > 0 and c < len(matrix[r]):
                    if matrix[r][c] in "!@#$%^&*()-+?_=,<>/":
                        return True
    return False



for line in file.readlines():
    matrix.append(line.strip())

for row in matrix:
    for char in row:
        if char.isnumeric():
            rowIndex = matrix.index(row)
            colIndex = row.index(char)
            if detectSymbols(rowIndex, colIndex, matrix):
    '''

#UNFINISHED

file = open("./trey_input.txt")
matrix = []
partNums = []
symbolLocations = 
for line in file.readlines():
    counter = 0
    rowDict = {}
    for char in line.strip():
        if char.isnumeric():
            for num in char:
                if counter <= len(line.strip()):
                    rowDict[counter] = char
                counter += 1
        else:
            rowDict[counter] = char
            counter += 1
        if isSymbolic(char):

    matrix.append(rowDict)
print(matrix)

def isSymbol(char):
    return char in '!@#$%^&*()-+?_=,<>/'

def isValidPosition(x,y,numRows,numCols):
    0 <= y < numRows and 0 <= x < numCols