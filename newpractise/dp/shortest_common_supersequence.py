'''
Problem statement
Given two strings, ‘A’ and ‘B’. Return the shortest supersequence string ‘S’, containing both ‘A’ and ‘B’ as its subsequences. If there are multiple answers, return any of them.

Note: A string 's' is a subsequence of string 't' if deleting some number of characters from 't' (possibly 0) results in the string 's'.

For example:
Suppose ‘A’ = “brute”, and ‘B’ = “groot”

The shortest supersequence will be “bgruoote”. As shown below, it contains both ‘A’ and ‘B’ as subsequences.

A   A A     A A
b g r u o o t e
  B B   B B B  

It can be proved that the length of supersequence for this input cannot be less than 8. So the output will be bgruoote.

APPROACH:
s1+s2 is a brute force supersequnce, for minimum we have to keep away the common characters
so we find the lcs and then use the table to move forward and only include lcs once

https://takeuforward.org/data-structure/shortest-common-supersequence-dp-31/

'''
INT_MIN=-9999999999
def shortestSupersequence(a: str, b: str) -> str:
    m = len(a)
    n = len(b)
    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            m1=m2=INT_MIN
            if a[i-1] == b[j-1]:
                 dp[i][j] = 1 + dp[i-1][j-1]
            else:
                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            # dp[i][j] = max(m1, m2)
    
    
    i = m
    j = n
    s = ""
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            s += a[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                s += a[i-1]
                i -= 1
            else:
                s += b[j-1]
                j = j-1
    
    while i > 0:
        s += a[i-1]
        i -= 1
    while j > 0:
        s += b[j-1]
        j -= 1
    
    return s[::-1]

    
    


a="brute"
b="groot"
print(shortestSupersequence(a,b))