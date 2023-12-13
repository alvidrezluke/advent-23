file = open("./trey_input.txt")
copies = {i:1 for i in range(193)}
card = 0
for line in file.readlines():
    game = line.strip().split(': ')[1].split(' | ')
    winNums = list(filter(None, game[0].split(' ')))
    myNums = list(filter(None, game[1].split(' ')))
    matches = 0
    for i in myNums:
        if i in winNums:
            matches += 1
    for point in range(matches):
        copies[point + card + 1] += copies[card]
    card += 1

totalCopies = sum(copies.values())
print(totalCopies)