'''
Problem statement
Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?

You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
'''

from typing import *


# tabulation
def solve(arr):
    dp = [[-1 for i in range(3)] for i in range(len(arr))]
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        for j in range(3):
            m = -99999999
            for k in range(3):
                if k != j:
                    m = max(m, dp[i-1][k])  

            dp[i][j] = arr[i][j] + m
    
    return max(dp[len(arr)-1])

# recursion
def solve(arr, i, prev, dp):
    if i == len(arr)-1:
        return arr[i][prev]
    
    if i >= len(arr):
        return 0

    if dp[i][prev] != -1:
        return dp[i][prev]
    
    m = -999999999

    for j in range(3):
        if j != prev:
            m = max(arr[i][prev] + solve(arr, i+1, j, dp), m)
    
    dp[i][prev] = m
    return m
    
    


    
    

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for i in range(3)] for i in range(n+1)]
    m1 = solve(points, 0, 0, dp)
    m2 = solve(points, 0, 1, dp)
    m3 = solve(points, 0, 2, dp)

    return max(m1, m2, m3)






l = [[1,2,5], [3 ,1 ,1] ,[3,3,3] ]
l = [[10, 40, 70],[20, 50, 80],[30, 60, 90]]
# l = [[1,2,3]]
# l = [[10, 50, 1],[5, 100, 11]]
n = len(l)
print(ninjaTraining(n,l))
print(tab(l))