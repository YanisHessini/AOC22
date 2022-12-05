import numpy as np
import math

input = open("input.txt")
reading = input.readlines()

lines = []

for line in reading:
	line = line.strip("\n")
	lines.append(line)

def answer(opponent_move: str):
	if (opponent_move == "A"): return "Y"
	elif (opponent_move == "B"): return "X"
	elif (opponent_move == "C"): return "Z"

def score(moves):
	if (moves == "A X"): return 3 + 1
	elif (moves == "A Y"): return 6 + 2
	elif (moves == "A Z"): return 0 + 3
	elif (moves == "B X"): return 0 + 1
	elif (moves == "B Y"): return 3 + 2
	elif (moves == "B Z"): return 6 + 3
	elif (moves == "C X"): return 6 + 1
	elif (moves == "C Y"): return 0 + 2
	elif (moves == "C Z"): return 3 + 3

rounds = np.array_split(lines, math.ceil(len(lines)/3))

total = 0
for round in rounds:
	for game in round:
		total += score(game)

print(total)

def action(moves):
	if (moves == "A X"): return score("A Z")
	elif (moves == "A Y"): return score("A X")
	elif (moves == "A Z"): return score("A Y")
	elif (moves == "B X"): return score("B X")
	elif (moves == "B Y"): return score("B Y")
	elif (moves == "B Z"): return score("B Z")
	elif (moves == "C X"): return score("C Y")
	elif (moves == "C Y"): return score("C Z")
	elif (moves == "C Z"): return score("C X")

total2 = 0
for round in rounds:
	for game in round:
		total2 += action(game)

print(total2)