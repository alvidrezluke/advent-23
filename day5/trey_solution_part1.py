file = open("./trey_input.txt")

seeds = list(filter(None, file.readline().strip().split(': ')[1].split(' ')))
seeds = [int(i) for i in seeds]
maps = []
'''
maps[0] = seed2soil
    .   = soil2fert
    .   = fert2water
    .   = water2light
    .   = light2temp
    .   = temp2hum
maps[6] = hum2loc
        '''