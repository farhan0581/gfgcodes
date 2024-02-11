'''
Problem statement
You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.



Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.



Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.



Example:
Input: 'arr' = [1, 1, 4, 5]

Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.
https://takeuforward.org/data-structure/count-subsets-with-sum-k-dp-17/
'''
mod=1000000007
def solve(arr, i, k,dp):
    if k == 0:
        return 1
    
    if i >= len(arr):
        return 0
    
    if dp[i][k]:
        return dp[i][k]%mod
    
    t=nt=0
    if i < len(arr):
        #take
        if k-arr[i] >= 0:
            t = solve(arr, i+1, k-arr[i],dp)%mod
        #nottake
        nt = solve(arr, i+1, k,dp)%mod
    
    dp[i][k]= (t + nt)%mod
    return dp[i][k]

# recursion not working
def _findWays(arr,k):
    # Write your code here.
    dp = [[None for i in range(k+1)] for i in range(len(arr))]
    return solve(arr, 0, k, dp)


# tabulation works when there is 0 in the array
def findWays(arr,k):
    # Write your code here.
    dp = [[0 for i in range(k+1)] for i in range(len(arr))]
    n = len(arr)
    for i in range(n):
        dp[i][0] = 1
    
    if arr[0] <= k:
        dp[0][arr[0]] = 1

    
    for i in range(1, n):
        for s in range(k+1):
            t=nt=0
            #take
            if s-arr[i] >= 0:
                t = dp[i-1][s-arr[i]]
            #not
            nt= dp[i-1][s]

            dp[i][s] = (t%mod + nt%mod)%mod
    
    return dp[n-1][k]%mod
    
    # print(dp)
    

    # return solve(arr, 0, k, dp)

l = [1,4,4,5,10]
k = 5
print(findWays(l,k))