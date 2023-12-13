file = open("./luke_input.txt")
#file = open("./trey_input.txt")

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


calibration_value = 0
for line in file.readlines():
    orgLine = line
    mins = [line.find(key) for key in nums.keys()]
    mins = [m if m>=0 else len(line) for m in mins]
    firstword = list(nums.keys())[mins.index(min(mins))]
    line = line.replace(firstword, f"{nums.get(firstword)}{firstword}", 1)
    
    maxs = [line.rfind(key) for key in nums.keys()]
    lastword = list(nums.keys())[maxs.index(max(maxs))]
    line = f"{nums.get(lastword)}".join(line.rsplit(lastword, 1))
    print(f"{orgLine}{line}\n")
    #print(f"{orgLine}\n{line}\n")
    numbers = [x.strip() for x in line if x.isnumeric()]
    # print(f"{orgLine} with number: {int(numbers[0]+numbers[-1])}")
    #if len(numbers) > 1:
    calibration_value += int(numbers[0]+numbers[-1])
    #else:
    #    calibration_value += int(numbers[0])


print(f"Calibration Value: {calibration_value}")