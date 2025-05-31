myfile = open("Input 1-1.txt")
filedata = myfile.readlines()

solution = 0
leftList = []
rightList = []

for line in filedata:
	nums = line.split("   ")
	leftList.append(nums[0])
	rightList.append(nums[1])

leftList.sort()
rightList.sort()

for i in range(len(leftList)):
	diff = abs(int(leftList[i]) - int(rightList[i]))
	solution = solution + diff

print("Solution is: " + str(solution))