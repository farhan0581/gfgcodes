'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''

from typing import List


class Solution:
    def solve(self, arr, i,dp):
        if i >= len(arr)-1:
            return True
        
        if dp[i] != -1:
            return dp[i]
        
        steps = arr[i]

        for j in range(1, steps+1):
            if self.solve(arr, i+j, dp):
                dp[i] = True
                return True
        
        dp[i] = False
        return dp[i]

        
    def _canJump(self, nums: List[int]) -> bool:
        dp = [-1]*len(nums)
        return self.solve(nums, 0, dp)

    # greedy approach
    def canJump(self, nums: List[int]) -> bool:
        
        last_position = 0
        for i in range(len(nums)):
            if last_position < i:
                return False
            
            last_position = max(last_position, nums[i]+i)

            if last_position >= len(nums)-1:
                return True
        
        return False
        