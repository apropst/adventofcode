with open('Data1-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

solution = 0
index1 = 0
index2 = 0
index3 = 0
	
for num1 in filedata:
	for num2 in filedata:
		for num3 in filedata:
			if ((index1 != index2) and (index1 != index3) and (index2 != index3) and (int(num1) + int(num2) + int(num3) == 2020)):
				solution = int(num1) * int(num2) * int(num3)
			index3 += 1
		index2 += 1
	index1 += 1

print("Solution is: " + str(solution))