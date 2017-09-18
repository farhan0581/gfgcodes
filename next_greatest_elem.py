'''
Given an array A [ ] having distinct elements, the task is to find the next greater element for each element of the array
 in order of their appearance in the array. If no such element exists, output -1 

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow.
Each test case consists of two lines. The first line contains an integer N denoting the size of the array. 
The Second line of each test case contains N space separated positive integers denoting the values/elements 
in the array A[ ].
 
Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1<=T<=200
1<=N<=1000
1<=A[i]<=1000

Example:
Input
1
4
1 3 2 4

Output
3 4 4 -1

'''
import sys
test_cases = int(input())
# array = [99,222,40,50,11,32,55,68,75,234]
# array = [1,2,2,2,2,2]
# array = [99,222,40,50,11,32,55,68,75,234]
while test_cases:   
    stack = []
    greater_map = {}
    temp = input().split(" ")
    array = [int(elem) for elem in temp if elem.strip() != '']
    temp = []

    for item in array:
        if len(stack) > 0:
            while len(stack) > 0 and stack[-1] < item:
                greater_map[stack[-1]] = item
                temp.append(item)
                stack.pop()
            stack.append(item)
            if len(stack) > 0 and stack[-1] > item:
                stack.append(item)
        else:
            stack.append(item)

    for item in array:
        x = greater_map.get(item, -1)
        # print (x)
        print (x ,end=' ')
    test_cases -= 1

test_cases = input()
while test_cases:
    stray = input()
    temp = input().split(" ")
    array = [int(elem) for elem in temp if elem.strip() != '']
    map = {}
    for item in array:
        try:
            x=map[item]
            x+=1
            map[item]=x
       except:
           map[item] = 1
    
    maj = len(array)/2 + 1
    flag=0
    for key, value in map.items():
        if value >= maj:
            print (key)
            flag=1
            break
    if flag == 0:
        print("NO Majority Element")
    test_cases -= 1