'''
Problem statement
You are given two strings 'S' and 'T' of lengths 'N' and 'M' respectively. Find the "Edit Distance" between the strings.

Edit Distance of two strings is the minimum number of steps required to make one string equal to the other. In order to do so, you can perform the following three operations:

1. Delete a character
2. Replace a character with another one
3. Insert a character
Note:
Strings don't contain spaces in between.

APPROACH:
- there are 3 cases, delete , insert, replace
replace is simple
in delete, we delete from the string from s1 and move forward in s1
in insert, we insert in s1 and then move in s2
'''

INT_MAX=9999999999
def solve(s1,s2,i,j, dp):

    if i < 0:
        return j+1
    
    if j < 0:
        return i+1
    
    if dp[i][j] != -1:
        return dp[i][j]
    

    m1=m2=m3=m4=INT_MAX
    if s1[i] == s2[j]:
        m1 = 0 + solve(s1,s2,i-1,j-1, dp)
    else:
        # replace
        m2 = 1 + solve(s1,s2,i-1,j-1, dp)

        # delete
        m3 = 1 + solve(s1,s2,i-1,j, dp)

        # insert
        m4 = 1 + solve(s1, s2, i, j-1, dp)

    dp[i][j] = min(m1, m2, m3, m4)
    
    return dp[i][j]
    



def _editDistance(str1, str2) :
    
    # Your code goes here
    dp = [[-1 for i in range(len(str2))] for i in range(len(str1))]
    return solve(str1, str2, len(str1)-1, len(str2)-1, dp)


def editDistance(str1, str2) :
    m = len(str1)
    n = len(str2)
    # Your code goes here
    dp = [[INT_MAX for i in range(n+1)] for i in range(m+1)]

    
    for i in range(m+1):
        dp[i][0] = i
    
    for j in range(n+1):
        dp[0][j] = j
    
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            m1=m2=m3=m4=INT_MAX
            if str1[i-1] == str2[j-1]:
                m1 = 0 + dp[i-1][j-1]
            else:
                m2 = 1 + dp[i-1][j-1]
                m3 = 1 + dp[i][j-1]
                m4 = 1 + dp[i-1][j]
            dp[i][j] = min(m1,m2,m3,m4)
    
    return dp[m][n]





s1 = "whgtdwhgtdg"
s2 = "aswcfg"
print(editDistance(s1,s2))