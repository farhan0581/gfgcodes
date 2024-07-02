'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep a list of index to frequency
        m = [0]*128
        count = 0
        start_ind = 0
        
        for char in t:
            m[ord(char)] += 1
            count += 1 # count of total words in "t"

        # in m, only characters in c have freq > 0, all others have freq as 0;
        
        minlen = 9999999

        start = end = 0

        while end < len(s):
            
            # if char is present in "t"
            if m[ord(s[end])] > 0:
                count -= 1

            m[ord(s[end])] -= 1

            # this means we have found all charaters in the t
            while count == 0:
                if minlen > end-start+1:
                    minlen = end-start+1
                    start_ind = start
                
                # shrink window

                # this means we now need to find this char again
                if m[ord(s[start])] == 0:
                    count += 1
                
                m[ord(s[start])] += 1
                start += 1
            
            end += 1
        
        # print(minlen, start_ind)
        if minlen == 9999999:
            return ""
        return s[start_ind:start_ind+minlen]



        