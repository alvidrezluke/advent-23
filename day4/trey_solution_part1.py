file = open("./trey_input.txt")
points = 0
for line in file.readlines():
    game = line.strip().split(': ')[1].split(' | ')
    winNums = list(filter(None, game[0].split(' ')))
    myNums = list(filter(None, game[1].split(' ')))
    matches = 0
    for i in myNums:
        if i in winNums:
            matches += 1
    if matches != 0:
        points += 2**(matches - 1)
print(points)

