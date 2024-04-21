'''
Problem statement
Given a text and a wildcard pattern of size N and M respectively, implement a wildcard pattern matching algorithm that finds if the wildcard pattern is matched with the text. The matching should cover the entire text not partial text.

The wildcard pattern can include the characters ‘?’ and ‘*’

 ‘?’ – matches any single character 
 ‘*’ – Matches any sequence of characters(sequence can be of length 0 or more)
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
1 <= N <= 200
1 <= M <= 200

Where 'N' denotes the length of 'TEXT' and 'M' denotes the length of 'PATTERN'.

'TEXT' and 'PATTERN' contain only lowercase letters and patterns may contain special characters ‘*’ and ‘?’

Time Limit: 1sec
Sample Input 1:
3
?ay
ray
ab*cd
abdefcd
ab?d
abcc
Sample Output 1:
True
True
False
Explanation of the Sample Input1:
Test Case 1:
The pattern is “?ay” and the text is ray.
‘?’ can match a character so it matches with a character ‘r’ of the text and rest of the text matches with the pattern so we print True.

Test Case 2:
“ab” of text matches with “ab” of pattern and then ‘*’ of pattern matches with “def” of the text and “cd” of text matches with “cd” of the pattern. Whole text matches with the pattern so we print True.

Test Case 3:
“ab” of pattern matches with “ab” of text. ‘?’ of pattern matches with ‘c’ of the text but ‘d’ of the pattern do not match with ‘c’ of the text so we print False.
Sample Input 1:
1
ba*a?
baaabab
Sample Output 1:
True
'''
def solve(pat, txt, i, j, dp):

    if i < 0 and j < 0:
        return True
    
    if i < 0 and j >= 0:
        return False
    if i >= 0 and j < 0:
        k = i
        while k >=0:
            if pat[k] != "*":
                return False
            k -= 1
        return True

    if dp[i][j] != -1:
        return dp[i][j]

    
    if pat[i] == txt[j] or pat[i] == "?":
        dp[i][j] = solve(pat, txt, i-1, j-1, dp)
    
    elif pat[i] == "*":
        c1 = solve(pat, txt, i-1, j, dp) #ignore * or consider as empty
        c2 = solve(pat, txt, i, j-1, dp) # match with *
        dp[i][j] = c1 or c2
    else:
        dp[i][j] = False
    
    return dp[i][j]
        



def wildcardMatching(pattern, text):
    # Write your code here.
    m = len(pattern)
    n = len(text)
    dp =[[-1 for i in range(n)] for i in range(m)]
    return solve(pattern, text, m-1, n-1, dp)


s1="a*at"
s2="chat"
print(wildcardMatching(s1, s2))
