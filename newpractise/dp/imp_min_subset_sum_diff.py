'''
Problem statement
You are given an array 'arr' containing 'n' non-negative integers.



Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.



You just need to find the minimum absolute difference considering any valid division of the array elements.



Note:

1. Each array element should belong to exactly one of the subsets.

2. Subsets need not always be contiguous.
For example, for the array : [1, 2, 3], some of the possible divisions are 
   a) {1,2} and {3}
   b) {1,3} and {2}.

3. Subset-sum is the sum of all the elements in that subset. 
Example:
Input: 'n' = 5, 'arr' = [3, 1, 5, 2, 8].

Ouput: 1

Explanation: We can partition the given array into {3, 1, 5} and {2, 8}. 
This will give us the minimum possible absolute difference i.e. (10 - 9 = 1).

APPROACH:
- use subset sum approach
- the catch is to use the dp array that we have filled
now we fill the array from sum 0 to total_sum, then we check from 0 to s
- so now we have the ability to check every possible thats possible, then just check the mindiff
by iterating the last row of the array
'''


def minSubsetSumDifference(arr,n):
    s = sum(arr)
    dp = [[False for i in range(s+1)] for i in range(n)]
    
    for i in range(n):
        dp[i][0] = True
    
    dp[0][arr[0]] = True


    for i in range(n):
        for k in range(s+1):
            take=ntake=False
            if i-1 >= 0:
                #take
                if k-arr[i] >= 0:
                    take = dp[i-1][k-arr[i]]

                #nottake
                ntake = dp[i-1][k]
                dp[i][k] = ntake or take


    target = s//2

    # possible_sum = arr[n-1][:target+1]

    minDiff = 999999999999
    k = 0
    # print(arr[n-1][:target+1])
    for possibleSum in dp[n-1]:
        if possibleSum: 
            s1 = k
            s2 = s-s1

            minDiff = min(minDiff, abs(s1-s2))
        k+=1
        if k > target:
            break
    return minDiff


l = [1,2,3,4,5,20]
n=len(l)

print(minSubsetSumDifference(l,n))