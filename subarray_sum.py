# test_cases = 1
test_cases = int(input())
while test_cases:
	initial = 0
	cur_sum = 0
	flag = 0
	no_elem, rsum = [42, 468]
	no_elem, rsum = [int(elem) for elem in input().split(" ")]
	temp = input().split(" ")
	# temp = "135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134".split(" ")
	array = [int(elem) for elem in temp if elem.strip() != '']
	# print array
	for index, item in enumerate(array):
		cur_sum += item
		# print cur_sum
		if cur_sum == rsum:
			print (initial+1, index+1)
			flag = 1
			# print 'found'
			break

		elif cur_sum > rsum:
			while not cur_sum <= rsum:
				# print 'initial=%s' % initial
				cur_sum -= array[initial]
				initial += 1
				# print cur_sum
				# print '-------------------'
			if cur_sum == rsum:
				print (initial+1, index+1)
				flag = 1
				break
				# print 'found2'
				# break

	if flag == 0:
		print (-1)
	test_cases -= 1
