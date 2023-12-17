file = open("./trey_input.txt")

directions = file.readline().strip()
dict = {}
for line in file.readlines():
    line = line.strip()
    if line != '':
        parts = line.replace('(','').replace(')','').split(' = ')
        defNodes = parts[1].split(', ')
        dict[parts[0]] = (defNodes[0],defNodes[1])

count = 0
done = False
while not done:
    node = 'AAA'
    for char in directions:
        count += 1
        if char == 'R':
            node = dict[node][0]
        elif char == 'L':
            node = dict[node][1]
        if node == 'ZZZ':
            done = True
            break

print(count)
        

