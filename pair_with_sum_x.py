# array = [1, 4, 45, 6, 10, -8]
# array = sorted(array)
# start = 0
# end = len(array) - 1
# rsum = 16
test_cases = int(input())
while test_cases:
	no_elem, rsum = [int(elem) for elem in input().split(" ")]
	temp = input().split(" ")
	array = sorted([int(elem) for elem in temp if elem.strip() != ''])
	start = 0
	flag = 0
	end = len(array) - 1
	while start <= end:
		sum = array[start] + array[end]
		if sum == rsum:
			# print array[start], array[end]
			print ('Yes')
			flag = 1
			break
		elif sum > rsum:
			end -= 1
		elif sum < rsum:
			start += 1
	if flag == 0:
		print ('No')

	test_cases -= 1

# method 2 
# hmap = dict()
# for item in array:
# 	rnum = rsum - item
# 	try:
# 		ans = hmap[rnum]
# 		if ans == 1:
# 			print ans, item
# 	except:
# 		hmap[item] = 1
