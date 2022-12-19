priorities = [None, "a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

f = open("d3-data.txt", "r")

print("Pt 1:")

totalPriority = 0

for line in f:
	strlen = len(line) - 1

	firstCompartment = line[0:int(strlen/2)]
	secondCompartment = line[int(strlen/2):strlen]

	linePriority = 0

	charactersChecked = []
	for character in firstCompartment:
		if character not in charactersChecked:
			charactersChecked.append(character)
			if character in secondCompartment:
				# print("Found a match: " + character)
				# print("Priority: " + str(priorities.index(character)))
				linePriority += priorities.index(character)
	
	totalPriority += linePriority

print(totalPriority)
f.close()
print("Pt 2:")

f = open("d3-data.txt", "r")

totalPriority = 0

lineCache = []
for line in f:
	lineCache.append(line)

	if len(lineCache) == 3:
		# loop through chars in 1st line cached, see if the character is present in the other two lines
		checkedChars = []
		for i in lineCache[0]:
			if i not in checkedChars:
				checkedChars.append(i)
				if i in lineCache[1] and i in lineCache[2] and i != "\n":
					# print("Found a match: " + i)
					# print("Priority: " + str(priorities.index(i)))
					totalPriority += priorities.index(i)
		lineCache = []

print(totalPriority)