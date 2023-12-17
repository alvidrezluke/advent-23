from collections import deque

def bfs_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    
    # Define the directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Create a queue for BFS
    queue = deque([(start[0], start[1], 0)])  # Include the distance
    
    # Set to store visited nodes
    visited = set()
    
    while queue:
        current_row, current_col, distance = queue.popleft()
        
        # Check if the current node is the destination
        if (current_row, current_col) == end:
            return distance  # Return the shortest distance
        
        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            # Check if the new position is valid and not visited
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                # Enqueue the new node with increased distance
                queue.append((new_row, new_col, distance + 1))
                # Mark the node as visited
                visited.add((new_row, new_col))
    
    return -1  # If no path is found

def add_column(grid, column_index, column_value):
    for row in grid:
        # Insert the new column_value at the specified index
        row.insert(column_index, column_value)

file = open("./trey_input.txt")
space = []
count = 0
length = 0
galaxyIndexes = []
for line in file.readlines():
    line = line.strip()
    length = len(line)
    currentGalIndexes = []
    [currentGalIndexes.append(index) for index, char in enumerate(line) if char == '#']
    line = list(line)
    if '#' in line:
        for index in currentGalIndexes:
            line[index] = count
            count += 1
        space.append(line)
    else:
        space.append(line)
        space.append(['.' for i in range(length)])

    [galaxyIndexes.append(index) for index in currentGalIndexes if index not in galaxyIndexes]

addedCols = 0
for i in range(length):
    if i not in galaxyIndexes:
        add_column(space, i + addedCols, '.')
        addedCols += 1

galaxies = [] # (galaxy num, row, col)
for row in range(len(space)):
    for col in range(len(space[0])):
        item = space[row][col]
        if type(item) == int:
            galaxies.append([item, (row, col)])

sumOfPaths = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        galaxy1, pos1 = galaxies[i]
        galaxy2, pos2 = galaxies[j]
        distance = bfs_shortest_path(space, pos1, pos2)
        sumOfPaths += distance

print(sumOfPaths)