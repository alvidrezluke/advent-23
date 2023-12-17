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
for line in file.readlines():
    line = line.strip()
    orgRow = line.split('.')
    list_chars = []
    counter = 0
    print(orgRow)
    row = []
    for char in row:
        if char.isnumeric():
            num_list = list(char)
            for i in num_list:
                if counter <= len(row):
                    row[counter] = char
                counter += 1
        else:
            row.append(char)
            counter += 1
    matrix.append(row)
#print(matrix)
