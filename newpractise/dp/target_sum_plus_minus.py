'''
Problem statement
You are given an array ‘ARR’ of ‘N’ integers and a target number, ‘TARGET’. Your task is to build an expression out of an array by adding one of the symbols '+' and '-' before each integer in an array, and then by concatenating all the integers, you want to achieve a target. You have to return the number of ways the target can be achieved.

For Example :
You are given the array ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
1. -1 + 1 + 1 + 1 + 1 = 3
2. +1 - 1 + 1 + 1 + 1 = 3
3. +1 + 1 - 1 + 1 + 1 = 3
4. +1 + 1 + 1 - 1 + 1 = 3
5. +1 + 1 + 1 + 1 - 1 = 3
These are the 5 ways to make. Hence the answer is 5.

https://takeuforward.org/data-structure/target-sum-dp-21/

'''
def solve(arr, i, k, dp):

    # if k == 0:
    #     return 1
    
    if i == 0:
        # If the target is equal to the first element, there is one possibility.
        if arr[0] == k or k == 0:
            return 1
        if k == 0 and arr[0] == 0:
            return 2
        # Otherwise, there is no valid partition.
        return 0
    
    if dp[i][k] != -1:
        return dp[i][k]

    tk=0
    if k-arr[i] >= 0:
        #take
        tk=solve(arr, i-1, k-arr[i], dp)

    #not
    nt = solve(arr, i-1, k, dp)
    dp[i][k] = tk+nt
    return  tk+nt



def _targetSum(arr, target):
    n = len(arr)
    s = sum(arr)

    if (s-target) % 2 != 0:
        return 0
    
    t = (s-target)//2

    dp = [[-1 for i in range(t+1)] for i in range(n)]

    return solve(arr, n-1, t, dp)


def targetSum(arr, target):
    n = len(arr)
    s = sum(arr)

    if (s-target) % 2 != 0:
        return 0
    
    t = (s-target)//2

    dp = [[0 for i in range(t+1)] for i in range(n)]

    for i in range(n):
        dp[i][0] = 0

    # most important condition
    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1

    
    if arr[0] <= t and arr[0]!= 0:
        dp[0][arr[0]] = 1

    
    for i in range(1,n):
        for k in range(t+1):
            tk=0

            if k-arr[i] >= 0:
                tk = dp[i-1][k-arr[i]]
            
            nt = dp[i-1][k]

            dp[i][k] = tk+nt
    
    return dp[n-1][t]




    



l = [1,1,1,1,1]
k=3

print(targetSum(l,k))
