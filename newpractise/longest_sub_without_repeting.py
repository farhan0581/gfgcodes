'''
Given a string s, find the length of the longest 
substring(should be continous)
 without repeating characters.

 Approach
use sliding window, start and end
keep map to keep track of frequency , if frequency > 1, then increment the start
otherwise increase end

'''
class Solution(object):
    def lengthOfLongestSubstring(self, arr):
        """
        :type s: str
        :rtype: int
        """
        start = end = 0
        maxlen = 0
        m = {}

        while start < len(arr) and end < len(arr):

            freq = m.get(arr[end], 0)
            if freq == 0:
                m[arr[end]] = 1
                l = end-start+1
                maxlen=max(maxlen,l)
                end += 1
                
            else:
                removed = arr[start]
                f = m.get(removed,0)
                m[removed] = f-1
                start += 1
        
        return maxlen


s="abcabcdbertyub"
print(Solution().lengthOfLongestSubstring(s))