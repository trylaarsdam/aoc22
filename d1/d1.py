f = open("d1-data.txt", "r")

print("Pt 1:")

maxCals = 0
currentCals = 0

for line in f:
	if line == "\n":
		if currentCals > maxCals:
			maxCals = currentCals
		currentCals = 0
	else:
		currentCals += int(line)

f.close()
print(maxCals)

print("Pt 2:")

f = open("d1-data.txt", "r")

cals = []
currentCals = 0

for line in f:
	if line == "\n":
		cals.append(currentCals)
		currentCals = 0
	else:
		currentCals += int(line)

cals.sort(reverse=True)

print(cals[0] + cals[1] + cals[2])