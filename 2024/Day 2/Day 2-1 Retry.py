print()
myfile = open("Input 2-1.txt")
filedata = myfile.readlines()

solution = 0

for line in filedata:
	nums = line.rstrip().split()
	direc = 0
	safe = True

	leng = len(nums) - 1

	for i, num in enumerate(nums):
		if i == 0:
			if nums[i] < nums[i + 1]:
				direc = 1
			else:
				direc = -1
			diff = abs(int(nums[i]) - int(nums[i + 1]))
			if not (0 < diff < 4):
				safe = False
				break
		elif 0 < i < len(nums) - 1:
			if nums[i] < nums[i + 1]:
				if direc == -1:
					safe = False
					break
			elif nums[i] > nums[i + 1]:
				if direc == 1:
					safe = False
					break
			diff = abs(int(nums[i]) - int(nums[i + 1]))
			if not (0 < diff < 4):
				safe = False
				break
	if safe == True:
		solution = solution + 1

print("Solution is: " + str(solution))