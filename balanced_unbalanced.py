'''
Given an expression string exp, examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

 

Input:

The first line of input contains an integer T denoting the number of test cases. 
Each test case consist of a string of expression, in a separate line.

Output:

Print 'balanced' without quotes if pair of parenthesis are balanced else print 'not balanced' in a separate line.


Constraints:

1 ≤ T ≤ 100
1 ≤ |s| ≤ 100


Example:

Input:
3
{([])}
()
()[]

Output:
balanced
balanced
balanced
'''
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
