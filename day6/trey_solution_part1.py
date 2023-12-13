import numpy

file = open("./trey_input.txt")
times, distances = file.readline().strip().split()[1:], file.readline().strip().split()[1:]
games = {i:(times[i], distances[i]) for i in range(len(times))}
marginsError = []

for key in games:
    count = 0
    record = int(games[key][1])
    time = int(games[key][0])
    for sec in range(time + 1):
        dist = sec * (time - sec)
        if dist > record:
            count += 1
    marginsError.append(count)

print(numpy.prod(marginsError))