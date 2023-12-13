file = open('luke_input.txt')

sum = 0

# max_red = 12
# max_green = 13
# max_blue = 14

# for line in file.readlines():
#     [game, pulls] = line.split(':', 1);
#     [_, game] = game.split(" ", 1)
#     rounds = pulls.split(";")
#     valid = True
#     for round in rounds:
#         colors = round.strip().split(", ")
#         for color in colors:
#             if "red" in color:
#                 if int(color.split(" ")[0]) > max_red:
#                     valid = False
#             elif "green" in color:
#                 if int(color.split(" ")[0]) > max_green:
#                     valid = False
#             elif "blue" in color:
#                 if int(color.split(" ")[0]) > max_blue:
#                     valid = False
#     if valid:
#         sum += int(game)

for line in file.readlines():
    [game, pulls] = line.split(':', 1);
    [_, game] = game.split(" ", 1)
    rounds = pulls.split(";")
    min_red = 0
    min_green = 0
    min_blue = 0
    for round in rounds:
        colors = round.strip().split(", ")
        for color in colors:
            if "red" in color:
                if int(color.split(" ")[0]) > min_red:
                    min_red = int(color.split(" ")[0])
            elif "green" in color:
                if int(color.split(" ")[0]) > min_green:
                    min_green = int(color.split(" ")[0])
            elif "blue" in color:
                if int(color.split(" ")[0]) > min_blue:
                    min_blue = int(color.split(" ")[0])
    sum += min_red * min_green * min_blue

print(sum)

    