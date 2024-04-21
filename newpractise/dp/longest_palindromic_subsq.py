'''
Problem statement
You have been given a string ‘A’ consisting of lower case English letters. Your task is to find the length of the longest palindromic subsequence in ‘A’.

A subsequence is a sequence generated from a string after deleting some or no characters of the string without changing the order of the remaining string characters. (i.e. “ace” is a subsequence of “abcde” while “aec” is not).

A string is said to be palindrome if the reverse of the string is the same as the actual string. For example, “abba” is a palindrome, but “abbc” is not a palindrome.

APPROACH:
- we will convert this to a problem of longest common subseq:
  since we need longest palindromic subseq, we will reverse the original string
  then we find lcs of s and reverse of s
  why this work ?
  palindrome is basically reverse(s) == s
  so it means if some subseq is common in both, it must be palindrome
'''
INT_MIN=-9999999999
def solve(s1,s2, i, j, dp):
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != INT_MIN:
        return dp[i][j]
    
    m1=m2=INT_MIN
    if s1[i] == s2[j]:
        m1 = 1 + solve(s1,s2,i-1,j-1,dp)
    else:
        m2 = max(solve(s1,s2,i-1, j, dp), solve(s1,s2,i,j-1,dp))
    dp[i][j] = max(m1,m2)
    return dp[i][j]
    


def longestPalindromeSubsequence(s):
    # Write your code here.
    s1 = s
    s2 = s[::-1]
    dp = [[INT_MIN for i in range(len(s))] for i in range(len(s))]
    return solve(s1,s2,len(s)-1, len(s)-1, dp)
    


s="bbbab"
print(longestPalindromeSubsequence(s))