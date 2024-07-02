'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        
        minlen = 99999999
        s = 0

        start = end = 0

        while end < len(nums) and start <= end:
            s += nums[end]

            while s >= target:
                minlen = min(minlen, end-start+1)
                s -= nums[start]
                start += 1
            
            end += 1
        
        if minlen == 99999999:
            return 0
        return minlen




        