input = open("input.txt")
lines = input.readlines()

def answer(opponent_move: str):
	if (opponent_move == "A"): return "Y"
	elif (opponent_move == "B"): return "X"
	elif (opponent_move == "C"): return "Z"

i = 0
rounds = []
current_round = []

for line in lines:
	if (i%3 == 0): current_round.append(line)
	else: rounds.append(current_round)

