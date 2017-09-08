test_cases = int(input())
while test_cases:
	test_cases -= 1
	stray = input()
	temp = input().split(" ")
	array = sorted([int(elem) for elem in temp if elem.strip() != ''])
	total = sum(array)
	left_sum = flag = 0
	for index, item in enumerate(array):
		total -= item
		print left_sum, total
		if left_sum == total:
			print (index + 1)
			flag = 1
			break
		else:
			left_sum += item
	if flag == 0:
		print (-1)


