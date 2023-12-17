def containsNumbers(input_string):
    return any(char.isdigit() for char in input_string)

def convert_range(source, conversion_map):
    for dest_start, source_start, length in conversion_map:
        if source_start <= source < source_start + length:
            return dest_start + (source - source_start)
    return source  # If not found, return the original source number

def convert(seed, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    soil = convert_range(seed, seed_to_soil)
    fertilizer = convert_range(soil, soil_to_fertilizer)
    water = convert_range(fertilizer, fertilizer_to_water)
    light = convert_range(water, water_to_light)
    temperature = convert_range(light, light_to_temperature)
    humidity = convert_range(temperature, temperature_to_humidity)
    location = convert_range(humidity, humidity_to_location)
    return location
'''
def find_lowest_location(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    min_location = float('inf')
    seedStarts = [seeds[i] for i in range(len(seeds)) if i % 2 == 0]
    seedRanges = [seeds[i] for i in range(len(seeds)) if i % 2 == 1]
    for seed in seedStarts:
        for i in range(seedRanges[seedStarts.index(seed)]):
            location = convert(seed+i, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location)
            min_location = min(min_location, location)
    return min_location
    '''
def find_lowest_location(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    min_location = float('inf')
    
    for i in range(0, len(seeds), 2):
        seed_start, seed_range = seeds[i], seeds[i + 1]
        for j in range(seed_range):
            seed_number = seed_start + j
            location = convert(seed_number, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location)
            min_location = min(min_location, location)
            
    return min_location

# Rest of your code remains unchanged


file = open("./trey_input.txt")

seeds = list(filter(None, file.readline().strip().split(': ')[1].split(' ')))
seeds = [int(i) for i in seeds]
file.readline()
maps = [[] for i in range(7)]
#print(maps)
'''
maps[0] = seed2soil
    .   = soil2fert
    .   = fert2water
    .   = water2light
    .   = light2temp
    .   = temp2hum
maps[6] = hum2loc
        '''
currentMap = -1
for line in file.readlines():
    line = line.strip()
    if line != '':
        if not containsNumbers(line):
            currentMap += 1
        else:
            maps[currentMap].append([int(i) for i in line.split()]) 
#print(maps)
#print(seeds)

result = find_lowest_location(seeds, maps[0], maps[1], maps[2], maps[3], maps[4], maps[5], maps[6])
print(result)
