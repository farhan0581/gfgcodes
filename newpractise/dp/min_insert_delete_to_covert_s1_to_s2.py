'''
Problem statement
You are given 2 non-empty strings 's1' and 's2' consisting of lowercase English alphabets only.



In one operation you can do either of the following on 's1':

(1) Remove a character from any position in 's1'.

(2) Add a character to any position in 's1'.



Find the minimum number of operations required to convert string 's1' into 's2'.



Example:
Input: 's1' = "abcd", 's2' = "anc"

Output: 3

Explanation:
Here, 's1' = "abcd", 's2' = "anc".
In one operation remove 's1[3]', after this operation 's1' becomes "abc".    
In the second operation remove 's1[1]', after this operation 's1' becomes "ac".
In the third operation add 'n' in 's1[1]', after this operation 's1' becomes "anc".

Hence, the minimum operations required will be 3. It can be shown that there's no way to convert s1 into s2 in less than 3 moves.

APPROACH:
- we can always fully delete s1 and then insert s2 to make them same, so total will be s1+s2
 for minimum we will find the lcs of them , then we can subtract s1 + s2- 2*lcs
'''

INT_MIN=-999999999
def canYouMake(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            m1=m2=INT_MIN
            if s1[i-1] == s2[j-1]:
                m1 = 1 + dp[i-1][j-1]
            else:
                m2 = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = max(m1, m2)
    
    return m+n-(2*dp[m][n])


s1="aaa"
s2="aa"
print(canYouMake(s1,s2))