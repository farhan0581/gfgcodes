'''
The cost of a stock on each day is given in an array, 
find the max profit that you can make by buying and selling in those days. 

Input:
First line contains number of test cases T. Each test case contain the integer value 'N' 
denoting days followed by an array of stock prices in N days.

Output:
The maximum profit is displayed as shown below. And if there is no profit then print "No Profit".
'''
# 4335 1257 3515 5056 
test_cases = int(input())
while test_cases:
	test_cases -= 1
	stray = input()
	result = []
	temp = input().split(" ")
	array = [int(elem) for elem in temp if elem.strip() != '']
	local_max = array[0]
	minIndex = 0
	maxIndex = 0

	index =0
	while index+1 < len(array):

		if local_max > array[index+1]:
			if maxIndex-minIndex > 0:
				result.append((minIndex, maxIndex))

			minIndex = maxIndex = index+1
			local_max = array[index+1]

		
		elif local_max < array[index+1]:
			local_max = array[index+1]
			maxIndex =index+1

		index += 1
	try:
		if result[-1][0] != minIndex and result[-1][1] != maxIndex and maxIndex-minIndex>0:
			result.append((minIndex, maxIndex))
	except:
		pass

	if len(result) > 0:
		for item in result:
			string = "(%s %s)" % (item[0], item[1])
			print(string,  end=' ')
		print()
	else:
		if maxIndex - minIndex > 0:
			string = "(%s %s)" % (minIndex, maxIndex)
			print(string,  end=' ')
			print()
		else:
			print ("No Profit")