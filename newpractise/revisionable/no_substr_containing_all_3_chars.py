'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        posa=posb=posc= -1

        for i in range(len(s)):
            if s[i] == "a":
                posa = i
            elif s[i] == "b":
                posb = i
            else:
                posc = i
            
            mi = min(posa,posb,posc)
            if mi != -1:
                cnt += (mi-0) + 1
        
        return cnt


