'''
Subset some problem

Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both 
subsets is same or not.

Input:The first line contains an integer 'T' denoting the total number of test cases. Each test case constitutes of two 
lines. First line contains 'N', representing the number of elements in the set and the second line contains the elements 
of the set.
Output: Print YES if the given set can be partioned into two subsets such that the sum of elements in both subsets
is equal, else print NO.
Constraints: 

1 <= T<= 100
1 <= N<= 100
0 <= arr[i]<= 1000

                   
Example:

Input:
2
4
1 5 11 5
3
1 3 5 

Output:

YES
NO
'''

def compute(val1, val2):
	return val1 or val2


test_cases = int(input())
while test_cases:
	test_cases -= 1
	stray = input()
	temp = input().split(" ")
	array = [int(elem) for elem in temp if elem.strip() != '']
	total = sum(array)
	if total % 2 != 0:
		print("NO")
	else:
		total = total // 2
		table = [[False for j in range(total+1)] for i in range(len(array)+1)]
		for i in range(len(array)+1):
			table[i][0] = True
		

		for i in range(len(array)):
			for j in range(total):
				if array[i] > j+1:
					table[i+1][j+1] = table[i][j+1]
				else:
					prev = table[i][j+1]
					req_val = (j+1) - array[i]
					table[i+1][j+1] = compute(table[i][j+1],table[i][req_val])

		last = table[len(array)][total]
		if last:
			print("YES")
		else:
			print("NO")