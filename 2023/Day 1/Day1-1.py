with open('Day1-Input1.txt', 'r') as file:
	data = file.read().splitlines()

sum = 0

for line in data:
	lastnum = None
	firstnum = None
	for character in line:
		if character.isdigit():
			if firstnum == None:
				firstnum = character
			lastnum = character
	if lastnum == None:
		sum += int(firstnum) * 10
	else:
		sum += ((int(firstnum) * 10) + int(lastnum))

print(sum)