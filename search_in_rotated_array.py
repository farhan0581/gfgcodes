def binary_search(arr, start, end, elem):
	mid = start + ((end-start) // 2)
	# print arr
	# print mid
	if start <= end:
		if arr[mid] ==  elem:
			return mid

		elif arr[mid] > elem:

			return binary_search(arr, start, mid-1, elem)

		elif arr[mid] < elem:

			return binary_search(arr, mid + 1, end, elem)
	else:
		return -1

test_cases = int(input())
while test_cases:
	test_cases -= 1
	stray = input()
	temp = input.split(" ")
	array = [int(temp) for item in temp if temp != '']
	elem_to_search = int(input())
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
	arr1 = array[0:pivot]
	arr2 = array[pivot:]
	ind = -1
	# first list
	if len(arr1) > 0:
		ind = binary_search(arr1, 0, pivot-1, elem_to_search)
		if ind != -1:
			print (ind)
	# second list
	if len(arr2) > 0 and ind == -1:
		ind = binary_search(arr2, 0, len(arr2)-1, elem_to_search)
		if ind != -1:
			print (ind+pivot)
		else:
			print(-1)

	# print arr1, arr2