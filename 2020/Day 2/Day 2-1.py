with open('Data2-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

solution = 0
	
for line in filedata:
	linedata = line.split(" ")
	rules = linedata[0].split("-")
	min = rules[0]
	max = rules[1]
	target = linedata[1][0]
	password = linedata[2]
	count = 0
	for letter in password:
		if (letter == target):
			count += 1
	if ((count >= int(min)) and (count <= int(max))):
		solution += 1

print("Solution: " + str(solution))