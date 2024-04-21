'''
Problem statement
You are given a list of stock prices of size 'n' called ‘prices’, where ‘prices[i]’ represents the price on ‘i’th day.



Your task is to calculate the maximum profit you can earn by trading stocks if you can only hold one stock at a time.



After you sell your stock on the ‘i’th day, you can only buy another stock on ‘i + 2’ th day or later.



Example:
Input: 'prices' = [4, 9, 0, 4, 10]

Output: 11

Explanation:
You are given prices = [4, 9, 0, 4, 10]. To get maximum profits you will have to buy on day 0 and sell on day 1 to make a profit of 5, and then you have to buy on day 3  and sell on day 4 to make the total profit of 11. Hence the maximum profit is 11.
'''
from typing import List


def solve(arr, i, buy, dp):
    if i >= len(arr):
        return 0
    
    if dp[i][buy] != -1:
        return dp[i][buy]
    
    # need t0 buy
    if buy == 0:
        m1 = -arr[i] + solve(arr, i+1, 1, dp)
        m2 = 0 + solve(arr, i+1, 0, dp)
        dp[i][buy] = max(m1, m2)
    
    # can sell
    else:
        m3 = arr[i] + solve(arr, i+2, 0, dp)
        m4 = 0 + solve(arr, i+1, 1, dp)
        dp[i][buy] = max(m3, m4)
    
    return dp[i][buy]

# recursion
def _stockProfit(prices: List[int]) -> int:
    # Write your code here.
    dp = [[-1 for i in range(2)] for i in range(len(prices))]
    return solve(prices, 0, 0, dp)


# tabulation
def stockProfit(prices: List[int]) -> int:
    # Write your code here.
    n = len(prices)
    dp = [[-1 for i in range(2)] for i in range(n+2)]
    
    dp[n][0] = dp[n][1] = 0
    dp[n+1][0] = dp[n+1][1] = 0


    for i in range(n-1, -1, -1):
        for j in range(2):
            if j == 0:
                dp[i][j] = max(-prices[i]+dp[i+1][1], dp[i+1][0])
            else:
                dp[i][j] = max(prices[i]+dp[i+2][0], dp[i+1][1])

    
    return dp[0][0]


l = [4, 9, 0, 4, 10]
print(stockProfit(l))