'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

'''
class Solution:
    def solve(self, s1, s2, i, j, dp):
        if j >= len(s2):
            return 1
        
        if i >= len(s1):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        

        if s1[i] == s2[j]:
            dp[i][j] = self.solve(s1, s2, i+1, j+1, dp) + self.solve(s1, s2, i+1, j, dp)
            
        else:
            dp[i][j] = self.solve(s1, s2, i+1, j, dp)
        
        return dp[i][j]
        
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for i in range(len(t))] for i in range(len(s))]
        return self.solve(s,t, 0, 0, dp)