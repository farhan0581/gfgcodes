'''
Problem statement
A Subsequence of a string is the string that is obtained by deleting 0 or more letters from the string and keeping the rest of the letters in the same order.



We are given two strings, 'str' and 'sub'.



Find the number of subsequences of 'str' which are equal to 'sub'.



Since the answer can be very large, print it modulo 10 ^ 9 + 7.



Example :
Input: 'str' = “brootgroot” and 'sub' = “brt”

Output: 3

Explanation: The following subsequences formed by characters at given indices (0-based) of 'str' are equal to 'sub' :

str[0] = ‘b’, str[1] = ‘r’, str[4] = ‘t’

str[0] = ‘b’, str[1] = ‘r’, str[9] = ‘t’

str[0] = ‘b’, str[6] = ‘r’, str[9] = ‘t’
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
brootgroot
brt


Sample Output 1 :
3


Explanation For Sample Input 1 :
The following subsequences formed by characters at given indices (0-based) of 'str' are equal to 'sub' :

str[0] = ‘b’, str[1] = ‘r’, str[4] = ‘t’

str[0] = ‘b’, str[1] = ‘r’, str[9] = ‘t’

str[0] = ‘b’, str[6] = ‘r’, str[9] = ‘t’


Sample Input 2 :
dingdingdingding
ing


Sample Output 2 :
20


Sample Input 3:
aaaaa
a


Sample Output 3:
5


Expected time complexity :
The expected time complexity is O(|str| * |sub|).
'''

def solve(s1, s2, i, j, dp):
    if j < 0:
        return 1
    if i < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    m1=m2=m3=0
    # this is the only difference , when match we decrement both and also consider the case
    # when we can have another encounter of the same character also
    if s1[i] == s2[j]:
        m1=solve(s1,s2,i-1, j-1, dp)
        m2=solve(s1,s2,i-1, j, dp)

    else:
        m3=solve(s1,s2, i-1, j, dp)
    
    dp[i][j] = m1+m2+m3
    return dp[i][j]


def _distinctSubsequences(s1: str, s2: str) -> int:
    # write your code here
    if len(s2) > len(s1):
        s1,s2 = s2,s1
    dp = [[-1 for i in range(len(s2))] for i in range(len(s1))]
    return solve(s1, s2, len(s1)-1, len(s2)-1, dp)
'''
 tabulation
  Base case: There is exactly one subsequence of an empty string s2 in s1
    for i in range(n + 1):
        dp[i][0] = 1

    # Initialize dp[0][i] to 0 for i > 0 since an empty s1 cannot have a non-empty subsequence of s2
    for i in range(1, m + 1):
        dp[0][i] = 0
'''
def distinctSubsequences(s1: str, s2: str) -> int:
    # write your code here
    if len(s2) > len(s1):
        s1,s2 = s2,s1
    m = len(s1)
    n = len(s2)
    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        dp[i][0] = 1
    

    for i in range(1, m+1):
        for j in range(1, n+1):
            m1=m2=m3=0
            if s1[i-1] == s2[j-1]:
                m1 = dp[i-1][j-1]
                m2 = dp[i-1][j]
            else:
                m3 = dp[i-1][j]
            dp[i][j] = m1+m2+m3
    return dp[m][n]


    


s1 = "brootgroot"
s2 = "brt"
print(distinctSubsequences(s1, s2))