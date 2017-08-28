import sys
test_cases = int(input())
# array = [99,222,40,50,11,32,55,68,75,234]
# array = [1,2,2,2,2,2]
# array = [99,222,40,50,11,32,55,68,75,234]
while test_cases:	
	stack = []
	greater_map = {}
	temp = input().split(" ")
	array = [int(elem) for elem in temp if elem.strip() != '']
	temp = []

	for item in array:
		if len(stack) > 0:
			while len(stack) > 0 and stack[-1] < item:
				greater_map[stack[-1]] = item
				temp.append(item)
				stack.pop()
			stack.append(item)
			if len(stack) > 0 and stack[-1] > item:
				stack.append(item)
		else:
			stack.append(item)

	for item in array:
		x = greater_map.get(item, -1)
		# print (x)
		print (x, " " ,end='')
	test_cases -= 1