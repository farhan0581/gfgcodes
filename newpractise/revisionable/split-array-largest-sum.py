'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
'''
class Solution:
    def check(self, arr, cap, k):
        s = 0
        cnt = 1

        for i in range(len(arr)):
            s += arr[i]

            if s > cap:
                cnt += 1
                s = arr[i]
            
            if cnt > k:
                return False
        
        return True

        
    
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        
        start = 0
        end = 0
        for i in range(len(nums)):
            end += nums[i]
            start = max(start, nums[i])
        
        while start <= end:
            mid = (start+end)//2

            if self.check(nums, mid, k):
                end = mid-1
            else:
                start = mid+1
        
        return start
        