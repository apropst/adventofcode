myfile = open("Input 1-1.txt")
filedata = myfile.readlines()

solution = 0
leftList = []
rightList = []

for line in filedata:
	nums = line.split("   ")
	leftList.append(nums[0])
	rightList.append(nums[1].replace("\n",""))

leftList.sort()
rightList.sort()

for i in range(len(leftList)):
	left = int(leftList[i])
	count = rightList.count(leftList[i])
	if count > 0:
		print(left)
	score = left * rightList.count(leftList[i])
	
	solution = solution + score

print("Solution is: " + str(solution))