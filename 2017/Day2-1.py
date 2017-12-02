with open('linedata.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

solution = 0
	
for line in filedata:
	linedata = line.split("\t")
	min = 1000000
	max = 0
	for number in linedata:
		if int(number) < min:
			min = int(number)
		if int(number) > max:
			max = int(number)
	solution = solution + (max - min)

print("Solution is: " + str(solution))