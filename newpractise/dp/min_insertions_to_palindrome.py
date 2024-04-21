'''
Problem statement
A palindrome string is one that reads the same backward as well as forward.



You are given a string 'str'.



Find the minimum number of characters needed to insert in 'str' to make it a palindromic string.



Example :
Input: 'str' = "abca"

Output: 1

Explanation:
If we insert the character ‘b’ after ‘c’, we get the string "abcba", which is a palindromic string. Please note that there are also other ways possible.

APPROACH:
- the min insertions required will be total length - max length of palindromic sub 
'''
def minInsertion(str):
    s1 = s
    s2 = s[::-1]
    n = len(s)

    dp = [[0 for i in range(n+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, n+1):
            m1=m2=-99999999
            if s1[i-1] == s2[j-1]:
                m1 = 1 + dp[i-1][j-1]
            else:
                m2 = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = max(m1, m2)
    
    return n - dp[n][n]

    


s = "abca"
print(minInsertion(s))