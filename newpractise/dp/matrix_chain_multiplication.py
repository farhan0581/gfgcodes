from os import *
from sys import *
from collections import *
from math import *

def solve(arr, i, j, dp):
	if i == j:
		return 0

	if dp[i][j] != -1:
		return dp[i][j]
	
	mini = 9999999999
	for k in range(i, j):
		ans = solve(arr, i, k, dp) + arr[i-1]*arr[k]*arr[j]  +  solve(arr, k+1, j, dp)
		mini = min(mini, ans)
	
	dp[i][j] = mini
	return mini
	
def _matrixMultiplication(arr, n):
	dp = [[-1 for i in range(n)] for i in range(n)]
	return solve(arr, 1, n-1, dp)


def matrixMultiplication(arr, n):
	dp = [[0 for i in range(n)] for i in range(n)]
	
	for i in range(n):
		dp[i][i] = 0
	m = 9999999
	for i in range(n-1, 0, -1):
		for j in range(i+1, n):
			m = 9999999
			for k in range(i,j):
				x = dp[i][k] + arr[i-1]*arr[k]*arr[j] + dp[k+1][j]
				m = min(m, x)
			dp[i][j] = m
	# print(dp)
	return dp[1][n-1]




	