'''
Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.
 
Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
 
Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.
 
Example:
Input
2
3
1 2 3
4
-1 -2 -3 -4
Output
6
-1
'''
test_cases = int(input())
while test_cases:
    test_cases -= 1
    stray = input()
    temp = input().split(" ")
    array = [int(elem) for elem in temp if elem.strip() != '']
    max_so_far = array[0]
    local_max = 0
    start = end = beg = 0

    for index, item in enumerate(array):
        local_max += item

        if local_max > max_so_far:
            max_so_far = local_max
            start = beg
            end = index

        if local_max < 0:
            beg = index+1
            local_max = 0

    print(max_so_far)

