'''
Problem statement
You are given two strings, 'str1' and 'str2'. You have to find the length of the longest common substring.



A substring is a continuous segment of a string. For example, "bcd" is a substring of "abcd", while "acd" or "cda" are not.



Example:
Input: ‘str1’ = “abcjklp” , ‘str2’ = “acjkp”.

Output: 3

Explanation:  The longest common substring between ‘str1’ and ‘str2’ is “cjk”, of length 3.

APPROACH:
- approach is similar to subset, just that now we have to take care of continous equal length
- so when s1[i] != s2[j], we make it to 0 , instead of checking the previous




'''
def lcs(str1: str, str2: str) -> int:
    # write your code here
    m = len(str1)
    n = len(str2)

    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    maxlen = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 0
            maxlen = max(dp[i][j], maxlen)
    return maxlen

s1 = "ccdebbbcca"
s2 = "ddaddc"
print(lcs(s1, s2))
