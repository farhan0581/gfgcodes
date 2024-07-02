'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


SOLUTIRON:
- consider 0 as -1, so we now need to find max subarray with sum as 0
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = cnt = 0
        m = {}
        start=end=maxlen=0

        while end < len(nums):
            
            if nums[end] == 0:
                s += -1
            else:
                s += 1
            

            if s == 0:
                maxlen = max(maxlen, end+1)
            
            ind = m.get(s, -1)
            if ind != -1:
                maxlen = max(maxlen, end-ind)

            try:
                m[s]
            except:
                m[s] = end
            
            end += 1

            
        return maxlen