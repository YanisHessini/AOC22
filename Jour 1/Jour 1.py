# Lecture du fichier

text = open("input.txt", "r")
lines = text.readlines()

i = 0
elves = []
temp_list = []

# Tableau d'entiers 2D contenant les nombres
for line in lines:
	if (line.strip('\n') != ""):
		temp_list.append(int(line.strip("\n")))
	else: 
		elves.append(temp_list)
		temp_list = []

# Nombre d'elfes

print(len(elves), "elves")

# Somme de chaque sous tableau

values = []

for elf in elves:
	values.append(sum(elf))

# Tri fusion des valeurs du tableau

def TriFusion(liste):
	if len(liste) == 1:
		return liste
	else:
		return fusion( TriFusion(liste[:len(liste)//2]), TriFusion(liste[len(liste)//2:]) )

def fusion(A, B):
	if (len(A) == 0):
		return B
	elif (len(B) == 0):
		return A
	elif (A[0] <= B[0]):
		return [A[0]] + fusion(A[1:], B)
	else:
		return [B[0]] + fusion(A, B[1:])

print (TriFusion([1, 3, 0, 5, 0, 1, -3]))

# Tri du tableau
elves_sorted = []

for elf in elves:
	elves_sorted.append(TriFusion(elf))

	# Somme de chaque sous tableau

values_elf = []

for elf in elves_sorted:
	values_elf.append(sum(elf))

sum_sorted = TriFusion(values_elf)
max = sum_sorted[-1]

print(max)

max_3 = sum(sum_sorted[-3:])
print(max_3)