# https://www.codingninjas.com/studio/problems/frog-jump_3621012?leftPanelTab=1
from os import *
from sys import *
from collections import *
from math import *

from typing import *

''' bottom-up
def solve(i, n,heights,dp):
    if i >= n-1:
        return 0
    
    if dp[i] != None:
        return dp[i]
    
    j1=j2=999999999

    if i+1 <= n-1:
        j1 = solve(i+1, n, heights,dp) + abs(heights[i]-heights[i+1])
    if i+2 <= n-1:
        j2 = solve(i+2, n, heights,dp) + abs(heights[i]-heights[i+2])
    cost = min(j1, j2)
    dp[i] = cost
    return cost
        


def frogJump(n, heights):
    # print("====")
    dp = [None]*n
    x = solve(0, n, heights,dp)
    return x
'''

'''
# recursion top down
def solve(i,heights,dp):
    if i <= 0:
        return 0

    if dp[i] != None:
        return dp[i]
    
    jump1=jump2=999999999999
    if i-1 >= 0:
        jump1 = solve(i-1, heights, dp) + abs(heights[i]-heights[i-1])
    if i-2 >= 0:
        jump2 = solve(i-2, heights, dp) + abs(heights[i]-heights[i-2])

    cost = min(jump1, jump2)
    dp[i] = cost
    return cost
    
        


def frogJump(n, heights):
    # print("====")
    dp = [None]*n
    x = solve(n-1, heights,dp)
    return x
'''


    
        

# tabulation
def frogJump(n, heights):
    # print("====")
    dp = [None]*n
    dp[0] = 0

    for i in range(1,n):
        jump1=jump2=999999999999
        if i-1 >= 0:
            jump1 = dp[i-1] + abs(heights[i]-heights[i-1])
        if i-2 >= 0:
            jump2 = dp[i-2] + abs(heights[i]-heights[i-1])
        dp[i] = min(jump1,jump2)

    return dp[n-1]




    # x = solve(n-1, heights,dp)
    # return x

print(frogJump(8, [7, 4, 4, 2, 6, 6, 3, 4 ]))