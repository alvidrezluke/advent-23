#file = open("./luke_input.txt")
file = open("./trey_input.txt")
counter = 0
sum = 0
r_max = 12
g_max = 13
b_max = 14
powers = []
for game in file.readlines():
    counter += 1
    dict = {'red':0,'green':0,'blue':0 }
    line = game.split(': ')[1].strip() # '4 blue, 4 red, 16 green; 14 green, 5 red; 1 blue, 3 red, 5 green'
    rolls = line.split('; ') # ['4 blue, 4 red, 16 green', '14 green, 5 red', '1 blue, 3 red, 5 green']
    for roll in rolls: #'4 blue, 4 red, 16 green'
        dice = roll.split(', ') # ['4 blue','4 red','16 green']
        for die in dice: # '4 blue'
            value = die.split(' ')
            if dict[value[1]] < int(value[0]):
                dict[value[1]] = int(value[0])
    if dict['red'] <= r_max and dict['green'] <= g_max and dict['blue'] <= b_max:
        sum += counter
    powers.append(dict['red']*dict['green']*dict['blue'])
print(sum)
power_sum = sum(powers)
print(power_sum)

