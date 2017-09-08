test_cases = int(input())
while test_cases:
	test_cases -= 1
	stray = input()
	temp = input().split(" ")
	array = [int(item) for item in temp if item != '']
	# pivot
	pivot = 0
	for index,item in enumerate(array):
		try:
			if item > array[index+1]:
				pivot = index + 1
				break
		except:
			pass

	# print pivot
	# separate lists
	min_elem2 = min_elem1 = 99999
	arr1 = array[0:pivot]
	arr2 = array[pivot:]
	ind = -1
	# first list
	if len(arr1) > 0:
		min_elem1 = arr1[0]
	# second list
	if len(arr2) > 0:
		min_elem2 = arr2[0]

	print (min(min_elem1, min_elem2))