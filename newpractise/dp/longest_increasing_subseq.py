'''
Problem statement
For a given array with N elements, you need to find the length of the longest subsequence from the array such that all the elements of the subsequence are sorted in strictly increasing order.

Strictly Increasing Sequence is when each term in the sequence is larger than the preceding term.

For example:
[1, 2, 3, 4] is a strictly increasing array, while [2, 1, 4, 3] is not.


# good example of shifting the array index
we need to store -1 in dp arry for previous
but to do that we shift the index as:
-1, 0, .... n-1
0, 1    .... n => add 1
'''
def solve(arr, i, prev, dp):
    if i >= len(arr):
        return 0
    
    if dp[i][prev+1] != -1:
        return dp[i][prev+1]

    #nottake
    l = 0 + solve(arr, i+1, prev, dp)
    #take
    if prev == -1 or arr[i] > arr[prev]:
        l = max(l, 1 + solve(arr, i+1, i, dp))
    dp[i][prev+1] = l
    return l
    

def _longestIncreasingSubsequence(arr, n):

	# Your code goes here
    dp = [[-1 for i in range(n+1)] for i in range(n)]
    return solve(arr, 0, -1, dp)


def longestIncreasingSubsequence(arr, n) :

	# Your code goes here
    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    
    
    for i in range(n-1, -1, -1):
        for prev in range(i-1, -2, -1):
            # print(i, prev)
            
            l = 0 + dp[i+1][prev+1]
            #take
            if prev == -1 or arr[i] > arr[prev]:
                l = max(l, 1 + dp[i+1][i+1]) # in recursion we used prev+1, so here also prev+1
            dp[i][prev+1] = l
    
    return dp[0][0]


#space opt
def longestIncreasingSubsequence(arr, n) :

	# Your code goes here
    # dp = [[0 for i in range(n+1)] for i in range(n+1)]

    cur = [0 for i in range(n+1)]
    prev = [0 for i in range(n+1)]
    
    
    for i in range(n-1, -1, -1):
        for _prev in range(i-1, -2, -1):
            # print(i, prev)
            
            # l = 0 + dp[i+1][prev+1]
            l = 0 + prev[_prev+1]
            #take
            if _prev == -1 or arr[i] > arr[_prev]:
                l = max(l, 1 + prev[i+1]) # in recursion we used prev+1, so here also prev+1
            cur[_prev+1] = l
            prev = cur
    
    return cur[0]



def binary_search(arr, num):    
    i = 0
    j = len(arr)-1

    mid = 0
    while i <= j and i >= 0 and j < len(arr):
        mid = (i+j)//2
        if arr[mid] == num:
            arr[mid] = num
            return arr
        elif arr[mid] > num:
            j = mid-1
        else:
            i = mid+1
    # print(mid, num, arr)

    if len(arr) == 0:
        return arr.append(num)

    if arr[mid] < num:
        if mid+1 >= len(arr):
            arr.append(num)
        else:
            arr[mid+1] = num
    else:
        arr[mid] = num

    # try:
    #     arr[mid] = num
    # except:
    #     arr.append(num)
    # return arr
    # print(mid, num, arr)
    # if len(arr) > mid:
    #     arr[mid] = num
    # else:
    #     arr.insert(mid, num)


def longestIncreasingSubsequence(arr, n) :
    lis = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            binary_search(lis, arr[i])
    
    return len(lis)




l = [5, 4, 11, 1, 16, 8]
# l = [1,2,2]
# l = [1,7,8,4,5,6,-1,9]
print(longestIncreasingSubsequence(l, len(l)))