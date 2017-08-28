test_cases = int(input())
# test_cases = 1
while test_cases:
	# array = '{}{(}))}'
	# array = '}[])]'
	array = input()

	to_pop = [')', '}', ']']
	to_push = ['(', '{', '[']
	rev_map = {')':'(', '}':'{', ']':'['}
	stack = []
	for item in array:

		if item in to_push:
			stack.append(item)

		elif item in to_pop:
			if len(stack) >0 and stack[-1] == rev_map.get(item, ''):
				stack.pop()
			else:
				# print stack, item
				stack.append(item)

	# print len(stack)
	# print stack
	if len(stack) == 0:
		print ('balanced')
	else:
		print ('not balanced')
	test_cases -= 1
