'''
Problem statement
You are given ‘n’ items with certain ‘profit’ and ‘weight’ and a knapsack with weight capacity ‘w’.



You need to fill the knapsack with the items in such a way that you get the maximum profit. You are allowed to take one item multiple times.



Example:
Input: 
'n' = 3, 'w' = 10, 
'profit' = [5, 11, 13]
'weight' = [2, 4, 6]

Output: 27

Explanation:
We can fill the knapsack as:

1 item of weight 6 and 1 item of weight 4.
1 item of weight 6 and 2 items of weight 2.
2 items of weight 4 and 1 item of weight 2.
5 items of weight 2.

The maximum profit will be from case 3 = 11 + 11 + 5 = 27. Therefore maximum profit = 27.
'''
INT_MIN = -9999999999
def solve(profit, weight, i, k,dp):
    if k == 0:
        return 0
    if i == 0:
        if weight[0] > k:
            return INT_MIN
        else:
            return (k//weight[0])*profit[0]
    
    if dp[i][k] != -1:
        return dp[i][k]

    tk = INT_MIN
    if k-weight[i] >= 0:
        tk = solve(profit, weight, i, k-weight[i],dp) + profit[i]

    nt = solve(profit, weight, i-1, k,dp) + 0
    dp[i][k] = max(tk, nt)
    return dp[i][k]


def _unboundedKnapsack(n, w, profit, weight):
    # write your code here
    dp = [[-1 for i in range(w+1)] for i in range(n)]
    ans = solve(profit, weight, n-1, w, dp)
    if ans == INT_MIN:
        return 0
    return ans


def unboundedKnapsack(n, w, profit, weight):
    # write your code here
    dp = [[INT_MIN for i in range(w+1)] for i in range(n)]
    
    for i in range(n):
        dp[i][0] = 0
    

    for i in range(w+1):
        # no need for if
        # if i <= weight[0]:
        dp[0][i] = (i//weight[0])*profit[0]
        




    for i in range(1, n):
        for k in range(w+1):
            tk = INT_MIN
            if k-weight[i] >= 0:
                tk = profit[i] + dp[i][k-weight[i]]
            
            nt = 0 + dp[i-1][k]

            dp[i][k] = max(tk, nt)

    ans = dp[n-1][w]
    # print(dp)
    if ans == INT_MIN:
        return 0
    return ans




p=[5, 11, 13]
we=[2,4,6]
w=10
n=len(p)
print(unboundedKnapsack(n,w,p,we))

