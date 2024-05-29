'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

TOUGH
'''
class Solution:
    def _subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt = 0
        m = {}
        end = 0
        start = 0


        while start <= end and end < len(nums):
            # print(m)
            if len(m) <= k:
                tmp = m.get(nums[end], -1)
                if tmp != -1:
                    m[nums[end]] = tmp+1
                else:
                    m[nums[end]] =  1
                end += 1
            
            # here we need to use a while loop
            while len(m) > k and start <= end:
                m[nums[start]] -= 1
                if m[nums[start]] == 0:
                    del m[nums[start]]
                start += 1
            
            if len(m) <=k:
                cnt += end-start+1
        # print(cnt)
        return cnt
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self._subarraysWithKDistinct(nums, k) - self._subarraysWithKDistinct(nums, k-1)
