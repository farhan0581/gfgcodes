'''
Problem statement
Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.

For a string 'str'(per se) of length K, the subsequences are the strings containing characters in the same relative order as they are present in 'str,' but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K.

Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.

AAPRACOH:
- here only change is that we have to check when the string character is matching or not
- when match we decrement both the strings
- when not match, we decremnt both alternate and check
- then compare the max from both
'''

INT_MIN=-9999999999

def solve(s1,s2,i,j, dp):

    if i < 0 or j < 0:
        return 0
    
    if dp[i][j] != INT_MIN:
        return dp[i][j]

    
    mtch=nmtch1=nmtch2=INT_MIN
    #match
    if s1[i] == s2[j]:
        mtch = 1 + solve(s1, s2, i-1, j-1, dp)
    #notmatch
    else:
        nmtch1 = 0 + solve(s1, s2, i-1, j, dp)
        nmtch2 = 0 + solve(s1, s2, i, j-1, dp)

    dp[i][j] = max(mtch, max(nmtch1, nmtch2))
    return dp[i][j]




def lcs(s1, s2) :
	#Your code goes here
    m = len(s1)
    n = len(s2)
    dp = [[INT_MIN for i in range(len(s2))] for i in range(len(s1))]
    return solve(s1,s2, len(s1)-1, len(s2)-1, dp)


def lcs(s1, s2) :
	#Your code goes here
    m = len(s1)
    n = len(s2)
    # for tabulation you have to extend the array because, we have to cover -1 for i-1 and j-1
    dp = [[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            m1 = m2 =0
            if s1[i-1] == s2[j-1]:
                m1 = 1 + dp[i-1][j-1]
            else:
                m2 = max(dp[i-1][j], dp[i][j-1])
            
            dp[i][j] = max(m1,m2)
    
    return dp[m][n] 



def printlcs(s1, s2) :
	#Your code goes here
    m = len(s1)
    n = len(s2)
    # for tabulation you have to extend the array because, we have to cover -1 for i-1 and j-1
    dp = [["" for i in range(len(s2)+1)] for i in range(len(s1)+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            m1 = m2 = ""
            if s1[i-1] == s2[j-1]:
                m1 = dp[i-1][j-1] + s1[i-1]
            else:
                if len(dp[i-1][j]) >= len(dp[i][j-1]):
                    m2 = dp[i-1][j]
                else:
                    m2 = dp[i][j-1]
            
            if len(m1) > len(m2):
                dp[i][j] = m1
            else:
                dp[i][j] = m2
    
    return dp[m][n] 





s1 = "adebc"
s2 = "cd"

print(lcs(s1, s2))
print(printlcs(s1,s2))