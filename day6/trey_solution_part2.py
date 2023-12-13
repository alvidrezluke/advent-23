file = open("./trey_input.txt")
times, records = file.readline().strip().split()[1:], file.readline().strip().split()[1:]
(time, record) = int(''.join(times)), int(''.join(records))
count = 0
for sec in range(time + 1):
    dist = sec * (time - sec)
    if dist > record:
        count += 1
print(count)