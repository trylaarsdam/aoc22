f = open("d2-data.txt", "r")

print("Pt 1:")
score = 0

for line in f:
	# split line at space
	splitLine = line.split(" ")
	# opponent move
	opponentMove = splitLine[0]
	# player move
	playerMove = splitLine[1].split("\n")[0]

	# print("Opponent: " + opponentMove + " Player: " + playerMove)

	round_score = 0

	if playerMove == "X": # rock
		round_score += 1
		if opponentMove == "C": # scissors
			round_score += 6
		elif opponentMove == "A": # tie
			round_score += 3 

	if playerMove == "Y": # paper
		round_score += 2
		if opponentMove == "A": # rock
			round_score += 6
		elif opponentMove == "B": # tie
			round_score += 3
		
	if playerMove == "Z": # scissors
		round_score += 3
		if opponentMove == "B": # paper
			round_score += 6
		elif opponentMove == "C": # tie
			round_score += 3

	score += round_score
f.close()
print(score)

f = open("d2-data.txt", "r")
print("Pt 2:")

score = 0

for line in f:
	# split line at space
	splitLine = line.split(" ")
	# opponent move
	opponentMove = splitLine[0]
	# player move
	playerMove = splitLine[1].split("\n")[0]

	# print("Opponent: " + opponentMove + " Player: " + playerMove)

	round_score = 0

	if playerMove == "X": # lose
		if opponentMove == "A": # rock, so play scissors
			round_score += 3
		elif opponentMove == "B": # paper, so play rock
			round_score += 1
		elif opponentMove == "C": # scissors, so play paper
			round_score += 2

	if playerMove == "Y": # tie
		if opponentMove == "A": # rock, so play rock
			round_score += 4
		elif opponentMove == "B": # paper, so play paper
			round_score += 5
		elif opponentMove == "C": # scissors, so play scissors
			round_score += 6
		
	if playerMove == "Z": # win
		if opponentMove == "A": # rock, so play paper
			round_score += 2 + 6
		elif opponentMove == "B": # paper, so play scissors
			round_score += 3 + 6
		elif opponentMove == "C": # scissors, so play rock
			round_score += 1 + 6

	score += round_score

print(score)