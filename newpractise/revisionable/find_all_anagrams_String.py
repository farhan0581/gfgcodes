'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m1 = {}
        m2 = {}
        ans = []
        if len(s) < len(p):
            return []
            
        for i in range(len(p)):
            f=m1.get(p[i], 0)
            m1[p[i]] = f+1
            f=m2.get(s[i], 0)
            m2[s[i]] = f+1 
        
        if m1 == m2:
            ans.append(0)
        # print(m1,m2)
        for i in range(1, len(s)-len(p)+1):
            f = m2.get(s[i-1],0)
            m2[s[i-1]] = f-1

            if m2[s[i-1]] == 0:
                del m2[s[i-1]]

            f = m2.get(s[i+len(p)-1],0)
            m2[s[i+len(p)-1]] = f+1
            # print(m1,m2,s[i])
            if m1 == m2:
                ans.append(i)
        
        return ans

            


        