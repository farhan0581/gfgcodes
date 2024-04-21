from typing import List

def solve(arr, fee, i, buy, dp):
    if i >= len(arr):
        return 0
    
    if dp[i][buy] != -1:
        return dp[i][buy]
    
    if buy == 0:
        dp[i][buy] = max(-arr[i]+solve(arr, fee, i+1, 1, dp), solve(arr, fee, i+1, 0, dp))
    else:
        dp[i][buy] = max(arr[i]-fee+solve(arr, fee, i+1, 0, dp), solve(arr, fee, i+1, 1, dp))
    
    return dp[i][buy]

def maximumProfit(prices: List[int], n: int, fee: int) -> int:
    # write your code here
    dp = [[-1 for i in range(2)] for i in range(n)]
    return solve(prices, fee, 0, 0, dp)

l = [1, 2, 3]
f =1
print(maximumProfit(l, len(l),f))