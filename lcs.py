# remains : to traverse back and find the lcs
test_cases = int(input())

def max(val1, val2):
	if val1 >= val2:
		return val1
	else:
		return val2

def prepare_lcs(array, a, b):
	for ind1, elem1 in enumerate(b):
		for ind2, elem2 in enumerate(a):
			if elem1 == elem2:
				array[ind1+1][ind2+1] = array[ind1][ind2] + 1
				return 1
			elif elem1 != elem2:
				array[ind1+1][ind2+1] = max(array[ind1][ind2+1], array[ind1+1][ind2])
	if array[ind1+1][ind2+1] > 0:
		return 1
	else:
		return 0


while test_cases:
	a, b = input().split(" ")
	array = [[0 for j in range(len(a)+1)] for i in range(len(b)+1)]
	print (prepare_lcs(array, a, b))
	test_cases -= 1