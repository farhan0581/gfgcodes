'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


solution:

sort it and check for next element, simple
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        n = len(nums)
        maxlen = 0
        start = 0
        end = 0
        print(nums)
        m = {}
        while end < n:
            if end+1 < n:
                if nums[end+1]-nums[end] == 1:
                    end += 1
                    maxlen = max(maxlen, end-start+1)
                else:
                    start += 1
                    end = start
            else:
                break
        if maxlen == 0 and len(nums) > 0:
            maxlen = 1
        return maxlen


        

l=[100,4,200,1,3,2]
# l = [0,3,7,2,5,8,4,6,0,1]
l = [1,4]
l = [1,2,3,5,6,7,8,9,11,22]
l=[0,1,1,2]
print(Solution().longestConsecutive(l))