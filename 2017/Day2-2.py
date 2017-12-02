with open('linedata.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

solution = 0
	
for line in filedata:
	linedata = line.split("\t")

	for index, number in enumerate(linedata):
		for index2, number2 in enumerate(linedata):
			if index != index2:
				if int(number) % int(number2) == 0:
					solution = solution + int((int(number) / int(number2)))

print("Solution is: " + str(solution))